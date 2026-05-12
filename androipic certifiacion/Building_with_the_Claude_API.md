# Building with the Claude API
**Plataforma:** Anthropic Academy (Skilljar)  
**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/  
**Progreso:** 51 / 85 lecciones completadas (60%)  
**Última actualización:** 2026-05-12

---

# Sección 1: Introduction

## Lección 1 — Welcome to the course ✅
**Tipo:** Video (2 min 14 seg)

### Resumen
Introducción al curso y su estructura. El curso enseña a integrar la API de Claude en aplicaciones reales, desde la primera request hasta arquitecturas agénticas avanzadas.

### ¿Qué aprenderás?
- Configurar y autenticar con la API de Anthropic
- Conversaciones single-turn y multi-turn
- System prompts y control del comportamiento del modelo
- Flujos de evaluación de prompts (evals)
- Técnicas de prompt engineering
- Tool use (herramientas externas)
- RAG (Retrieval-Augmented Generation)
- Extended thinking, imágenes, PDFs, prompt caching
- MCP (Model Context Protocol)
- Agentes y workflows (paralelización, chaining, routing)

### Prerrequisitos
- Python intermedio
- Manejo básico de JSON

---

# Sección 2: Anthropic Overview

## Lección 2 — Overview of Claude models ✅
**Tipo:** Video

### La familia de modelos Claude

| Modelo | Descripción | Casos de uso |
|--------|-------------|--------------|
| **Claude Opus** | El más poderoso, razonamiento profundo | Tareas complejas, análisis exhaustivo |
| **Claude Sonnet** | Balance entre capacidad y velocidad | Uso general, producción |
| **Claude Haiku** | El más rápido y económico | Tareas simples, alta frecuencia |

### Selección del modelo correcto
- **Haiku:** clasificación, extracción simple, alto volumen, bajo costo
- **Sonnet:** la mayoría de aplicaciones en producción
- **Opus:** razonamiento complejo, alta precisión, investigación

### Anthropic y su misión
- Empresa de seguridad en IA
- Claude usa **Constitutional AI** (IA Constitucional)
- Enfocada en IA confiable, interpretable y segura

> **Nota:** Los nombres siguen el patrón `claude-{familia}-{versión}`. Verificar siempre en [docs.anthropic.com](https://docs.anthropic.com) los modelos más recientes.

---

# Sección 3: Accessing Claude with the API

## Lección 3 — Accessing the API ✅
**Tipo:** Video

### Instalación del SDK
```bash
pip install anthropic python-dotenv
```

### Configuración del entorno
Crear un archivo `.env` en la raíz del proyecto:
```
ANTHROPIC_API_KEY=sk-ant-...
```

Cargar en Python:
```python
from dotenv import load_dotenv
load_dotenv()
```

### Crear el cliente
```python
from anthropic import Anthropic

client = Anthropic()
# Toma automáticamente ANTHROPIC_API_KEY del entorno
```

---

## Lección 4 — Getting an API key ✅
**Tipo:** Texto

### Pasos
1. Ir a [https://console.anthropic.com/](https://console.anthropic.com/) e iniciar sesión
2. Clic en **"Get API Keys"** (esquina superior derecha)
3. Clic en **"Create Key"**
4. Seleccionar workspace `Default` y darle un nombre descriptivo
5. **Copiar y guardar inmediatamente** — la key solo se muestra una vez

### Buenas prácticas de seguridad
- Nunca poner la key directamente en el código fuente
- Nunca subirla a Git
- Usar `.env` y agregarlo al `.gitignore`
- Rotar las keys periódicamente

---

## Lección 5 — Making a request ✅
**Tipo:** Video

### Primera llamada a la API

```python
from dotenv import load_dotenv
load_dotenv()
from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-5"

message = client.messages.create(
    model=model,
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hola Claude, ¿cómo estás?"}
    ]
)

print(message.content[0].text)
```

### Estructura de la respuesta (`Message` object)

```python
message.id                    # ID único del mensaje
message.role                  # "assistant"
message.content[0].type       # "text"
message.content[0].text       # El texto de la respuesta
message.stop_reason           # "end_turn", "max_tokens", etc.
message.usage.input_tokens    # Tokens de entrada consumidos
message.usage.output_tokens   # Tokens de salida generados
```

### Parámetros principales de `messages.create()`

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `model` | str | Nombre del modelo |
| `max_tokens` | int | Máximo de tokens en la respuesta |
| `messages` | list | Historial de la conversación |
| `system` | str | Instrucciones del sistema (opcional) |
| `temperature` | float | Aleatoriedad 0.0–1.0 (opcional) |

---

## Lección 6 — Multi-Turn Conversations ✅
**Tipo:** Video

### Concepto clave
Claude **no tiene memoria persistente** entre llamadas. Para mantener contexto, debes enviar **todo el historial de mensajes** en cada request.

### Patrón básico

```python
def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

messages = []

add_user_message(messages, "Define quantum computing en una oración")
respuesta = chat(messages)
add_assistant_message(messages, respuesta)

add_user_message(messages, "Escribe otra oración más")
respuesta_2 = chat(messages)  # Claude recuerda el contexto
```

### Reglas del historial de mensajes
- Los mensajes deben **alternar** entre `user` y `assistant`
- No pueden haber dos mensajes del mismo rol consecutivos
- Cada modelo tiene un límite de tokens (context window) — Claude Sonnet/Opus: 200k tokens

---

## Lección 7 — Chat exercise ✅
**Tipo:** Video (ejercicio práctico)

### Chat interactivo en terminal

```python
messages = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        break
    add_user_message(messages, user_input)
    response = chat(messages)
    print(f"Claude: {response}")
    add_assistant_message(messages, response)
```

---

## Lección 8 — System prompts ✅
**Tipo:** Video

### ¿Qué es un system prompt?
Instrucción que define **cómo debe comportarse Claude** durante toda la conversación. Se pasa como parámetro `system=`.

### Ejemplo

```python
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system="Eres un asistente experto en Python. Responde siempre con ejemplos de código.",
    messages=[
        {"role": "user", "content": "¿Cómo itero una lista?"}
    ]
)
```

### Usos comunes

| Uso | Ejemplo |
|-----|---------|
| Definir el rol | `"Eres un asistente de soporte para Acme Corp."` |
| Establecer tono | `"Responde siempre de forma concisa y profesional."` |
| Dar contexto | `"El usuario tiene el plan Pro activo."` |
| Restricciones | `"No discutas temas fuera del soporte técnico."` |
| Formato de salida | `"Responde siempre en JSON válido."` |

### Diferencia entre `system` y `user`
- **system:** instrucciones para Claude, aplica a toda la conversación
- **user:** mensajes del usuario final

---

## Lección 9 — System prompts exercise ✅
**Tipo:** Video (1 min 25 seg) — `03 - 007 - System Prompts Exercise.mp4`

### Planteamiento
Ejercicio práctico: el notebook pide a Claude que escriba una función Python que compruebe si una cadena tiene caracteres duplicados. Sin system prompt, Claude devuelve mucho código + mucha explicación + comentarios.

**Objetivo del ejercicio:** reducir la cantidad de código generado pasando un `system` prompt a la función `chat()` que asigne un rol a Claude y lo anime a responder lo más conciso posible.

### Solución propuesta
System prompt ejemplo:
```python
system = "Eres un ingeniero de Python que escribe código muy conciso."
```
Con ese system prompt la respuesta queda mucho más corta y alineada con lo pedido.

### Takeaway
El rol asignado en el system prompt es suficiente para condicionar el estilo/longitud de la respuesta sin cambiar el user message.

---

## Lección 10 — Temperature ✅
**Tipo:** Video (6 min 7 seg) — `03 - 008 - Temperature.mp4`

### Cómo genera texto Claude (recap)
1. **Tokenización:** divide el input en tokens.
2. **Predicción:** calcula probabilidades de cada siguiente token candidato.
3. **Muestreo (sampling):** elige un token según esas probabilidades.
4. Se repite token a token hasta completar la respuesta.

### Qué es `temperature`
Parámetro decimal entre **0 y 1** que se pasa en la llamada al modelo y modifica la distribución de probabilidades en la fase de sampling.

| Temperatura | Efecto |
|-------------|--------|
| **0.0** | Salida determinista: siempre se elige el token con mayor probabilidad. |
| **Bajo (0.0–0.3)** | Menos aleatoriedad. Ideal para extracción de datos, clasificación, tareas donde no hace falta creatividad. |
| **Medio** | Mezcla de consistencia y variedad. |
| **Alto (0.7–1.0)** | Sube la probabilidad de elegir tokens menos comunes. Ideal para brainstorming, escritura creativa, marketing creativo, chistes. |

### Código — pasar `temperature` a la función chat
```python
def chat(messages, temperature=1.0):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        temperature=temperature,
    )
    return message.content[0].text
```

### Demo del video
- Prompt: "genera una idea de película en una sola frase".
- Con `temperature=0.0` se repiten ideas muy parecidas (en el video: varias ideas sobre un "viajero del tiempo").
- Con `temperature=1.0` las ideas se diversifican.
- **Nota importante:** subir la temperatura no garantiza ideas drásticamente distintas, solo **aumenta la probabilidad** de que lo sean.

### Regla general
- Tarea determinista / extracción → temperatura baja.
- Tarea creativa → temperatura alta.

---

## Lección 11 — Course satisfaction survey ✅
**Tipo:** Encuesta de satisfacción del curso (sin contenido técnico).

---

## Lección 12 — Response streaming ✅
**Tipo:** Video (8 min 24 seg) — `03 - 009 - Response Streaming.mp4`

### Problema que resuelve
Una llamada normal a la API puede tardar 10–30 s según el tamaño del input/output. Mostrar solo un spinner es mala UX. Los usuarios esperan ver la respuesta aparecer token a token.

### Cómo funciona streaming
1. El cliente envía el mensaje del usuario a Claude.
2. Claude responde casi inmediatamente con un evento inicial (sin contenido) indicando que empieza a generar.
3. Se recibe una **secuencia de eventos**, cada uno con un fragmento del mensaje.
4. El servidor puede reenviar cada fragmento al cliente web/móvil conforme llega.

### Tipos de eventos que emite Claude al hacer streaming
- `message_start`
- `content_block_start`
- `content_block_delta` ← **los que traen el texto real generado**
- `content_block_stop`
- `message_delta`
- `message_stop`

### Forma 1 — Iterador raw con `stream=True`
```python
messages = []
add_user_message(messages, "Escribe una descripción de una frase de una base de datos ficticia")

stream = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    stream=True,
)

for event in stream:
    print(event)
```
Obtienes los eventos en crudo; tendrías que filtrar manualmente los `content_block_delta` para extraer el texto.

### Forma 2 — Helper del SDK: `client.messages.stream(...)` (recomendado)
```python
messages = []
add_user_message(messages, "Escribe una descripción de una frase de una base de datos ficticia")

with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages,
) as stream:
    for text in stream.text_stream:
        print(text, end="")
```
`stream.text_stream` entrega solo el **texto** de cada delta, sin que tengas que lidiar con los tipos de evento.

### Recuperar el mensaje final completo después del stream
```python
with client.messages.stream(...) as stream:
    for text in stream.text_stream:
        pass  # (o reenviar al cliente)
    final_message = stream.get_final_message()
```
Útil para guardar toda la conversación en base de datos al terminar el stream.

### Nota
Un fragmento puede contener una o varias palabras (no hay garantía de un token por evento).

---

## Lección 13 — Structured data ✅
**Tipo:** Video (5 min 59 seg) — `03 - 011 - Structured Data.mp4`

### Problema
Cuando pides a Claude que genere datos estructurados (JSON, Python, lista, etc.), suele envolverlos con:
- Un **header** explicativo.
- Un **footer** con comentarios.
- **Triple backtick** de Markdown (` ```json `).

Ejemplo: si tu app web muestra una regla de AWS EventBridge generada por Claude, quieres solo el JSON puro para poder copiarlo sin parsear a mano.

### Técnica: **assistant prefill** + **stop sequences**
Combinar un mensaje `assistant` pre-rellenado con `stop_sequences` fuerza a Claude a "continuar" escribiendo solo el contenido que quieres, y a detenerse justo cuando lo cierra.

### Código
```python
messages = []
add_user_message(messages, "Genera una regla de EventBridge muy corta en JSON")
add_assistant_message(messages, "```json")

message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    stop_sequences=["```"],
)
text = message.content[0].text
```

### Qué pasa internamente
1. Claude ve el user message y decide que va a escribir una regla con header + JSON en un bloque Markdown.
2. Al leer el assistant pre-relleno ` ```json `, Claude asume que él ya empezó ese bloque y continúa directamente con el JSON.
3. Al terminar el JSON, Claude intenta cerrar el bloque con ` ``` `, pero la `stop_sequence` lo corta justo ahí.
4. Resultado: solo el JSON crudo.

### Limpieza opcional
```python
import json
data = json.loads(text.strip())
```

### Generalización
La técnica no es solo para JSON — sirve para Python, regex, listas con viñetas, o cualquier dato estructurado donde quieras solo el contenido sin comentarios alrededor.

---

## Lección 14 — Structured data exercise ✅
**Tipo:** Video (4 min 57 seg) — `03 - 012 - Structured Data Exercise.mp4`

### Planteamiento
Partiendo de un prompt que pide "tres comandos de AWS CLI de ejemplo", obtener los tres comandos juntos sin comentarios usando **solo** assistant prefill + stop sequences (sin modificar el user prompt).

### Paso 1 — prefill con backticks y stop sequence
```python
add_assistant_message(messages, "```")
# stop_sequences=["```"]
```
Problema: a veces Claude añade la palabra `bash` como identificador de lenguaje Markdown al principio.

### Paso 2 — incluir el identificador de lenguaje en el prefill
```python
add_assistant_message(messages, "```bash")
```
Ahora Claude sabe que está dentro de un bloque de código bash y no añade el identificador.

### Paso 3 — problemas residuales
- A veces devuelve solo un comando (Claude quiere abrir 3 bloques separados).
- Al estar en bloque bash, puede añadir comentarios con `#`.

### Paso 4 — ampliar el prefill con guía explícita
El hint del ejercicio: el prefill no tiene por qué limitarse a caracteres de formato. Puedes escribir texto para guiar a Claude.
```python
add_assistant_message(
    messages,
    "Aquí están los tres comandos en un solo bloque sin ningún comentario:\n```bash",
)
```
Con esto se obtiene consistentemente los 3 comandos, en un solo bloque, sin comentarios.

### Takeaway
El assistant prefill permite guiar drásticamente el formato y el contenido de la respuesta, no solo poner caracteres de apertura.

---

## Lección 15 — Quiz on accessing Claude with the API ✅
**Tipo:** Quiz. Sin contenido teórico nuevo.

---

# Sección 4: Prompt evaluation

## Lección 16 — Prompt evaluation ✅
**Tipo:** Video (1 min 48 seg) — `04 - 001 - Prompt Evaluation.mp4`

### Dos temas nuevos
- **Prompt engineering:** técnicas para escribir/editar prompts y obtener mejores respuestas.
- **Prompt evaluation (evals):** pruebas automatizadas sobre un prompt para obtener una métrica objetiva de su efectividad.

> En esta sección el foco es **evals**. Una vez que sepamos medir, aplicaremos técnicas de prompt engineering.

### Tres caminos típicos tras escribir un prompt
1. Probar una o dos veces y dar por bueno → **trampa común**.
2. Probar con algunos inputs personalizados y ajustar casos borde → **también una trampa**.
3. ✅ **Ejecutar el prompt por un pipeline de evaluación** que dé una puntuación objetiva y permita iterar hasta maximizarla.

---

## Lección 17 — A typical eval workflow ✅
**Tipo:** Video (4 min 36 seg) — `04 - 002 - A Typical Eval Workflow.mp4`

### Notas previas
- No hay una metodología única estándar en la industria.
- Existen libs open-source y servicios de pago, pero en este curso se implementa todo desde cero en un Jupyter notebook para entender el funcionamiento.

### Pasos de un eval workflow típico

1. **Redactar el prompt inicial (v1).** Algo simple, ej. `"Please answer the user's question: {question}"`.
2. **Crear un eval dataset.** Lista de inputs posibles para el prompt. Puede tener 3, 30, 300 o 3.000 registros. Se puede hacer a mano o con Claude.
3. **Interpolar cada input del dataset en el prompt** y enviar cada uno a Claude para obtener respuestas reales.
4. **Calificar (grading).** Emparejar cada (input, respuesta) y pasarlo por un grader que devuelve una puntuación (comúnmente 1–10).
5. **Promediar las puntuaciones** para tener una métrica objetiva de la versión actual del prompt.

### Fórmula mental
```
Score = mean(grade(output_i) for i in dataset)
```

Una vez tienes esa métrica, puedes iterar sobre el prompt e intentar subirla.

---

## Lección 18 — Generating test datasets ✅
**Tipo:** Video (4 min 44 seg) — `04 - 003 - Generating Test Datasets.mp4`

### Caso de uso del curso
Prompt que ayuda a un usuario a resolver tareas específicas de AWS devolviendo **solo** uno de tres formatos: Python, JSON config o una regex — **sin** headers/footers/explicaciones.

### Prompt v1
```
Please provide a solution to the following task: {task}
```

### Estructura del dataset
Array de objetos JSON, cada uno con al menos:
```json
{"task": "descripción de la tarea"}
```

### Generar el dataset con Haiku (modelo rápido/barato)
Patrón: función `generate_dataset()` que llama a Claude Haiku con un prompt que pide que devuelva un array JSON de tareas. Se combina con assistant prefill + stop sequence para obtener solo el JSON.

```python
def generate_dataset():
    prompt = "..."  # prompt largo que pide N casos de prueba en formato JSON
    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)
