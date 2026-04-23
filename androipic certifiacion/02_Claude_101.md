# Claude 101 — Notas Completas del Curso
**Plataforma:** Anthropic Academy (Skilljar)
**URL:** https://anthropic.skilljar.com/page/claude-101
**Fecha de extracción:** Abril 2026
**Relevancia para Certificación:** Claude Certified Architect – Foundations

---

## Estructura del Curso (13 lecciones, 4 secciones + Conclusión)

| Sección | Lección | ID | Duración | Video YouTube |
|---|---|---|---|---|
| Meet Claude | What is Claude? | 383389 | 15 min | VHsp6Hp7Stw |
| Meet Claude | Your first conversation with Claude | 383390 | 20 min | 0vZ_UVLhSQQ |
| Meet Claude | Getting better results | 383392 | 20 min | Zzn-g8lvLMA |
| Meet Claude | Claude desktop app: Chat, Cowork, Code | 440908 | 20 min | — |
| Organizing your work | Introduction to projects | 383393 | 25 min | GJ5jTgcbRHA |
| Organizing your work | Creating with artifacts | 383394 | 20 min | — |
| Organizing your work | Working with skills | 383396 | 20 min | LpGpwhORWr0 |
| Expanding Claude's reach | Connecting your tools | 383397 | 20 min | _jjSS0qGFbI, QTfoYDzqXn0 |
| Expanding Claude's reach | Enterprise search | 383398 | 15 min | — |
| Expanding Claude's reach | Research mode for deep dives | 383399 | 20 min | R-KJgjIrh24 |
| Putting it all together | Claude in action: use-cases by role | 383401 | 10 min | — |
| Putting it all together | Other ways to work with Claude | 383402 | 10 min | s-avRazvmLg, tI1uzSJuSxc, 8ZRTSIRWLu4, IypXvHej9eY |
| Conclusion | What's next? | 385338 | 5 min | — |

---

## SECCIÓN 1: Meet Claude

---

### Lección 1: What is Claude? (ID: 383389)
**Duración:** 15 minutos | **Video:** https://youtu.be/VHsp6Hp7Stw

#### Objetivos de Aprendizaje
- Explicar qué es Claude y los principios que guían su diseño
- Describir las capacidades fundamentales de Claude y cómo difiere de un simple chatbot
- Identificar las diferentes formas de acceder a Claude (web, desktop, mobile)

#### Video: Turning Claude into your thinking partner
*Transcript completo (1:09):*
> You had an idea. It started yesterday with a glimmer. What was it? Right. Claude remembered it. Your idea was hungry. Hungry for answers and connections. Claude helped you look, reading alongside you. Turn this into what? A deck, spreadsheets, documents, the tedious parts handled. Your idea stopped being just words and slides. It became entries, updates, actions, real things in real places. You kept going. You left your desk. Your idea followed into your phone. Calendar for when, maps for where, reminders for later. By evening, it was done. The idea was always yours. With Claude as your thinking partner, you made it real.

#### Key Takeaways
Claude is built to be **helpful, harmless, and honest**: At a high level, Claude is guided by principles that help it avoid toxic or discriminatory outputs, avoid helping humans engage in illegal or harmful activities, and avoid deception.

#### Qué es Claude
- Claude es más que un chatbot: es un asistente de IA diseñado para ser tu socio de pensamiento
- Claude se guía por principios que lo hacen genuinamente útil, honesto y que evita daños
- Creado por Anthropic con un enfoque en la seguridad y alineación de IA

#### Capacidades Principales de Claude
- **Escritura y edición:** redacción, edición, brainstorming, resúmenes para cualquier audiencia
- **Análisis:** proceso e interpretación de datos, informes, tendencias, y perspectivas accionables
- **Investigación:** síntesis de información, identificación de patrones, análisis de documentos extensos (200K+ tokens = ~500 páginas; hasta 1M tokens en planes Pro/Max/Team/Enterprise con Opus 4.6)
- **Programación:** Claude Opus 4.6 es el mejor modelo de codificación. Escribe, depura y explica código en múltiples lenguajes
- **Resolución de problemas:** problemas cognitivos complejos, matemáticas, pensamiento estratégico. Claude Opus 4.6 y Sonnet 4.6 son modelos híbridos con "extended thinking" para razonamiento profundo
- **Aprendizaje:** explicaciones adaptadas, exploración de ideas, práctica de conceptos

#### Cómo Acceder a Claude
- **Web:** claude.ai — acceso universal desde cualquier navegador
- **Desktop:** App de escritorio con Claude Chat, Cowork y Code
- **Mobile:** App móvil con sync entre dispositivos
- **API:** Para desarrolladores integrando Claude en productos

