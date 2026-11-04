# Taxonomía multicapas y evidencia para Humanizar

Usar este archivo como investigación de respaldo. Aplicar SKILL.md y SALIDA_LIMPIA.md al producir texto encargado o comentarios de chat. Las descripciones históricas de recursos lingüísticos no autorizan su uso contra esas instrucciones.


Consulta: 26 de octubre de 2026. Objetivo: orientar edición académica y profesional en español sin inventar contenido. Este recurso no implementa detección ni atribución de autoría.

## Contenido

1. Distinciones y niveles de evidencia
2. Investigación contrastada
3. Taxonomía operativa
4. Estadística y procedencia
5. Transferencia al español
6. Decisiones de incorporación y límites
7. Ampliación de evidencia y controles

## 1. Distinciones y niveles de evidencia

Separar tres preguntas: ¿el texto necesita una corrección?, ¿fue generado con IA?, ¿qué modelo lo generó? La respuesta a la primera puede justificarse por el propio texto. Las otras exigen procedimientos y evidencia adicionales y quedan fuera de la función de esta skill.

Clasificar el respaldo de cada pauta:

- **E — Empírico acotado:** estudio con corpus y condiciones identificables. Indicar idioma, género, modelos y límites antes de generalizar.
- **C — Comunitario:** observaciones editoriales de una plataforma; sirven para formular preguntas, no como estándar científico.
- **O — Operativo:** decisión editorial de esta skill, justificada por claridad, coherencia o fidelidad; no presentarla como resultado experimental.
- **P — Pendiente:** afirmación sin comprobación suficiente. No convertirla en regla ni completar sus datos de memoria.

Estas etiquetas son una clasificación interna de respaldo, no una escala de probabilidad de IA. No sumar indicios para producir porcentajes.

## 2. Investigación contrastada

### E1. Diferencias lingüísticas de corpus

Muñoz-Ortiz, Gómez-Rodríguez y Vilares (2024), *Contrasting Linguistic Patterns in Human and LLM-Generated News Text*. El estudio compara noticias en inglés con salidas de seis LLM y analiza dimensiones morfológicas, sintácticas, psicométricas y sociolingüísticas. Encuentra diferencias de vocabulario, distribución de longitudes de oración y estructura sintáctica. El resultado describe ese corpus; no prescribe cómo debe redactarse una tesis en español. **Decisión O:** revisar reiteración y complejidad por su efecto comunicativo, sin introducir emociones, toxicidad o variabilidad artificial para imitar un grupo.

Fuente: https://doi.org/10.1007/s10462-024-10903-2 . Consultados resumen y alcance en la publicación.

### E2. Atribución entre modelos

Sun et al. (2025), *Idiosyncrasies in Large Language Models*, publicado en ICML; arXiv v2 del 16 de junio de 2025. Reporta 97,1 % de exactitud en validación para una clasificación de cinco modelos. Estudia distribuciones de palabras, formato y contenido. Distinguir modelos en ese experimento no equivale a distinguir humano/IA en cualquier texto. **Decisión O:** no etiquetar pasajes como «ChatGPT», «Claude» o «Gemini» por una palabra, un guion o una intuición. No importar preferencias históricas como reglas permanentes.

Fuentes: https://arxiv.org/abs/2502.12150v2 y https://arxiv.org/html/2502.12150v2 . Consultados resumen y estructura metodológica.

### E3. Cambio de dominio y versión

Ko et al. (2026), *Who's Behind the Text? Robust Model Authorship Attribution*. Prepublicación arXiv v1, 14 de octubre de 2026; no atribuirle revisión por pares a partir de esa ficha. Propone ATLAS y MAABench para evaluar atribución bajo cambios de dominio y versión. Reporta 74,27 % de exactitud en el escenario de cambio conjunto. **Decisión O:** una firma de versión no autoriza un diagnóstico universal ni una regla de reescritura. Esta skill no ejecuta ATLAS ni reproduce ese benchmark.

