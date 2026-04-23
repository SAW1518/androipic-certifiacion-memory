# Plan de Estudio — Claude Certified Architect – Foundations

**Fuente:** Exam Guide oficial (PDF en esta misma carpeta) + catálogo de Anthropic Academy ([skilljar.com](https://anthropic.skilljar.com/)).
**Última actualización:** 2026-04-22

---

## 1. Sobre el examen

- **Formato:** multiple choice, 1 respuesta correcta de 4.
- **Estructura:** 4 escenarios elegidos al azar de 6 posibles.
- **Score:** escala 100–1000. **Mínimo para pasar: 720**.
- **Sin penalización** por respuestas en blanco (se cuentan como incorrectas — siempre contestar).
- **Fecha de la guía:** v0.1, Feb 2025.

### Perfil del candidato ideal

Arquitecto de soluciones con **6+ meses de experiencia práctica** construyendo con:
- Claude Agent SDK (multi-agent orchestration, subagents, tool integration, hooks)
- Claude Code (CLAUDE.md, skills, MCP, plan mode)
- MCP (diseño de tools y resources)
- Prompt engineering para structured output
- Context window management
- CI/CD con Claude Code
- Error handling y human-in-the-loop

### Los 5 dominios (con peso)

| # | Dominio | Peso | Enfoque |
|---|---------|------|---------|
| 1 | **Agentic Architecture & Orchestration** | **27%** ⭐ | Agentic loops, stop_reason, coordinator-subagent, Task tool, hooks, session mgmt |
| 2 | **Tool Design & MCP Integration** | 18% | Tool descriptions, MCP servers, isError, tool distribution, built-in tools |
| 3 | **Claude Code Configuration & Workflows** | 20% | CLAUDE.md hierarchy, slash commands, skills, plan mode, CI/CD |
| 4 | **Prompt Engineering & Structured Output** | 20% | Few-shot, JSON schemas, tool_use, validation/retry, Batch API |
| 5 | **Context Management & Reliability** | 15% | Context windows, escalation, error propagation, confidence calibration |

### Los 6 escenarios (salen 4 en el examen)

1. **Customer Support Resolution Agent** — Dominios 1, 2, 5
2. **Code Generation with Claude Code** — Dominios 3, 5
3. **Multi-Agent Research System** — Dominios 1, 2, 5
4. **Developer Productivity with Claude** — Dominios 2, 3, 1
5. **Claude Code for Continuous Integration** — Dominios 3, 4
6. **Structured Data Extraction** — Dominios 4, 5

---

## 2. Mi estado actual (2026-04-22)

### ✅ Cursos completados (6)

1. Claude 101
2. Introduction to Claude Cowork
3. Claude Code in Action
4. AI Fluency: Framework & Foundations *(no relevante para cert)*
5. Introduction to agent skills
6. Introduction to subagents

### 🟡 En curso

- **Building with the Claude API** — 8/85 lecciones (9%)

### ⬜ Pendientes (relevantes para la cert)

- Claude Code 101
- Introduction to Model Context Protocol
- Model Context Protocol: Advanced Topics

---

## 3. Mapeo cursos → dominios

### 🔥 Prioridad ALTA

| Curso | Dominios cubiertos | Estado |
|-------|-------------------|--------|
| **Building with the Claude API** | 1, 2, 4, 5 (tool use, prompt eng, JSON schemas, Batch API, agents) | 🟡 En curso |
| **Introduction to Model Context Protocol** | 2 (core), parte de 1 | ⬜ |
| **Claude Code 101** | 3 (complemento) | ⬜ |
| **Model Context Protocol: Advanced Topics** | 2 profundo | ⬜ |

### ✅ Ya completados — repasar antes del examen

| Curso | Dominios que toca |
|-------|-------------------|
| Introduction to subagents | 1 (coordinator-subagent, Task tool, context: fork) |
| Introduction to agent skills | 3 (SKILL.md, allowed-tools, context: fork, argument-hint) |
| Claude Code in Action | 3 (CLAUDE.md, slash commands, plan mode, hooks) |
| Introduction to Claude Cowork | 1, 5 (task loop, research workflows) |
| Claude 101 | Fundamentos generales |

### ❌ NO relevantes — saltar

- AI Fluency for educators / students / nonprofits / Teaching AI Fluency
- AI Capabilities and Limitations
- Claude with Amazon Bedrock
- Claude with Google Cloud's Vertex AI

**Razón:** el PDF marca *"specific cloud provider configurations"* y temas no técnicos como **out-of-scope**.

---

## 4. Orden recomendado de estudio

1. **Terminar Building with the Claude API** (77 lecciones pendientes) — curso más denso, cubre 4 de 5 dominios.
2. **Introduction to Model Context Protocol** — dominio 2 completo.
3. **Model Context Protocol: Advanced Topics** — profundiza dominio 2.
4. **Claude Code 101** — relleno para dominio 3.
5. **Repaso** de los cursos ya completados con enfoque en dominios 1 y 3.
6. **Hacer los 4 Preparation Exercises del PDF** (ver sección 5).
7. **Practice Exam oficial** (link lo entrega Anthropic aparte).

---

## 5. Preparation Exercises del PDF oficial

Son 4 ejercicios prácticos obligatorios para consolidar:

### Ejercicio 1 — Multi-Tool Agent con Escalation Logic
**Dominios:** 1, 2, 5
- Definir 3-4 MCP tools con descripciones diferenciadas.
- Implementar agentic loop con chequeo de `stop_reason` ("tool_use" vs "end_turn").
- Errores estructurados: `errorCategory` (transient/validation/permission), `isRetryable`, descripciones humanas.
- Hook programático que intercepta tool calls para enforcement de reglas de negocio (ej. bloquear refunds > threshold).
- Tests con multi-concern messages (decomposition + síntesis).

### Ejercicio 2 — Claude Code para Team Dev Workflow
**Dominios:** 2, 3
- CLAUDE.md a nivel proyecto con estándares universales.
- `.claude/rules/` con YAML frontmatter y glob patterns (`paths: ["src/api/**/*"]`).
- Skill en `.claude/skills/` con `context: fork` y `allowed-tools`.
- MCP server en `.mcp.json` con expansión de env vars + MCP personal en `~/.claude.json`.
- Probar plan mode vs direct execution en tareas de distinta complejidad.

### Ejercicio 3 — Pipeline de Extracción Estructurada
**Dominios:** 4, 5
- Tool de extracción con JSON schema (required/optional, enum + "other", nullable fields).
- Validation-retry loop con Pydantic/JSON schema.
- Few-shot examples para documentos con formatos variados.
- Message Batches API para 100 docs con manejo de fallos por `custom_id`.
- Human review routing con field-level confidence scores.

### Ejercicio 4 — Multi-Agent Research Pipeline
**Dominios:** 1, 2, 5
- Coordinator con `allowedTools: ["Task"]` + 2+ subagents.
- Ejecución paralela emitiendo múltiples `Task` en una sola respuesta.
- Structured output separando content de metadata (source URLs, fechas).
- Error propagation con structured error context.
- Manejo de conflicting source data con attribution preservada.

---

## 6. Topics in-scope / out-of-scope (del PDF)

### ✅ In-scope (estudiar)

- Agentic loop implementation (stop_reason, tool result handling, termination)
- Multi-agent orchestration (coordinator-subagent, task decomposition, paralelo)
- Subagent context management (explicit passing, structured state, crash recovery)
- Tool interface design (descripciones, splitting vs consolidating)
- MCP tool/resource design
- MCP server configuration (project vs user scope, env vars)
- Error handling & propagation (structured, transient/business/permission)
- Escalation decision-making (criterios explícitos, customer preferences)
- CLAUDE.md configuration (jerarquía, @import, `.claude/rules/` con globs)
- Custom commands y skills (project vs user, `context: fork`, `allowed-tools`, `argument-hint`)
- Plan mode vs direct execution
- Iterative refinement (examples, test-driven, interview pattern)
- Structured output via tool_use (schema design, tool_choice)
- Few-shot prompting (ambiguity, format, reducción de false positives)
- Batch processing (Message Batches API, latency tolerance, custom_id)
- Context window optimization (trimming, structured facts, position-aware ordering)
- Human review workflows (confidence calibration, stratified sampling)
- Information provenance (claim-source mappings, conflict annotation)

### ❌ Out-of-scope (NO estudiar)

- Fine-tuning / custom model training
- Auth, billing, account management
- Detalles de lenguajes/frameworks específicos
- Hosting/deploy de MCP servers (infra, networking)
- Arquitectura interna de Claude, entrenamiento, pesos
- Constitutional AI, RLHF, safety training
- Embeddings, vector DBs
- **Computer use (browser automation, desktop)** ← ojo
- Vision/image analysis
- Streaming API implementation
- Rate limiting, quotas, pricing
- OAuth, API key rotation
- Configs específicas de AWS/GCP/Azure
- Benchmarking de performance
- Detalles de prompt caching (solo saber que existe)
- Token counting / tokenization

---

## 7. Anti-patterns críticos (salen mucho en preguntas)

Estos aparecen como opciones incorrectas ("distractors") en preguntas de ejemplo:

- **Confiar en prompts** cuando se requiere **enforcement programático** (ej. bloquear refunds con hook, no con prompt).
- **Parsear texto natural** para decidir terminación del loop (usar `stop_reason`).
- **Self-reported confidence scores** como proxy de complejidad del caso (mal calibrados).
- **Sentiment analysis** para decidir escalation (no correlaciona con complejidad).
- **Classifier/ML separado** cuando un prompt mejor basta (sobre-ingeniería).
- **Consolidar tools** cuando el problema son descripciones pobres.
- **Self-review** por el mismo modelo que generó el output (usar instancia independiente).
- **Context window más grande** para resolver attention dilution (no lo resuelve — usar multi-pass).
- **Silenciar errores** o terminar todo el workflow en un fallo único (usar error propagation estructurado).
- **Consensus voting** (3 pasadas, flag si aparece en 2+) — suprime bugs reales.

---

## 8. Recursos complementarios

- **Exam Guide PDF oficial:** `instructor_8lsy243ftffjjy1cx9lm3o2bw_public_1773274827_Claude+Certified+Architect+–+Foundations+Certification+Exam+Guide.pdf` (misma carpeta)
- **Anthropic Academy:** https://anthropic.skilljar.com/
- **Docs oficiales:** https://docs.anthropic.com
- **Practice Exam:** link entregado por Anthropic (no público)