#### Modelos Actuales (a mayo 2025)
- **Claude Opus 4.6** — Modelo más poderoso, mejor en codificación del mundo, extended thinking
- **Claude Sonnet 4.6** — Modelo equilibrado, alta inteligencia con velocidad
- **Claude Haiku** — Modelo más rápido y ligero

---

### Lección 2: Your First Conversation with Claude (ID: 383390)
**Duración:** 20 minutos | **Video:** https://youtu.be/0vZ_UVLhSQQ

#### Objetivos de Aprendizaje
- Iniciar y navegar una primera conversación con Claude
- Aplicar el framework SAR (Stage, Action, Rules) para mejores prompts
- Utilizar carga de archivos e iteración para obtener mejores resultados

#### Video: Getting started with Claude.ai
*Descripción (5440 chars de transcript):*
> "Imagine this. You're looking at a blank page, wrestling with a [music] big complex project, and not sure where to start. What if you had a partner who could help..."
*(Tutorial completo sobre cómo empezar con Claude.ai, estructura de conversaciones y mejores prácticas)*

#### Key Takeaways
- Claude es un poderoso colaborador inteligente que amplifica tus capacidades en todo tu trabajo. Aporta inteligencia IA, pero tú traes el contexto y la experiencia que hace el trabajo significativo.
- La mejor forma de hablar con Claude es como lo harías con un compañero de trabajo — naturalmente, concisamente y conversacionalmente.
- Antes de tu próxima conversación, considera: **configurar el escenario** (tu rol, objetivos y contexto), **definir la tarea** (qué acción quieres que tome Claude), y **especificar las reglas** (estilo, tono y ejemplos).
- Cuando subes documentos relevantes o información de contexto a un chat, Claude considera ese contenido en su respuesta.
- El poder real de Claude viene con la comunicación continua y frecuente, no solo con prompts únicos.

#### El Framework SAR para Prompts
```
S = Stage (Escenario/Contexto)
    → Tu rol, objetivos, contexto relevante

A = Action (Acción)
    → Qué tarea específica quieres que realice Claude

R = Rules (Reglas)
    → Formato, tono, longitud, restricciones, ejemplos
```

#### Iniciando tu primera conversación
- Cuando abres claude.ai, ves un campo de entrada de texto prominente
- Escribe tu mensaje de forma natural y presiona Enter o haz clic en el botón Enviar
- Puedes incluir texto, cargar archivos, o incluso pegar capturas de pantalla

#### Carga de Archivos
Tipos de archivos soportados: PDF, DOCX, CSV, TXT, PNG, JPEG
Usos prácticos:
- Subir un documento y pedir un resumen de puntos clave
- Compartir una imagen para que Claude la describa o analice
- Adjuntar una hoja de cálculo para identificar tendencias
- Subir código para que Claude lo explique o encuentre bugs

#### Pro-tip
Para que Claude considere preferencias específicas en cada respuesta, ir a Settings > General > 'What personal preferences should Claude consider?'

#### Restricciones Éticas (Constitutional AI)
Claude evita:
- Contenido tóxico o discriminatorio
- Ayudar en actividades ilegales o dañinas
- Engaño y desinformación

---

### Lección 3: Getting Better Results (ID: 383392)
**Duración:** 20 minutos | **Video:** https://youtu.be/Zzn-g8lvLMA

#### Objetivos de Aprendizaje
- Identificar por qué los primeros intentos pueden no ser perfectos y cómo mejorarlo
- Aplicar técnicas de refinamiento iterativo de prompts
- Resolver problemas comunes (respuestas genéricas, tono incorrecto, respuestas incompletas)

#### Video: Data analysis with AI (6976 chars de transcript)
*Preview del transcript:*
> "In our last lesson, we dealt with data privacy and security. What you absolutely need to protect and how to do it. So, now let's talk about the question of: what should you actually do with AI? Because that's really the point, isn't it? There's a lot of hype around AI, but I want to talk about something more practical — the actual 'so what' of it all..."

#### El Mindset de Iteración
Uno de los cambios más importantes al trabajar con Claude es reconocer que tu primer prompt raramente produce un resultado perfecto — y eso está bien. Piensa en tu prompt inicial como el inicio de una conversación, no como una solicitud única.

Los usuarios efectivos de Claude:
- **Tratan los primeros borradores como puntos de partida.** Revisan lo que Claude produce, identifican qué funciona y qué no, y refinan.
- **Dan retroalimentación específica.** "Hazlo más corto" está bien, pero "Corta los primeros dos párrafos y haz la conclusión más orientada a la acción" es mejor.
- **Saben cuándo empezar de nuevo.** Si una conversación se ha desviado, a veces es mejor iniciar una nueva conversación con un prompt mejorado.

#### Problemas Comunes y Cómo Resolverlos