Fuentes: https://arxiv.org/abs/2610.19583v1 y https://arxiv.org/html/2610.19583v1 . Consultados resumen y definición del problema.

### E4. Estilometría en ensayos

Chen et al. (2026), *Stylometric detection of AI-generated texts: evidence from human and machine-written essays*, publicado el 23 de junio de 2026. Compara 2.173 ensayos de Aeon y 2.173 generados con GPT-4o mini: 4.346 textos, 110 áreas. Emplea palabras funcionales y clasificadores estilométricos. La generación usa un procedimiento uniforme; el artículo reconoce límites de género, instrucciones, idioma y autoría híbrida no evaluada. **Decisión O:** la variación entre escritores merece atención, pero el estudio no valida listas españolas de expresiones prohibidas ni la atribución de tesis mixtas.

Fuente: https://doi.org/10.1093/llc/fqag064 . Consultados resumen, sección 3 y sección 6. No reproducir como resultado de Humanizar la exactitud de estos clasificadores.

### E5. Robustez: resultados condicionados, no absolutos

Dugan et al. (2024), RAID, evalúa detectores frente a variaciones de generación y ataques; documenta vulnerabilidades fuera de las condiciones habituales. Fuente: https://aclanthology.org/2024.acl-long.674/ .

Dugan et al. (2025), GenAI Content Detection Task 3, informa resultados superiores al 99 % sobre texto generado con 5 % de falsos positivos en una tarea con dominios y modelos vistos durante entrenamiento. Fuente: https://aclanthology.org/2025.genaidetect-1.45/ .

Consultados los resúmenes de ambas publicaciones. **Decisión O:** evitar tanto «los detectores siempre funcionan» como «ningún detector funciona». Son evaluaciones con condiciones distintas. Ninguna permite garantizar el resultado de un documento particular en Turnitin.

Sadasivan et al., *Can AI-Generated Text be Reliably Detected?*, versión arXiv v4 de 2025, publicado en TMLR, estudia vulnerabilidades ante paráfrasis y condiciones de detección. Fuente: https://arxiv.org/abs/2303.11156v4 . Consultado resumen. **Decisión O:** reconocer límites de robustez sin transformar la investigación en instrucciones de evasión ni suponer que cualquier detector actual usa el mismo método.

### E6. Idioma y sesgo

Liang et al. (2023), *GPT detectors are biased against non-native English writers*, documenta errores sobre escritores no nativos de inglés en los detectores estudiados. Fuente: https://arxiv.org/abs/2304.02819v3 . Consultado resumen. No generalizar sus magnitudes a español, a todos los grupos ni a herramientas actuales.

Macko et al. (2023), MULTITuDE, incorpora 11 idiomas, incluido español, y evalúa generalización a idiomas y LLM no vistos. Fuente: https://aclanthology.org/2023.emnlp-main.616/ . Consultado resumen. **Decisión O:** el idioma es una condición de evaluación; traducir una lista inglesa no la valida para español académico peruano.

### C1. Wikipedia

*Wikipedia:Signs of AI writing* es una guía comunitaria de observaciones, con rasgos de contenido, lenguaje, estilo, comunicación al usuario, referencias y edición de la plataforma. Incluye precauciones e indicadores ineficaces. Es útil para revisar solemnidad vacía, atribuciones vagas, análisis superficiales y residuos conversacionales; la pertinencia debe justificarse en cada texto. No constituye una taxonomía científica universal ni una prueba de autoría.

Versión consultada: https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1382015304 , última edición indicada: 26 de octubre de 2026, 01:40 UTC. Consultados estructura, advertencias y apartados de limitaciones. El archivo MAPA_DE_89_INDICIOS.md conserva una síntesis interna histórica, no 89 encabezados oficiales ni un cotejo exhaustivo de esta revisión.

### Documentación oficial de Turnitin

La guía oficial distingue el indicador de IA del de similitud, admite errores y desaconseja usarlo como única base para acciones adversas. En la versión consultada, la detección específica de paráfrasis y bypass corresponde al detector inglés, no al español ni al japonés. **Decisión O:** no confundir similitud con autoría ni atribuir iguales funciones a todos los idiomas.

