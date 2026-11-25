# Glossar: Wiki-Projekt Kienbacher

Die verbindliche Projektsprache. Pro Konzept **ein** Begriff, Alternativen stehen unter *Vermeiden*.
Gilt für Repo, Agentenregeln, Wiki-Seiten und Gespräche.
Allgemeine Branchenbegriffe (APQP, PPF, Nachdruck …) stehen im Lernlexikon `docs/branchenlexikon.md`.

Stand: 2026-11-25

---

## Bestand und Quellen

**Altbestand**:
Alle Dokumente und Ablagen, die es vor dem Wiki gibt (Fileserver, Teams-Ablagen, Papier).
_Vermeiden_: Altdaten, Altablage, Bestand

**Quelldokument**:
Ein einzelnes Dokument aus dem Altbestand mit genau einer Zeile im Inventar.
_Vermeiden_: Rohdokument, Originaldatei, „Quelle“ allein

**Inventar**:
Die Liste aller Quelldokumente mit Status und Metadaten (`inventar.csv`).
_Vermeiden_: Dokumentenliste, Index, Verzeichnis

**Extrakt**:
Die Markdown-Fassung eines Quelldokuments, auf der der Agent arbeitet.
_Vermeiden_: Konvertat, Abschrift, Textversion

**Dublette**:
Ein Quelldokument, das inhaltlich gleich oder nahezu gleich einem anderen ist; eines davon gilt als Hauptdokument.
_Vermeiden_: Kopie, Duplikat

## Ordnen und Einstufen

**Taxonomie**:
Die verbindliche Gliederung Abteilung → Themenbereich → Dokumenttyp samt Pflicht-Metadaten.
_Vermeiden_: Struktur, Kategorien, Ordnerstruktur

**Einordnung**:
Einem Quelldokument Begriffe aus der Taxonomie zuweisen.
_Vermeiden_: Klassifikation, Kategorisierung (zu nah an „Klassifizierung“)

**Zuordnung**:
Ein Quelldokument mit der Wiki-Seite verknüpfen, für die es als Beleg dient.
_Vermeiden_: Mapping, Verknüpfung

**Klassifizierung**:
Die Schutzstufe einer Information nach ISMS/TISAX: öffentlich, intern, vertraulich, streng vertraulich.
_Vermeiden_: Vertraulichkeit (als Feldname), Einstufung, Klassifikation

**Lenkungsstatus**:
Ob ein Quelldokument ein gelenktes Dokument, eine Aufzeichnung oder Erfahrungswissen ist.
_Vermeiden_: Dokumentstatus, Status (allein)

**Gelenktes Dokument**:
Ein Dokument, das im QM-System mit Version und Freigabe geführt wird; im Wiki wird es nur verlinkt, nie kopiert.
_Vermeiden_: offizielles Dokument, QM-Dokument, Vorgabedokument

**Aufzeichnung**:
Ein Nachweis, dass etwas getan wurde (Prüfprotokoll, 8D, Bemusterung); wird nicht migriert, nur ausgewertet und verlinkt.
_Vermeiden_: Record, Nachweisdokument

**Erfahrungswissen**:
Ungelenkter Inhalt, der ins Wiki übernommen wird: Erklärungen, Störungsbehebung, Lessons Learned.
_Vermeiden_: Know-how, „Wissen“ allein

## Wiki

**Wiki**:
Das Zielsystem für Erfahrungswissen bei Kienbacher; ergänzt das QM-System, ersetzt es nicht (vorgeschlagen, siehe Entscheidung 4).
_Vermeiden_: Wissenssammlung, Wissensdatenbank, Wissensportal

**Wiki-Seite**:
Eine veröffentlichte Seite zu genau einem Thema, einer Maschine oder einem Prozess.
_Vermeiden_: Artikel, Eintrag, Beitrag

**Seitenentwurf**:
Eine Wiki-Seite vor der Seitenfreigabe.
_Vermeiden_: Draft, Wiki-Entwurf

**Seitenverantwortliche/r**:
Die Fachperson, die eine Wiki-Seite inhaltlich verantwortet und freigibt.
_Vermeiden_: Owner, Autor, Pate

**Seitenfreigabe**:
Die Bestätigung durch die Seitenverantwortlichen, dass ein Seitenentwurf veröffentlicht werden darf.
_Vermeiden_: „Freigabe“ allein (verwechselbar mit PPF, Sonderfreigabe, Werkzeugfreigabe)

**Review-Datum**:
Datum, bis zu dem eine Wiki-Seite erneut fachlich überprüft werden muss (Feld `review_bis`).
_Vermeiden_: Prüfdatum (verwechselbar mit QS-Prüfungen), Ablaufdatum

**Offene Frage**:
Ein Widerspruch oder eine Lücke, die auf der Seite sichtbar bleibt, bis ein Mensch sie klärt.
_Vermeiden_: Todo, Anmerkung

**Pilotbereich**:
Die Abteilung, mit der das Wiki startet (voraussichtlich Produktion).
_Vermeiden_: Testbereich, Pilotabteilung

## Agentenarbeit

**Agent**:
Das KI-Werkzeug, das im Arbeitsbereich die Pipeline nach `AGENTS.md` abarbeitet.
_Vermeiden_: Bot, „die KI“ allein

**Arbeitsbereich**:
Der lokale Ordner außerhalb des Repos, in dem Quelldokumente, Extrakte und Seitenentwürfe liegen.
_Vermeiden_: Arbeitsordner, Workspace

**Arbeitspaket**:
Der Umfang einer Agentensitzung, z. B. 30–50 Quelldokumente oder ein Thema.
_Vermeiden_: Batch, Stapel, Sprint

**Gegenprüfung**:
Ein getrennter Durchlauf, der jeden Seitenentwurf gegen seine Quelldokumente und die Checkliste prüft.
_Vermeiden_: Prüfung, Review, QA (in der Firma meint „Prüfung“ die Qualitätsprüfung am Teil)

**Klärung**:
Status eines Quelldokuments oder Seitenentwurfs, über den ein Mensch entscheiden muss.
_Vermeiden_: Rückfrage, Eskalation

**Goldstandard**:
50–100 von Menschen eingeordnete Quelldokumente, gegen die die Einordnung des Agenten gemessen wird.
_Vermeiden_: Testset, Referenzliste

**Wiki-Gärtner**:
Der regelmäßige Agentenlauf nach der Migration, der Pflegebedarf meldet, aber nichts selbst ändert.
_Vermeiden_: Wartungsbot, Pflegeagent

---

## Offene Abgrenzungen (mit QMB/ISB klären)

1. **Einstelldatenblatt als Excel auf dem Fileserver**, nicht im QM-System, aber an der Maschine ausgehängt:
   gelenktes Dokument oder Erfahrungswissen? (Vermutung: faktisch gelenkt und gehört ins QM-System.)
2. **8D-Bericht:** Aufzeichnung (bleibt, wo er ist). Die Erkenntnis daraus wird Erfahrungswissen auf einer Lessons-Learned-Seite. So bestätigen?
3. **Arbeitsanweisung mit eingefügtem Ausschnitt einer Kundenzeichnung:** Erbt sie die Klassifizierung „streng vertraulich“?
4. **Werkzeug oder Maschine als eigene Seite?** Bekommt jedes Spritzgießwerkzeug eine Wiki-Seite, oder nur Teilefamilien?
