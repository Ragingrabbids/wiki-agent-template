#!/usr/bin/env python3
"""Inventur eines Quellordners: eine Zeile pro Datei in inventar.csv.

Erfasst Pfad, Typ, Größe, Änderungsdatum und SHA-256-Hash und markiert exakte
Dubletten (gleicher Hash). Bereits vorhandene Einträge (gleicher Pfad) bleiben
mit ihren Status-/Metadaten erhalten; neue Dateien werden mit Status "neu" ergänzt.

Nur Python-Standardbibliothek.

Aufruf:
    python inventur.py <quellordner> <inventar.csv> [--endungen .docx,.pdf,...]
"""
import argparse
import csv
import hashlib
import os
import sys
from datetime import datetime
from pathlib import Path

FELDER = [
    "id", "pfad", "dateiname", "endung", "groesse_bytes", "geaendert_am", "sha256",
    "dublette_von", "status", "klassifizierung", "lenkungsstatus", "abteilung",
    "themenbereich", "dokumenttyp", "maschine_werkzeug", "kunde", "aktualitaet",
    "aktualitaet_begruendung", "personenbezug", "konfidenz", "wiki_seite", "bemerkung",
]

STANDARD_ENDUNGEN = {
    ".doc", ".docx", ".xls", ".xlsx", ".xlsm", ".ppt", ".pptx", ".pdf",
    ".txt", ".md", ".rtf", ".odt", ".ods", ".msg", ".png", ".jpg", ".jpeg", ".tif", ".tiff",
}
IGNORIEREN = {"thumbs.db", "desktop.ini", ".ds_store"}


def sha256(pfad: Path, block: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(pfad, "rb") as f:
        while chunk := f.read(block):
            h.update(chunk)
    return h.hexdigest()


def lade_inventar(datei: Path) -> list[dict]:
    if not datei.exists() or datei.stat().st_size == 0:
        return []
    with open(datei, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("quellordner", type=Path)
    ap.add_argument("inventar", type=Path)
    ap.add_argument("--endungen", help="Kommagetrennte Liste, z. B. .docx,.pdf (Standard: Office/PDF/Bilder)")
    args = ap.parse_args()

    if not args.quellordner.is_dir():
        print(f"Quellordner nicht gefunden: {args.quellordner}", file=sys.stderr)
        return 1

    endungen = (
        {e.strip().lower() if e.strip().startswith(".") else "." + e.strip().lower()
         for e in args.endungen.split(",")}
        if args.endungen else STANDARD_ENDUNGEN
    )

    bestand = lade_inventar(args.inventar)
    nach_pfad = {z["pfad"]: z for z in bestand}
    naechste_id = max((int(z["id"]) for z in bestand if z.get("id", "").isdigit()), default=0) + 1

    neu = fehler = 0
    for wurzel, _, dateien in os.walk(args.quellordner):
        for name in sorted(dateien):
            p = Path(wurzel) / name
            if name.lower() in IGNORIEREN or name.startswith("~$"):
                continue
            if p.suffix.lower() not in endungen:
                continue
            rel = str(p.relative_to(args.quellordner)).replace("\\", "/")
            try:
                st = p.stat()
                hashwert = sha256(p)
            except OSError as e:
                print(f"Übersprungen ({e}): {rel}", file=sys.stderr)
                fehler += 1
                continue
            zeile = nach_pfad.get(rel)
            if zeile is None:
                zeile = {f: "" for f in FELDER}
                zeile.update(id=str(naechste_id), pfad=rel, status="neu")
                naechste_id += 1
                nach_pfad[rel] = zeile
                neu += 1
            zeile.update(
                dateiname=name,
                endung=p.suffix.lower(),
                groesse_bytes=str(st.st_size),
                geaendert_am=datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d"),
                sha256=hashwert,
            )

    # Exakte Dubletten: ältester Eintrag (kleinste id) gilt als Hauptdokument
    zeilen = sorted(nach_pfad.values(), key=lambda z: int(z["id"]))
    erstes = {}
    dubletten = 0
    for z in zeilen:
        h = z["sha256"]
        if h in erstes:
            z["dublette_von"] = erstes[h]
            if z["status"] in ("", "neu"):
                z["status"] = "dublette"
            dubletten += 1
        else:
            erstes[h] = z["id"]
            if z["status"] == "dublette":
                z["status"], z["dublette_von"] = "neu", ""

    args.inventar.parent.mkdir(parents=True, exist_ok=True)
    with open(args.inventar, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FELDER, extrasaction="ignore")
        w.writeheader()
        w.writerows(zeilen)

    print(f"Dateien gesamt: {len(zeilen)} | neu: {neu} | exakte Dubletten: {dubletten} | Fehler: {fehler}")
    print(f"Inventar: {args.inventar}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
