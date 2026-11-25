# Glossar: Automotive-Qualität, Informationssicherheit und Spritzguss

Für den Einstieg bei Kienbacher. Begriffe und Abkürzungen, die im Alltag eines Automotive-Zulieferers
ständig fallen. Sortiert nach Themen, innerhalb alphabetisch.
**★ = zuerst lernen** (fällt praktisch täglich).

> Hinweis: Firmen und Kunden verwenden teils eigene Bezeichnungen. Was hier steht, ist der Branchenstandard.
> Wo Kienbacher anders spricht, in der Spalte „Firmensprache“ von `vorlagen/TAXONOMIE.md` ergänzen.

---

## 1. Akteure in der Lieferkette

| Begriff | Bedeutung |
|---|---|
| ★ **OEM** | *Original Equipment Manufacturer* – der Fahrzeughersteller (BMW, VW, Volvo …). |
| ★ **Tier 1 / Tier 2 / Tier 3** | Zulieferstufen: Tier 1 liefert direkt an den OEM, Tier 2 an den Tier 1 usw. Ein Spritzgießer kann je nach Teil Tier 1 oder Tier 2 sein. |
| **AIAG** | *Automotive Industry Action Group* – nordamerikanischer Branchenverband; Herausgeber der „Core Tools“-Handbücher (APQP, PPAP, MSA, SPC). |
| ★ **VDA** | Verband der Automobilindustrie (Deutschland). Gibt die „VDA-Bände“ heraus (z. B. VDA 2, VDA 6.3) – im deutschsprachigen Raum oft maßgeblicher als AIAG. |
| **VDA QMC** | Qualitätsmanagement-Center des VDA; Schulungen, Zertifizierungen, Normen-Interpretationen. |
| **IATF** | *International Automotive Task Force* – Zusammenschluss von OEMs und Verbänden, Herausgeber der IATF 16949. |
| **ENX** | ENX Association – betreibt TISAX im Auftrag des VDA. |
| **SQE** | *Supplier Quality Engineer* – Lieferantenqualitätsingenieur des Kunden; dein Ansprechpartner beim OEM bei Qualitätsthemen. |
| **Resident Engineer** | Mitarbeiter des Zulieferers, der beim Kunden vor Ort sitzt und Probleme direkt klärt. |

## 2. Normen und Regelwerke

| Begriff | Bedeutung |
|---|---|
| ★ **ISO 9001** | Grundnorm für Qualitätsmanagementsysteme. Aktuelle Fassung **ISO 9001:2026** (veröffentlicht 16.09.2026, Übergangsfrist bis 30.09.2029). |
| ★ **IATF 16949** | Automotive-QM-Norm; ergänzt ISO 9001 um branchenspezifische Anforderungen. Pflicht für Serienlieferanten der meisten OEMs. Neufassung für ca. Mitte 2027 erwartet. |
| ★ **CSR** | *Customer Specific Requirements* – kundenspezifische Anforderungen, die zusätzlich zur IATF gelten (je OEM eigene Dokumente). |
| ★ **Formel Q** | Qualitätsanforderungen des VW-Konzerns an Lieferanten (Formel Q-Konkret, Formel Q-Fähigkeit, Formel Q-Neuteile). |
| **ISO 14001** | Umweltmanagementsystem. |
| **ISO 45001** | Arbeitsschutzmanagementsystem. |
| **ISO 50001** | Energiemanagementsystem. |
| **ISO/IEC 27001** | Informationssicherheits-Managementsystem (ISMS); Grundlage, auf die TISAX aufbaut. |
| **VDA 2** | VDA-Band „Sicherung der Qualität von Lieferungen“ – regelt die **PPF** (Produktionsprozess- und Produktfreigabe). |
| ★ **VDA 6.3** | Prozessaudit – bewertet Prozesse von der Entwicklung bis zur Serie anhand eines Fragenkatalogs. Kunden auditieren Lieferanten häufig danach. |
| **VDA 6.5** | Produktaudit – prüft fertige Produkte gegen Anforderungen. |
| **VDA 5** | Prüfprozesseignung (deutsches Pendant zu MSA). |
| **IMDS** | *International Material Data System* – Datenbank, in die Zulieferer die Werkstoffzusammensetzung ihrer Teile melden. Für Kunststoffteile Pflicht. |
| **REACH / RoHS** | EU-Chemikalienrecht bzw. Beschränkung gefährlicher Stoffe. Relevant für Werkstoffe und Zusätze. |

