# Claude Code in Action — Notas del Curso
**Fuente:** [Anthropic Academy](https://anthropic.skilljar.com/claude-code-in-action)
**Relevancia para certificación:** Dominio 3 (Claude Code Config & Workflows, 20%) + Dominio 1 parcial
**Estado:** ✅ Completado (21/21 lecciones)

---

## Estructura del Curso

- **Sección 1:** What is Claude Code? (3 videos)
- **Sección 2:** Getting Hands On (8 lecciones — videos + texto)
- **Sección 3:** Hooks and the SDK (7 lecciones — videos + texto)
- **Sección 4:** Wrapping Up (quiz + video)

---

## SECCIÓN 1: What is Claude Code?

### Lección 1 — Introduction

Stephen Grider (Member of Technical Staff at Anthropic) presenta el curso. El curso tiene 4 secciones:
1. Entender qué es un coding assistant
2. Ver Claude Code y qué lo hace diferente
3. Uso práctico en un proyecto real (hands-on)
4. Cómo sacarle el máximo provecho en proyectos propios

---

### Lección 2 — What is a Coding Assistant?

**Coding Assistant** = herramienta que usa language models para escribir código y completar tareas de desarrollo.

**Proceso core:**
1. Recibe una tarea (ej. arreglar un bug a partir de un error message)
2. El language model recopila contexto (lee archivos, entiende el codebase)
3. Formula un plan para resolver el problema
4. Toma acción (actualiza archivos, corre tests)

**Limitación clave:** Los language models solo procesan texto de entrada/salida — NO pueden leer archivos directamente, ejecutar comandos, ni interactuar con sistemas externos.

**Tool Use System** = el mecanismo que permite a los LMs realizar acciones:
- El assistant añade instrucciones al request del usuario
- Las instrucciones especifican respuestas formateadas para acciones (ej. "lee el archivo: nombre")
- El LM responde con la acción formateada solicitada
- El assistant ejecuta la acción real (lee el archivo, corre el comando)
- Los resultados se envían de vuelta al LM para generar la respuesta final

**Ventaja de Claude:**
- Capacidades superiores de tool use vs otros LMs
- Mejor en entender funciones de tools y combinarlas para tareas complejas
- Claude Code es extensible — fácil de añadir nuevas herramientas
- Mejor seguridad: búsqueda directa en código vs indexación que envía el codebase a servidores externos

**Puntos esenciales:**
- Todos los LMs requieren tool use para tareas que no sean generación de texto
- La calidad del tool use impacta directamente la efectividad del coding assistant
- La fortaleza de Claude en tool use lo hace adaptable a los cambios de desarrollo

---

### Lección 3 — Claude Code in Action

**Claude Code** = AI assistant con capacidades basadas en tools para tareas de código.

**Herramientas por defecto:** lectura/escritura de archivos, ejecución de comandos, operaciones básicas de desarrollo.

**Demo 1 — Optimización de performance:**
- Claude analizó la librería Chalk de JavaScript (paquete #5 más descargado, 429M descargas semanales)
- Usó benchmarks, profiling tools, creó todo lists, identificó bottlenecks, implementó fixes
- **Resultado: mejora de 3.9x en throughput**

**Demo 2 — Análisis de datos:**
- Claude realizó un análisis de churn en datos CSV de plataforma de video streaming usando Jupyter notebooks
- Ejecutó celdas de código iterativamente, vio resultados, personalizó análisis sucesivos basándose en hallazgos

**Extensibilidad de tools:**
- Claude Code acepta nuevos conjuntos de tools
- Ejemplo: se usó Playwright MCP server para automatización de browser
- Claude abrió el browser, tomó screenshots, actualizó UI styling, iteró mejoras de diseño

**GitHub integration:**
- Claude Code corre en GitHub Actions, disparado por pull requests/issues
- Obtiene tools específicas de GitHub (comments, commits, PR creation)
- Detectó automáticamente exposición de PII en una PR review (email de usuario en output de Lambda enviado a partner externo)

**Principio clave:** Claude Code = assistant flexible que crece con las necesidades del equipo mediante expansión de tools, no funcionalidad fija.

---

## SECCIÓN 2: Getting Hands On

### Lección 4 — Claude Code Setup (Texto)

**Instalación:**

```bash
# MacOS (Homebrew)
brew install --cask claude-code

# MacOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows CMD
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

**Primera ejecución:** `claude` en la terminal → se solicitará autenticación la primera vez.

**Setup especial (cloud providers):**
- AWS Bedrock: https://code.claude.com/docs/en/amazon-bedrock
- Google Cloud Vertex: https://code.claude.com/docs/en/google-vertex-ai

**Documentación completa:** https://code.claude.com/docs/en/quickstart

---

### Lección 5 — Project Setup (Texto)

Configuración del proyecto de práctica del curso para seguir los ejemplos hands-on.

---

### Lección 6 — Adding Context

**Gestión de contexto** = crítica para la efectividad de Claude Code. Demasiada información irrelevante disminuye el rendimiento.

**Comando `/init`** = analiza todo el codebase en el primer uso, crea el archivo `Claude.md` con:
- Resumen del proyecto
- Arquitectura
- Archivos clave

El contenido de este archivo se incluye en cada request.

**Tres tipos de archivo `Claude.md`:**
| Tipo | Descripción | Compartido |
|------|-------------|-----------|
| Project level | Instrucciones del equipo | ✅ Sí (versionado) |
| Local level | Instrucciones personales | ❌ No (no committed) |
| Machine level | Instrucciones globales para todos los proyectos | ❌ No |

**Memory mode (símbolo `#`)** = editar archivos `Claude.md` de forma inteligente con lenguaje natural.

**Símbolo `@`** = mencionar archivos específicos para incluirlos en requests. Proporciona contexto dirigido en lugar de dejar que Claude busque.

**Best practice:** referenciar archivos críticos (como database schemas) en `Claude.md` para que siempre estén disponibles como contexto.

**Objetivo:** Proveer justo la información relevante necesaria para que Claude complete tareas efectivamente.

---

### Lección 7 — Making Changes

**Integración de screenshots:**
- `Control-V` (no `Command-V` en macOS) pega screenshots para ayudar a Claude a entender elementos UI específicos a modificar

**Modos de boost de performance:**

| Modo | Activación | Uso ideal |
|------|-----------|-----------|
| **Plan Mode** | Shift + Tab (dos veces) | Tareas multi-paso que requieren entender amplio codebase |
| **Thinking Mode** | Frases como "Ultra think" | Lógica compleja o debugging de problemas específicos (profundidad) |

**Notas importantes:**
- Ambos modos consumen tokens adicionales (consideración de costo)
- Se pueden combinar para tareas complejas
- Plan Mode: investigación más amplia antes de ejecutar
- Thinking Mode: razonamiento extendido para lógica difícil

**Git integration:** Claude Code puede hacer stage/commit de cambios y escribir mensajes de commit descriptivos.

**Workflow clave:**
`Screenshot del área problemática → pegar con Control-V → describir el cambio deseado → activar Plan/Thinking modes si aplica → revisar y aceptar la implementación`

---

### Lección 8 — Controlling Context

**Técnicas de control de contexto:**

| Comando | Función |
|---------|---------|
| **Escape** (una vez) | Detiene a Claude a mitad de respuesta para redirigir el flujo de conversación |
| **Escape + Memory (`#`)** | Detiene a Claude + añade memoria sobre errores repetidos para prevenirlos en el futuro |
| **Doble Escape** | Rebobina la conversación. Muestra todos los mensajes anteriores y permite saltar a un punto anterior |
| **`/compact`** | Resume toda la historia de conversación preservando el conocimiento aprendido. Usar cuando Claude ganó expertise pero la conversación acumuló desorden |
| **`/clear`** | Elimina toda la historia de conversación para empezar de cero. Usar al cambiar a tareas completamente diferentes |

**Beneficios clave:** Mantiene el foco, reduce contexto distractor, preserva conocimiento relevante, previene errores repetidos. Más efectivo para conversaciones largas y transiciones entre tareas.

---

### Lección 9 — Custom Commands

**Custom Commands** = comandos de automatización definidos por el usuario en Claude Code, accesibles vía `/`

**Ubicación:** carpeta `.claude/commands/` en el directorio del proyecto

**Nomenclatura:** el nombre del archivo se convierte en el nombre del comando
- `audit.md` → crea el comando `/audit`

**Activación:** reiniciar Claude Code después de crear archivos de comando

**Estructura:** archivo markdown con instrucciones que Claude ejecutará

**Argumentos:** usar el placeholder `$arguments` en el texto del comando para aceptar parámetros en runtime. Los argumentos pueden ser cualquier string (rutas de archivos, texto descriptivo, etc.)

**Casos de uso:** automatizar tareas repetitivas como auditorías de dependencias, generación de tests, arreglo de vulnerabilidades.

**Ejecución:** `/nombrecomando` en la interfaz de Claude Code, opcionalmente seguido de un string de argumento.

---

### Lección 10 — MCP Servers with Claude Code

**MCP servers** = herramientas externas que extienden las capacidades de Claude Code, corren local o remotamente.

**Playwright MCP server** = server popular que permite a Claude controlar browsers para automatización web.

**Instalación:**
```bash
claude mcp add [nombre] [start-command]
```
Añade el MCP server a Claude Code.

**Gestión de permisos:**
- El primer uso de cada tool requiere aprobación
- Auto-aprobar añadiendo `"MCP__[servername]"` al array `allow` en `settings.local.json`

**Ejemplo práctico:**
- Claude usó Playwright para navegar a `localhost:3000`, generar un componente UI, analizar calidad de styling, y luego actualizar automáticamente los prompts de generación basándose en feedback visual
- El refinamiento automatizado de prompts produjo un styling significativamente mejor

**Beneficio clave:** Los MCP servers permiten a Claude realizar tareas complejas de múltiples pasos involucrando sistemas externos, expandiendo más allá de la edición de código hacia automatización completa de desarrollo.

---

### Lección 11 — GitHub Integration

**Integración GitHub de Claude Code** = integración oficial que permite a Claude correr dentro de GitHub Actions.

**Proceso de setup:**
1. Correr el comando `/install GitHub app`
2. Instalar la app de Claude Code en GitHub
3. Añadir API key
4. PR auto-generada añade dos GitHub Actions

**Acciones por defecto:**
1. **Mention support** = `@Claude` en issues/PRs para asignar tareas
2. **PR review** = revisión automática de código en nuevas pull requests

**Customización:**
- Las actions son customizables vía config files en directorio `.github/workflows/`
- **Custom instructions** = contexto/instrucciones directas pasadas a Claude
- **MCP server integration** = permite a Claude acceder a herramientas externas (ej. Playwright para automatización de browser)

**Requisitos de permisos:**
- Se deben listar explícitamente TODOS los permisos para Claude Code en las actions
- Las tools de MCP servers requieren listado individual de permisos (sin atajos)

**Ejemplo de uso:**
- Integración de Playwright MCP server para browser testing
- Setup del servidor de desarrollo antes de que Claude corra
- Claude puede visitar la app en el browser, testear funcionalidad, crear checklists
- Provee testing automatizado y verificación de issues

**Características clave:** asignación de tareas basada en menciones, PR reviews automatizadas, workflows customizables, integración de MCP servers para funcionalidad extendida.

---

## SECCIÓN 3: Hooks and the SDK

### Lección 12 — Introducing Hooks

**Hooks** = comandos que corren antes/después de que Claude ejecute tools.

**Tipos:**

| Tipo | Cuándo corre | Puede bloquear |
|------|-------------|---------------|
| **Pre-tool use hook** | Antes de la ejecución del tool | ✅ Sí |
| **Post-tool use hook** | Después de la ejecución del tool | ❌ No |

**Configuración:** se añaden al archivo de settings de Claude (global/project/personal) vía edición manual o comando `/hooks`.

**Estructura de un hook:**
- Dos secciones: pre-tool use y post-tool use
- Cada sección tiene: **matcher** (especifica qué tools observar) + **comandos** a ejecutar

**Ejemplos de uso:**
- Auto-formatear archivos después de crearlos
- Correr tests después de edits
- Bloquear acceso a archivos
- Checks de calidad de código
- Type checking

**Hook commands:** reciben los detalles del tool call, pueden modificar el workflow de Claude mediante bloqueo o mecanismos de feedback.

---

### Lección 13 — Defining Hooks

**Tipos de hooks:**

| Hook | Cuándo | ¿Puede bloquear? |
|------|--------|-----------------|
| Pre-tool use | Antes del tool call | ✅ Sí (exit 2) |
| Post-tool use | Después del tool call | ❌ No |

**Proceso de implementación:**
1. Elegir tipo de hook (pre vs post)
2. Identificar nombres de tools objetivo a monitorear
3. Escribir comando que reciba datos del tool call vía `stdin` como JSON
4. Parsear JSON que contiene `tool_name` y parámetros de input
5. Salir con el código apropiado para señalizar intención

**Exit codes:**

| Código | Significado |
|--------|------------|
| `exit 0` | Permitir que el tool call proceda |
| `exit 2` | Bloquear el tool call (solo pre-tool use) |
| `stderr output` | Mensaje de feedback enviado a Claude al bloquear |

**Estructura de datos del tool call (JSON via stdin):**
```json
{
  "tool_name": "read",
  "input": {
    "path": "/ruta/al/archivo"
  }
}
```

**Caso de uso común:** Bloquear acceso a archivos monitoreando los tools `read` y `grep`.

**Para conocer los tool names disponibles:** Preguntarle directamente a Claude la lista de nombres de tools disponibles.

---

### Lección 14 — Implementing a Hook

**Propósito del hook de ejemplo:** prevenir que Claude lea el contenido del archivo `.env`.

**Configuración:**
- **Ubicación:** `.claude/settings.local.json`
- **Tipo:** pre-tool use hook (bloquea antes de ejecución)
- **Matcher:** `"read|grep"` (el símbolo pipe separa nombres de tools)
- **Comando:** `"node ./hooks/read_hook.js"`

**Detalles de implementación:**
```javascript
// El hook recibe JSON via stdin
// { sessionId, toolName, toolInput: { path } }

// Lógica:
if (toolInput.path.includes(".env")) {
  console.error("Acceso a .env bloqueado por política de seguridad");
  process.exit(2); // exit 2 = operación bloqueada
}
```

**Requisitos importantes:**
- ⚠️ **Reiniciar Claude después de cambios en hooks**
- `console.error()` envía feedback a Claude vía stderr
- El hook funciona tanto para `read` como para `grep`
- Verificar `tool_input.path` con manejo de fallback

**Resultados de testing:**
- ✅ Bloquea exitosamente acceso al archivo `.env`
- ✅ Claude reconoce la prevención por el read hook
- ✅ Funciona para operaciones de read y grep

---

### Lección 15 — Gotchas Around Hooks (Texto)

Lección de texto con casos especiales y errores comunes al implementar hooks:
- Consideraciones sobre el reinicio de Claude tras cambios
- Manejo de rutas de archivos (path checking con fallback)
- Separación de tool names con pipe `|`
- Uso correcto de stderr vs stdout para feedback a Claude

---

### Lección 16 — Useful Hooks!

**Problema:** Claude Code frecuentemente comete errores de type y crea código duplicado, especialmente en proyectos grandes.

#### Hook 1: TypeScript Type Checker

**Propósito:** Detectar errores de tipo inmediatamente después de editar archivos.

**Implementación:** Correr `tsc --no-emit` después de cambios a archivos TypeScript vía post-tool-use hook.

**Proceso:**
`Detecta errores de tipo → alimenta errores de vuelta a Claude → Claude arregla automáticamente los call sites`

**Beneficios:**
- Previene llamadas a funciones rotas cuando cambian las firmas
- Adaptable: funciona para cualquier lenguaje tipado con type checker, o usar tests para lenguajes sin tipos

#### Hook 2: Duplicate Code Prevention

**Problema:** Claude crea nuevas queries/funciones en lugar de reutilizar las existentes, especialmente en tareas complejas.

**Solución:** Lanzar una instancia separada de Claude para revisar cambios en directorios específicos (ej. carpeta de queries).

**Proceso:**
1. Detectar edits en el directorio monitoreado
2. Lanzar nueva instancia de Claude vía TypeScript SDK
3. Nueva instancia analiza queries existentes
4. Reporta duplicados a la instancia principal
5. Claude original recibe feedback y reutiliza código existente

**Trade-offs:**
- ⚠️ Tiempo y costo adicional vs codebase más limpio con menos duplicación
- **Recomendación:** Solo aplicar a directorios críticos para minimizar overhead

**Conclusión clave:** Hooks = loops de feedback automatizados que detectan debilidades comunes de Claude Code (errores de tipo, duplicación de código) ejecutando checks adicionales y alimentando resultados de vuelta a Claude para auto-corrección.

---

### Lección 17 — Another Useful Hook (Texto)

Lección de texto complementaria con otro hook práctico (patrón post-tool-use que proporciona feedback automatizado a Claude para mejora continua del código).

---

### Lección 18 — The Claude Code SDK

**Claude Code SDK** = interfaz programática para Claude Code con librerías CLI, TypeScript y Python. Contiene los mismos tools que la versión de terminal.

**Caso de uso principal:** integración en pipelines/workflows más grandes para añadir inteligencia a procesos existentes.

**Permisos por defecto:** solo lectura (archivos, directorios, operaciones grep).

**Para añadir permisos de escritura:**
```typescript
// En las opciones de query:
options.allowTools = ["edit", "write"]; // especificar tools explícitamente
// O configurar via directorio .claude
```

**Ejecución del SDK:** muestra la conversación raw entre el Claude Code local y el language model, con la respuesta final como último mensaje.

**Mejor para:** comandos helper, scripts y hooks dentro de proyectos existentes — no para uso standalone.

---

## SECCIÓN 4: Wrapping Up

### Lección 20 — Summary and Next Steps

Resumen del curso y siguientes pasos recomendados para profundizar en Claude Code.

---

## 📋 Resumen Ejecutivo para la Certificación

### Conceptos Clave por Dominio del Examen

**Dominio 3 — Claude Code Configuration & Workflows (20%):**
- Jerarquía de `Claude.md`: Machine > Project > Local
- Custom commands en `.claude/commands/` (compartidos vía version control)
- `.claude/rules/` con YAML frontmatter para reglas path-específicas
- Plan Mode (`Shift+Tab` dos veces) vs Direct Execution
- CI/CD: flag `-p` para modo no-interactivo
- `/compact` para reducir contexto, `/clear` para reset completo

**Dominio 2 — Tool Design & MCP Integration (18%):**
- `claude mcp add [nombre] [comando]` para instalar MCP servers
- Permisos: listar explícitamente en `settings.local.json`
- Auto-approve: `"MCP__[servername]"` en array `allow`

**Dominio 1 — Agentic Architecture & Orchestration (27%):**
- Hooks: pre-tool (puede bloquear con exit 2) vs post-tool (solo feedback)
- Exit codes: 0 = permitir, 2 = bloquear
- Feedback a Claude vía stderr
- Claude Code SDK para integración programática

### Puntos que Aparecen en Preguntas de Examen
- ⚡ Tool use = mecanismo fundamental de todos los coding assistants
- ⚡ `Claude.md` project-level se commitea, local-level no
- ⚡ `@symbol` para mencionar archivos específicos en requests
- ⚡ Plan Mode = breadth (múltiples archivos), Thinking Mode = depth (lógica compleja)
- ⚡ Hooks se configuran en settings de Claude y requieren reinicio para tomar efecto
- ⚡ SDK default = read-only, necesitas configurar write permissions explícitamente

---

*Notas generadas el 2026-04-13 | Curso completado 100% (21/21 lecciones)*
