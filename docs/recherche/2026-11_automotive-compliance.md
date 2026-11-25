# Recherche: Wiki und Automotive-Compliance (ISO 9001, IATF 16949, TISAX)

Stand: 25.11.2026 · Kurzrecherche, ersetzt keine Normlektüre. Normtexte selbst sind kostenpflichtig und liegen idealerweise beim QMB.

## Kontext Kienbacher

- Oswald Kienbacher GmbH, österreichischer Familienbetrieb (gegründet 1965), Pfarrkirchen bei Bad Hall (OÖ).
- Spritzgussteile aus technischen Kunststoffen (formstabil, hochtemperaturbeständig) für Automotive und Nutzfahrzeuge.
  Genannte Kunden u. a. BMW, VW, Volvo, Jaguar, Maserati, Lamborghini.
- Maschinenpark laut Firmenprofil: Schließkräfte 750–27.000 kN, Werkzeuggewichte bis 45 t.
- IT: Microsoft 365 und Teams. QM-System vorhanden (Name/Software noch klären).

Quellen: jobs.at Firmenprofil; automa.net Firmenprofil (Mitarbeiterzahl dort offensichtlich falsch).

## 1. Normenstand – gutes Timing

- **ISO 9001:2026** wurde am **16.09.2026** veröffentlicht. Übergangsfrist 3 Jahre: Zertifizierungsentscheidungen nach 2015 bis 31.03.2028, Ende der Übergangsfrist 30.09.2029. Keine grundlegende Strukturänderung; Prozessansatz, PDCA, risikobasiertes Denken bleiben.
- **IATF 16949** baut auf ISO 9001 auf und wird überarbeitet; Veröffentlichung laut TÜV SÜD voraussichtlich **Mitte 2027**.
- **Folge für das Projekt:** Das QMS muss in den nächsten 1–3 Jahren ohnehin auf die neuen Fassungen umgestellt werden. Ein sauber strukturiertes Wiki und eine Dokumenten-Inventur sind dafür eine direkte Vorarbeit (Gap-Analyse, Verweise auf Normkapitel). Das ist ein starkes Argument gegenüber der GF.

## 2. Wiki vs. gelenkte Dokumentation (ISO 9001 / IATF 16949 Kap. 7.5)

- „Dokumentierte Information“ im Normsinn ist nicht jede Information, sondern das, was die Norm fordert oder was die Organisation für die Wirksamkeit des QMS als notwendig festlegt.
- Für diese Dokumente gelten Lenkungsanforderungen: Verfügbarkeit und Eignung, Zugriff, Schutz, Aufbewahrung, Verteilung, Änderungslenkung (Versionen, Freigabe), Aufbewahrungsfristen. IATF fordert zusätzlich u. a. eine dokumentierte Aufbewahrungsrichtlinie für Aufzeichnungen (7.5.3.2.1) und die Lenkung technischer Spezifikationen/Kundenvorgaben (7.5.3.2.2).
- **Wissen der Organisation (7.1.6)** ist ausdrücklich mehr als dokumentierte Information: Erfahrung, Kontext, Lessons Learned. Genau hier ist das Wiki stark – und hier scheitern Wikis laut DQS typischerweise daran, dass sie verwaisen.

**Daraus folgt die wichtigste Architekturentscheidung:**

| Modell | Beschreibung | Vorteile | Nachteile |
|---|---|---|---|
| **A – Wiki ergänzt das QMS** (empfohlen als Start) | Gelenkte Dokumente (Verfahrens-/Arbeitsanweisungen, Prüfpläne, Produktionslenkungspläne, FMEA, Formulare) bleiben im QM-System. Das Wiki enthält Erfahrungswissen, Erklärungen, Störungsbehebung, Lessons Learned und **verlinkt** auf die gültige Version im QM-System. | Keine Doppelpflege, kein Auditrisiko durch ungelenkte Kopien, schnell startbar | Zwei Orte; Nutzer müssen wissen, wo was liegt |
| **B – Wiki wird Teil des gelenkten Systems** | Wiki-Seiten durchlaufen Freigabe, Versionierung, Änderungshistorie wie gelenkte Dokumente | Ein Ort für alles („eines für alles“) | Wiki-Plattform muss Lenkungsanforderungen nachweislich erfüllen; Auditor muss das akzeptieren; höherer Aufwand |
| **C – QM-System ablösen** | Wiki/SharePoint ersetzt das bestehende QM-Tool | Langfristig schlank | Großprojekt, nur mit QMB und Zertifizierer; nicht im Pilot |