| Problema | Causa | Solución |
|---|---|---|
| Respuestas genéricas | Falta de contexto específico | Añadir más contexto sobre tu audiencia, industria o caso de uso específico |
| Tono incorrecto | No especificaste el tono deseado | Indicar explícitamente: "formal", "casual", "técnico", "amigable" |
| Respuesta incompleta | Instrucciones ambiguas | Ser más específico sobre qué quieres cubierto |
| Resultado demasiado largo | Falta de restricciones de longitud | Especificar longitud: "en 3 bullet points", "en menos de 200 palabras" |
| Claude no sigue las instrucciones | Instrucciones enterradas | Poner instrucciones importantes al inicio o al final, no en el medio |

#### Técnicas Avanzadas de Prompting
- **Ejemplos few-shot:** Dar ejemplos de lo que quieres ("Aquí hay 2 ejemplos del estilo que busco...")
- **Cadena de pensamiento:** Pedir a Claude que explique su razonamiento ("Piensa paso a paso...")
- **Formato estructurado:** Especificar el formato de salida (tabla, lista, JSON, XML)
- **Rol de experto:** Asignar un rol específico ("Actúa como un analista financiero senior con 20 años de experiencia...")
- **Restricciones negativas:** Decir qué NO quieres ("Sin jerga técnica", "No menciones competidores")

---

### Lección 4: Claude Desktop App — Chat, Cowork, Code (ID: 440908)
**Duración:** 20 minutos | **Sin video YouTube**

#### Objetivos de Aprendizaje
- Distinguir entre los tres modos de la app desktop: Chat, Cowork y Code
- Elegir el modo correcto según el tipo de trabajo
- Navegar las características específicas de cada modo

#### Los Tres Modos del Desktop App

**CHAT**
El mismo Claude que conoces de claude.ai, más:
- Entrada rápida de texto
- Capturas de pantalla directas
- Dictado de voz
- Conectores nativos del computador
Ideal para: conversaciones, preguntas rápidas, análisis de textos

**COWORK**
Herramienta agéntica: defines un objetivo, conectas herramientas/recursos, y dejas que Claude trabaje:
- Alcance más amplio para investigación y análisis exhaustivos
- Puede producir documentos y entregables complejos
- Acceso a carpetas del computador
- Tareas programadas (agendadas)
- Múltiples tareas simultáneas en el sidebar

**CODE** (= Claude Code)
Para construir software:
- Desde escritura y prueba de código hasta deployment
- Funciona directamente en tu codebase
- Claude Code corre localmente en tu máquina
- Puede ejecutar subagentes
- Disponible en terminal, IDE, browser o Slack

#### Cowork vs Code — Misma base
Cowork y Code corren sobre el mismo motor — ambos son Claude Code por debajo — local en tu máquina, capaces de trabajo independiente, pueden crear sub-agentes y manejar tareas de larga duración.

#### Ejemplos de Uso de Cowork
- Revisar una carpeta de 50+ documentos de proyecto (contratos, informes financieros, transcripciones) → encontrar los más relevantes → producir un memo resumen
- Configurar tareas recurrentes: briefing diario que jala de Slack y calendario, resumen semanal de lo que se entregó, revisión matutina del inbox

**Disponibilidad:** Cowork disponible para usuarios Pro, Max, Team y Enterprise.

---

## SECCIÓN 2: Organizing Your Work and Knowledge

---

### Lección 5: Introduction to Projects (ID: 383393)
**Duración:** 25 minutos | **Video:** https://youtu.be/GJ5jTgcbRHA

#### Objetivos de Aprendizaje
- Crear y configurar un Proyecto de Claude
- Subir documentos a la base de conocimiento del proyecto
- Establecer instrucciones de proyecto para guiar el comportamiento de Claude
- Compartir proyectos con compañeros de equipo (planes Team/Enterprise)

#### Video: Getting started with projects in Claude.ai (7286 chars de transcript)
*Preview del transcript:*
> "What are projects and how do they improve working with Claude? With projects, Claude users can create self-contained workspaces with persistent context, custom knowledge bases, and tailored instructions..."

**Descripción del video (YouTube):** "Discover how to use Projects in Claude to organize your work with persistent context and custom instructions. This tutorial walks you through creating your first project, adding a knowledge base, setting up project instructions, and collaborating with team members."

#### Key Takeaways
- Los proyectos son **espacios de trabajo autónomos** con su propia memoria, historial de chats, bases de conocimiento e instrucciones personalizadas. Piensa en ellos como entornos dedicados para flujos de trabajo específicos.
- El **conocimiento del proyecto** mejora la comprensión de Claude al permitirte subir documentos relevantes que Claude referencia en todos los chats dentro de ese proyecto. No más re-subir los mismos archivos.
- Las **instrucciones del proyecto** guían el comportamiento de Claude — puedes especificar tono, nivel de expertise, estilo de respuesta, y más. Estas instrucciones se aplican a cada conversación dentro del proyecto.
- Los proyectos **escalan automáticamente**. Cuando tu base de conocimiento se acerca a los límites de contexto, Claude habilita Retrieval Augmented Generation (RAG) para expandir la capacidad hasta 10x.

