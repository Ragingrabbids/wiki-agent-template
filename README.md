# wiki-agent-template

Recherche, Vorgehen und Agenten-Anweisungen für den KI-gestützten Aufbau eines Firmenwikis
(Kuratierung von Altbestand, Zuordnung nach Taxonomie, Seitenentwürfe mit Quellenpflicht, menschliche Freigabe).

> **Wichtig:** Dieses Repo enthält **keine Firmendaten**. Es enthält nur Recherche, Regeln, Vorlagen und Skripte.
> Quelldokumente, Inventar und Wiki-Entwürfe liegen **lokal** in einem separaten Arbeitsbereich (siehe unten)
> und werden nie hierher committet.

## Inhalt

| Pfad | Zweck |
|---|---|
| `GLOSSARY.md` | Verbindliche Projektsprache (ein Begriff pro Konzept) |
| `AGENTS.md` | Vorlage der verbindlichen Arbeitsregeln für den KI-Agenten im Arbeitsbereich (Claude, Codex o. ä.) |
| `CLAUDE.md` | Projektkontext für die Arbeit mit Claude **in diesem Repo** |
| `docs/recherche/` | Rechercheergebnisse (Stand der Technik, Werkzeuge, Recht) |
| `docs/konzept.md` | Architektur und Pipeline |
| `docs/stufenplan.md` | Phasen von der Vorbereitung bis zum Betrieb |
| `docs/gf-gespraech.md` | Leitfaden Gespräch mit der Geschäftsführung (Erstgespräch erledigt) |
| `docs/branchenlexikon.md` | Lernhilfe: allgemeine Fachbegriffe und Abkürzungen: Automotive-QM, TISAX, Spritzguss, Werkstoffe |
| `docs/naechste-gespraeche.md` | Fragen und Ergebnis-Checks für QMB, ISB (TISAX) und IT |
| `docs/entscheidungen.md` | Offene und getroffene Entscheidungen |
| `vorlagen/` | Vorlagen für Taxonomie, Inventar, Wiki-Seite, Fortschritt, Gegenprüf-Checkliste |
| `scripts/` | Hilfsskripte (Arbeitsbereich anlegen, Inventur mit Dublettenerkennung) |

## Lokaler Arbeitsbereich

Der Agent arbeitet in einem Ordner **außerhalb** dieses Repos, z. B. `D:\Wiki-Arbeitsbereich\produktion\`.
Anlegen mit:

```bash
python scripts/init_arbeitsbereich.py "D:/Wiki-Arbeitsbereich/produktion"
```

Danach sieht er so aus:

```
produktion/
├── AGENTS.md          # Kopie der Regeln (Agent startet in diesem Ordner)
├── TAXONOMIE.md       # aus vorlagen/, von Menschen freigegeben
├── inventar.csv       # eine Zeile pro Quelldokument, Status-Spalten
├── progress.md        # Fortschritt pro Sitzung
├── log.md             # Entscheidungen und Begründungen
├── raw/               # Verweise/Kopien der Originale – NIE verändern
├── extrakt/           # Markdown-Extrakte der Quelldokumente
├── wiki/              # Seitenentwürfe
└── review/            # Warteschlange für Klärung und Seitenfreigabe
```

Der Arbeitsbereich kann ein eigenes, **lokales** Git-Repo sein (ohne Remote), damit jeder Agentenschritt nachvollziehbar committet wird.

## Inventur

```bash
python scripts/inventur.py "\\\\fileserver\\Produktion" "D:/Wiki-Arbeitsbereich/produktion/inventar.csv"
```

Erfasst Pfad, Typ, Größe, Änderungsdatum und SHA-256-Hash; markiert exakte Dubletten. Nur Python-Standardbibliothek.

## Grundsätze (Kurzfassung)

1. Ein steuernder Agent, feste Pipeline, kein Agentenschwarm.
2. Fortschritt steht in Dateien, nicht im Kopf des Agenten.
3. Jede Aussage im Wiki hat eine Quelle; Werte nur wörtlich aus der Quelle.
4. Getrennte Gegenprüfung (Ersteller ≠ Prüfer).
5. Veröffentlichen, Löschen und „gültig vs. veraltet“ entscheidet immer ein Mensch.