Fuente: https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report . Consultada guía de interpretación y limitaciones.

Las notas de versiones registran actualización española el 5 de mayo de 2026 e inglesa el 14 de octubre de 2026; indican que no recalculan retrospectivamente los informes existentes. Fuente: https://guides.turnitin.com/hc/en-us/articles/28294949544717-AI-writing-detection-model . **Decisión O:** fechar cualquier descripción del producto y volver a consultar la documentación cuando una decisión dependa de su comportamiento actual. No deducir pesos, umbrales léxicos ni algoritmo completo a partir de estas notas.

## 3. Taxonomía operativa (O)

Esta tabla traduce preguntas editoriales en acciones; no es un detector derivado de los estudios.

| Capa | Qué observar | Cuándo intervenir | Qué conservar o comprobar |
|---|---|---|---|
| Léxica y semántica | Comodines, elogios, sinónimos que desplazan el concepto | La frase oculta el objeto o promete más de lo demostrado | Términos disciplinares, unidades y sentido técnico de «significativo» |
| Morfosintáctica | Nominalizaciones, pasivas encadenadas, referentes ambiguos, subordinación difícil | Cuesta identificar agente, acción o relación | Pasiva e impersonal válidas; no imponer primera persona |
| Discursiva | Conectores sin relación, estructura repetida, conclusiones rituales | La organización repite o falsea el razonamiento | Comparaciones documentadas y enumeraciones factuales completas; aplicar las reglas de expresión de SKILL.md |
| Argumentativa | Consenso sin fuentes, salto causal, citas aditivas, explicación sin dato | La conclusión excede premisas o evidencia | Grado de certeza y alcance; pedir el respaldo ausente |
| Voz y consistencia | Cambio terminológico, registro desigual, pérdida de voz | Hay incoherencia que afecta comprensión | Coautoría, traducción y secciones con funciones distintas pueden explicarlo |
| Residuos de herramienta | Interlocución del asistente, placeholders, códigos de cita | Son ajenos al género del documento final | Citas textuales, ejemplos analizados, código e identificadores legítimos |
| Procedencia y verificación | Fuente no aportada, enlace roto, metadatos discordantes | Debe comprobarse una atribución factual | No localizado no significa fabricado; conservar versiones y registrar las dudas internamente; comunicarlas en el chat cuando corresponda |
| Descripción cuantitativa | Longitud, reiteración o distribución de rasgos | Ayuda a localizar un problema que puede explicarse | No fijar porcentajes óptimos ni inferir autoría |

Para cada intervención: identificar fragmento, problema concreto, evidencia disponible, cambio mínimo y comprobación de significado. Si no existe un problema comunicativo o factual, conservar el texto aunque aparezca un patrón del inventario.

## 4. Estadística y procedencia

**Perplejidad:** depende del modelo que asigna probabilidades, tokenización y contexto. No es una propiedad universal del autor. No inventar una medición si no se ha ejecutado y documentado un procedimiento.

**Burstiness:** la palabra se usa con distintos significados; si se solicita una medición, definir antes qué distribución y fórmula se medirán. No equiparar automáticamente dispersión de longitud de oraciones, diversidad léxica y variación de probabilidad.

**Decisión O:** no añadir errores, oraciones inconexas o sinónimos extraños para incrementar esas magnitudes. Las métricas descriptivas pueden orientar lectura; no verifican hechos ni sustituyen el argumento. Humanizar no requiere calcularlas para editar.

**Marcas de agua:** Kirchenbauer et al., *A Watermark for Large Language Models*, presenta inserción de señales durante generación y detección estadística bajo su esquema. Fuente: https://arxiv.org/abs/2301.10226v4 . Consultado resumen. No confundir una marca diseñada con un signo de puntuación recurrente ni suponer que cualquier texto contiene una. La ausencia de detección no acredita autoría humana. La skill no incluye verificación criptográfica ni detección de marcas.

