#!/usr/bin/env python3
"""Legt einen lokalen Arbeitsordner für den Wiki-Agenten an.

Kopiert AGENTS.md, CLAUDE.md und die Vorlagen hinein, legt die Ordnerstruktur an
und initialisiert optional ein lokales Git-Repo (ohne Remote).
Bestehende Dateien werden nicht überschrieben.

Aufruf:
    python init_arbeitsbereich.py <zielordner> [--ohne-git]
"""
import argparse
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ORDNER = ["raw", "extrakt", "wiki", "review"]
KOPIEN = {
    REPO / "AGENTS.md": "AGENTS.md",
    REPO / "CLAUDE.md": "CLAUDE.md",
    REPO / "vorlagen" / "TAXONOMIE.md": "TAXONOMIE.md",
    REPO / "vorlagen" / "inventar.csv": "inventar.csv",
    REPO / "vorlagen" / "progress.md": "progress.md",
    REPO / "vorlagen" / "wiki-seite.md": "vorlagen/wiki-seite.md",
    REPO / "vorlagen" / "pruef-checkliste.md": "vorlagen/pruef-checkliste.md",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ziel", type=Path)
    ap.add_argument("--ohne-git", action="store_true")
    args = ap.parse_args()

    ziel = args.ziel.resolve()
    if REPO == ziel or REPO in ziel.parents:
        print("Der Arbeitsordner darf nicht im Repo liegen (Firmendaten!).", file=sys.stderr)
        return 1

    for o in ORDNER:
        (ziel / o).mkdir(parents=True, exist_ok=True)
    for quelle, rel in KOPIEN.items():
        dst = ziel / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists():
            shutil.copy2(quelle, dst)
    log = ziel / "log.md"
    if not log.exists():
        log.write_text(f"# Entscheidungslog\n\n- {date.today()}: Arbeitsbereich angelegt.\n", encoding="utf-8")

    if not args.ohne_git and not (ziel / ".git").exists() and shutil.which("git"):
        subprocess.run(["git", "init", "-q"], cwd=ziel, check=False)
        (ziel / ".gitignore").write_text("raw/\n", encoding="utf-8")  # Originale nicht versionieren
        print("Lokales Git-Repo angelegt (ohne Remote). raw/ ist ausgeschlossen.")

    print(f"Arbeitsbereich bereit: {ziel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
