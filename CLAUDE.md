# Projektkontext: wiki-agent-template

Dieses Repo dient der **Recherche, Planung und Anleitung** für den KI-gestützten Aufbau eines Firmenwikis
(Firma mit ca. 100 Mitarbeitern, Pilotbereich voraussichtlich Produktion). Lukas arbeitet hier mit Claude
am Konzept, an Vorlagen und an Skripten.

## Wichtig

- **Keine Firmendaten in dieses Repo.** Quelldokumente, Inventare und Wiki-Entwürfe liegen nur lokal
  im Arbeitsordner (siehe README). Keine Beispiele mit echten Firmeninhalten committen.
- `AGENTS.md` im Repo-Stamm ist die **Vorlage der Agentenregeln** für den lokalen Arbeitsordner.
  Ihre Sitzungsabläufe (progress.md lesen usw.) gelten **nicht** für die Arbeit in diesem Repo.
  Änderungen an den Regeln werden hier gepflegt und per `scripts/init_arbeitsbereich.py` verteilt.

## Arbeitsweise im Repo

- Sprache: Deutsch.
- Entscheidungen in `docs/entscheidungen.md` festhalten (Tabelle fortschreiben).
- Neue Rechercheergebnisse als datierte Datei in `docs/recherche/` (`JJJJ-MM_thema.md`), mit Quellen.
- Skripte: nur Python-Standardbibliothek, sofern nicht anders entschieden; vor dem Commit mit Testdateien ausprobieren.
- Commit-Nachrichten auf Deutsch, kurz und aussagekräftig.

## Offene Punkte (Stand 2026-11-25)

Plattform (IT-Entscheidung), KI-Anbieter/Endpunkt (EU-Residenz/ZDR), Pilotbereich, Extraktionswerkzeug,
Betriebsvereinbarung – siehe `docs/entscheidungen.md`. Nächster Schritt: `docs/gf-gespraech.md` für das
Sondierungsgespräch mit der Geschäftsführung schärfen.
