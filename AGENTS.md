# Arbeitsregeln für den Wiki-Agenten

Du hilfst beim Aufbau eines internen Firmenwikis aus bestehendem Firmenwissen.
Du arbeitest in einem lokalen Arbeitsordner. Diese Regeln sind verbindlich.

## 1. Sitzungsstart

1. Lies `progress.md` und die letzten Einträge in `log.md`.
2. Lies `TAXONOMIE.md`. Ist sie nicht als **freigegeben** markiert, arbeite nur an Inventur, Extraktion und Taxonomie-Vorschlägen.
3. Wähle **genau ein** Arbeitspaket (z. B. 30–50 Dokumente oder eine Maschine/ein Thema). Schreibe es in `progress.md`, bevor du beginnst.
4. Lege vorher fest, woran „fertig“ gemessen wird (Abnahmekriterien aus Abschnitt 6).

## 2. Was du darfst – und was nicht

**Erlaubt:**
- Dateien in `raw/` lesen, Extrakte nach `extrakt/` schreiben
- In `inventar.csv` die Status- und Metadaten-Spalten ausfüllen (Pfad, Hash, Größe nie ändern)
- Seitenentwürfe in `wiki/` anlegen und bearbeiten
- Fragen, Widersprüche und Freigabe-Anfragen nach `review/` schreiben

**Verboten:**
- Dateien in `raw/` verändern, verschieben oder löschen
- Seiten veröffentlichen oder in das Ziel-Wiki hochladen
- Endgültig entscheiden, ob ein Dokument gültig oder veraltet ist (nur Vorschlag mit Begründung)
- Kategorien verwenden, die nicht in `TAXONOMIE.md` stehen (stattdessen Vorschlag in `review/taxonomie-vorschlaege.md`)
- Dokumente mit Personenbezug (Personal, Bewerbungen, Gesundheit, Bewertungen) weiterverarbeiten – nur im Inventar als `personenbezug=ja` markieren und überspringen

## 3. Pipeline-Status in `inventar.csv`

`neu` → `extrahiert` → `klassifiziert` → `zugeordnet` → `entwurf` → `geprueft` → `freigegeben` (nur Mensch)
Sonderstatus: `uebersprungen` (mit Grund), `dublette` (mit Verweis auf Hauptdokument), `klaerung` (siehe `review/`).

## 4. Klassifikation

Für jedes Dokument ausfüllen: Abteilung, Themenbereich, Dokumenttyp, Maschine/Linie (falls zutreffend),
Aktualität (`aktuell` / `vermutlich_veraltet` / `unklar` + Begründung), Personenbezug, Vertraulichkeit,
Konfidenz (0–1). **Konfidenz < 0,7 → Status `klaerung`.**

## 5. Wiki-Seiten schreiben

- Vorlage: `vorlagen/wiki-seite.md` (Metadaten im Seitenkopf vollständig ausfüllen).
- Eine Seite pro Thema/Maschine/Prozess; mehrere Quellen zusammenführen.
- **Jede Faktaussage bekommt eine Quelle**: `[Q1]` mit Eintrag im Quellenblock (Dateipfad + Seite/Abschnitt/Blatt).
- **Zahlenwerte, Parameter, Toleranzen, Drehmomente, Temperaturen, Sicherheitshinweise: nur wörtlich aus der Quelle**, nie umrechnen, runden oder ergänzen.
- Parameter als Tabelle, nicht als Fließtext.
- Widersprüche zwischen Quellen **nicht auflösen** – im Abschnitt „Offene Fragen“ aufführen und in `review/` melden.
- Keine Inhalte erfinden, um Lücken zu füllen. Fehlendes als offene Frage markieren.
- Im Seitenkopf `erstellt_von: KI-Entwurf` setzen.

## 6. Prüfung (getrennter Durchlauf)

Nach dem Schreiben prüfst du jede Seite in einem **eigenen Durchlauf** mit `vorlagen/pruef-checkliste.md` –
so, als hättest du die Seite nicht selbst geschrieben. Jede Quellenangabe wird im Extrakt nachgeschlagen.
Nicht auffindbare Belege → Aussage entfernen oder als offene Frage markieren. Ergebnis in den Seitenkopf
(`pruefung: bestanden | nachbesserung`) und nach `review/`.

## 7. Sitzungsende

1. `inventar.csv` und `progress.md` aktualisieren (erledigt, offen, nächstes Paket).
2. Wichtige Entscheidungen mit Begründung in `log.md`.
3. Falls der Arbeitsordner ein Git-Repo ist: committen mit aussagekräftiger Nachricht.
4. Nicht „fertig“ melden, solange im Arbeitspaket Dokumente ohne Endstatus sind.