## 3. Qualitätsplanung und „Core Tools“

| Begriff | Bedeutung |
|---|---|
| ★ **APQP** | *Advanced Product Quality Planning* – strukturierte Qualitätsvorausplanung eines neuen Produkts in Phasen bis zum Serienstart. VDA-Gegenstück: Reifegradabsicherung (RGA). |
| ★ **FMEA** | Fehlermöglichkeits- und Einflussanalyse – systematische Risikoanalyse. **D-FMEA** für das Produktdesign, **P-FMEA** für den Fertigungsprozess (beim Spritzgießer meist P-FMEA). Aktueller Standard: AIAG-VDA-FMEA-Handbuch mit 7 Schritten; Priorisierung über die **Aufgabenpriorität (AP)** statt der früheren RPZ. |
| **RPZ** | Risikoprioritätszahl (alte FMEA-Bewertung: Bedeutung × Auftreten × Entdeckung). Taucht in älteren FMEAs noch auf. |
| ★ **Control Plan / PLP** | Produktionslenkungsplan – legt pro Prozessschritt fest, welche Merkmale wie, wie oft und womit geprüft werden und was bei Abweichung passiert. Wird aus der P-FMEA abgeleitet. |
| ★ **PPAP** | *Production Part Approval Process* (AIAG) – Serienfreigabe: Nachweis, dass der Serienprozess spezifikationsgerechte Teile liefert. |
| ★ **PPF** | Produktionsprozess- und Produktfreigabe nach VDA 2 – deutsches Gegenstück zu PPAP. |
| **EMPB** | Erstmusterprüfbericht – Messprotokoll der ersten Serienteile aus Serienwerkzeug und Serienprozess; Teil von PPF/PPAP. |
| ★ **Bemusterung** | Gesamter Vorgang, dem Kunden Muster mit Unterlagen zur Freigabe vorzulegen. |
| **Run@Rate** | Nachweis, dass der Prozess die geplante Stückzahl in der geplanten Zeit schafft. |
| ★ **SPC** | *Statistical Process Control* – statistische Prozessregelung (Regelkarten). |
| ★ **Cpk / Ppk** | Prozessfähigkeitsindizes: Wie gut passt die Prozessstreuung in die Toleranz? Typische Forderung: Cpk ≥ 1,33 in Serie, Ppk ≥ 1,67 bei Vorserie/Erstbemusterung (CSR prüfen). |
| **Cmk** | Maschinenfähigkeit – Kurzzeitfähigkeit nur der Maschine. |
| **MSA** | *Measurement System Analysis* – Messsystemanalyse: Ist das Messmittel geeignet? Z. B. **Gage R&R** (Wiederhol- und Vergleichspräzision). |
| ★ **Besondere Merkmale (BM)** | Merkmale mit Einfluss auf Sicherheit, Gesetzeskonformität oder Funktion; werden besonders überwacht und gekennzeichnet. Kürzel je Kunde, z. B. **CC** (*Critical Characteristic*), **SC** (*Significant Characteristic*), bei manchen OEMs eigene Symbole. |
| **SOP / EOP** | *Start / End of Production* – Serienstart bzw. Serienende eines Fahrzeugs oder Teils. |
| **Lastenheft / Pflichtenheft** | Anforderungen des Kunden bzw. die Antwort des Lieferanten, wie er sie umsetzt. |

## 4. Problemlösung und Verbesserung

