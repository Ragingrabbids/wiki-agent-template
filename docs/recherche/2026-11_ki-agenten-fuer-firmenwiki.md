# Recherche: KI-Agenten für den Aufbau eines Firmenwikis

Stand: 25.11.2026 · Zusammenfassung der Deep-Research-Ergebnisse. Produkte ändern sich monatlich – vor Entscheidungen Herstellerseiten prüfen.

## Kernaussage

Die beste Lösung ist derzeit kein Schwarm autonomer Agenten, sondern eine **feste, wiederholbare Pipeline mit einem steuernden Agenten**.
Dazu kommen Gedächtnis in Dateien, ein getrennter Prüfschritt und eine menschliche Freigabe vor jeder Veröffentlichung.
Realistisch nimmt die KI 70–90 % der Fleißarbeit ab (sichten, sortieren, entwerfen). Gültigkeit, Struktur und Veröffentlichung bleiben beim Menschen.

## Stand der Technik

- **Workflow vor Agent:** Bekannte Abläufe (Inventur → Extraktion → Klassifikation → Entwurf → Freigabe) fest vorgeben. Agentische Freiheit nur dort, wo Urteil gefragt ist.
- **Ein Agent zuerst:** OpenAI („A Practical Guide to Building Agents“) und Anthropic empfehlen, erst einen Agenten auszureizen. Multi-Agent lohnt nur bei echt paralleler Arbeit (z. B. Massen-Extraktion). Laut Anthropic verbrauchen Agenten etwa 4× und Multi-Agenten-Systeme etwa 15× so viele Tokens wie Chats.
- **Unabhängige Forschung (MAST, UC Berkeley, NeurIPS 2025):** In 7 Multi-Agenten-Frameworks lagen die Fehlerraten bei 41–86,7 %. Die Ursachen sind meist Spezifikation/Design, Abstimmung zwischen Agenten und fehlende Verifikation.
- **Harness-Muster (Anthropic 2025/2026):** Zu Beginn wird eine vollständige Aufgabenliste angelegt. Pro Sitzung erledigt der Agent ein Arbeitspaket und schreibt eine Fortschrittsdatei, danach wird in Git committet. Ein **getrennter Evaluator** prüft, weil Agenten ihre eigene Arbeit zu positiv bewerten.
- **„Stille Fehler“:** Plausible, aber falsche Ergebnisse fallen oft erst Wochen später und meist durch Menschen auf. Für ein Wiki ist das das Hauptrisiko.
- **LLM-Wiki-Muster (Karpathy, April 2026):** Unveränderliche Rohquellen (`raw/`), ein vom Agenten gepflegtes Markdown-Wiki (`wiki/`) und eine Regeldatei (`AGENTS.md`/`CLAUDE.md`). Für Firmen kommen Berechtigungen, Freigaben und Quellenpflicht hinzu.

## Werkzeuge (Kurzbewertung)

| Werkzeug | Stärke | Datenschutz-Hinweis |
|---|---|---|
| Claude Code / Claude mit Skills, MCP | Stärkstes Werkzeug für dateilastige Agentenarbeit | Keine EU-Residenz direkt bei Anthropic. EU-Verarbeitung nur über AWS Bedrock / Google Cloud EU. ZDR nur API bzw. qualifizierte Enterprise-Konten |
| OpenAI Codex / API / ChatGPT Enterprise | Ähnlich stark | EU-Datenresidenz für API und Enterprise verfügbar (Vertragsdetails prüfen) |
| M365 Copilot / AI in SharePoint / Copilot Studio | Metadaten, Klassifikation und Suche integriert, berechtigungsgetreu | EU Data Boundary. Claude-Modelle in Copilot ab Dez. 2026 innerhalb der EU Data Boundary |
| Microsoft Agent Framework (Nachfolger AutoGen/Semantic Kernel) | C#/.NET verfügbar, v1.0 seit April 2026 | Abhängig vom Modellendpunkt. **AutoGen ist archiviert** und nicht mehr für Neuprojekte geeignet |
| n8n | Visuelle Pipeline, self-hosted möglich | Kann komplett im Haus laufen |
| Dify | RAG-Chat über Dokumente | Self-hosted, Ollama-Anbindung |
| Lokale Modelle (Ollama) | Reicht für Klassifikation und Zusammenfassung | Alles im Haus. Als steuernder Projektagent unzuverlässig (Einschätzung, im Pilot testen) |

**Wichtig:** ZDR ≠ EU-Datenresidenz. ZDR regelt die Speicherung beim Anbieter, nicht den Verarbeitungsort.

## Extraktion (PDF/Scan/Office → Markdown)

Docling, Marker oder Azure AI Document Intelligence. Die Benchmarks widersprechen sich und sind teils vom Hersteller selbst. Deshalb **mit 20–30 eigenen typischen Dokumenten selbst testen** (Prüfprotokolle, Maschinenhandbücher, Excel-Parameterlisten). Excel-Parametertabellen als Tabelle übernehmen, nicht zusammenfassen.