#### RAG (Retrieval Augmented Generation) en Proyectos
Cuando el conocimiento del proyecto se acerca al límite de la ventana de contexto, Claude habilita RAG automáticamente:
- En lugar de cargar todo el contenido del proyecto en memoria de una vez, Claude busca y recupera inteligentemente solo la información más relevante
- Esto expande la capacidad del proyecto hasta **10x** mientras mantiene la calidad de respuesta
- Verás un indicador visual cuando tu proyecto esté en modo RAG

#### Anatomía de un Proyecto Claude
```
Proyecto
├── Nombre e ícono
├── Instrucciones del proyecto (system prompt persistente)
│   ├── Tono y estilo de respuesta
│   ├── Nivel de expertise asumido
│   ├── Restricciones y preferencias
│   └── Ejemplos y templates
├── Base de conocimiento (documentos subidos)
│   ├── PDFs, DOCXs, TXTs, CSVs
│   └── Hasta 10x capacidad con RAG
└── Historial de chats del proyecto
```

#### Casos de Uso de Proyectos
- **Proyectos de investigación:** cargar papers, extraer insights, mantener contexto entre sesiones
- **Proyectos de marca:** cargar brand guidelines para que Claude siempre respete el estilo
- **Proyectos de código:** cargar documentación de la codebase, políticas de código
- **Proyectos de contenido:** cargar ejemplos de contenido, guías de estilo, audiencia objetivo

---

### Lección 6: Creating with Artifacts (ID: 383394)
**Duración:** 20 minutos | **Sin video YouTube**

#### Objetivos de Aprendizaje
- Entender qué son los artifacts y cuándo Claude los crea
- Trabajar con diferentes tipos de artifacts
- Solucionar problemas comunes con artifacts

#### ¿Qué son los Artifacts?
Los artifacts son salidas autónomas e interactivas que Claude crea en una ventana dedicada junto a tu conversación. En lugar de obtener un bloque largo de código o texto enterrado en el chat, ves tu contenido renderizado y listo para usar.

Claude crea automáticamente un artifact cuando el contenido cumple ciertos criterios:
- Es significativo y autónomo, típicamente más de 15 líneas
- Es algo que probablemente querrás editar, iterar o reutilizar
- Representa contenido complejo que se sostiene por sí solo
- Es contenido que querrás referenciar o usar más tarde

#### Tipos Comunes de Artifacts
- **Documentos** (Markdown, texto plano, Word, PDFs, PowerPoint, Excel): Para contenido extenso que querrás exportar o seguir editando
- **Código** (Python, JavaScript, etc.): Para scripts, funciones o programas completos
- **HTML/React:** Para páginas web, prototipos, dashboards interactivos
- **SVG/Mermaid:** Para diagramas, gráficos, visualizaciones
- **Datos estructurados** (JSON, CSV): Para datos que serán procesados o importados

#### Cuándo Claude crea Artifacts vs. respuesta inline
| Artifact | Respuesta inline |
|---|---|
| +15 líneas de código | Snippet corto de código |
| Documento completo | Párrafo de texto |
| Componente reutilizable | Respuesta de una sola vez |
| HTML renderizable | Descripción de UI |

---

### Lección 7: Working with Skills (ID: 383396)
**Duración:** 20 minutos | **Video:** https://youtu.be/LpGpwhORWr0

#### Objetivos de Aprendizaje
- Entender qué son los Skills y cómo mejoran el rendimiento de Claude
- Usar Skills de Anthropic y Skills personalizados
- Gestionar Skills en configuraciones

#### Video: Claude works with you on slides, spreadsheets, and contract redlines (1:38)
**Descripción:** "See Claude Opus 4.5 tackle real work tasks—building board decks, transforming spreadsheet data, redlining contracts. Not generating drafts you'll throw away. Actual outputs you can download and use immediately."

#### ¿Qué son los Skills?
Los Skills son **carpetas de instrucciones, scripts y recursos** que Claude carga dinámicamente para mejorar el rendimiento en tareas especializadas. Piensa en ellos como paquetes de expertise — enseñan a Claude cómo completar tareas específicas de manera repetible.

Ya has visto Skills en acción si has usado Claude para crear hojas de cálculo Excel, presentaciones PowerPoint, documentos Word o PDFs. Esas capacidades de creación de archivos están powered by Skills corriendo detrás de escenas.

#### Tipos de Skills