| Begriff | Bedeutung |
|---|---|
| ★ **8D** | Problemlösungsmethode in 8 Disziplinen (Team, Problembeschreibung, Sofortmaßnahme, Ursache, Abstellmaßnahme, Umsetzung/Wirksamkeit, Vorbeugung, Abschluss). Standardantwort auf Kundenreklamationen. |
| ★ **Reklamation** | Beanstandung durch den Kunden; meist mit 8D-Forderung und Fristen (z. B. Sofortmaßnahme in 24 h). |
| **5-Why** | Ursachenanalyse durch wiederholtes „Warum?“. |
| **Ishikawa** | Ursache-Wirkungs-Diagramm (Fischgräte) – Ursachen nach Mensch, Maschine, Material, Methode, Milieu, Messung. |
| ★ **PPM** | *Parts per Million* – fehlerhafte Teile pro Million geliefert; zentrale Kennzahl der Lieferantenbewertung. |
| **Controlled Shipping (CS1/CS2)** | Eskalationsstufe: zusätzliche 100-%-Prüfung vor Auslieferung, bei CS2 durch einen externen Dienstleister. Vor allem bei US-OEMs gebräuchlich. |
| **Sonderfreigabe / Abweichgenehmigung** | Befristete Erlaubnis des Kunden, Teile mit einer bekannten Abweichung zu liefern. |
| ★ **KVP** | Kontinuierlicher Verbesserungsprozess (japanisch *Kaizen*). |
| **PDCA** | *Plan – Do – Check – Act*, Grundzyklus jedes Managementsystems. |
| **Poka-Yoke** | Fehlervermeidung durch Gestaltung (z. B. Vorrichtung, in die das Teil nur richtig herum passt). |
| **Lessons Learned** | Gesammelte Erfahrungen aus Projekten und Fehlern; von IATF ausdrücklich gefordert – **Kernstück fürs Wiki**. |

## 5. Audits und QM-System

| Begriff | Bedeutung |
|---|---|
| ★ **QMB** | Qualitätsmanagementbeauftragte/r. |
| ★ **QMH** | Qualitätsmanagementhandbuch. |
| ★ **Dokumentierte Information** | Normbegriff für Dokumente und Aufzeichnungen, die das QMS fordert oder die die Firma als notwendig festlegt. |
| ★ **Gelenktes Dokument** | Dokument mit Versionsstand, Freigabe und Änderungsverfolgung. Nur die gültige Version darf in Umlauf sein. |
| **Aufzeichnung** | Nachweis, dass etwas getan wurde (Prüfprotokoll, Schulungsnachweis). Wird nicht geändert, nur aufbewahrt. |
| **VA / AA / PA** | Verfahrensanweisung (Ablauf über Abteilungen) / Arbeitsanweisung (Tätigkeit am Arbeitsplatz) / Prüfanweisung. |
| **Prozesslandkarte** | Übersicht aller Prozesse der Firma (Management-, Kern-, Unterstützungsprozesse). |
| **Turtle-Diagramm** | Prozessbeschreibung in einer „Schildkröten“-Form: Eingaben, Ausgaben, mit wem, womit, wie, Kennzahlen. Beliebt in IATF-Audits. |
| **Systemaudit / Prozessaudit / Produktaudit** | IATF fordert intern alle drei Auditarten. |
| **1st / 2nd / 3rd Party Audit** | Internes Audit / Audit durch den Kunden / Zertifizierungsaudit durch eine Zertifizierungsstelle. |
| ★ **Abweichung (Major / Minor)** | Feststellung im Audit: Hauptabweichung (gefährdet die Zertifizierung) / Nebenabweichung. |
| **Managementbewertung** | Regelmäßige Bewertung des QMS durch die Geschäftsführung. |
| **PSB / PSCR** | Produktsicherheitsbeauftragter / *Product Safety & Conformity Representative* – Rolle für Produktsicherheit, von IATF und vielen OEMs gefordert. |
| **Notfallplan** | Von IATF geforderter Plan, wie die Belieferung bei Ausfällen (Maschine, Strom, IT, Lieferant) gesichert wird. |
| ★ **CAQ** | *Computer Aided Quality* – QM-Software (Reklamationen, Prüfplanung, Messmittel, Audits, Dokumentenlenkung). **Sehr wahrscheinlich ist euer „QM-System“ eine CAQ-Software.** |
| **DMS** | Dokumentenmanagementsystem. |
| **Prüfmittelmanagement** | Verwaltung und Kalibrierung aller Messmittel mit Fristen. |
| **Rückverfolgbarkeit** | Nachvollziehbarkeit, aus welcher Charge, Maschine, Schicht ein Teil stammt. |

