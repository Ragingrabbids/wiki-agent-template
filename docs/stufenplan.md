# Stufenplan

## Phase 0 – Weichen stellen (2–4 Wochen)

- [x] Erstgespräch mit der GF (Stelle zugesagt, Umfang inkl. Compliance)
- [ ] Gespräche mit QMB und ISB (→ `naechste-gespraeche.md`): QM-System, gelenkte Dokumente, TISAX-Label, Klassifizierung, KI-Richtlinie
- [ ] **Entscheidung Wiki ↔ QM-System** (Modell A/B/C, siehe Recherche automotive-compliance)
- [ ] IT-Runde: M365/SharePoint ja/nein · erlaubte KI-Endpunkte (EU-Residenz? ZDR?) · Self-Hosting möglich?
- [ ] Betriebsrat und Datenschutz einbinden, KI-Betriebsvereinbarung anstoßen
- [ ] KI-Richtlinie + Kurzschulung dokumentieren (Art. 4 AI Act)
- [ ] Taxonomie Produktion: KI-Vorschlag aus Ordnerstruktur → Workshop mit 3–5 Fachleuten → freigeben
- [ ] Extraktions-Test mit 20–30 typischen Dokumenten

## Phase 1 – Pilot Produktion (8–12 Wochen)

**Variante A – M365-Umfeld:** Coding-Agent (Claude über EU-konformen Weg oder OpenAI mit EU-Residenz) im lokalen Arbeitsbereich → SharePoint-Site „Produktion“ mit Metadatenspalten. AI in SharePoint pflegt Metadaten nach, Copilot übernimmt später die Suche.

**Variante B – alles im Haus:** Docmost oder BookStack, n8n als Pipeline-Gerüst, Docling/Marker für die Extraktion, Ollama für Klassifikation und Zusammenfassung. Ein stärkeres Modell für die Entwürfe nur, wenn die IT es freigibt.

- [ ] Arbeitsbereich anlegen (`scripts/init_arbeitsbereich.py`)
- [ ] Inventur Produktionsordner (`scripts/inventur.py`)
- [ ] Goldstandard: 50–100 Dokumente von Hand klassifizieren
- [ ] Arbeitspakete abarbeiten (je 30–50 Dokumente oder eine Maschine)
- [ ] 100 % menschliche Freigabe im Pilot
- [ ] Auswertung der Messgrößen, Entscheidung über Ausweitung

## Phase 2 – Ausweitung (ab Monat 4)

- [ ] Weitere Abteilungen nacheinander, je mit Taxonomie-Erweiterung und benannten Seitenverantwortlichen
- [ ] Freigabe auf Stichproben umstellen, wo die Messwerte stabil sind (Sicherheit und Parameter bleiben bei 100 %)
- [ ] KI-Suche freischalten, erst nach Bereinigung der Berechtigungen

## Phase 3 – Betrieb und Übergabe

- [ ] Abteilungen pflegen selbst
- [ ] Wiki-Gärtner-Lauf wöchentlich
- [ ] Alte Doku läuft aus: nicht migrierter Altbestand bleibt archiviert und durchsuchbar

## Fallstricke

- Kein Multi-Agenten-Framework als Startpunkt (insbesondere kein AutoGen)
- Nicht alles auf einmal migrieren
- Keine Seite ohne verantwortliche Person und Review-Datum
- Copilot/KI-Suche nicht vor der Berechtigungsbereinigung freischalten
- Budgetgrenzen pro Agentenlauf setzen
