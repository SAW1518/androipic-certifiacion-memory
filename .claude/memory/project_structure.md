---
name: Project structure and progress
description: Estructura de archivos del proyecto de certificación, progreso real por curso en Anthropic Academy y plan de estudio al 2026-04-22.
type: project
originSessionId: 27293b13-1991-47cf-a19c-4a9881e6a8a3
---
Estructura dentro de `androipic certifiacion/` (sic, typo intencional):

- `00_Plan_de_estudio.md` — **hoja de ruta del examen**. Resumen de dominios, estado actual, mapeo cursos→dominios, orden recomendado, anti-patterns. **Consultarlo primero cuando el usuario pregunte por el plan o qué sigue.**
- `01_Claude_Code_in_Action.md` — notas del curso (completado ✅).
- `02_Claude_101.md` — notas del curso (completado ✅).
- `Building_with_the_Claude_API.md` — notas del curso (**en curso**, 8/85 lecciones). Línea `Progreso:` al inicio.
- `Building with the Claude API/` — notebooks Jupyter prácticos + `dataset.json` + `.env`.
- `instructor_*_Claude+Certified+Architect+–+Foundations+Certification+Exam+Guide.pdf` — guía oficial del examen.

**Progreso real en Anthropic Academy (verificado 2026-04-22 con Playwright):**

Cursos ✅ completados (6):
1. Claude 101
2. Introduction to Claude Cowork
3. Claude Code in Action
4. AI Fluency: Framework & Foundations (no relevante para cert)
5. Introduction to agent skills
6. Introduction to subagents

🟡 En curso: Building with the Claude API (8/85).

⬜ Pendientes relevantes: Claude Code 101, Introduction to MCP, MCP: Advanced Topics.

**Why:** Saber qué está hecho y qué queda permite priorizar el siguiente paso sin que el usuario tenga que re-explicar.

**How to apply:**
- Si pide "¿qué sigue?" o ayuda para organizar estudio, referir a `00_Plan_de_estudio.md` y al orden recomendado (terminar API → MCP Intro → MCP Advanced → Claude Code 101 → exercises → practice exam).
- Si pide algo relacionado a un curso, verificar primero si está completado/en curso/pendiente antes de asumir nivel de conocimiento.
- El usuario solo notas de cursos completados + el en-curso, así que solo existen archivos .md de esos. Notas de Cowork, Agent Skills y Subagents **no existen como archivo** aunque estén completados en la Academy.
