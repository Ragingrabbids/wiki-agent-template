# Konzept: KI-gestützter Wiki-Aufbau

## Architektur

```
 Fileserver / Altbestand        Lokaler Arbeitsbereich (Markdown, lokales Git)        Ziel-Wiki
 ───────────────────────        ──────────────────────────────────────────────        ─────────
  Word, Excel, PDF, Scans  ──►  raw/ ─► extrakt/ ─► inventar.csv ─► wiki/ ─► review/  ──►  SharePoint /
        (unverändert)                    ▲                                    │  Freigabe     Docmost /
                                         │      AGENTS.md · TAXONOMIE.md      │  durch        BookStack …
                                         └──── progress.md · log.md ◄─────────┘  Fachperson   (per API)
```

- **Steuernder Agent:** ein Agent (z. B. Claude Code), der pro Sitzung ein Arbeitspaket abarbeitet.
- **Hilfsschritte:** parallelisierbar ist nur Extraktion und Einordnung (Stapelverarbeitung, ggf. lokales Modell).
- **Schreiben und Zusammenführen:** immer ein Agent mit Gesamtüberblick, weil Konsistenz zählt.
- **Prüfer:** eigener Durchlauf mit `vorlagen/gegenpruef-checkliste.md`.
- **Mensch:** Taxonomie-Freigabe, Klärungsfälle, Gültigkeit, Veröffentlichung.

## Pipeline

| Schritt | Wer | Ergebnis | Status in Inventar |
|---|---|---|---|
| 0 Taxonomie & Regeln | Mensch (KI schlägt vor) | `TAXONOMIE.md` freigegeben | – |
| 1 Inventur | Skript `inventur.py` | `inventar.csv`, exakte Dubletten | `neu` / `dublette` |
| 2 Extraktion | Konverter (Docling/Marker/…) | `extrakt/*.md` | `extrahiert` |
| 3 Einordnung | Agent / lokales Modell | Metadaten + Konfidenz | `eingeordnet` / `klaerung` |
| 4 Dubletten & Veraltetes | Agent (Vorschlag) + Fachabteilung | Cluster, vermutlich gültige Version | `dublette` / `klaerung` |
| 5 Zuordnung & Entwurf | Agent | `wiki/*.md` mit Quellen | `zugeordnet` / `entwurf` |
| 6 Gegenprüfung | Agent (getrennter Durchlauf) | Prüfvermerk | `gegengeprueft` |
| 7 Seitenfreigabe & Veröffentlichung | Fachperson | Seite im Ziel-Wiki | `freigegeben` |

## Messgrößen im Pilot

- Einordnungsgenauigkeit gegen 50–100 Golddokumente (Ziel > 90 % bei Abteilung/Dokumenttyp)
- Anteil korrekt belegter Aussagen (Stichprobe)
- Zeitaufwand der Fachleute pro freigegebener Seite
- Anteil Dokumente in `klaerung`

## Betrieb nach der Migration („Wiki-Gärtner“)

Der Agent prüft wöchentlich auf abgelaufene Review-Daten, tote Links, neue Dateien ohne Wiki-Zuordnung und Widersprüche zwischen Seiten. Das Ergebnis ist eine **Aufgabenliste an die Verantwortlichen**, keine automatische Änderung.