```

### Persistir el dataset a disco
```python
with open("dataset.json", "w") as f:
    json.dump(generate_dataset(), f, indent=2)
```

Así se puede reutilizar sin regenerarlo cada vez.

---

## Lección 19 — Running the eval ✅
**Tipo:** Video (6 min 42 seg) — `04 - 004 - Running the Eval.mp4`

### Tres funciones base del pipeline

**1. `run_prompt(test_case)`** — fusiona el test case con el prompt y lo envía a Claude.
```python
def run_prompt(test_case):
    prompt = f"Please solve the following task: {test_case['task']}"
    messages = []
    add_user_message(messages, prompt)
    output = chat(messages)
    return output
```

**2. `run_test_case(test_case)`** — ejecuta el prompt y califica la salida. Devuelve un dict con output, test_case y score.
```python
def run_test_case(test_case):
    output = run_prompt(test_case)
    score = 10  # TODO: grading real se añade más adelante
    return {
        "output": output,
        "test_case": test_case,
        "score": score,
    }
```

**3. `run_eval(dataset)`** — itera el dataset y acumula los resultados.
```python
def run_eval(dataset):
    results = []
    for test_case in dataset:
        results.append(run_test_case(test_case))
    return results
```

### Ejecutar
```python
with open("dataset.json") as f:
    dataset = json.load(f)
