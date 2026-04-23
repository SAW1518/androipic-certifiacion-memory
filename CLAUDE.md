# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Memoria y estado persistentes

Estos archivos contienen contexto que debe cargarse al inicio de la sesión:

- @.claude/memory/MEMORY.md
- @.claude/memory/user_profile.md
- @.claude/memory/project_context.md
- @.claude/memory/project_structure.md
- @.claude/memory/exam_guide_ref.md
- @STATE.md

Viajan con el repo (a diferencia de la auto-memoria de `~/.claude/projects/...` que es local por Mac). Si se actualizan hechos, actualizar el archivo correspondiente.

## Primera acción en cada sesión nueva

**Antes de responder al usuario en el primer mensaje de la sesión**, hacer un chequeo rápido de capacidades y reportar el resultado en una línea o dos. Esto importa porque el usuario usa este repo desde dos Macs (personal y de trabajo) y los MCPs/tools pueden no estar instalados en ambas.

Qué chequear:

1. **MCP servers esperados** en este proyecto (definidos más abajo en *MCP servers configurados*):
   - `playwright` — buscar en las herramientas disponibles algo con prefijo `mcp__playwright__` (ej. `mcp__playwright__browser_navigate`). Si no aparece → no está instalado en esta Mac.
2. **Herramientas web** nativas: `WebFetch`, `WebSearch` (siempre deberían estar).
3. **Skills** relevantes: `init`, `review`, `security-review`, `loop` (vienen con Claude Code).

Formato del reporte (ejemplo):

> Sesión lista. ✅ Playwright MCP disponible. ✅ WebFetch/WebSearch. Si falta algo, te aviso el comando para instalarlo.

Si falta algún MCP esperado, decirlo con el comando exacto para arreglarlo (ej. `claude mcp add playwright -- npx -y @playwright/mcp@latest`) y preguntar al usuario si quiere que lo instale ahora o después.

No hacer este chequeo en mensajes posteriores — solo el primero de la sesión.

## Qué es este repositorio

**No es un proyecto de software.** Es la carpeta de apuntes y preparación para el examen **Claude Certified Architect – Foundations** de Anthropic. El contenido principal son notas en markdown (en español) de los cursos de Anthropic Academy más notebooks prácticos del curso *Building with the Claude API*.

El usuario escribe y prefiere respuestas en **español informal** (suele tener typos — no corregirle la ortografía salvo que lo pida).

## Estructura

Todo el material vive dentro de `androipic certifiacion/` (sí, el nombre del directorio tiene typos — mantenerlo así, no renombrar):

- `01_Claude_Code_in_Action.md` — notas del curso Claude Code in Action (completado).
- `02_Claude_101.md` — notas del curso Claude 101 (completado).
- `Building_with_the_Claude_API.md` — notas del curso Building with the Claude API (**en curso**). Al inicio del archivo hay una línea `Progreso:` con el conteo de lecciones completadas; actualízala al terminar una lección.
- `Building with the Claude API/` — notebooks Jupyter prácticos del curso de API + `dataset.json` + `.env`.
- `instructor_*_Claude+Certified+Architect+–+Foundations+Certification+Exam+Guide.pdf` — guía oficial del examen. Leer con la herramienta `Read` y el parámetro `pages` cuando haga falta consultar dominios/objetivos.

## Convenciones de las notas

- Cada archivo de curso empieza con metadatos: fuente, relevancia para el examen, estado/progreso.
- Las lecciones llevan ✅ cuando están completadas.
- Cuando se complete una nueva lección del curso de API, actualizar **dos sitios**: la sección correspondiente de `Building_with_the_Claude_API.md` y la línea `Progreso:` de arriba.

## Entorno para los notebooks

Los notebooks usan el Python del sistema (`/Applications/Xcode.app/Contents/Developer/usr/bin/python3`, 3.9) con paquetes instalados en `~/Library/Python/3.9/lib/python/site-packages` (user install).

Dependencias:

```bash
pip install --user anthropic python-dotenv
```

La API key vive en `androipic certifiacion/Building with the Claude API/.env`:

```
ANTHROPIC_API_KEY="sk-ant-..."
```

**Al clonar este repo en otra Mac el `.env` no se transfiere automáticamente** (si algún día se sube a git debería estar gitignoreado). Hay que crearlo a mano con la key del usuario antes de correr los notebooks.

Patrón estándar de los notebooks:

```python
from dotenv import load_dotenv
load_dotenv()
from anthropic import Anthropic
client = Anthropic()  # toma ANTHROPIC_API_KEY del entorno
```

Modelo usado en los ejercicios: `claude-sonnet-4-0` (es lo que trae el curso; los modelos recientes son `claude-sonnet-4-6` y `claude-opus-4-7`, pero mantener lo que use la lección a menos que el usuario pida actualizar).

## Skills del proyecto

En `.claude/skills/` viven skills custom que Claude Code carga automáticamente al abrir este repo:

- **`extract-skilljar-course`** — pipeline para extraer lecciones de cursos de Anthropic Academy (Skilljar) a notas markdown. Documenta el uso de Playwright MCP + JW Player API + curl con header Referer + limpieza de SRTs. Invocarlo cuando el usuario pida "documentar/extraer/pasar a notas" un curso o lecciones específicas.

## MCP servers configurados en este proyecto

Registrados en `~/.claude.json` bajo la entrada de este proyecto:

- **playwright** (`npx -y @playwright/mcp@latest`) — control de un Chromium headful. La primera navegación descarga Chromium (~150 MB).

Para replicar en otra Mac:

```bash
claude mcp add playwright -- npx -y @playwright/mcp@latest
```

## Bootstrap en Mac nueva

Al abrir este repo por primera vez en una Mac donde no se ha trabajado antes, ejecutar (o sugerirle al usuario que ejecute):

```bash
# 1. Deps del sistema
brew install poppler                                                 # para leer PDFs con Read

# 2. Deps Python (para los notebooks del curso de API)
pip3 install --user anthropic python-dotenv

# 3. MCP Playwright (para el skill extract-skilljar-course)
claude mcp add playwright -- npx -y @playwright/mcp@latest
# tras instalarlo hay que reiniciar Claude Code para que cargue el MCP

# 4. API key — copiar el template y pegar la key real
cp "androipic certifiacion/Building with the Claude API/.env.example" \
   "androipic certifiacion/Building with the Claude API/.env"
# editar el archivo y reemplazar el placeholder con una key de https://console.anthropic.com/

# 5. Primera vez que uses el skill extract-skilljar-course: abrir el Chromium que controla
#    Playwright y loguearse en https://anthropic.skilljar.com/ con la cuenta del usuario.
#    La sesión persiste en el profile del MCP.
```

## Cómo ayudar aquí

- El objetivo transversal es prep de examen. Al explicar conceptos, conectar con los dominios del examen (Claude básico, Claude Code & workflows, Claude API). Priorizar claridad didáctica sobre ingeniería.
- Los notebooks son para practicar conceptos puntuales de una lección — no refactorizar ni añadir abstracciones "de producción" que no pidió el curso.
- Si un notebook tiene errores (ej. `NameError` por orden de celdas), lo normal es arreglar el orden o re-ejecutar, no reescribir toda la lógica.
- Al terminar una sesión con cambios significativos (lecciones nuevas, nuevos cursos completados, cambio de plan), actualizar `STATE.md`.
