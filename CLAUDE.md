# Projektkontext: wiki-agent-template

Dieses Repo dient der **Recherche, Planung und Anleitung** für den KI-gestützten Aufbau eines Firmenwikis
bei **Kienbacher** (Oswald Kienbacher GmbH, Pfarrkirchen bei Bad Hall, OÖ; Spritzgussteile aus technischen
Kunststoffen für die Automobilindustrie; ca. 100 Mitarbeiter). Lukas hat die Stelle für dieses Projekt.
Er arbeitet hier mit Claude am Konzept, an Vorlagen und an Skripten.

**Umfang:** Wiki/Wissensmanagement **und** Unterstützung der Compliance mit ISO 9001 (Revision 2026),
IATF 16949 und TISAX. Die Firma nutzt Microsoft 365 und Teams und hat ein QM-System (Software noch unbekannt).
Grundsatz: gelenkte Dokumente bleiben im QM-System und werden im Wiki nur verlinkt
(siehe `docs/recherche/2026-11_automotive-compliance.md`).

## Wichtig

- **Keine Firmendaten in dieses Repo.** Quelldokumente, Inventare und Wiki-Entwürfe liegen nur lokal
  im Arbeitsbereich (siehe README). Keine Beispiele mit echten Firmeninhalten committen.
- `AGENTS.md` im Repo-Stamm ist die **Vorlage der Agentenregeln** für den lokalen Arbeitsbereich.
  Ihre Sitzungsabläufe (progress.md lesen usw.) gelten **nicht** für die Arbeit in diesem Repo.
  Änderungen an den Regeln werden hier gepflegt und per `scripts/init_arbeitsbereich.py` verteilt.

## Arbeitsweise im Repo

- Sprache: Deutsch. Begriffe nach `GLOSSARY.md` verwenden; neue Projektbegriffe sofort dort eintragen.
- Entscheidungen in `docs/entscheidungen.md` festhalten (Tabelle fortschreiben).
- Neue Rechercheergebnisse als datierte Datei in `docs/recherche/` (`JJJJ-MM_thema.md`), mit Quellen.
- Skripte: nur Python-Standardbibliothek, sofern nicht anders entschieden; vor dem Commit mit Testdateien ausprobieren.
- Commit-Nachrichten auf Deutsch, kurz und aussagekräftig.

## Offene Punkte (Stand 2026-11-25)

Erstgespräch mit der GF hat stattgefunden. Offen: Verhältnis Wiki ↔ QM-System, Plattform, KI-Anbieter im
Rahmen von ISMS/TISAX, Klassifizierung, QM-Software, Pilotbereich – siehe `docs/entscheidungen.md`.
Nächster Schritt: Gespräche mit IT, QMB und ISB vorbereiten (`docs/naechste-gespraeche.md`).