results = run_eval(dataset)
print(json.dumps(results, indent=2))
```

### Observación
Sin formatting instructions en el prompt inicial, Claude devuelve respuestas con mucho texto extra. Eso se atacará con prompt engineering más adelante. La primera pasada tarda ~30 s (Haiku, 3 casos).

---

## Lección 20 — Model based grading ✅
**Tipo:** Video (10 min 1 seg) — `04 - 005 - Model Based Grading.mp4`

### Tres tipos de grader

| Tipo | Cómo | Ventaja | Desventaja |
|------|------|---------|------------|
| **Code-based** | Función Python que valida programáticamente (longitud, presencia de palabras, sintaxis JSON/Python, readability score, etc.) | Rápido, determinista, barato | Solo aplica a criterios verificables con código |
| **Model-based** | Otro llamado a Claude que evalúa la respuesta según criterios (calidad, completitud, adherencia al prompt) | Muy flexible, evalúa casi cualquier criterio | Costo extra de API, puede ser variable |
| **Human-based** | Personas reales revisan las respuestas | Máxima flexibilidad | Lento, tedioso, caro |

Todos devuelven una **señal objetiva** (típicamente número 1–10, aunque no es obligatorio).

### Criterios de evaluación del caso del curso
1. Solo Python, JSON o regex — sin explicaciones adicionales.
2. La sintaxis del código debe ser válida.
3. La respuesta debe abordar la tarea del usuario correctamente.

**Decisión:**
- 1 y 2 → code-based grader.
- 3 → model-based grader (su flexibilidad se ajusta mejor).

### Implementación — `grade_by_model(test_case, output)`
```python
def grade_by_model(test_case, output):
    prompt = f"""You are an expert evaluator...
    Task: {test_case['task']}
    AI-generated solution: {output}
    Respond with JSON:
    {{
      "strengths": [...],
      "weaknesses": [...],
      "reasoning": "...",
      "score": <number>
    }}
    """
    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)
```

### Truco importante — pedir razones además del score
Si solo pides un número, el modelo tiende a devolver siempre un 6 ("término medio"). Pedirle `strengths`, `weaknesses` y `reasoning` lo obliga a fundamentar y dar scores más concretos.

### Integración en `run_test_case`
```python
def run_test_case(test_case):
    output = run_prompt(test_case)
    model_grade = grade_by_model(test_case, output)
    return {
        "output": output,
        "test_case": test_case,
        "score": model_grade["score"],
        "reasoning": model_grade["reasoning"],
    }
```

### Puntuación promedio
```python
from statistics import mean

def run_eval(dataset):
    results = [run_test_case(tc) for tc in dataset]
    average_score = mean(r["score"] for r in results)
    print(f"Average: {average_score}")
    return results
```

---

## Lección 21 — Code based grading ✅
**Tipo:** Video (7 min 26 seg) — `04 - 006 - Code Based Grading.mp4`

### Qué valida el code grader del curso
1. Que la salida sea del formato esperado (Python / JSON / regex puro).
2. Que la sintaxis sea válida.

### Validadores auxiliares
```python
import json, ast, re

def validate_json(text):
    try:
        json.loads(text)
        return 10
    except Exception:
        return 0

def validate_python(text):
    try:
        ast.parse(text)
        return 10
    except Exception:
        return 0

def validate_regex(text):
    try:
        re.compile(text)
        return 10
    except Exception:
        return 0
```
Cada uno intenta parsear/compilar: si funciona → 10, si falla → 0.

### Necesidad: que el dataset incluya el formato esperado
Cada test case debe indicar qué formato se espera. Se actualiza el prompt de `generate_dataset` para que cada objeto devuelva también `"format": "python" | "json" | "regex"`.

### Función dispatcher
```python
def grade_syntax(output, test_case):
    fmt = test_case["format"]
    if fmt == "json":   return validate_json(output)
    if fmt == "python": return validate_python(output)
    if fmt == "regex":  return validate_regex(output)
```

### Cuatro pasos para integrarlo
1. **Añadir los validadores** (JSON/Python/regex) + `grade_syntax`.
2. **Actualizar `generate_dataset`** para que cada test case tenga la clave `format`.
3. **Actualizar el prompt v1** para pedir explícitamente solo Python/JSON/regex sin comentarios.
4. **Añadir assistant prefill + stop sequence** para forzar el formato crudo:
   ```python
   add_assistant_message(messages, "```")
   # stop_sequences=["```"]
   ```
   Truco: como no sabes de antemano el lenguaje, prefill con ` ``` ` (sin identificador) o con la palabra `"code"` es suficiente para que Claude empiece a escribir código directamente.

### Combinar los dos graders en `run_test_case`
```python
def run_test_case(test_case):
    output = run_prompt(test_case)
    model_grade = grade_by_model(test_case, output)
    model_score = model_grade["score"]
    syntax_score = grade_syntax(output, test_case)
    score = (model_score + syntax_score) / 2
    return {
        "output": output,
        "test_case": test_case,
        "score": score,
        "reasoning": model_grade["reasoning"],
    }
```

### Resultado en el video
Score final promedio: **8.166**. Si es bueno o no, solo se sabrá cambiando el prompt e intentando subir el score.

---

## Lección 22 — Exercise on prompt evals ✅
**Tipo:** Video (4 min 44 seg) — `04 - 007 - Exercise on Prompt Evals.mp4`

### Tarea del ejercicio
Mejorar el workflow de evaluación dándole **más contexto** al model grader sobre qué constituye una buena solución. Dos pasos:

### Paso 1 — Actualizar `generate_dataset` para incluir `solution_criteria`
En el prompt que genera el dataset se pide una clave adicional:
```
"solution_criteria": "texto describiendo qué hace buena a una solución"
```
Cada test case ahora lleva criterios de qué debería incluir una buena respuesta.

### Paso 2 — Inyectar `solution_criteria` en el prompt del model grader
Dentro del prompt de `grade_by_model`, además de la task y el output, añadir:
```
<criteria>
{test_case["solution_criteria"]}
</criteria>
```
(Las etiquetas tipo XML se explican en la siguiente sección del curso — ingeniería de prompts.)

### Efecto
El grader ahora tiene una referencia concreta contra la que evaluar. Las razones ("reasoning") vuelven más detalladas y el score más consistente.

---

## Lección 23 — Quiz on prompt evaluation ✅
**Tipo:** Quiz. Sin contenido teórico nuevo.

---

# Sección 5: Prompt engineering techniques

## Lección 24 — Prompt engineering ✅
**Tipo:** Video (10 min 50 seg) — `05 - 001 - Prompt Engineering.mp4`

### Qué es prompt engineering
Serie de técnicas para mejorar un prompt existente y obtener resultados más confiables y de mayor calidad. La lección abre el módulo.

### Setup del módulo
- Se reutiliza el pipeline de evaluación del módulo anterior, pero encapsulado en una clase `PromptEvaluator`.
- El notebook correspondiente es **`001_prompting.ipynb`** (ya está en la carpeta del proyecto).
- Parámetro clave: `max_concurrent_tasks`. Permite paralelizar las llamadas para acelerar evaluación y generación de dataset. **Ojo con rate limits**: empezar en 3 y bajar si aparecen 429. El autor del curso usa 50 por tener cuota alta.

### Caso de uso del módulo
Prompt que genere un **plan de comidas de un día** para un atleta, dado:
- altura
- peso
- objetivo
- restricciones dietéticas

Output ideal: plan compacto con desglose calórico, macronutrientes, comidas con alimentos específicos, porciones y tiempos.

### Generación del dataset
```python
evaluator = PromptEvaluator(max_concurrent_tasks=3)
evaluator.generate_dataset(
    prompt_description="escribir un plan de comidas compacto, conciso, de un día para un atleta",
    prompt_inputs_spec={
        "height": "altura del atleta en cm",
        "weight": "peso del atleta en kg",
        "goal":   "objetivo del atleta",
        "restrictions": "restricciones dietéticas del atleta",
    },
    num_test_cases=3,
)
```
Se crea `dataset.json` en el mismo directorio (es el mismo archivo que ya tienes en la carpeta del proyecto).

### Prompt v1 (intencionalmente mal)
```python
def run_prompt(prompt_inputs):
    prompt = f"""What should this person eat?
    {prompt_inputs['height']}
    {prompt_inputs['weight']}
    {prompt_inputs['goal']}
    {prompt_inputs['restrictions']}
    """
    ...
```

### Ejecutar la eval inicial con `extra_criteria`
`run_eval` acepta un `extra_criteria` (string) que se concatena a los criterios del grader:
```python
extra_criteria = (
    "Asegurarse de que la salida incluya un total calórico diario, "
    "un desglose de macronutrientes, y comidas con alimentos exactos, "
    "porciones y tiempos"
)
evaluator.run_eval(run_prompt, extra_criteria=extra_criteria)
```

### Resultado v1
Puntuación ~**2.32** (el autor usa un modelo "malo" a propósito para que se vea la mejora con cada técnica). Probablemente tu score sea mayor con un modelo más potente.

### Reporte HTML
Cada evaluación genera `output.html` en el mismo directorio. Al abrirlo en el navegador aparece un reporte con resultados por test case: score, reasoning, criterios de solución y salida real. Es la herramienta principal para entender qué mejorar.

---

## Lección 25 — Being clear and direct ✅
**Tipo:** Video (2 min 5 seg) — `05 - 002 - Being Clear and Direct.mp4`

### La regla
La **primera línea** del prompt es la más importante. En ella hay que:
- Usar lenguaje simple y directo.
- Empezar con un **verbo de acción** que le diga a Claude exactamente qué tarea hacer.
- Aclarar qué debe contener la salida esperada.

### Ejemplos del video
- ✅ `"Write three paragraphs about how solar panels work."`
- ✅ `"Identify three countries that use geothermal energy and for each include generation statistics."`

Ambos empiezan con verbo (*Write*, *Identify*) + tarea + detalle del output.

### Aplicación al prompt del plan de comidas
Primera línea del v1 era `"What should this person eat?"` — es una pregunta, no una instrucción. Se reemplaza por:
```
Generate a one-day meal plan for an athlete that meets their dietary restrictions.
```
Verbo de acción (*Generate*) + tarea concreta + restricción explícita.

### Resultado en el video
El score subió de **2.32 → 3.92**. Sigue lejos del ideal, pero ya mejora solo con reescribir la primera línea.

---

## Lección 26 — Being specific ✅
**Tipo:** Video (5 min 14 seg) — `05 - 003 - Being Specific.mp4`

### La idea
Ser específico = darle a Claude **directrices** o **pasos** que dirijan el output en una dirección concreta. Sin esto, Claude tiene libertad infinita para variar longitud, estructura, número de personajes, formato, etc.

### Dos tipos de directrices

