#!/usr/bin/env python3
"""Validate skill structure, local links, and exact preservation manifests."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
START_OF_FRONTMATTER = "---\n"
END_OF_FRONTMATTER = "\n---\n"


def calculate_git_blob_hash(content: str) -> str:
    encoded_content = content.encode("utf-8")
    header = f"blob {len(encoded_content)}\0".encode("utf-8")
    return hashlib.sha1(header + encoded_content).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_frontmatter(content: str) -> str:
    if not content.startswith(START_OF_FRONTMATTER):
        raise ValueError("le frontmatter YAML ne commence pas au début du fichier")
    closing_position = content.find(END_OF_FRONTMATTER, len(START_OF_FRONTMATTER))
    if closing_position < 0:
        raise ValueError("le délimiteur de fin du frontmatter YAML est absent")
    return content[: closing_position + len(END_OF_FRONTMATTER)]


def validate_skill_frontmatter(skill_path: Path, errors: list[str]) -> None:
    try:
        content = read_text(skill_path)
        frontmatter = extract_frontmatter(content)
    except (OSError, ValueError) as error:
        errors.append(f"{skill_path.relative_to(REPOSITORY_ROOT)}: {error}")
        return
    if not re.search(r"^name:\s*[a-z0-9-]+\s*$", frontmatter, re.MULTILINE):
        errors.append(f"{skill_path.relative_to(REPOSITORY_ROOT)}: nom de skill absent ou invalide")
    if not re.search(r"^description:\s*(?:.+|>)\s*$", frontmatter, re.MULTILINE):
        errors.append(f"{skill_path.relative_to(REPOSITORY_ROOT)}: description absente")


def validate_local_links(markdown_path: Path, errors: list[str]) -> None:
    content = read_text(markdown_path)
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
        if target.startswith(("http://", "https://", "#")):
            continue
        target_without_anchor = target.split("#", 1)[0]
        resolved_target = (markdown_path.parent / target_without_anchor).resolve()
        if not resolved_target.exists():
            errors.append(
                f"{markdown_path.relative_to(REPOSITORY_ROOT)}: lien local absent vers {target}"
            )


def validate_preservation_manifest(manifest_path: Path, errors: list[str]) -> None:
    manifest = json.loads(read_text(manifest_path))
    destination_root = REPOSITORY_ROOT / manifest["destination_root"]
    reconstructed_parts: list[str] = []

    frontmatter_definition = manifest.get("source_frontmatter")
    if frontmatter_definition:
        frontmatter_path = destination_root / frontmatter_definition["destination_path"]
        try:
            reconstructed_parts.append(extract_frontmatter(read_text(frontmatter_path)))
        except (OSError, ValueError) as error:
            errors.append(f"{manifest_path.relative_to(REPOSITORY_ROOT)}: {error}")
            return

    for part in manifest["preserved_parts"]:
        destination_path = destination_root / part["destination_path"]
        if not destination_path.is_file():
            errors.append(
                f"{manifest_path.relative_to(REPOSITORY_ROOT)}: fichier préservé absent {destination_path}"
            )
            return
        content = read_text(destination_path)
        part_identifier = part["part_identifier"]
        start_marker = f"<!-- preserved-source-part-start: {part_identifier} -->\n"
        end_marker = f"<!-- preserved-source-part-end: {part_identifier} -->"
        start_position = content.find(start_marker)
        if start_position < 0:
            errors.append(f"{destination_path}: marqueur de début absent pour {part['part_identifier']}")
            return
        content_position = start_position + len(start_marker)
        end_position = content.find(end_marker, content_position)
        if end_position < 0:
            errors.append(f"{destination_path}: marqueur de fin absent pour {part['part_identifier']}")
            return
        reconstructed_parts.append(content[content_position:end_position])

    reconstructed_source = "".join(reconstructed_parts)
    actual_hash = calculate_git_blob_hash(reconstructed_source)
    expected_hash = manifest["source_git_blob_hash"]
    if actual_hash != expected_hash:
        errors.append(
            f"{manifest_path.relative_to(REPOSITORY_ROOT)}: contenu source altéré; "
            f"empreinte attendue {expected_hash}, obtenue {actual_hash}"
        )


def main() -> int:
    errors: list[str] = []
    skill_paths = sorted(REPOSITORY_ROOT.glob("skills/**/SKILL.md"))
    expected_skill_paths = {
        REPOSITORY_ROOT / "skills/orchestration/ai-orchestrator-methodology/SKILL.md",
        REPOSITORY_ROOT / "skills/frontend/react/react-vite-enterprise-saas/SKILL.md",
        REPOSITORY_ROOT / "skills/frontend/nextjs/nextjs-enterprise-saas/SKILL.md",
        REPOSITORY_ROOT / "skills/fullstack/nextjs/nextjs-fullstack-enterprise-saas/SKILL.md",
    }
    if set(skill_paths) != expected_skill_paths:
        errors.append("les quatre unités de skill attendues ne sont pas les seules détectées")

    expected_installation_paths = {
        REPOSITORY_ROOT
        / "skills/orchestration/ai-orchestrator-methodology/installation/installation.md",
        REPOSITORY_ROOT
        / "skills/frontend/react/react-vite-enterprise-saas/installation/installation.md",
        REPOSITORY_ROOT
        / "skills/frontend/nextjs/nextjs-enterprise-saas/installation/installation.md",
        REPOSITORY_ROOT
        / "skills/fullstack/nextjs/nextjs-fullstack-enterprise-saas/installation/installation.md",
    }
    for installation_path in expected_installation_paths:
        if not installation_path.is_file():
            errors.append(
                "guide d’installation propre au skill absent: "
                f"{installation_path.relative_to(REPOSITORY_ROOT)}"
            )

    for skill_path in skill_paths:
        validate_skill_frontmatter(skill_path, errors)

    for markdown_path in REPOSITORY_ROOT.rglob("*.md"):
        validate_local_links(markdown_path, errors)

    for manifest_path in REPOSITORY_ROOT.rglob("content-preservation.json"):
        validate_preservation_manifest(manifest_path, errors)

    legacy_paths = [
        REPOSITORY_ROOT / "#00-SKILL_METHODOLOGIE_TRAVAIL_AGENT_IA.md",
        REPOSITORY_ROOT / "SKILL_FRONTEND_REACT_VITE_ENTERPRISE_SAAS_V1.1.md",
    ]
    for legacy_path in legacy_paths:
        if legacy_path.exists():
            errors.append(f"ancien fichier racine encore présent: {legacy_path.name}")

    if errors:
        print("Validation échouée :")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Validation réussie : quatre skills valides et trois documents sources "
        "reconstruits sans perte."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