**Trazabilidad O:** conservar original y revisión; respetar declaraciones de uso de IA y registros aportados. Un historial o metadato documenta determinados actos o versiones, no necesariamente todo el proceso de autoría. No afirmar procedencia demostrada sin comprobar qué evidencia cubre realmente.

## 5. Transferencia al español

- Revisar claridad en el español del documento, sin imponer anglicismos ni traducciones literales de listas inglesas.
- Mantener terminología de la disciplina y voz institucional sin folclorizar el contexto peruano.
- No usar extensión, complejidad o corrección gramatical como diagnóstico de origen.
- Comparar muestras del autor solo cuando estén disponibles y sean pertinentes al género; sin ellas, conservar la voz visible.
- Respetar segmentos técnicos, citas, coautoría y traducción. La discontinuidad estilística exige comprensión contextual antes que homogeneización.
- No inventar rasgos constantes de ChatGPT, Claude o Gemini actuales a partir de versiones estudiadas anteriormente.

Estas son decisiones editoriales prudentes, no una validación experimental de Humanizar en población peruana.

## 6. Incorporación y límites

Aportes frente a v1.0: separar E/C/O/P; desarrollar lectura multicapas; documentar límites por idioma, dominio y versión; diferenciar ausencia de fuente de falsedad; exigir respaldo para proposiciones añadidas; precisar límites de detectores sin negar resultados favorables; proteger voz y citas; declarar que cero coincidencias heurísticas no acredita calidad.

No se recuperó el informe completo del chat anterior: se dispuso de un resumen de continuidad, los archivos actuales de la skill y, en la ampliación a v1.2, el material y alcance retrospectivo pegados por el usuario. Por ello se reconsultaron las líneas principales de investigación identificables, sin afirmar reproducción exhaustiva de cada búsqueda previa. Tampoco se ejecutaron experimentos de atribución, consultas a Turnitin ni estudios de eficacia en usuarios. Los resúmenes y secciones indicados delimitan la profundidad de consulta; no declarar lectura íntegra de todos los artículos.

Las fuentes anteriores sustentan límites y decisiones de diseño; no prueban que esta skill mejore por sí misma las tesis. Validar su comportamiento con casos de fidelidad, inferencia y voz, sin presentar esas pruebas como validación científica.

## 7. Ampliación de evidencia y controles (v1.2, 2026-10-26)

### E7. Reescritura y normalización de voz

Van Nuenen (2026), *Voice Under Revision: Large Language Models and the Normalization of Personal Narrative*, prepublicación arXiv v1 del 24 de abril de 2026. Reporta 300 narraciones y comparación de GPT-5.4, Claude Sonnet 4.6 y Gemini 3.1 Pro bajo tres instrucciones de revisión. En ese corpus inglés, la reescritura desplaza rasgos de voz hacia un registro más uniforme; pedir conservar la voz atenúa cambios sin eliminarlos. No mide directamente la percepción humana de naturalidad ni demuestra generalización a tesis en español.

Fuente: https://arxiv.org/abs/2604.22142v1 y https://arxiv.org/html/2604.22142v1 . Consultados resumen, modelos y limitaciones. Los nombres y condiciones son los reportados por el autor; no constituyen una certificación independiente de versiones ni de sus capacidades actuales. **Decisión O:** cambiar solo lo necesario, conservar voz y no interpretar mayor elaboración léxica como mejora automática.

### E8. Evidencia multilingüe reciente

Gargova et al. (2026), *A Multilingual Linguistic Analysis of Human vs LLM-Generated News in a Disinformation Context*, compara GPT-5, Gemini 2.5 y Grok 4 en noticias inglesas, españolas y búlgaras. Analiza semejanza semántica, consistencia factual, legibilidad, riqueza léxica y persuasión, y reporta regularidades estilísticas. Fuente: https://aclanthology.org/2026.indor-1.9/ . Consultado resumen. **Límite:** incluye español, pero no Claude ni un corpus de tesis peruanas; no convertir la exactitud reportada en rendimiento de Humanizar o Turnitin.