**Tipo A — Lista de cualidades del output** (lo más usado):
- Controla atributos de la salida: longitud, estructura, elementos obligatorios.
- Ejemplo (cuento corto): *"Mantén la historia por debajo de 1000 palabras, agrega acción ascendente, incluye al menos un personaje secundario"*.

**Tipo B — Lista de pasos a seguir**:
- Le dice al modelo *cómo* pensar el problema, paso a paso.
- Ejemplo (cuento corto): *"Primero haz brainstorming de 3 talentos, elige el más interesante, esboza una escena que lo revele, piensa en personajes secundarios"*.

Muy a menudo se combinan ambas en prompts profesionales.

### Cuándo usar cada una
- **Tipo A** (cualidades): casi siempre. En prácticamente cualquier prompt.
- **Tipo B** (pasos): cuando el problema es complejo y quieres forzar a Claude a considerar perspectivas o datos adicionales que no consideraría por defecto. Ejemplo del video: *"descubre por qué las ventas del equipo cayeron este trimestre"* — útil forzar pasos para que considere múltiples ángulos.

### Aplicación al prompt del plan de comidas
- Añadir lista de directrices (Tipo A): score subió de **3.92 → 7.86**.
- Probar con pasos (Tipo B) en lugar de directrices: bajó a **7.3**.
- **Conclusión del autor:** las directrices ganaron. Se queda con Tipo A.

### Takeaway
Por defecto, lista de directrices (Tipo A). Añade pasos (Tipo B) solo cuando quieras forzar razonamiento más amplio.

---

## Lección 27 — Structure with XML tags ✅
**Tipo:** Video (4 min 1 seg) — `05 - 004 - Structure with XML Tags.mp4`

### El problema
Cuando interpolas mucho contenido en un prompt (ej. 20 páginas de registros de ventas, código + documentación, etc.), Claude puede confundirse sobre qué texto pertenece a qué cosa.

### La solución
Envolver bloques de contenido con etiquetas XML que indiquen su naturaleza:
```xml
<sales_records>
  ...20 páginas de registros...
</sales_records>
```

### Ejemplo del video — depurar código
Prompt malo:
```
Depura mi código a continuación usando la documentación proporcionada.
[código]
[documentación]
```
Claude no sabe qué es código y qué es documentación.

Prompt bueno:
```xml
Depura mi código usando la documentación proporcionada.
<my_code>
  ...
</my_code>
<documentation>
  ...
</documentation>
```

### Reglas prácticas
- Los nombres de las etiquetas son **inventados** por ti — no hay un set "oficial".
- Cuanto más descriptivo el nombre, mejor (`sales_records` > `records` > `data`).
- Útil incluso cuando el contenido interpolado es corto (ej. envolver datos del atleta en `<athlete_info>...</athlete_info>` añade claridad).

### Aplicación al prompt del plan de comidas
Envolver `height/weight/goal/restrictions` con `<athlete_info>...</athlete_info>` subió la puntuación bastante respecto al 7.3 anterior.

### Takeaway
Las etiquetas XML son la forma estándar y más confiable de dar estructura a un prompt. Usar siempre que haya contenido interpolado, no solo cuando sea grande.

---

## Lección 28 — Providing examples (one-shot / multi-shot prompting) ✅
**Tipo:** Video (6 min 44 seg) — `05 - 005 - Providing Examples.mp4`

### Qué es
Incluir en el prompt uno (one-shot) o varios (multi-shot) **ejemplos** concretos de pares input → output ideal. Es probablemente la técnica más efectiva del módulo.

### Estructura de un ejemplo
Siempre se envuelven con etiquetas XML para que Claude entienda dónde empieza y termina cada par:

```xml
Aquí hay un ejemplo con una entrada de muestra y una salida ideal.

<sample_input>
  great game tonight
</sample_input>

<ideal_output>
  positive
</ideal_output>
```

### Para qué sirve
1. **Cubrir casos extremos** — ej. tweets sarcásticos. Sin ejemplo, Claude clasifica *"oh sí, justo lo que necesitaba, un retraso de vuelo"* como positivo. Con un ejemplo de sarcasmo etiquetado como negativo, lo aprende.
2. **Formatos de salida complejos** — si necesitas un JSON con una estructura específica, mostrar un ejemplo es más eficaz que describirlo.

### Truco extra del video — explicar por qué el ejemplo es bueno
Después del `<ideal_output>`, añadir una pequeña explicación del **por qué** ese output es ideal. Ej:

> *"Este plan de comidas de ejemplo está bien estructurado, contiene un total calórico, desglose macronutricional, y respeta las restricciones del atleta."*

Refuerza qué características debe replicar Claude. El autor copia el `reasoning` del grader del `report.html` para esto.

### Workflow recomendado para evals
1. Corres una eval inicial.
2. Abres `report.html`.
3. Buscas el caso con score más alto (idealmente un 10).
4. Copias ese par input/output como ejemplo en el prompt.
5. Vuelves a correr la eval.

### Aplicación al prompt del plan de comidas
Score subió a **7.96**.

### Takeaway
Casi siempre vale la pena agregar al menos un ejemplo. Multi-shot cuando hay casos extremos o formato complejo de salida.

---

## Lección 29 — Exercise on prompting ✅
**Tipo:** Video ejercicio (5 min 22 seg) — `05 - 006 - Exercise on Prompting.mp4`

### El ejercicio
Notebook nuevo: **`003_exercise.ipynb`**.

**Tarea:** mejorar un prompt malo que recibe un pasaje de texto académico y debe devolver un **array JSON de strings con todos los temas** mencionados.

- Input del prompt: `content` (un párrafo de texto).
- Output esperado: array JSON, ej. `["paneles solares", "energía renovable", ...]`.
- Score base con prompt malo: **2.8**.
- Objetivo: superar 7.

### Solución del autor

**Paso 1 — Ser claro y directo (Lección 25)**
Reescribir la primera línea del prompt:
```
Extract key topics mentioned from a text passage of an academic journal in a JSON array of strings.
```
Score saltó a **9.5**. La técnica más simple ya casi resolvió el problema.

**Paso 2 — Estructura con XML (Lección 27)**
Envolver el contenido interpolado:
```xml
<text>
  {content}
</text>
```

**Paso 3 — Ser específico (Lección 26) con pasos**
```
Sigue estos pasos:
1. Examina cuidadosamente el texto proporcionado
2. Identifica cada tema mencionado
3. Añade cada tema a un array JSON
4. Responde con el array JSON. No proporciones ningún otro texto ni comentario.
```

**Resultado final:** score se mantuvo en **9.5** — para esta tarea simple, ser claro y directo bastó.

### Lección general
A veces una sola técnica resuelve el problema. Aplicar todas las técnicas no siempre mejora el score; lo importante es identificar qué falla en el output (mirar `report.html`) y aplicar la técnica que lo arregle.

---

## Lección 30 — Quiz on prompt engineering techniques ✅
**Tipo:** Quiz (sin video)

Quiz interactivo en Skilljar que cubre las técnicas: ser claro y directo, ser específico, XML tags, providing examples. No hay material descargable.

---

# Sección 6: Tool use with Claude

## Lección 31 — Introducing tool use ✅
**Tipo:** Video (2 min 55 seg) — `06 - 001 - Introducing Tool Use.mp4`

### Para qué sirven las tools
Las tools permiten a Claude **acceder a información del mundo exterior**. Por defecto Claude solo conoce sus datos de entrenamiento — no sabe eventos recientes, no puede consultar APIs en vivo, no puede modificar nada.

**Ejemplo motivador:** un usuario pregunta *"¿cuál es el clima en San Francisco ahora?"*. Claude responde *"lo siento, no tengo acceso a información meteorológica actual"*. Con tools, podemos solucionarlo.

### Flujo completo de tool use (5 pasos)

1. **Request inicial:** Tú → Claude. Envías el prompt del usuario + las instrucciones sobre las tools disponibles.
2. **Claude decide usar una tool:** Claude → Tú. Responde diciendo *"necesito información adicional"* + qué tool quiere usar + qué argumentos.
3. **Tú ejecutas la tool:** En tu servidor corres el código (ej. llamar a una API meteorológica externa).
4. **Follow-up request:** Tú → Claude. Le envías el resultado de la tool.
5. **Respuesta final:** Claude → Tú. Genera la respuesta final aumentada con la info de la tool.

### Takeaway
Claude **no ejecuta** la tool — solo te dice cuál quiere usar y con qué argumentos. Tu código es quien corre la función real y devuelve el resultado.

---

## Lección 32 — Project overview ✅
**Tipo:** Video (2 min 23 seg) — `06 - 002 - Project Overview.mp4`

### El proyecto del módulo
Enseñar a Claude a **configurar recordatorios futuros**. Ej:
> *"Pon un recordatorio para mi cita médica, es dentro de una semana a partir del jueves"* → *"OK, te lo recordaré en ese momento."*

### Por qué necesita tools (3 problemas)
1. **Claude conoce la fecha pero no la hora exacta.** Si le pides "en 24 horas", no sabe a qué hora del día empezar a contar.
2. **Aritmética temporal poco fiable.** "¿Cuántos días desde el 13 de enero de 1973 + 379 días?" — a veces falla.
3. **No tiene mecanismo real para crear recordatorios.** Conoce el concepto pero no puede ejecutar la acción.

### Las 3 tools del proyecto
| # | Tool | Función |
|---|------|---------|
| 1 | `get_current_datetime` | Devuelve la fecha y hora actuales |
| 2 | `add_duration_to_datetime` | Suma una duración a un datetime |
| 3 | `set_reminder` | Configura el recordatorio en el futuro |

Las iremos construyendo una por una.

---

## Lección 33 — Tool functions ✅
**Tipo:** Video (5 min 22 seg) — `06 - 003 - Tool Functions.mp4`

### Notebook
**`001_tools.ipynb`** — adjunto a la lección. Trae código boilerplate y la función `add_duration_to_datetime` ya escrita para ahorrar tiempo.

> Nota: en este módulo **no se usan** las funciones auxiliares (`add_user_message`, `add_assistant_message`) porque tienen que refactorizarse para soportar bloques múltiples. Mejor hacerlo manualmente primero y luego actualizar las helpers.

