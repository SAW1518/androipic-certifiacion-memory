# Building with the Claude API
**Plataforma:** Anthropic Academy (Skilljar)  
**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/  
**Progreso:** 25 / 85 lecciones completadas (29%)  
**Última actualización:** 2026-04-22

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

# Próximas lecciones (pendientes)

| # | Lección | Sección |
|---|---------|---------|
| 26 | Being specific | Prompt engineering techniques |
| 27 | Structure with XML tags | Prompt engineering techniques |
| 28 | Providing examples | Prompt engineering techniques |
| 29 | Exercise on prompting | Prompt engineering techniques |
| 30 | Quiz on prompt engineering techniques | Prompt engineering techniques |
| 31+ | Tool use, RAG, Features of Claude, MCP, Claude Code, Agents & workflows, Final assessment | ... |