## 6. Informationssicherheit (TISAX)

| Begriff | Bedeutung |
|---|---|
| ★ **TISAX** | *Trusted Information Security Assessment Exchange* – Prüf- und Austauschverfahren für Informationssicherheit in der Autoindustrie. Ergebnis wird mit dem Kunden geteilt, nicht als Zertifikat ausgestellt. |
| ★ **VDA ISA** | *Information Security Assessment* – der Fragenkatalog, nach dem TISAX prüft (aktuell Version 6, Nachfolger „ISA 2027“ angekündigt). |
| ★ **ISMS** | Informationssicherheits-Managementsystem. |
| ★ **ISB** | Informationssicherheitsbeauftragte/r (englisch CISO/ISO). |
| **Label** | Umfang des TISAX-Ergebnisses, z. B. Vertraulichkeit hoch / strikt, Verfügbarkeit, Prototypenschutz, Datenschutz. |
| **AL2 / AL3** | *Assessment Level* – Prüftiefe: AL2 = Plausibilitätsprüfung (Dokumente, Interviews, oft remote), AL3 = gründliche Prüfung vor Ort. |
| ★ **Klassifizierung** | Einstufung von Informationen nach Schutzbedarf (z. B. öffentlich, intern, vertraulich, streng vertraulich). |
| **Prototypenschutz** | Schutzanforderungen für Teile, Fahrzeuge und Daten vor Serienstart (Fotografierverbot, abgeschlossene Bereiche …). |
| ★ **NDA** | *Non-Disclosure Agreement* – Geheimhaltungsvereinbarung mit dem Kunden. |
| **OT** | *Operational Technology* – Produktions-IT (Maschinensteuerungen, Netzwerke in der Halle); seit ISA 6 stärker im Fokus. |
| **Asset** | Informationswert im ISMS (Daten, Systeme, Geräte) mit Eigentümer und Schutzbedarf. |

## 7. Spritzguss – Maschine und Werkzeug

| Begriff | Bedeutung |
|---|---|
| ★ **Spritzgießmaschine (SGM)** | Besteht aus Schließeinheit (hält das Werkzeug zu) und Spritzeinheit (plastifiziert und spritzt das Material ein). |
| ★ **Schließkraft** | Kraft, mit der das Werkzeug zugehalten wird (in kN; Kienbacher: 750–27.000 kN). Bestimmt, welche Teile auf welcher Maschine laufen. |
| ★ **Spritzgießwerkzeug („Form“)** | Das teilespezifische Werkzeug, in dem das Teil geformt wird. Oft Kundeneigentum, teuer und langlebig. |
| ★ **Kavität / Nest** | Formhohlraum für ein Teil. Ein 4-fach-Werkzeug hat 4 Kavitäten. |
| **Trennebene** | Fläche, an der sich die Werkzeughälften öffnen. |
| ★ **Anguss** | Kanal, über den die Schmelze ins Teil fließt; **Kaltkanal** (erstarrt mit, wird abgetrennt) oder **Heißkanal** (bleibt flüssig, kein Angussabfall). |
| **Anschnitt** | Übergang vom Angusskanal ins Teil. |
| **Auswerfer** | Stifte/Platten, die das Teil aus dem Werkzeug drücken. |
| **Schieber** | Bewegliche Werkzeugteile für Hinterschnitte. |
| **Entformungsschräge** | Leichte Neigung der Teilwände, damit das Teil sich lösen lässt. |
| **Temperiergerät** | Hält das Werkzeug über Wasser oder Öl auf Temperatur. |
| **Trockner** | Entzieht dem Granulat vor der Verarbeitung Feuchte. |
| **Handling / Roboter** | Entnimmt Teile, legt Einlegeteile ein, stapelt ab. |
| **Rüsten** | Umbau der Maschine auf ein anderes Werkzeug/Teil. **SMED** = Methode zur Rüstzeitverkürzung. |