### Paso 1 — Escribir la tool function
Una **tool function** es una función Python normal. Se ejecutará cuando Claude decida invocarla.

### Buenas prácticas para tool functions
1. **Nombres descriptivos** — tanto la función como sus argumentos deben ser auto-explicativos.
2. **Validar inputs y lanzar errores significativos** — Claude verá el mensaje de error y puede reintentar la llamada con args corregidos.
3. **Mensajes de error útiles** — ej. `"location cannot be empty"`, no `"invalid input"`.

### Implementación de `get_current_datetime`
```python
from datetime import datetime

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
        raise ValueError("Date format cannot be empty")
    return datetime.now().strftime(date_format)
```

- Argumento con default razonable.
- Validación: rechaza string vacío.
- Devuelve string formateado.

### Por qué validar aunque Claude difícilmente cometa el error
Aunque sea improbable que Claude pase un string vacío, si lo hace recibe el mensaje de error y puede corregirse en el siguiente intento.

---

## Lección 34 — Tool schemas ✅
**Tipo:** Video (4 min 39 seg) — `06 - 004 - Tool Schemas.mp4`

### Paso 2 — Escribir el JSON Schema de la tool
Para que Claude conozca la tool, hay que enviársela como una **especificación** con esta estructura:

```python
{
  "name": "get_weather",
  "description": "Retrieve the current weather...",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "City and state, e.g. San Francisco, CA"
      }
    },
    "required": ["location"]
  }
}
```

### Anatomía
- **`name`** — nombre de la función.
- **`description`** — qué hace, cuándo usarla, qué devuelve. **Buena práctica: 3-4 frases**, no una línea.
- **`input_schema`** — JSON Schema clásico (especificación estándar de validación, no es nada propio de Anthropic). Define args con tipo y descripción (también 3-4 frases por argumento).

### Truco del autor para generar schemas
1. Abrir Claude.ai en el navegador.
2. Pegar la función Python.
3. Adjuntar la página de docs *"Tool use with Claude"* de Anthropic completa (copy-paste todo el texto).
4. Pedirle a Claude que genere un JSON Schema siguiendo las best practices del documento adjunto.
5. Copiar el resultado a tu notebook.

### Convención de nombrado
```python
get_current_datetime          # la función
get_current_datetime_schema   # el schema
```

### Wrap con `ToolParam` (opcional pero recomendado)
```python
from anthropic.types import ToolParam

get_current_datetime_schema = ToolParam({
    "name": "get_current_datetime",
    "description": "...",
    "input_schema": {...}
})
```
No es estrictamente necesario, pero evita errores de tipo más adelante.

---

## Lección 35 — Handling message blocks ✅
**Tipo:** Video (5 min 44 seg) — `06 - 005 - Handling Message Blocks.mp4`

### Paso 3 — Llamar a Claude con el schema
Misma `client.messages.create()` de siempre + nuevo argumento `tools=[...]` con la lista de schemas:

```python
messages = [{"role": "user", "content": "¿Cuál es la hora exacta?"}]

response = client.messages.create(
    model="claude-sonnet-4-0",
    max_tokens=1024,
    messages=messages,
    tools=[get_current_datetime_schema],
)
```

### Cambio importante en la respuesta
Antes el `response.content` era una lista con **un solo bloque de texto**. Ahora puede tener **múltiples bloques**:

```python
response.content = [
    TextBlock(text="Voy a buscar la hora actual..."),
    ToolUseBlock(
        id="toolu_01...",
        name="get_current_datetime",
        input={"date_format": "%H:%M:%S"}
    )
]
```

- **`TextBlock`** — texto a mostrar al usuario.
- **`ToolUseBlock`** — señal de que Claude quiere invocar una tool. Trae `name`, `input` (los args) y un `id` único.

### Crítico: Claude NO recuerda historial
Cada request es independiente. Si vamos a responder a Claude con el resultado de la tool, **debemos enviarle todo el historial de la conversación** + el resultado.

Para mantener historial:
```python
messages.append({
    "role": "assistant",
    "content": response.content  # lista completa de bloques, no solo texto
})
```

### Implicación para las helpers
`add_user_message` y `add_assistant_message` (que se usaban en lecciones anteriores) **solo soportaban texto**. Hay que refactorizarlas más adelante para que acepten listas de bloques mixtos.

---

## Lección 36 — Sending tool results ✅
**Tipo:** Video (9 min 22 seg) — `06 - 006 - Sending Tool Results.mp4`

### Paso 4 — Ejecutar la tool function
Claude nos devolvió un `ToolUseBlock` con el campo `input` (los args). Para invocar la función Python:

```python
tool_use = response.content[1]  # el bloque ToolUse
result = get_current_datetime(**tool_use.input)
# **input desempaqueta el dict como kwargs
```

### Paso 5 — Follow-up request con un `tool_result` block
Hay que enviarle a Claude el resultado en un **mensaje de usuario** que contenga un nuevo tipo de bloque: `tool_result`.

```python
messages.append({
    "role": "user",
    "content": [{
        "type": "tool_result",
        "tool_use_id": tool_use.id,
        "content": result,
        "is_error": False
    }]
})
```

### Anatomía del `tool_result` block
| Campo | Para qué sirve |
|-------|----------------|
| `type` | Siempre `"tool_result"` |
| `tool_use_id` | **Crítico.** Debe coincidir con el `id` del `ToolUseBlock` original. Es lo que vincula request ↔ result. |
| `content` | El output de la tool, como string (usar `json.dumps()` si es complejo) |
| `is_error` | `False` por defecto. `True` si la tool falló. |

### Por qué importa el `tool_use_id`
Si Claude pide ejecutar la **calculadora** dos veces (`10+10` y `30+30`), el `assistant message` trae **dos** `ToolUseBlocks` con IDs distintos (ej. `AB3` y `PO9`). Tu follow-up debe traer dos `tool_result` blocks, cada uno con el `tool_use_id` que vincule cada resultado a su request. Claude no se basa en el orden — usa los IDs.

### Reenvío del schema
En la follow-up request hay que **incluir de nuevo** el `tools=[...]`, aunque probablemente no se use otra tool. Sin él Claude no entiende los IDs que mencionas.

### Resultado del flujo completo
Claude responde con un mensaje final tipo *"La hora actual es 15:04"*. Tool use end-to-end completado.

### Resumen del ciclo
1. Tú escribes la **tool function** (Python normal).
2. Tú escribes el **schema** (`name`, `description`, `input_schema`).
3. Llamas a Claude con `tools=[schema]`.
4. Claude responde con `TextBlock` + `ToolUseBlock`.
5. Ejecutas la tool con `**tool_use.input`.
6. Mandas follow-up con un `tool_result` block (vinculado por `tool_use_id`).
7. Claude responde con texto final.

---

## Lección 37 — Multi-turn conversations with tools ✅
**Tipo:** Video (9 min 11 seg) — `06 - 007 - Multi-Turn Conversations with Tools.mp4`

### El problema
Una sola pregunta del usuario puede requerir **múltiples tool calls encadenadas**. Ejemplo:

> *"¿Qué día será dentro de 103 días a partir de hoy?"*

Claude necesita:
1. `get_current_datetime` → fecha actual.
2. `add_duration_to_datetime` → fecha actual + 103 días.

Y en muchos casos Claude no sabe de antemano cuántas tools va a necesitar. Si la entrada viene de un usuario real, no se puede predecir.

### La solución: bucle `run_conversation`
```python
def run_conversation(messages):
    while True:
        response = chat(messages, tools=[...])
        add_assistant_message(messages, response)
        if response.stop_reason != "tool_use":
            break
        tool_results = run_tools(response)
        add_user_message(messages, tool_results)
    return messages
```

Sigue llamando a Claude hasta que `stop_reason != "tool_use"`.

### Refactorización previa necesaria
Para llegar al bucle hay que hacer 3 cambios en las helpers:

**1. `add_user_message` / `add_assistant_message` flexibles**
Antes asumían un string de texto. Ahora deben aceptar string, lista de bloques, o un objeto `Message` completo:

```python
from anthropic.types import Message

def add_assistant_message(messages, message):
    content = message.content if isinstance(message, Message) else message
    messages.append({"role": "assistant", "content": content})
```

**2. `chat()` acepta `tools` y devuelve el `Message` completo**
Antes devolvía `response.content[0].text` (asumía un solo bloque de texto). Ahora devuelve el mensaje entero porque puede haber múltiples bloques.

```python
def chat(messages, tools=None, ...):
    params = {"model": ..., "messages": messages, ...}
    if tools:
        params["tools"] = tools
    return client.messages.create(**params)
```

**3. Helper `text_from_message`**
Reemplaza la conveniencia perdida. Extrae todo el texto concatenado de un mensaje:

```python
def text_from_message(message):
    return "\n".join(
        block.text for block in message.content
        if block.type == "text"
    )
```

---

## Lección 38 — Implementing multiple turns ✅
**Tipo:** Video (16 min 25 seg) — `06 - 008 - Implementing Multiple Turns.mp4`

### Detectar si Claude quiere otra tool: `stop_reason`
La `response` tiene un campo `stop_reason`. Si vale `"tool_use"`, Claude pide más tools. Si no, ya tiene su respuesta final.

```python
if response.stop_reason != "tool_use":
    break  # salir del bucle, Claude ya terminó
```

### Función `run_tools(message)`
Recibe el mensaje del asistente, encuentra todos los `tool_use` blocks (puede haber varios), ejecuta cada uno, y devuelve una lista de `tool_result` blocks.

```python
import json

def run_tools(message):
    tool_requests = [b for b in message.content if b.type == "tool_use"]
    tool_result_blocks = []
    for tool_request in tool_requests:
        try:
            output = run_tool(tool_request.name, tool_request.input)
            tool_result_blocks.append({
                "type": "tool_result",
                "tool_use_id": tool_request.id,
                "content": json.dumps(output),
                "is_error": False
            })
        except Exception as e:
            tool_result_blocks.append({
                "type": "tool_result",
                "tool_use_id": tool_request.id,
                "content": f"Error: {e}",
                "is_error": True
            })
    return tool_result_blocks
```