**Anthropic Skills**
- Creados y mantenidos por Anthropic
- Incluyen capacidades mejoradas de creación de documentos: Excel, Word, PowerPoint, PDF
- Disponibles para todos los usuarios de Claude (aplicables automáticamente)

**Skills Personalizados (Custom Skills)**
- Codifican flujos de trabajo repetibles específicos de tu organización:
  - Metodología de análisis de varianza trimestral
  - Proceso de revisión de voz de marca
  - Checklist de cumplimiento normativo
- Garantizan que Claude siga los mismos pasos rigurosos cada vez
- Pueden incluir plantillas, prompts especializados, y acceso a recursos específicos

#### Skills vs. Instrucciones de Proyecto
| Skills | Instrucciones de Proyecto |
|---|---|
| Carpeta de instrucciones + scripts + recursos | Texto de instrucciones |
| Tarea específica y especializada | Comportamiento general del proyecto |
| Cargados dinámicamente cuando se necesitan | Siempre activos en el proyecto |
| Pueden compartirse entre proyectos | Específicos del proyecto |

---

## SECCIÓN 3: Expanding Claude's Reach

---

### Lección 8: Connecting Your Tools (ID: 383397)
**Duración:** 20 minutos | **Videos:** https://youtu.be/_jjSS0qGFbI, https://youtu.be/QTfoYDzqXn0

#### Objetivos de Aprendizaje
- Configurar la primera conexión (connector)
- Usar herramientas conectadas efectivamente en conversaciones con Claude

#### Video 1: Getting started with connectors in Claude.ai (3918 chars de transcript)
> Connect the tools you already use to unlock a smarter, more capable productivity partner with Claude. Claude can help you write, comment, create, code, draft, design, and so much more. However, it becomes an even more effective partner when you provide Claude more access and connectors make this possible. Connect supported apps to give Claude access to your knowledge and files, including permission to perform actions in connected sources. Connectors make Claude more knowledgeable, which means more useful responses for you. For example, with file handling capabilities, Claude can read your uploaded documents, analyze spreadsheet data, create presentations, and generate reports, all while keeping track of your broader goals and maintaining full context throughout the process. To start using connectors, navigate to the lower left portion of your Claude chat window and click the search and tools button. Once the submenu is open, you may have some existing connectors, a button to add connections...

#### Video 2: Connect Claude to Microsoft 365 (0:39)
**Descripción:** "Connect Claude with Microsoft 365 using our MCP connector. Claude integrates with SharePoint, Outlook, and Teams to bring context from your documents, emails, and calendar directly into your conversations. Search across files, analyze email threads, and surface insights to help you reason through complex problems, make informed decisions, and take action faster—all without leaving Claude."

#### Key Takeaways
- Los conectores transforman a Claude de un asistente en un **colaborador informado** al darle acceso a las mismas herramientas, datos y contexto que usas todos los días
- Los conectores permiten que Claude **lea información Y realice acciones** en tu nombre: buscar archivos, recuperar documentos, analizar datos, crear contenido, actualizar registros, ejecutar tareas
- El **Model Context Protocol (MCP)** impulsa los conectores. Piensa en MCP como **USB-C para IA** — un estándar universal que permite a Claude conectarse a muchas aplicaciones diferentes a través de una interfaz consistente

#### MCP — Model Context Protocol
```
MCP = "USB-C para IA"
├── Estándar abierto
├── Desarrolladores pueden construir conectores para cualquier herramienta
├── Claude se conecta a través de una interfaz única y consistente
└── Permite tanto leer información como ejecutar acciones
```

#### Conectores Disponibles
- **Google Workspace** (Gmail, Drive, Docs, Calendar)
- **Microsoft 365** (SharePoint, Outlook, Teams)
- **Slack** (mensajes, canales, historial)
- **Notion**
- **Jira / Linear**
- Y más a través del ecosistema MCP

#### Cómo Configurar Conectores
1. Ir a la esquina inferior izquierda de la ventana de Claude
2. Hacer clic en el botón "Search and tools"
3. En el submenú, ver conectores existentes y botón para añadir conexiones
4. Seleccionar la app y autorizar el acceso
5. Especificar permisos (solo lectura vs. lectura + acciones)

---

### Lección 9: Enterprise Search (ID: 383398)
**Duración:** 15 minutos | **Sin video YouTube**

#### Objetivos de Aprendizaje
- Entender qué ofrece Enterprise Search más allá de los chats regulares con conectores
- Identificar tipos de preguntas adecuadas para Enterprise Search
- Reconocer cómo la seguridad y los permisos protegen los datos organizacionales

#### ¿Qué es Enterprise Search?
Enterprise Search añade una opción dedicada "Ask {Your Org Name}" a tu sidebar. Está diseñado específicamente para **encontrar y sintetizar conocimiento** enterrado a través de las herramientas y datos de tu empresa.

