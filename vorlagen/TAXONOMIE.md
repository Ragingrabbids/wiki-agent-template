---
status: ENTWURF          # ENTWURF | FREIGEGEBEN – erst nach Workshop mit Fachleuten, QMB und ISB auf FREIGEGEBEN setzen
bereich: Produktion (Spritzguss)
freigegeben_von:
freigegeben_am:
version: 0.2
---

# Taxonomie – Pilotbereich Produktion (Spritzguss, Automotive)

> Entwurf als Diskussionsgrundlage. Vor dem Einsatz mit Fachleuten aus Produktion/Werkzeugbau,
> dem QMB und dem ISB abstimmen. Der Agent darf nur Begriffe aus dieser Datei verwenden.
> Bezeichnungen an die Firmensprache und das bestehende QM-System anpassen.

## Ebene 1 – Abteilung

- Produktion
- Werkzeugbau / Werkzeuginstandhaltung
- Instandhaltung (Maschinen, Peripherie)
- Qualität
- Arbeitssicherheit & Umwelt
- *(weitere Abteilungen erst in Phase 2: Projektmanagement/APQP, Einkauf, Logistik, Vertrieb, IT)*

## Ebene 2 – Themenbereich

| Kürzel | Themenbereich | Beispiele |
|---|---|---|
| MAS | Maschinen & Peripherie | Spritzgießmaschinen, Handling/Roboter, Temperiergeräte, Trockner, Fördertechnik |
| WZ | Spritzgießwerkzeuge | Werkzeugdaten, Wartung, Änderungen, Heißkanal, Einbau/Rüsten |
| PRZ | Prozess & Einstellung | Einstelldaten, Anfahren, Produktwechsel, Prozessfenster, Nacharbeit |
| MAT | Werkstoffe | Technische Kunststoffe, Trocknung, Mahlgut, Farbe/Masterbatch, Datenblätter |
| QS | Prüfung & Qualität | Prüfanweisungen, Messmittel, Grenzmuster, Merkmale (inkl. besondere Merkmale) |
| STO | Störungen & Fehlerbilder | Fehlerkatalog (z. B. Einfallstellen, Grat, Verzug, Schlieren), Ursachen, Maßnahmen |
| KUN | Kunden & Produkte | Kundenspezifische Anforderungen (CSR), Teilefamilien, Verpackung |
| SIC | Sicherheit & Umwelt | Betriebsanweisungen, Gefährdungsbeurteilungen, Abfall |
| ORG | Organisation | Schichtübergabe, Zuständigkeiten, Abläufe |
| LL | Lessons Learned | 8D-Erkenntnisse, Bemusterungen, Projekte, Anläufe |

## Ebene 3 – Dokumenttyp

Arbeitsanweisung · Prüfanweisung · Prüfprotokoll · Einstelldatenblatt · Produktionslenkungsplan (Control Plan) ·
FMEA · Werkzeugdokumentation · Maschinendokumentation · Fehlerkatalog/Störungsbehebung · 8D-Bericht ·
Bemusterung (PPAP/VDA 2) · Kundenvorgabe/Zeichnung · Schulungsunterlage · Formular/Vorlage · Bericht · Präsentation · Sonstiges

## Lenkungsstatus (wichtig für IATF 16949, Kap. 7.5)

| Wert | Bedeutung | Umgang im Wiki |
|---|---|---|
| gelenkt | Dokument ist im QM-System gelenkt (Version, Freigabe) | **Nur verlinken**, Inhalt nie kopieren; Wiki darf erklären, worauf es ankommt |
| aufzeichnung | Nachweis/Record (Prüfprotokoll, 8D, Bemusterung) | Nicht migrieren; nur auswerten (Lessons Learned) und verlinken |
| wissen | Erfahrungswissen, ungelenkt | Wird Wiki-Inhalt |
| unklar | Status nicht erkennbar | Klärung mit QMB |

## Klassifizierung (an ISMS/TISAX-Richtlinie der Firma anpassen)

| Stufe | Beispiele | KI-Verarbeitung |
|---|---|---|
| öffentlich | Prospekte, Website | erlaubt |
| intern | Allgemeine Abläufe, Schulungen | nur über freigegebene Dienste |
| vertraulich | Prozessdaten, Kalkulation, interne Berichte | nur über freigegebene Dienste mit passendem Schutzniveau |
| streng vertraulich | OEM-Zeichnungen/CAD, Lastenhefte, Prototypinformationen, NDA-Inhalte | **keine** Inhaltsverarbeitung durch KI, bis ISB es ausdrücklich freigibt; nur Metadaten inventarisieren |

## Pflicht-Metadaten jeder Wiki-Seite

| Feld | Werte |
|---|---|
| verantwortlich | Name/Rolle der fachverantwortlichen Person |
| gueltig_ab | Datum |
| review_bis | Datum (Standard: +12 Monate; Sicherheit, CSR: +6 Monate) |
| status | entwurf · gueltig · veraltet |
| klassifizierung | öffentlich · intern · vertraulich · streng_vertraulich |
| lenkung_verweise | Links auf gelenkte Dokumente im QM-System |
| normbezug | optional, z. B. IATF 16949 8.5.1.1; VDA ISA 1.3 |
| kunde | optional |
| maschine / werkzeug | optional, aus Listen unten |
| quellen | Liste der Quelldokumente |

## Maschinen / Werkzeuge

- *(Maschinenliste mit Produktion ergänzen – Nummer, Schließkraft, Hersteller)*
- *(Werkzeugnummern-Schema klären; Werkzeugdaten nicht duplizieren, auf Werkzeugverwaltung verlinken)*

## Synonyme / Firmensprache

| Begriff im Altbestand | Normbegriff |
|---|---|
| *(z. B. „AA“)* | Arbeitsanweisung |
| *(z. B. „PLP“, „Control Plan“)* | Produktionslenkungsplan |
| *(z. B. „Form“)* | Spritzgießwerkzeug |