## 8. Spritzguss – Prozess

| Begriff | Bedeutung |
|---|---|
| ★ **Zyklus / Zykluszeit** | Ein kompletter Ablauf (Schließen, Einspritzen, Nachdruck, Kühlen, Öffnen, Auswerfen) bzw. dessen Dauer. Bestimmt Kosten und Ausbringung. |
| **Dosieren / Plastifizieren** | Aufschmelzen und Bereitstellen der Schmelzemenge durch die drehende Schnecke. |
| **Staudruck** | Gegendruck beim Dosieren; beeinflusst Homogenität der Schmelze. |
| **Einspritzen** | Füllen der Kavität mit Schmelze (geschwindigkeitsgeregelt). |
| ★ **Umschaltpunkt** | Moment, in dem vom Einspritzen auf den Nachdruck umgeschaltet wird. Einer der wichtigsten Prozessparameter. |
| ★ **Nachdruck** | Druck nach dem Füllen, der die Schwindung beim Abkühlen ausgleicht. |
| **Massepolster** | Restschmelze vor der Schnecke am Ende des Nachdrucks; Kontrollgröße für Prozessstabilität. |
| **Kühlzeit** | Zeit, bis das Teil formstabil entformt werden kann; oft größter Anteil der Zykluszeit. |
| **Massetemperatur / Werkzeugtemperatur** | Temperatur der Schmelze bzw. der Werkzeugoberfläche; beeinflussen Oberfläche, Maßhaltigkeit, Verzug. |
| ★ **Schwindung** | Volumenabnahme beim Abkühlen; muss im Werkzeug vorgehalten werden. |
| ★ **Einstelldatenblatt** | Dokumentierte Maschineneinstellung für ein Werkzeug/Teil. Meist gelenkt. |
| **Prozessfenster** | Bereich der Parameter, in dem gute Teile entstehen. |
| **Restfeuchte** | Feuchte im Granulat vor der Verarbeitung; zu hoch → Schlieren, Festigkeitsverlust (v. a. bei PA, PBT, PC). |
| **Konditionieren** | Gezielte Feuchtigkeitsaufnahme von PA-Teilen nach dem Spritzen, damit sie zäh werden und maßlich stabil sind. |
| **Mahlgut / Regranulat** | Zerkleinerte Angüsse oder Ausschussteile, die wieder zugemischt werden; Anteil oft vom Kunden begrenzt. |
| **Masterbatch** | Farb- oder Additivkonzentrat, das dem Granulat zugemischt wird. |
| **2K / Mehrkomponenten** | Teil aus zwei Werkstoffen oder Farben in einem Werkzeug. |
| **Umspritzen / Insert** | Einlegeteile (z. B. Metallbuchsen) werden mit Kunststoff umspritzt. |
| **GIT / WIT** | Gas- bzw. Wasserinjektionstechnik – Hohlräume in dicken Teilen. |

## 9. Spritzguss – Fehlerbilder