## Halluzinationen eindämmen

- Geschlossene Aufgaben: „Ordne einer dieser Kategorien zu“ statt „Was ist das?“
- Zitierpflicht mit maschineller Nachprüfung (Zitat muss in der Quelle auffindbar sein)
- Getrennter Prüfdurchlauf (Ersteller ≠ Prüfer)
- Goldstandard aus 50–100 von Menschen klassifizierten Dokumenten als Messlatte für jede Prompt-/Modelländerung
- Rohquellen nie überschreiben

## Spätere KI-Suche

Klassisches RAG (Vektor + Stichwort + Reranker) reicht zunächst. GraphRAG lohnt sich erst bei Zusammenhangsfragen; LazyGraphRAG ist später günstig nachrüstbar.
**Wichtiger als die Technik ist eine LLM-freundliche Struktur:** eine Seite pro Thema, Metadaten im Seitenkopf, Parameter als Tabellen, sprechende Links, ein Index pro Bereich.

## Wiki-Plattformen

| Plattform | Self-Hosting | KI / API | Einschätzung |
|---|---|---|---|
| SharePoint (+ Loop) | nein | Graph-API, Copilot | Erste Wahl, wenn M365 gesetzt ist |
| Confluence | Data Center | REST, Atlassian-MCP, Rovo | Stark, aber Zusatzkosten |
| Docmost | ja (AGPL) | API, Ollama-Anbindung | Beste Self-Hosted-Option mit KI im Haus |
| BookStack | ja (MIT) | REST, Community-MCP | Einfach, robust. Hierarchie Regal → Buch → Kapitel → Seite passt zu Abteilungen |
| Outline | ja (BSL) | offizieller MCP-Server | Sehr KI-nah, Lizenz prüfen |
| Wiki.js | ja (AGPL) | GraphQL, Git-Sync | Für Nicht-Techniker weniger komfortabel |
| Markdown-Repo | – | direkter Dateizugriff | Als **Arbeitsbereich** des Agenten ideal, als Firmenwiki ungeeignet (Berechtigungen) |

**Position:** Arbeitsbereich (Markdown, lokal) und Veröffentlichungsort (Wiki) trennen. Freigegebene Seiten werden per API publiziert. So bleibt die Kuratierungsarbeit unabhängig von der Plattformentscheidung der IT.

## Recht und Organisation (Österreich/EU)

- **DSGVO:** Auftragsverarbeitungsvertrag, Drittlandübermittlung prüfen, Eintrag im Verarbeitungsverzeichnis, ggf. Datenschutz-Folgenabschätzung. Personal-/HR-Bestände aus dem Pilot ausschließen.
- **EU AI Act:** Ein internes Wissenssystem ist in der Regel kein Hochrisiko-System. Es gilt die Pflicht zu KI-Kompetenzmaßnahmen nach Art. 4 (durch den „Digital Omnibus“ seit 07/2026 abgeschwächt). Die RTR-KI-Servicestelle empfiehlt Dokumentation: KI-Richtlinie, Schulungskonzept, Nachweise.
- **Betriebsrat (§ 96a ArbVG):** Zustimmungspflichtig, sobald nutzerbezogene Protokolle oder Auswertungen entstehen; bei Copilot laut Kanzleien regelmäßig der Fall. Eine **KI-Betriebsvereinbarung vor dem Pilot** abschließen.
- **Berechtigungen:** Eine KI-Suche macht übermäßig freigegebene Ordner plötzlich auffindbar. Berechtigungen vor dem Freischalten bereinigen. Bei Eigenbau-RAG müssen die Rechte pro Nutzer durchgereicht werden.

## Unsicherheiten

- Anthropic-Kennzahlen (z. B. 90,2 % Leistungsplus Multi-Agent, 15× Tokens) sind interne Messungen.
- PDF-Extraktions-Benchmarks widersprechen sich.
- Rechtliche Einordnungen stammen aus Kanzlei- und Fachportalen und ersetzen keine Rechtsprüfung.
- OpenAI-Residenzbedingungen und Preisaufschläge vertraglich verifizieren.

## Wichtige Quellen

- Anthropic: Building effective agents; Effective harnesses for long-running agents; How we built our multi-agent research system (13.06.2025)
- OpenAI: A Practical Guide to Building Agents; Introducing data residency in Europe (05.02.2025)
- MAST – Why Do Multi-Agent LLM Systems Fail? (UC Berkeley, arXiv 2503.13657)
- Wei Wu: When Errors Become Narratives (arXiv 2606.14589)
- Microsoft Learn: Microsoft 365 Copilot privacy; Anthropic models in Copilot / EU Data Boundary
- Microsoft Research: LazyGraphRAG (25.11.2024)
- Microsoft Agent Framework 1.0 (devblogs.microsoft.com)