Piensa en Enterprise Search como un **Proyecto pre-construido para toda tu organización** — la base de conocimiento de tu empresa ya está cargada, por lo que puedes saltar directamente para obtener respuestas contextualizadas.

A diferencia de los chats regulares con conectores habilitados, Enterprise Search está específicamente diseñado para la recopilación de información, usando instrucciones personalizadas configuradas por el equipo de Anthropic.

#### Casos de Uso: Enterprise Search vs. Chat Regular

**Preguntas ideales para Enterprise Search:**
- "¿Qué pasó ayer mientras estaba fuera?"
- "Resume las actualizaciones clave de los últimos 7 días"
- "¿Cuál es nuestra política de ventas para clientes Enterprise?"
- "¿Quién ha trabajado en proyectos similares a X?"
- "Dame contexto sobre el cliente Y antes de mi reunión"

**Cuando usar Chat regular:**
- Tareas de creación (redacción, código, análisis)
- Cuando necesitas conectar herramientas específicas
- Para proyectos de trabajo en curso

#### Seguridad y Permisos
- Enterprise Search respeta los permisos de acceso a datos existentes
- Los usuarios solo ven información a la que tienen acceso autorizado
- Los datos organizacionales permanecen seguros dentro de los límites de seguridad de la empresa

---

### Lección 10: Research Mode for Deep Dives (ID: 383399)
**Duración:** 20 minutos | **Video:** https://youtu.be/R-KJgjIrh24

#### Objetivos de Aprendizaje
- Habilitar y usar Research para recopilación de información exhaustiva
- Entender cómo Research trabaja con extended thinking
- Escribir prompts efectivos de Research para investigaciones complejas

#### Video: Getting started with research in Claude.ai
**Descripción (meta):** "See how Claude's Research feature transforms how you find and analyze information. This tutorial demonstrates how to use Research for comprehensive, multi-source investigations..."

#### Key Takeaways
- **Research transforma cómo Claude encuentra y analiza información.** En lugar de una búsqueda única, Claude opera agénticamente — realizando múltiples búsquedas que se construyen entre sí mientras determina exactamente qué investigar a continuación.
- **Research entrega respuestas exhaustivas en minutos.** La mayoría de los informes se completan en 5 a 15 minutos, aunque investigaciones más complejas pueden tomar hasta 45 minutos — trabajo que típicamente requeriría horas de investigación manual.
- **Extended thinking está habilitado automáticamente con Research.** Esta combinación permite a Claude tanto planificar su enfoque de manera reflexiva como recopilar información exhaustiva.

#### Cómo Funciona Research (4 Pasos)
```
Paso 1: Claude PLANIFICA la investigación
         → Descompone tu pregunta en temas de investigación
         → Determina qué ángulos explorar

Paso 2: Claude BUSCA múltiples fuentes
         → Web + conectores integrados (Gmail, Google Calendar, Drive)
         → Búsquedas iterativas que se construyen entre sí

Paso 3: Claude SINTETIZA la información
         → Analiza múltiples fuentes
         → Compila un informe exhaustivo y bien organizado

Paso 4: Claude CITA cada fuente
         → Cada afirmación en el informe enlaza a su fuente
         → Fácil de verificar y profundizar
```

#### Cómo Habilitar Research
1. Encontrar el botón Research en la parte inferior izquierda de la interfaz de chat
2. Hacer clic para habilitar — el botón se vuelve azul cuando Research está activo
3. Ingresar tu prompt y enviar
4. Ver indicadores de progreso mientras Claude busca y analiza
5. **Importante:** La búsqueda web debe estar habilitada para que Research funcione

#### Tips para Prompts Efectivos de Research
Dado que Research puede tomar 5 a 45 minutos, vale la pena invertir tiempo en el prompt:
- **Ser específico sobre el scope:** "Investiga X en el contexto de Y durante el período Z"
- **Especificar el formato de salida:** "Produce un informe de ejecutivo de 2 páginas con bullet points de acción"
- **Indicar las fuentes preferidas:** "Prioriza fuentes académicas y de industria reconocida"
- **Definir la audiencia:** "El informe es para C-suite sin conocimiento técnico"
- **Incluir restricciones:** "Enfócate en los últimos 2 años"

---

## SECCIÓN 4: Putting It All Together

---

### Lección 11: Claude in Action — Use Cases by Role (ID: 383401)
**Duración:** 10 minutos | **Sin video YouTube**

#### Casos de Uso por Rol (con links a Use Case Gallery)

**Uso General Profesional** (todos los roles):
- Generar informes de estado de proyectos
- Analizar patrones en feedback de usuarios
- Empaquetar brand guidelines en un Skill

**Ventas:**
- Construir biblioteca de battle cards (inteligencia competitiva)
- Prepararse para deals de ventas (investigación de prospectos)
- Crear materiales de ventas personalizados

