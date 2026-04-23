---
name: extract-skilljar-course
description: Extrae contenido de lecciones de Anthropic Academy (anthropic.skilljar.com) a notas markdown estructuradas en español. Usar cuando el usuario pida "extraer/documentar/pasar a notas" un curso o lecciones específicas de Skilljar. Requiere Playwright MCP y que el usuario ya esté logueado en Skilljar en el Chromium controlado.
argument-hint: "<course-slug> [<lesson-range>]  (ej: claude-with-the-anthropic-api 9-25)"
---

# extract-skilljar-course

Skill para documentar cursos de Anthropic Academy en notas markdown de estudio. Resume el pipeline completo con las herramientas y técnicas descubiertas trabajando sobre este repo.

---

## Prerrequisitos

1. **Playwright MCP instalado** en Claude Code:
   ```bash
   claude mcp add playwright -- npx -y @playwright/mcp@latest
   ```
   Verificar que `mcp__playwright__browser_*` esté disponible. La primera navegación descarga Chromium (~150 MB).

2. **Sesión de Skilljar iniciada** en el Chromium que controla Playwright. Como el navegador de Playwright no comparte cookies con el Chrome personal del usuario, **la primera vez** el usuario debe loguearse dentro del Chromium controlado (navegar a `https://anthropic.skilljar.com/` y usar el botón de login). La sesión persiste en el profile del MCP mientras no se cierre.

3. **Poppler** (opcional, solo si el curso incluye PDFs que haya que leer):
   ```bash
   brew install poppler
   ```
   El `Read` tool usa `pdftoppm` para leer PDFs por páginas; sin poppler hay que extraer texto con `pdftotext` via bash.

---

## Pipeline paso a paso

### Paso 1 — Ubicar el curso y su estado

Navegar al catálogo para identificar el curso:

```
mcp__playwright__browser_navigate  url=https://anthropic.skilljar.com/
mcp__playwright__browser_snapshot
```

En el snapshot se identifican:
- El link del curso (ej. `/claude-with-the-anthropic-api`).
- El badge de estado (`Complete`, `Registered`, vacío = no empezado).

### Paso 2 — Obtener el índice de lecciones con IDs

Navegar a la URL del curso:

```
mcp__playwright__browser_navigate  url=https://anthropic.skilljar.com/<course-slug>
mcp__playwright__browser_snapshot
```

En el snapshot cada lección aparece como un `listitem` con:
- **Título** (en el último `generic`).
- **Estado** (`This lesson has been completed.` vs `This lesson has not been completed.`).
- **URL con ID** tras hacer click (ej. `/claude-with-the-anthropic-api/287724`).

Para obtener todas las URLs sin hacer click uno por uno, navegar a **cualquier lección** una vez — la sidebar de navegación renderiza todos los links completos con el ID numérico de cada lección:

```
mcp__playwright__browser_navigate  url=https://anthropic.skilljar.com/<course-slug>/<first-lesson-id>
mcp__playwright__browser_snapshot
```

Extraer del snapshot el mapeo `[título → URL → estado]`.

### Paso 3 — Extraer metadata y captions de cada lección

El player de video es **JW Player**. Su API está expuesta en `window.jwplayer()`. Usar `browser_evaluate`:

```javascript
() => {
  try {
    const pl = window.jwplayer().getPlaylist()[0];
    const es = pl.tracks.find(t => t.label === 'Spanish');
    const en = pl.tracks.find(t => t.label === 'English');
    return {
      title: pl.title,
      duration: pl.duration,
      mediaid: pl.mediaid,
      es: es?.file,
      en: en?.file
    };
  } catch(e) {
    return { noVideo: true, error: e.message };
  }
}
```

El objeto `playlist[0]` tiene entre otras cosas:
- `title` — ej. `"03 - 007 - System Prompts Exercise.mp4"`.
- `duration` — en segundos (float).
- `tracks[]` — array con captions en múltiples idiomas (English, Spanish, French, German, Japanese, Korean, Portuguese). Cada track tiene `kind: "captions"`, `label`, `file` (URL del .srt en `cdn.jwplayer.com/tracks/<id>.srt`).
- `allSources[]` — URLs .mp4 directas en varias resoluciones (180p → 1080p).

Las lecciones tipo **quiz** o **survey** no tienen JW Player → la función devuelve `{noVideo: true}`. Se saltan sin tratamiento especial.

### Paso 4 — Descargar el SRT