### Función `run_tool(tool_name, tool_input)` — dispatcher
Para escalar a múltiples tools sin un `if` gigante:

```python
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    if tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    if tool_name == "set_reminder":
        return set_reminder(**tool_input)
    raise ValueError(f"Unknown tool: {tool_name}")
```

### Función `run_conversation(messages)` final
```python
def run_conversation(messages):
    while True:
        response = chat(messages, tools=[
            get_current_datetime_schema,
            add_duration_to_datetime_schema,
            set_reminder_schema
        ])
        add_assistant_message(messages, response)
        print(text_from_message(response))
        if response.stop_reason != "tool_use":
            break
        tool_results = run_tools(response)
        add_user_message(messages, tool_results)
    return messages
```

### Manejo de errores en tool execution
El `try/except` dentro de `run_tools` es importante: si una tool lanza, devolvemos el error como `tool_result` con `is_error=True` y el mensaje de error en `content`. Claude lo lee y puede **reintentar la tool con argumentos corregidos**.

### Test del bucle multi-turn
Pregunta: *"¿Qué hora es ahora en formato HH:MM, y también en formato segundos?"*

Resultado: Claude hace **dos tool calls separadas** (una por formato), cada una en un turno distinto. El mensaje final solo tiene un `TextBlock` con la respuesta consolidada. Funciona.

### Insight clave
Los mensajes intermedios pueden no tener bloque de texto (solo `tool_use`). Por eso es crítico que el código maneje siempre listas de bloques de cualquier tipo, no asumir nunca "el primer bloque es texto".

---

## Lección 39 — Using multiple tools ✅
**Tipo:** Video (3 min 38 seg) — `06 - 009 - Using Multiple Tools.mp4`

### Plug-and-play una vez tienes el bucle
Tras la dificultad de la lección 38, agregar tools nuevas es trivial. Solo hay que:

1. **Añadir la implementación** de la función en el notebook (ya estaban hechas: `add_duration_to_datetime` y `set_reminder`).
2. **Añadir su schema** a la lista en `run_conversation`.
3. **Añadir un `if`** en `run_tool` para despachar al nombre correcto.

```python
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    if tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    if tool_name == "set_reminder":
        return set_reminder(**tool_input)
```

### Sobre `set_reminder`
En este notebook la función no hace nada real — solo imprime *"Hola, hemos establecido un recordatorio a esta hora con este contenido"*. En una aplicación real conectarías aquí Google Calendar, una DB, lo que sea.

### Test del proyecto completo
Prompt: *"Pon un recordatorio 177 días después del 1 de enero de 2050"*.

Claude:
1. Llama `add_duration_to_datetime(start="2050-01-01", days=177)` → `"2050-06-27 (lunes)"`.
2. Llama `set_reminder(time="2050-06-27", content="...")` → print log.
3. Responde al usuario: *"Tu cita ha sido fijada en lunes 27 de junio de 2050"*.

### Takeaway del módulo de tools
La parte difícil es construir el bucle multi-turno una sola vez. Después, cada tool nueva = añadir 3 líneas.

---

## Lección 40 — Fine grained tool calling ✅
**Tipo:** Video (10 min 56 seg) — `011.1 - Fine Grained Tool Calling.mp4`

### Notebook
**`003_tool_streaming.ipynb`** — adjunto a la lección. Trae una versión modificada de `run_conversation` con `chat_stream` y manejo de eventos de streaming.

### Tool use + streaming: nuevo evento
Cuando se combinan tools y streaming, aparece un nuevo tipo de evento: **`InputJSON`** (también listado como `input_json_delta`).

```python
# En el handler del stream
elif event.type == "input_json_delta":
    print(event.partial_json)  # fragmento JSON
    # event.snapshot = acumulado de todos los fragmentos hasta ahora
```

### El problema del "buffering" por defecto
Por defecto, la API **valida el JSON** que Claude genera para los inputs de tools. Para hacerlo, **bufferiza fragmentos hasta tener un par clave-valor de top level completo**, lo valida contra el schema, y solo después libera todos los fragmentos juntos.

**Efecto observable:** ves un retraso largo, luego un golpe enorme de texto. No es un streaming "chunk a chunk" tradicional.

### Fine-Grained Tool Calling — la solución
Es un flag que **desactiva el paso de validación de JSON**. Resultado: streaming clásico, fragmento a fragmento, sin pausas.

Activación:
```python
response = run_conversation(
    messages,
    fine_grained_tool=True
)
```

(En la API se pasa como un beta header / param).

### Trade-off
Con fine-grained:
- ✅ Streaming inmediato, ideal para UI en tiempo real o procesamiento por chunks.
- ⚠️ **Puedes recibir JSON inválido**. Tu código debe manejarlo (try/except en el parser).

### Demo de JSON inválido
El video fuerza un caso donde Claude genera `"word_count": undefined` (válido en JS, **inválido en JSON** — el equivalente JSON sería `null`).

- **Sin fine-grained:** la API detecta el JSON inválido en validación, y para "salvarlo" envuelve todo el objeto `meta` como una **string** (no como objeto). Tu código recibe algo no acorde al schema.
- **Con fine-grained:** llega como JSON inválido directo y obtienes un error de parseo. Más explícito pero hay que manejarlo.

### Cuándo usarlo
- **No usar:** la mayoría de aplicaciones. El comportamiento default está bien.
- **Usar:** UI con feedback en tiempo real, o si necesitas empezar a procesar la salida de la tool antes de que termine de generarse (ej. mostrar un campo `word_count` apenas esté disponible sin esperar al resto del objeto).

---

## Lección 41 — The text edit tool ✅
**Tipo:** Video (8 min 41 seg) — `06 - 012 - The Text Edit Tool.mp4`

### Notebook
**`005_text_editor.ipynb`** — adjunto a la lección. Trae una clase `TextEditor` con todos los métodos requeridos (view, str_replace, create, undo, etc.).

### Qué es
Una **server tool** integrada en Claude — el modelo ya viene "entrenado" para invocarla. Le da habilidades de editor de texto:
- Abrir / leer archivos y directorios.
- Ver rangos específicos de líneas.
- Reemplazar texto en archivos.
- Crear archivos nuevos.
- Undo.

Esencialmente convierte a Claude en un mini ingeniero de software con acceso al filesystem.

### Lo que es y lo que NO es "built-in"
> ⚠️ Lo único built-in es el **JSON Schema**. La **implementación** la tienes que escribir tú.

Es decir, cuando Claude pide *"crea este archivo"*, tú tienes que tener una función real que escriba al disco. Anthropic no la ejecuta por ti.

### Schema mínimo a enviar
```python
{
    "type": "text_editor_20250124",  # cambia según versión del modelo
    "name": "str_replace_editor"
}
```

- Ese tipo con la fecha **depende del modelo** (Claude 3.5 vs 3.7 Sonnet, etc.).
- Internamente la API expande este pequeño schema al schema completo gigante con todos los métodos disponibles.

### Cómo funciona
1. Tú envías el mini schema en `tools=[...]`.
2. Claude responde con un `tool_use` block pidiendo, ej., `view` con `path="./main.py"`.
3. Tu código (la clase `TextEditor` del notebook) ejecuta esa acción real en el disco.
4. Devuelves el resultado en un `tool_result` block.

### Demo del notebook
1. Crear `main.py` con una función `greeting()`.
2. Pedir a Claude: *"Abre `./main.py` y resume su contenido"*. → Claude hace `view`, lee el archivo, responde.
3. Pedir: *"Abre el archivo y escribe una función para calcular pi con 5 decimales. Luego crea `test.py` con tests"*. → Claude hace `view`, luego `str_replace` con la nueva implementación, luego `create` para `test.py`.

### Cuándo usarla
Cuando necesitas darle a Claude acceso real a un sistema de archivos sin tener un editor de código moderno disponible (ej. un agente que opera en un servidor remoto, una herramienta CLI, un workflow programático). Si ya estás en Cursor/Claude Code, esto ya lo tienes.

---

## Lección 42 — The web search tool ✅
**Tipo:** Video (7 min 13 seg) — `06 - 013 - The Web Search Tool.mp4`

### Notebook
**`006_web_search.ipynb`** — adjunto a la lección.

### Qué es
Otra **server tool** built-in. Permite a Claude buscar información actualizada en la web. **A diferencia del text editor, NO tienes que implementar nada** — la búsqueda la ejecuta Anthropic. Solo declaras el schema y listo.

### Schema mínimo
```python
web_search_schema = {
    "type": "web_search_20250305",  # versión
    "name": "web_search",
    "max_uses": 5
}
```

- **`max_uses`**: límite de búsquedas que Claude puede hacer en una sola respuesta. Una búsqueda inicial puede generar follow-ups, así que limitas el total.

### Estructura de la respuesta
La `response.content` trae **muchos bloques nuevos** (no había visto antes):

| Bloque | Para qué |
|--------|----------|
| `text` | Texto normal de Claude (ej. *"voy a buscar info sobre X"*) |
| `server_tool_use` | Indica que Claude está ejecutando la search en el server |
| `web_search_tool_result` | Resultado de la búsqueda — contiene una lista de... |
| `web_search_result` | Cada resultado individual: `title`, `url` |
| `text` con `citations` | Texto final que cita fuentes específicas (`web_search_result_location`) |

### Restringir dominios — el "killer feature"
Cuando sabes que tus usuarios van a preguntar sobre temas con mucho ruido en la web (ej. salud, fitness), restringe a fuentes confiables:

```python
web_search_schema = {
    "type": "web_search_20250305",
    "name": "web_search",
    "max_uses": 5,
    "allowed_domains": ["nih.gov"]
}
```

- **Ejemplo del video:** preguntar *"¿cuál es el mejor ejercicio para ganar músculo en piernas?"*. Sin restricción → blogs random, mucho contenido generado por IA. Con `allowed_domains=["nih.gov"]` → solo fuentes científicas con respaldo de evidencia.