| Begriff | Bedeutung |
|---|---|
| ★ **Einfallstellen** | Mulden an dicken Stellen durch Schwindung (zu wenig Nachdruck/Nachdruckzeit). |
| ★ **Grat / Schwimmhaut** | Dünne Materialfahne an der Trennebene (Schließkraft zu gering, Werkzeug verschlissen, Druck zu hoch). |
| ★ **Unvollständige Füllung** | Teil nicht ganz ausgespritzt (englisch *short shot*). |
| ★ **Verzug** | Teil verformt sich nach dem Entformen (ungleiche Schwindung, Faserorientierung). |
| **Lunker** | Hohlräume im Inneren dicker Wände. |
| **Schlieren** | Streifen auf der Oberfläche: Feuchte-, Brand-, Farb- oder Glasfaserschlieren. |
| **Bindenaht** | Linie, wo zwei Fließfronten zusammentreffen; optische und mechanische Schwachstelle. |
| **Dieseleffekt / Brandstellen** | Eingeschlossene Luft wird komprimiert und verbrennt das Material (Entlüftung mangelhaft). |
| **Freistrahl** | Schmelze schießt wurmartig in die Kavität statt gleichmäßig zu fließen. |
| **Weißbruch / Spannungsrisse** | Risse oder Aufhellung durch innere Spannungen oder beim Entformen. |

## 10. Werkstoffe (Kurzzeichen)

| Kürzel | Werkstoff | Typisch für |
|---|---|---|
| **PA6 / PA66** | Polyamid | Technische Teile, Halter, Gehäuse; nimmt Feuchte auf |
| **PPA / PA6T** | Polyphthalamid (teilaromatisches PA) | Hohe Temperaturen im Motorraum |
| **PBT** | Polybutylenterephthalat | Steckverbinder, Gehäuse |
| **PPS** | Polyphenylensulfid | Sehr temperatur- und chemikalienbeständig |
| **PEEK** | Polyetheretherketon | Hochleistungskunststoff, sehr teuer |
| **POM** | Polyoxymethylen | Zahnräder, Gleitteile |
| **PP** | Polypropylen | Innenraum, Verkleidungen, günstig |
| **PC / PC-ABS** | Polycarbonat / Blend mit ABS | Sichtteile, Innenraum |
| **TPE** | Thermoplastisches Elastomer | Dichtungen, Soft-Touch (oft 2K) |
| **GF30, GF50 …** | 30 % bzw. 50 % Glasfaser | Steifigkeit, Formstabilität; mehr Verschleiß am Werkzeug, Verzug durch Faserorientierung |

## 11. Produktion, Logistik, IT

| Begriff | Bedeutung |
|---|---|
| ★ **OEE** | *Overall Equipment Effectiveness* – Gesamtanlageneffektivität = Verfügbarkeit × Leistung × Qualität. |
| **5S** | Arbeitsplatzorganisation: Sortieren, Systematisieren, Säubern, Standardisieren, Selbstdisziplin. |
| **BDE / MDE** | Betriebs- bzw. Maschinendatenerfassung. |
| **MES** | *Manufacturing Execution System* – Fertigungssteuerung zwischen ERP und Maschine. |
| ★ **ERP** | Unternehmenssoftware für Aufträge, Material, Einkauf (z. B. SAP, proALPHA, abas). |
| **AV** | Arbeitsvorbereitung. |
| **JIT / JIS** | *Just in Time* / *Just in Sequence* – Lieferung zum Bedarfszeitpunkt bzw. in Einbaureihenfolge. |
| **Lieferabruf** | Bedarfsmeldung des Kunden, meist per **EDI** (elektronischer Datenaustausch). |
| **KLT / GLT** | Klein- bzw. Großladungsträger (genormte Mehrwegbehälter). |
| **Warenanhänger (VDA 4902 / GTL)** | Standardisiertes Behälteretikett für Lieferungen. |

---

## Lernvorschlag

1. **Woche 1:** alle ★-Begriffe. Danach den Kienbacher-Prozess „Neues Teil bis Serie“ einmal mit APQP → FMEA → Control Plan → Bemusterung/PPF → SOP durchgehen.
2. **In der Halle:** Fehlerbilder am echten Teil zeigen lassen (Grenzmuster) und den Zyklus an einer Maschine mitverfolgen.
3. **Mit dem QMB:** Prozesslandkarte, QMH und eine typische 8D durchsprechen. Dabei die Firmensprache notieren.
4. **Mit dem ISB:** TISAX-Label und Klassifizierungsrichtlinie.