El CDN de JW Player **requiere header `Referer`** — sin él devuelve 200 con cuerpo vacío. Con bash:

```bash
curl -sL -H "Referer: https://anthropic.skilljar.com/" \
     "https://cdn.jwplayer.com/tracks/<id>.srt" \
     -o /tmp/bwca/L<NN>_es.srt
```

### Paso 5 — Limpiar el SRT a texto plano

Un `.srt` tiene bloques de `número\ntimestamps\ntexto\n\n`. Para convertir a prosa:

```bash
awk 'BEGIN{ORS=" "}
     /^[0-9]+$/ {next}
     /-->/ {next}
     /^$/ {print "\n"; next}
     {print}' archivo.srt | sed 's/  */ /g'
```

- Salta los números de secuencia y las líneas con `-->`.
- Preserva saltos en líneas vacías (separador de bloque).
- Colapsa espacios múltiples.

### Paso 6 — Sintetizar notas estructuradas (NO pegar subtítulos verbatim)

Los subtítulos son material con copyright del curso. **No pegarlos textualmente** en el archivo de notas. Usarlos como **fuente** para producir notas estructuradas en el mismo estilo didáctico que ya tenga el archivo:

- Título de la lección, tipo (video/ejercicio/quiz) y duración.
- Secciones de conceptos clave.
- Código (los snippets de API estándar se pueden escribir tal cual ya que son patrones de uso).
- "Takeaway" o regla práctica al final.

Ejemplos de formato correcto están en `androipic certifiacion/Building_with_the_Claude_API.md` (lecciones 9-25).

### Paso 7 — Escribir al archivo de notas

Insertar las nuevas lecciones en el archivo markdown del curso, respetando el formato existente (`## Lección N — Título ✅` + subsecciones). Actualizar el header con `Progreso: X / Y lecciones completadas`.

---

## Herramientas y técnicas — resumen

| Herramienta | Uso |
|-------------|-----|
| `mcp__playwright__browser_navigate` | Abrir URL en el Chromium controlado |
| `mcp__playwright__browser_snapshot` | Obtener árbol de accesibilidad con refs para click + text + URLs |
| `mcp__playwright__browser_evaluate` | Ejecutar JS en la página — la técnica clave (JW Player API, extracción de datos que no están en el DOM visible) |
| `mcp__playwright__browser_click` | Navegar a lecciones clickeando (alternativa a URL directa) |
| `mcp__playwright__browser_take_screenshot` | Verificación visual cuando el snapshot no basta |
| `Bash` + `curl -H "Referer: ..."` | Descargar SRT del CDN de JW Player |
| `Bash` + `awk` / `sed` | Limpiar SRT → texto plano |
| `Read` con `pages` | Leer PDFs del curso (requiere poppler) |
| `pdftotext` via `Bash` | Fallback si poppler no está instalado en el sistema |

---

## Troubleshooting

| Síntoma | Causa | Fix |
|---------|-------|-----|
| `browser_navigate` lleva a página de login | Sesión no iniciada en Chromium MCP | Usuario se loguea una vez dentro del navegador controlado |
| `window.jwplayer` es undefined | La lección no tiene video (quiz/survey), o el player no terminó de cargar | Si es quiz/survey, saltar; si es timing, esperar con `browser_wait_for` |
| SRT descarga vacío (HTTP 200, tamaño 0) | Falta header `Referer` | Añadir `-H "Referer: https://anthropic.skilljar.com/"` |
| `pdftoppm is not installed` al leer PDF | Falta poppler | `brew install poppler` o usar `pdftotext` via bash |
| Subtítulos en inglés (no español) | La lección no tiene traducción ES | Usar `en: pl.tracks.find(t => t.label === 'English').file` como fallback |

---

## Identificar hasta dónde llegar

Respetar siempre el alcance que pida el usuario. Dos fuentes de verdad:

1. **Progreso real en Skilljar** (header del curso: `"X of Y lessons completed"`). Es la fuente de verdad del estado actual.
2. **Archivo de notas local**. Puede estar desactualizado respecto a Skilljar — avisar al usuario si hay discrepancia antes de empezar.

**Nunca documentar lecciones que el usuario no haya completado aún** salvo que lo pida explícitamente.

---

## Output esperado

Al terminar, reportar al usuario:
- Lecciones procesadas (con números).
- Lecciones saltadas (quizzes/surveys) con razón.
- Tamaño final del archivo de notas.
- Siguiente lección pendiente (la primera `not completed`) por si quiere continuar con el curso.
