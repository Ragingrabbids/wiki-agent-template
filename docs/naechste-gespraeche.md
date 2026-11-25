# Nächste Gespräche: QMB, ISB, IT

Ziel: Die offenen Entscheidungen 4–8 aus `entscheidungen.md` vorbereiten. Die Gespräche lassen sich auch
zu einem Termin zusammenlegen, aber QM und Informationssicherheit haben unterschiedliche Fragen.

---

## 1. Qualitätsmanagementbeauftragte/r (QMB)

**Ziel:** Verstehen, wie das QM-System aufgebaut ist, und festlegen, wie Wiki und QMS zusammenspielen.

**Botschaft:** „Das Wiki soll das QM-System nicht ersetzen und keine ungelenkten Kopien erzeugen. Es soll
Erfahrungswissen sichern (7.1.6) und auf die gelenkten Dokumente verweisen – und uns bei der Umstellung
auf ISO 9001:2026 und die kommende IATF-Revision helfen.“

Fragen:
- **Welche QM-Software ist im Einsatz?** Was lenkt sie (Dokumente, Formulare, Aufzeichnungen, Maßnahmen)? Gibt es eine API, einen Export oder Teams/SharePoint-Anbindung?
- **Wie ist die Dokumentenstruktur aufgebaut?** (Prozesslandkarte, QM-Handbuch, Verfahrens-/Arbeitsanweisungen, Nummernschema)
- Wo liegen gelenkte Dokumente, wo Aufzeichnungen (Prüfprotokolle, 8D, Bemusterungen)?
- Wie werden technische Spezifikationen und Kundenzeichnungen gelenkt (IATF 7.5.3.2.2)?
- Wie werden kundenspezifische Anforderungen (CSR) verwaltet und bewertet?
- Wann sind die nächsten Audits (IATF, ISO 9001)? Gab es Feststellungen zu Dokumentation oder Wissen?
- Gibt es schon einen Plan für die Umstellung auf ISO 9001:2026 / IATF-Revision?
- Gibt es Lessons-Learned- oder 8D-Sammlungen, die heute ungenutzt sind?
- **Vorschlag Modell A** (Wiki ergänzt QMS, gelenkte Dokumente nur verlinkt) – passt das, oder soll das Wiki selbst gelenkt werden?

Ergebnis-Check:
- [ ] QM-Software + Zugriffsmöglichkeit
- [ ] Dokumentenstruktur verstanden
- [ ] Entscheidung oder Tendenz Wiki ↔ QMS
- [ ] Audittermine

---

## 2. Informationssicherheitsbeauftragte/r (ISB) – TISAX

**Ziel:** Klären, welche Daten mit welchen Werkzeugen verarbeitet werden dürfen – bevor der Agent ein Dokument anfasst.

**Botschaft:** „Ich will KI zum Sortieren und Entwerfen nutzen, aber nur innerhalb der Regeln des ISMS.
Kundenvertrauliches bleibt außen vor, bis Sie es freigeben.“

Fragen:
- **Welches TISAX-Label hat Kienbacher** (Vertraulichkeit hoch/strikt, Prototypenschutz, Verfügbarkeit)? Wann ist das nächste Assessment?
- **Gibt es eine Klassifizierungsrichtlinie?** Welche Stufen, wie werden Dokumente gekennzeichnet (z. B. Sensitivity Labels in M365)?
- **Gibt es eine KI-Richtlinie?** Welche KI-Dienste sind erlaubt (Copilot, ChatGPT, Claude …), für welche Stufen?
- Welche OEM-Vorgaben/NDAs schränken die Verarbeitung von Kundendaten ein?
- Darf der Agent lokal auf einer Kopie des Fileservers arbeiten? Wo muss diese Kopie liegen (verschlüsselt, Firmengerät)?
- Wie wird das Wiki als Asset ins ISMS aufgenommen (Eigentümer, Berechtigungen, Protokollierung)?

Ergebnis-Check:
- [ ] TISAX-Label + Termin
- [ ] Klassifizierungsstufen übernommen in `vorlagen/TAXONOMIE.md`
- [ ] Freigegebene KI-Dienste je Stufe
- [ ] Regeln für den lokalen Arbeitsbereich

---

## 3. IT

**Ziel:** Plattform und Infrastruktur klären.

Fragen:
- **SharePoint/Teams als Wiki-Plattform?** Gibt es schon Sites pro Abteilung, eine Berechtigungsstruktur, Sensitivity Labels?
- **Ist Microsoft 365 Copilot lizenziert oder geplant?** Wie ist der Stand bei Berechtigungen (übermäßige Freigaben vor Copilot bereinigen)?
- Welche Lizenz (Business/E3/E5)? Davon hängen Purview, Labels und SharePoint Advanced Management ab.
- Wo liegt der Altbestand (Fileserver, Laufwerke, Teams-Ablagen), wie groß ist er ungefähr?
- Darf ich für den Agenten Python/Werkzeuge auf einem Firmenrechner installieren? Welche KI-Zugänge (API-Schlüssel, Enterprise-Konto) sind möglich?
- Gibt es Kapazität für Self-Hosting, falls ISB externe KI für bestimmte Stufen ausschließt (lokales Modell)?

Ergebnis-Check:
- [ ] Plattform (Tendenz)
- [ ] Copilot-Status
- [ ] Größe/Ort des Altbestands
- [ ] Arbeitsumgebung für den Agenten

---

## Notizen

| Gespräch | Datum | Ergebnisse | Offene Punkte |
|---|---|---|---|
| QMB | | | |
| ISB | | | |
| IT | | | |