**Faustregel für den Agenten:** Inhalte gelenkter Dokumente werden **nie** ins Wiki kopiert, sondern verlinkt. Ein abweichender Wert im Wiki gegenüber der gelenkten Arbeitsanweisung wäre ein Auditbefund.

## 3. TISAX / VDA ISA

- TISAX ist der Bewertungs- und Austauschmechanismus der Autoindustrie auf Basis des VDA-ISA-Katalogs. Aktuell gilt ISA 6 (seit 01.04.2024, Verweise auf ISO/IEC 27001:2022, stärkerer OT-Fokus nach IEC 62443). Ein Nachfolgekatalog **ISA 2027** mit vereinfachten Prototypenschutz-Labels ist angekündigt.
- Labels u. a. „Vertraulichkeit hoch“ / „Vertraulichkeit strikt“, „Verfügbarkeit“, Prototypenschutz. **Welches Label Kienbacher hat, klären** – davon hängen die Anforderungen ab.
- **Folgen für Wiki und KI (eigene Ableitung, mit ISB abstimmen):**
  - Das Wiki ist ein Informationswert (Asset) im ISMS: Klassifizierung, Berechtigungskonzept, Protokollierung.
  - **Kundendaten der OEMs** (Zeichnungen, 3D-Daten, Lastenhefte, Prototypinformationen, Kundennormen) sind typischerweise vertraulich bis streng vertraulich und unterliegen oft NDAs. Sie dürfen nur über **vom ISMS freigegebene** Dienste verarbeitet werden – auch von KI.
  - Für den KI-Agenten bedeutet das: Klassifizierung **vor** der Verarbeitung. Kundenvertrauliches wird zunächst nur inventarisiert (Metadaten), nicht inhaltlich an einen KI-Dienst geschickt, bis IT/ISB den Dienst freigegeben haben.
  - Eine **KI-Richtlinie** gehört ins ISMS (erlaubte Tools, erlaubte Klassifizierungsstufen je Tool). Das deckt sich mit der Art.-4-KI-Kompetenzpflicht (siehe Recherche 2026-11_ki-agenten).
  - Microsoft 365 Copilot ist bei sauberer Berechtigungslage und EU Data Boundary am leichtesten ins bestehende ISMS einzuordnen, weil Daten im bestehenden M365-Mandanten bleiben. Eigenständige Agenten-Werkzeuge (Claude, OpenAI) brauchen eine eigene Bewertung.

## 4. Kundenspezifische Anforderungen (CSR)

IATF 16949 verlangt, kundenspezifische Anforderungen (z. B. BMW, VW-Formel Q, Volvo) zu erfüllen. Diese ändern sich regelmäßig. **Idee für das Wiki:** je Kunde eine Seite „Kundenanforderungen“ mit Link zur aktuellen CSR-Quelle, Verantwortlichem, Prüfdatum und Übersicht, wo im QMS die Anforderung umgesetzt ist. Der Wiki-Gärtner-Lauf meldet abgelaufene Prüfdaten.

## 5. Offene Fragen an QMB / ISB / IT

- Welches QM-System (Software) ist im Einsatz? Gibt es eine API oder einen Export? Lenkt es auch Formulare und Aufzeichnungen?
- Wer ist QMB, wer Informationssicherheitsbeauftragter (ISB)? Gibt es externe Berater?
- Welches TISAX-Label, wann ist das nächste Assessment? Wann das nächste IATF-Audit?
- Gibt es bereits eine Klassifizierungsrichtlinie (öffentlich / intern / vertraulich / streng vertraulich) und eine KI-Richtlinie?
- Ist Copilot lizenziert oder geplant? Welche KI-Dienste sind freigegeben?
- Wie werden technische Spezifikationen und Kundenzeichnungen heute gelenkt (7.5.3.2.2)?
- Gibt es bereits Lessons-Learned- oder 8D-Ablagen, die ins Wiki gehören?

## Quellen

- TÜV SÜD: ISO 9001:2026 Revision; Pressemitteilung September 2026 (Hinweis auf IATF-Revision Mitte 2027)
- LRQA: ISO 9001:2026 ist in Kraft getreten (16.09.2026)
- GUTcert via pressebox (03.11.2026): Übergangsfristen ISO 9001:2026
- Advisera 16949 Academy: Documented information / document and record control in IATF 16949
- DQS: Was ist dokumentierte Information?; Knowledge organization in ISO 9001 (7.1.6)
- DQS: ISA-Katalog 6.0 ab 2024; ISA 2027 – Änderungen im TISAX-Katalog
- DNV: Transition to TISAX VDA ISA Version 6