### E9. Clasificación de familias

Bitton, Bitton y Nisan (2025), *Detecting Stylistic Fingerprints of Large Language Models*, arXiv v1. Propone un conjunto de tres clasificadores para familias Claude, Gemini, Llama y OpenAI con una decisión basada en unanimidad. Fuente: https://arxiv.org/abs/2503.01659v1 . Consultado resumen. **Decisión O:** las firmas distribucionales requieren un procedimiento de clasificación evaluado; no equivalen a seis signos visibles ni justifican atribuir un modelo a simple vista. No se ejecutó ni reprodujo ese sistema.

### Comparación de modelos: qué puede afirmarse

| Evidencia | Versiones o alcance reportado | Uso permitido en Humanizar | Inferencia excluida |
|---|---|---|---|
| Sun et al., 2025 | Incluye GPT-4o, Claude 3.5 Sonnet y Gemini 1.5 Pro; modelos API y corpus de instrucciones | Reconocer diferencias de distribución y formato bajo condiciones identificadas | Atribuir una tesis actual a una marca por un conector o extrapolar versiones |
| Van Nuenen, 2026 | Reporta GPT-5.4, Claude Sonnet 4.6 y Gemini 3.1 Pro; revisión de narraciones inglesas | Prevenir sobreedición y pérdida de voz | Declarar un modelo universalmente «más humano» o diagnosticar textos españoles |
| Gargova et al., 2026 | GPT-5 y Gemini 2.5, entre otros; noticias en tres idiomas | Recordar dependencia de género, tarea e idioma | Presentarlo como comparación de las tres familias en tesis |
| Ko et al., 2026 | Atribución con cambio de dominio y versión | Fechar y delimitar cualquier firma | Prometer una taxonomía invariable o verificación completa de modelos actuales |

La consulta a fecha actual no significa que exista una comparación validada de todas las últimas versiones comerciales en todos los idiomas. No completar esa ausencia con estereotipos sobre ChatGPT, Claude o Gemini.

### Detectores: familias metodológicas y límite de atribución

Separar estilometría léxica/sintáctica, clasificadores entrenados, métodos de probabilidad del texto y marcas incorporadas durante generación. Las fuentes E2–E6 y el estudio de marcas de agua muestran enfoques distintos; esta clasificación es una síntesis de diseño, no el inventario interno de Turnitin. No afirmar que Turnitin suma rayas, tríadas o palabras de una lista.

En su ayuda oficial actual, GPTZero indica que desde otoño de 2023 migró de perplejidad y burstiness a una arquitectura de aprendizaje profundo. Fuente: https://support.gptzero.me/articles/9585228410-how-do-i-interpret-burstiness-or-perplexity . Consultada la nota de actualización; las explicaciones y umbrales históricos que siguen en esa misma página no deben presentarse como regla vigente. **Decisión O:** no atribuir a todos los detectores una fórmula común ni trasladar datos de un proveedor a otro.

La FAQ técnica enlazada desde la guía de Turnitin no pudo consultarse (fallo de acceso y respuesta 403 en la ruta ensayada). Se encontraron afirmaciones sobre sus métricas en sitios comerciales, pero no se incorporaron como hechos técnicos verificados. La guía oficial de interpretación y las notas de versiones sí pudieron leerse. **Estado P:** características y pesos internos de Turnitin; no inventar un léxico penalizado, una fórmula o umbrales de perplejidad/burstiness.

### Correcciones al material del usuario

No aceptar «marcas inconfundibles de autoría humana» ni equiparar el habla cotidiana con toda voz académica válida. El ejemplo de Pérez, correlación y entrevistas no acredita hechos por ser específico. Las decisiones metodológicas, anomalías y limitaciones se describen si existen; no se fabrican para humanizar. Las seis señales se operacionalizan en REDACCION_Y_SEIS_SENALES.md con excepciones y controles de fidelidad.