**Marketing:**
- Creación de contenido a escala
- Análisis de campañas
- Investigación de audiencias

**Finanzas:**
- Análisis de varianza
- Preparación de reportes financieros
- Modelado de escenarios

**RRHH:**
- Screening de candidatos
- Onboarding de empleados
- Políticas y documentación de RRHH

**Legal:**
- Revisión de contratos (redlining)
- Investigación legal
- Generación de documentos legales estándar

**Investigación:**
- Síntesis de literatura científica
- Análisis de datos de investigación
- Redacción de informes de investigación

---

### Lección 12: Other Ways to Work with Claude (ID: 383402)
**Duración:** 10 minutos | **Videos:** s-avRazvmLg, tI1uzSJuSxc, 8ZRTSIRWLu4, IypXvHej9eY

#### Objetivos de Aprendizaje
- Entender cuándo usar productos adicionales de Claude: Claude Code, Claude for Slack, Claude for Excel, Claude for Chrome

#### Como menciona la lección: "Claude es una inteligencia. Claude.ai es solo una forma de trabajar con ella."

---

#### 🖥️ Claude Code
Claude Code es una herramienta de codificación agéntica que trabaja donde tú trabajas:
- Terminal, IDE, browser, o incluso en Slack
- Entiende tu codebase, ejecuta comandos, maneja flujos de trabajo de desarrollo completos
- Trabaja a través de lenguaje natural

**Cuándo usar Claude Code:**
- Necesitas ayuda con tareas de programación complejas
- Quieres que Claude trabaje directamente en tu codebase
- Necesitas automatizar flujos de trabajo de desarrollo
- Quieres delegar tareas de código desde tu terminal

**Video: Claude Code on the web (s-avRazvmLg)**
Descripción: "Today, we're introducing Claude Code on the web, a new way to delegate coding tasks directly from your browser. Now in research preview, you can assign multi-step coding tasks..."

---

#### 💬 Claude for Slack (tI1uzSJuSxc)
Trae las capacidades de IA de Claude directamente a tu workspace de Slack.

**Cómo usar Claude en Slack:**
- Mensajes directos con Claude
- Panel asistente de IA
- Mencionando a @Claude en canales

**Cuándo usar Claude for Slack:**
- Quieres consolidar conversaciones relevantes y documentos compartidos de tu workspace
- Estás onboardeando a un nuevo equipo y quieres entender proyectos en curso revisando el historial de canales
- Quieres delegar tareas de código directamente desde un reporte de bug o discusión de feature — solo menciona @Claude y puede iniciar una sesión de Claude Code usando el contexto circundante
- Necesitas respuestas rápidas sobre tendencias de la industria, conceptos técnicos o información de la empresa durante una conversación

**Descripción del video:** "Bring Claude's AI capabilities directly into your Slack workspace. Use Claude in Slack through direct messages, the AI assistant panel, or by mentioning Claude in channels..."

---

#### 📊 Claude for Excel (8ZRTSIRWLu4)
Claude for Excel trae a Claude directamente dentro de Microsoft Excel a través de un sidebar, permitiendo analizar, entender y modificar hojas de cálculo a través de conversación.

**Cuándo usar Claude for Excel:**
- Trabajas con un workbook complejo multi-tab y quieres entender cómo fluyen las fórmulas o cálculos entre hojas
- Necesitas actualizar supuestos o entradas en todo tu modelo preservando las dependencias y relaciones de fórmulas
- Estás depurando errores de hojas de cálculo como #REF!, #VALUE!, o referencias circulares
- Necesitas construir modelos financieros complejos

**Video: Claude in Excel: Sample Use Case (8ZRTSIRWLu4)**
Descripción: "See how the Claude in Excel add-in transforms spreadsheet workflows. This tutorial demonstrates how to use Claude to build a complete HR headcount planning model..."

---

#### 🌐 Claude for Chrome (IypXvHej9eY)
La extensión de Chrome que permite a Claude hacer clic en botones, rellenar formularios y navegar la web junto a ti.

**Powered by:** Claude Sonnet 4.5

**Cuándo usar Claude for Chrome:**
- Quieres asistencia de IA mientras navegas la web
- Necesitas que Claude complete acciones en páginas web (formularios, clicks, navegación)
- Quieres contexto de IA sin cambiar de aplicación

**Descripción del video:** "Powered by Sonnet 4.5, the browser extension allows Claude to click buttons, fill out forms, and navigate the web alongside you."

---

## SECCIÓN 5: Conclusion & Certificate

---

### Lección 13: What's Next? (ID: 385338)
**Duración:** 5 minutos | **Sin video YouTube**

#### Resumen del Curso — Lo que Aprendiste