### Renderizar las citaciones
La idea de cómo presentar al usuario:
1. Mostrar el texto plano de los `text` blocks.
2. Cuando un texto tenga `citations` con `web_search_result_location`, renderizar al lado una pequeña cita con el dominio, título de la página y URL de la fuente.

Hace que la respuesta sea verificable en lugar de un wall of text.

---

## Lección 43 — Quiz on tool use with Claude ✅
**Tipo:** Quiz (sin video)

Quiz interactivo en Skilljar que cubre el módulo completo de tool use: schemas, flujo multi-turno, multiple tools, server tools (text editor + web search), fine-grained tool calling.

---

# Sección 7: RAG and Agentic Search

## Lección 44 — Introducing Retrieval Augmented Generation ✅
**Tipo:** Video (5 min 51 seg) — `07 - 001 - Introducing Retrieval Augmented Generation.mp4`

### El problema motivador
Tienes un documento financiero gigante (100-1000 páginas) y quieres que Claude responda preguntas específicas sobre él (ej. *"¿qué factores de riesgo tiene esta empresa?"*).

### Opción 1 — Pegar todo el documento en el prompt
Funciona a veces pero tiene 3 problemas:
1. **Límite de tokens** — documentos muy largos pueden exceder el context window (error 400).
2. **Calidad degrada** — Claude funciona peor con prompts enormes; le cuesta más enfocarse.
3. **Costo y latencia** — más tokens = más caro y más lento.

### Opción 2 — RAG (Retrieval Augmented Generation)
Dos pasos:
1. **Preprocessing:** dividir el documento en *chunks* pequeños.
2. **En query time:** recibir la pregunta del usuario, buscar los chunks **más relevantes** a esa pregunta, e incluir solo esos en el prompt.

### Ventajas de RAG
- ✅ Claude solo ve contenido relevante, no ruido.
- ✅ Escala a documentos enormes y a múltiples documentos simultáneamente.
- ✅ Prompts pequeños = baratos y rápidos.

### Desventajas de RAG
- ⚠️ **Mucha más complejidad** (preprocessing pipeline + sistema de búsqueda).
- ⚠️ **Sin garantía** de que los chunks recuperados contengan TODO el contexto necesario. Pregunta sobre *"riesgos"* puede recuperar la sección de Risk Factors pero perderse menciones a riesgos en la sección de Strategic Outlook.
- ⚠️ **Múltiples formas de chunkear** — hay que evaluar cuál funciona mejor para tu caso.

### Cuándo usar cada una
- **Sin RAG (todo el doc):** documento corto-medio, pregunta puede tocar cualquier parte.
- **Con RAG:** documentos grandes, múltiples documentos, queries puntuales sobre secciones específicas.

---

## Lección 45 — Text chunking strategies ✅
**Tipo:** Video (13 min 8 seg) — `07 - 002 - Text Chunking Strategies.mp4`

### Notebook
**`001_chunking.ipynb`** + archivo de prueba **`report.md`** (descargar y poner en el mismo directorio).

### Por qué importa cómo chunkeas
Ejemplo del video: documento con sección "Investigación médica" y "Ingeniería de software". Si chunkeas mal, puedes terminar con un chunk **etiquetado mentalmente como "ingeniería"** que contiene la frase *"infection vectors"* (vocabulario médico), o uno **médico** con la palabra *"bug"*. Cuando el usuario pregunte *"¿cuántos bugs corrigieron los ingenieros?"*, vas a recuperar el chunk médico por error y darle a Claude contexto irrelevante.

### Las 3 estrategias de chunking

#### 1. Size-based chunking
La más simple y la más usada en producción.

- Toma el documento completo y lo parte en chunks de N caracteres iguales.
- Ej. doc de ~325 chars → 3 chunks de ~108 chars.

**Problemas:**
- Cortes a mitad de palabra.
- Chunks pierden el contexto del encabezado de su sección.

**Solución: overlap.** Cada chunk incluye N caracteres de los chunks vecinos (delante y detrás), así no se pierden palabras y mantienen contexto. Hay duplicación pero mejora calidad.

```python
def chunk_by_character(text, chunk_size=500, overlap=150):
    ...
```

#### 2. Structure-based chunking
Divide por estructura del documento (headings, párrafos, secciones).

- Si el doc es Markdown, partir en `## ` (doble hash + espacio).
- Cada chunk = una sección completa.
- **Resultado ideal** cuando funciona: chunks limpios, semánticamente coherentes.

**Problema:** solo funciona si **garantizas la estructura** del documento. Si recibes PDFs sin formato, esta técnica no aplica.

```python
def chunk_by_section(text):
    return text.split("\n## ")
```

#### 3. Semantic-based chunking
La más avanzada. Parte el texto en oraciones, calcula similitud entre oraciones consecutivas usando NLP, y agrupa las relacionadas en chunks.

Resultado teórico ideal pero complejo de implementar. El curso no entra en detalle.

### Estrategia intermedia común — sentence-based con overlap
```python
def chunk_by_sentence(text, sentences_per_chunk=5, overlap=1):
    # split por regex de puntuación de fin de oración
    # cada chunk = N oraciones consecutivas
```

Buen balance: chunks coherentes + no asume estructura.

### Heurística de selección
| Garantías sobre el doc | Estrategia |
|------------------------|-----------|
| Sabes que es Markdown bien estructurado | **Structure-based** (mejor calidad) |
| Texto en prosa sin estructura clara | **Sentence-based** |
| Cualquier cosa (incluyendo código, PDFs raros) | **Character-based con overlap** (siempre funciona razonable) |

### Pruebas del notebook
- Defaults `chunk_size=150, overlap=20` → chunks demasiado chicos, no aportan info.
- Subir a `chunk_size=500, overlap=150` → chunks útiles con secciones reconocibles.

---

## Lección 46 — Text embeddings ✅
**Tipo:** Video (4 min 2 seg) — `07 - 003 - Text Embeddings.mp4`

### Notebook
**`002_embeddings.ipynb`** + un PDF guía adjunto para sacar la API key de Voyage AI.

### El problema
Después de chunkear, llega un usuario con una pregunta. Hay que **buscar entre todos los chunks** el más relacionado con esa pregunta. Esto es un problema de búsqueda — y la implementación más común es **semantic search** usando **text embeddings**.

### Qué es un embedding
Una **representación numérica** del *significado* de un texto. Lo genera un **embedding model**:

```
"I am very happy today" → [0.23, -0.41, 0.78, ..., 0.05]  (lista larga de floats entre -1 y +1)
```

### Cómo interpretar los números
Cada número del embedding es una "puntuación" de alguna cualidad del texto. **No sabemos en realidad cuál.** Pero ayuda visualizar:

| Posición | Cualidad imaginaria |
|----------|---------------------|
| `[0]` | qué tan "feliz" es el texto |
| `[1]` | qué tanto habla de "frutas" |
| `[2]` | qué tan "técnico" es |
| ... | ... |

**Reminder:** estas etiquetas son inventadas — solo la intuición es útil.

### Generador de embeddings: Voyage AI
Anthropic **no provee embeddings**. El proveedor recomendado es **Voyage AI**.

### Setup
1. Crear cuenta en Voyage AI (gratis para empezar). El PDF adjunto a la lección guía el proceso.
2. Generar API key.
3. Añadir al `.env`:
```
VOYAGE_API_KEY="..."
```
4. Instalar SDK:
```bash
pip install voyageai
```

### Función de generación (del notebook)
```python
import voyageai

vo = voyageai.Client()

def generate_embedding(text):
    result = vo.embed([text], model="voyage-3", input_type="document")
    return result.embeddings[0]
```

### Test en el notebook
Abre `report.md`, lo chunkea, toma el primer chunk, llama a `generate_embedding` → recibe lista larga de floats. Rápido e indoloro.

### Próximo paso
Generar embeddings es fácil. Lo que viene es entender **cómo usarlos** para encontrar el chunk más cercano a una query. Spoiler: distancia/similitud entre vectores.

---

## Lección 47 — The full RAG flow ✅
**Tipo:** Video (8 min) — `07 - 004 - The Full RAG Flow.mp4`

### Pipeline RAG completo — 5 pasos

| # | Cuándo | Qué |
|---|--------|-----|
| 1 | Preprocessing | Chunkear documentos fuente |
| 2 | Preprocessing | Generar embedding por cada chunk |
| 3 | Preprocessing | Almacenar embeddings en una **vector database** |
| 4 | Query time | Generar embedding de la pregunta del usuario |
| 5 | Query time | Buscar en la vector DB los chunks más similares al embedding del usuario |

Los pasos 1-3 son offline (haces el preprocessing una vez). 4-5 ocurren cada vez que un usuario hace una query.

### Visualización mental — círculo unitario
Imaginemos embeddings de **longitud 2** (en realidad son cientos de dimensiones) y que sabemos qué representa cada número:

- Eje X: cuánto habla de "medicina"
- Eje Y: cuánto habla de "ingeniería de software"

Después de un proceso de **normalización** (escala la magnitud a 1.0 — la mayoría de APIs lo hacen automáticamente), cada embedding cae sobre el círculo unitario. Visualmente puedes ver qué está cerca de qué.

### Cómo busca la vector DB: cosine similarity
Para encontrar el chunk más parecido a la query, la DB calcula el **coseno del ángulo** entre el vector de la query y cada vector almacenado:

$$\text{cos\_sim}(A, B) = \frac{A \cdot B}{||A|| \cdot ||B||}$$

- Resultado entre **-1 y +1**.
- **Cerca de +1** → muy similares (ángulo pequeño).
- **Cerca de 0** → no relacionados (90°).
- **Cerca de -1** → opuestos.

### Cosine distance vs cosine similarity
Muchas vector DBs reportan **cosine distance** = `1 - cosine_similarity`:
- Cerca de **0** → muy similares.
- Cerca de **1** → no relacionados.

Es solo una transformación más intuitiva. Saber esto evita confusión al leer documentación de Pinecone, Chroma, etc.

### Resultado del pipeline
Una vez identificado el/los chunk(s) con mayor similitud, los incluyes en el prompt junto con la pregunta del usuario y se lo envías a Claude.