**Getting started with Claude:**
- Claude es un asistente de IA construido para ser útil, inofensivo y honesto — más que un chatbot, es un socio de pensamiento para trabajo complejo
- Puedes acceder a Claude a través de apps web, desktop y móvil, con tus conversaciones sincronizadas entre dispositivos
- Los prompts efectivos configuran el escenario (contexto), definen la tarea (acción) y especifican reglas (formato y estilo)

**Getting better results:**
- La iteración es clave — trata las primeras respuestas como puntos de partida y refina a través de la conversación
- Los desafíos comunes como respuestas genéricas o tono incorrecto se pueden arreglar con contexto más específico

**Organizing your work:**
- Los proyectos organizan el trabajo a largo plazo con contexto persistente e instrucciones personalizadas
- Los artifacts son outputs autónomos renderizados en una ventana separada para facilitar el uso y reutilización
- Los Skills son paquetes de expertise que pueden cargar capacidades especializadas

**Expanding Claude's reach:**
- Los conectores vinculan a Claude a tus herramientas (Google Workspace, Slack, Notion y muchos más)
- Enterprise Search proporciona un proyecto dedicado para buscar en las fuentes de conocimiento de tu organización
- Research mode conduce investigaciones sistemáticas de múltiples fuentes que tomarían horas manualmente

**Putting it all together:**
- Claude se aplica en múltiples roles: ventas, marketing, finanzas, RRHH, legal, investigación y más
- Más allá de claude.ai, puedes trabajar con Claude a través de Claude Code, Slack, Excel y Chrome

#### Recursos Adicionales

**Aprender más sobre IA y Claude:**
- AI Fluency courses — Cursos gratuitos sobre colaboración efectiva con IA
- AI Capabilities and Limitations — Curso introductorio gratuito sobre qué puede y no puede hacer la IA
- Use Case Gallery — Guías paso a paso y prompts para flujos de trabajo poderosos
- Anthropic Help Center — Documentación detallada y solución de problemas
- Prompting documentation — Guía completa para obtener los mejores resultados

**Recursos específicos del producto:**
- Claude Code documentation
- Claude for Slack guide
- Claude for Excel guide
- Claude for Chrome guide

---

## Resumen Ejecutivo para la Certificación

### Conceptos Clave de Claude 101 Mapeados a Dominios del Examen

| Concepto | Dominio del Examen | Importancia |
|---|---|---|
| Model Context Protocol (MCP) | Tool Design & MCP Integration (18%) | Alta |
| Projects + RAG automático | Context Management & Reliability (15%) | Alta |
| Prompting (SAR framework, iteración) | Prompt Engineering & Structured Output (20%) | Alta |
| Claude Code / Cowork | Claude Code Configuration & Workflows (20%) | Alta |
| Skills (Anthropic + Custom) | Tool Design & MCP Integration (18%) | Media |
| Artifacts (tipos y cuándo se crean) | Prompt Engineering & Structured Output (20%) | Media |
| Enterprise Search | Agentic Architecture & Orchestration (27%) | Media |
| Research Mode (agéntico) | Agentic Architecture & Orchestration (27%) | Alta |
| Extended thinking | Prompt Engineering & Structured Output (20%) | Media |
| Conectores (Slack, M365, etc.) | Tool Design & MCP Integration (18%) | Alta |

### Conceptos Críticos a Memorizar

1. **MCP = "USB-C para IA"** — Estándar abierto y universal para conectar Claude a herramientas
2. **Ventana de contexto:** 200K tokens estándar, hasta 1M tokens en Opus 4.6 Pro/Max/Team/Enterprise
3. **RAG en Proyectos:** Automático cuando el conocimiento se acerca al límite, expande capacidad 10x
4. **Research Mode:** 5-45 minutos, búsquedas iterativas + extended thinking automático + citations
5. **Tipos de artifacts:** Documents, Code, HTML/React, SVG/Mermaid, datos estructurados
6. **Umbral para crear artifact:** +15 líneas, contenido autónomo, reutilizable
7. **Cowork vs Code:** Mismo motor (Claude Code), Cowork = tareas no-código, Code = desarrollo de software
8. **Skills:** Carpetas de instrucciones + scripts + recursos; Anthropic Skills (docs) + Custom Skills (workflows)
9. **Modelos:** Opus 4.6 (más potente/codificación), Sonnet 4.6 (equilibrado), Haiku (rápido/ligero)
10. **Claude for Chrome:** Claude Sonnet 4.5, puede hacer clicks, rellenar formularios, navegar la web

### Framework de Prompting SAR
```
Stage  → Contexto, rol, objetivos, audiencia
Action → Tarea específica que Claude debe realizar
Rules  → Formato, tono, longitud, restricciones, ejemplos
```

---

*Archivo generado: Abril 2026 | Fuente: Anthropic Academy — Claude 101*