---

## Lección 48 — Implementing the RAG flow ✅
**Tipo:** Video (5 min 12 seg) — `07 - 005 - Implementing the RAG Flow.mp4`

### Notebook
**`003_vectordb.ipynb`** — adjunto a la lección. Trae una clase `ClaudeVectorIndex` que actúa como vector DB en memoria.

### Patrón estándar: guardar embedding + metadata (el chunk original)
```python
store = ClaudeVectorIndex()

for embedding, chunk in zip(embeddings, chunks):
    store.add(
        vector=embedding,
        metadata={"content": chunk}
    )
```

**Clave:** además del embedding, guardas el **texto original** (o un ID de referencia). Si solo guardas el embedding, cuando hagas la búsqueda recuperarás un vector — pero el vector no sirve para construir el prompt; necesitas el texto.

### Búsqueda
```python
user_embedding = generate_embedding(
    "¿Qué hizo el departamento de ingeniería de software el año pasado?"
)

results = store.search(user_embedding, 2)  # top-2 más similares

for doc, distance in results:
    print(distance, doc.content[:200])
```

### Resultado del notebook (con `report.md`)
Top-2: Sección 2 (ingeniería de software, distance 0.71) y Metodología (0.72). Funciona.

### Próximo paso: hay casos donde falla
La búsqueda semántica funciona bien en general, pero tiene casos extremos. Se aborda en la siguiente lección con búsqueda léxica (BM25).

---

## Lección 49 — BM25 lexical search ✅
**Tipo:** Video (10 min) — `07 - 006 - BM25 Lexical Search.mp4`

### Notebook
**`004_bm25.ipynb`** — adjunto a la lección. Trae una clase `BM25Index`.

### El problema de la búsqueda semántica
Búsqueda: *"¿qué pasó con el incidente 2023Q4-011?"*

El término **"2023Q4-011"** aparece literalmente en la Sección 10 (Ciberseguridad) y se referencia en la Sección 2 (Ingeniería de software). Pero la búsqueda semántica devuelve:
1. ✅ Sección 10 (correcta)
2. ❌ Sección 3 (Análisis financiero) — **ni siquiera menciona el incidente**

La búsqueda semántica se "deja llevar" por el sentido general y pasa por alto **términos exactos raros**.

### La solución: combinar semántica + léxica
- **Búsqueda semántica** → entiende significado pero ignora términos exactos.
- **Búsqueda léxica** (clásica) → busca palabras exactas, ideal para identificadores raros.

Ambos en paralelo, luego fusionar resultados.

### BM25 (Best Match 25)
El algoritmo léxico estándar en pipelines RAG. Funcionamiento simplificado:

1. **Tokenizar la query.** Quitar puntuación, split por espacios. *"a incident 2023Q4-011"* → `["a", "incident", "2023Q4-011"]`.
2. **Contar frecuencia de cada término en el corpus completo.** *"a"* aparece 5 veces en total, *"2023Q4-011"* aparece 1 vez.
3. **Asignar peso inverso a la frecuencia.** Términos comunes (*"a"*) → peso bajo. Términos raros (*"2023Q4-011"*) → peso alto.
4. **Rankear chunks** por la frecuencia con que usan los términos de mayor peso.

### Intuición
Términos comunes son ruido. Los términos **raros y específicos** son los discriminantes. Por eso BM25 brilla con IDs, números de versión, nombres propios, etc.

### Resultado del notebook
Misma query (*"qué pasó con el incidente 2023Q4-011"*):
1. ✅ Ingeniería de software (Sección 2)
2. ✅ Ciberseguridad (Sección 10)
3. Metodología

Mucho mejor que el resultado semántico.

### API consistente con la vector store
La clase `BM25Index` tiene los mismos métodos `add_document(...)` y `search(...)` que `ClaudeVectorIndex`. **Esto es deliberado** — permite combinarlos en un retriever común en la siguiente lección.

---

## Lección 50 — A Multi-Index RAG pipeline ✅
**Tipo:** Video (6 min 45 seg) — `07 - 007 - A Multi-Index RAG Pipeline.mp4`

### Notebook
**`005_hybrid.ipynb`** — adjunto. Trae una clase `Retriever` que encapsula ambos índices.

### Diseño: el `Retriever`
```python
class Retriever:
    def __init__(self, indexes):
        self.indexes = indexes  # lista: [vector_index, bm25_index]

    def add_document(self, doc):
        for index in self.indexes:
            index.add_document(doc)

    def search(self, query, k):
        # 1. Busca en cada índice por separado.
        # 2. Fusiona resultados con Reciprocal Rank Fusion.
        # 3. Devuelve top-k.
```

### Reciprocal Rank Fusion (RRF)
Algoritmo para fusionar rankings de fuentes distintas. Funcionamiento:

1. Tomar el ranking de cada índice (vector index, BM25, etc.).
2. Para cada chunk, calcular un **score combinado**:

$$\text{score}(d) = \sum_{i \in \text{indices}} \frac{1}{1 + \text{rank}_i(d)}$$

3. Si un chunk no aparece en una fuente, ese término es 0 (o muy chico).
4. Ordenar por score descendente.

### Ejemplo numérico
| Chunk | Rank Vector | Rank BM25 | Score = 1/(1+rv) + 1/(1+rb) |
|-------|-------------|-----------|-----------------------------|
| Sección 2 | 1 | 2 | 1/2 + 1/3 = **0.833** |
| Sección 6 | 1 | 3 | 1/2 + 1/4 = **0.750** |
| Sección 7 | 2 | 3 | 1/3 + 1/4 = **0.583** |
| Sección 27 | 1 | — | 1/2 + 0 = 0.500 |

Sección 2 gana porque apareció alto en ambos índices.

### Resultado del notebook con la query problemática
Query: *"¿qué pasó con el incidente 2023Q4-011?"* → Top-3:
1. ✅ Sección 10 (Ciberseguridad)
2. ✅ Sección 2 (Ingeniería de software) — **finalmente la conseguimos**
3. Sección 5

Justo lo que queríamos. Lo mejor de búsqueda semántica + lo mejor de búsqueda léxica.

### Extensibilidad
Como cada índice cumple la misma interfaz (`add_document` + `search`), agregar un tercer tipo de índice (ej. una búsqueda por metadata, una basada en grafos, etc.) es trivial. El `Retriever` no cambia.

### Estado del pipeline RAG
- ✅ Chunking
- ✅ Embeddings
- ✅ Vector store
- ✅ BM25
- ✅ Retriever híbrido con RRF

Aún quedan técnicas adicionales para refinar la precisión, pero esto ya es un pipeline RAG de producción funcional.

---

# Sección 8: Features of Claude

## Lección 51 — Extended thinking ✅
**Tipo:** Video (7 min 1 seg) — `08 - 001 - Extended Thinking.mp4`

### Notebook
**`001_thinking.ipynb`** — adjunto a la lección.

### Qué es Extended Thinking
Una feature que le da a Claude **tiempo para razonar** antes de generar la respuesta final. En interfaces como Claude.ai aparece como un "pensamiento" colapsable que el usuario puede expandir.

### Trade-offs
- ✅ Mayor precisión en tareas complejas.
- ⚠️ **Costo:** se cobran los tokens del pensamiento.
- ⚠️ **Latencia:** la fase de pensamiento toma tiempo.

### Cuándo activarlo
Cuando ya:
1. Tienes evals corriendo sobre el prompt.
2. Has iterado el prompt con todas las técnicas (claro, específico, XML, ejemplos).
3. Y aún no llegas a la precisión que quieres.

En ese punto activa thinking. **No por defecto.**

### Nuevo tipo de bloque: `thinking`
La respuesta ahora tiene 2 bloques:
```python
response.content = [
    ThinkingBlock(thinking="Voy a abordar esto pensando primero en...", signature="..."),
    TextBlock(text="La respuesta final es...")
]
```

### La `signature` criptográfica
Cada `thinking` block trae una **`signature`** (token criptográfico). Sirve para que, si reenvías el mensaje a Claude como parte del historial, Claude pueda **verificar que no manipulaste el texto del pensamiento**. Si lo manipulaste, Claude rechaza el mensaje. Es una protección de seguridad — evita que un desarrollador modifique el razonamiento para dirigir a Claude hacia output inseguro.

### `RedactedThinkingBlock`
A veces el sistema de seguridad interno detecta que el pensamiento generado podría ser problemático y lo **redacta**. En su lugar recibes:
```python
RedactedThinkingBlock(data="<contenido encriptado>", type="redacted_thinking")
```

Sin texto plano, solo datos encriptados. Tu app debe igualmente reenviar este bloque si vuelve a llamar a Claude para preservar el contexto.

### Cómo activarlo en código
```python
def chat(messages, thinking=False, thinking_budget=1024, max_tokens=4000, ...):
    params = {...}
    if thinking:
        params["thinking"] = {
            "type": "enabled",
            "budget_tokens": thinking_budget
        }
    return client.messages.create(**params)
```

### Reglas del `thinking_budget`
- Mínimo: **1024 tokens**. Menos no se permite.
- Claude puede gastar menos del budget si no lo necesita.
- **`max_tokens` debe ser MAYOR que `thinking_budget`.** Si pones `thinking_budget=1024` y `max_tokens=1024`, no queda margen para la respuesta. Usa por ejemplo `thinking_budget=1024, max_tokens=4000`.

### Test con prompt redacted (para desarrollo)
Para probar que tu código maneja `RedactedThinkingBlock`, hay una **magic string** específica que fuerza la redacción:

```python
thinking_test_string = "ANTHROPIC_MAGIC_STRING_TRIGGER_REDACTED_THINKING_..."
# (la string completa está en la celda del notebook)
```

Mandar esa string como user message garantiza que recibas un `RedactedThinkingBlock`. Útil para testear que tu UI/código no se rompa con ese tipo de bloque.

---
| 31+ | Tool use, RAG, Features of Claude, MCP, Claude Code, Agents & workflows, Final assessment | ... |
