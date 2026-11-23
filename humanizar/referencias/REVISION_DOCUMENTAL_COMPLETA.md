# Revisión documental completa

Leer antes de auditar o humanizar un documento. Aplicar SALIDA_LIMPIA.md y las reglas de expresión de SKILL.md.

## 1. Confirmar instrucciones y archivo de trabajo

Leer la habilidad seleccionada en el entorno del encargo. Cuando se indique una ruta local concreta, comprobar su contenido y versión en ese entorno. Las instalaciones de equipos distintos pueden tener versiones diferentes. Resolver cualquier solicitud de acceso o de archivo en el chat.

Identificar el documento de entrada y la ruta de salida. Trabajar sobre una copia y mantener el original. Si hay una guía de formato separada, conservar la presentación solicitada durante la reescritura.

## 2. Inventariar antes de decidir

Para Word, ejecutar:

```bash
python scripts/auditar_estilo.py entrada.docx --json --inventario
```

Examinar todos los bloques extraídos. El inventario incluye el texto del cuerpo, las celdas de las tablas y los cuadros de texto. También localiza encabezados, pies y notas presentes en las partes admitidas del DOCX. Identificar por separado comentarios de revisión y cambios controlados. Comprobar las imágenes visualmente cuando contengan material necesario para la edición. Usar OCR si se requiere localizar texto rasterizado y confirmar su lectura visualmente.

El inventario registra extracción. Cada bloque empieza con `revision_editorial: sin_registrar`. Completar internamente su decisión después de leerlo. Evitar presentar el recuento de bloques como prueba de revisión realizada.

Para otros formatos, usar una extracción que conserve las ubicaciones y comprobar su cobertura. El script no lee PDF, imágenes ni objetos incrustados. Identificar esos componentes en el registro interno y resolver su lectura con la herramienta adecuada.

## 3. Decidir sobre cada bloque

Mantener un registro de trabajo con identificador, sección, texto original, decisión y redacción final. Usar decisiones concretas: `conservado_tras_lectura`, `reformulado`, `comentario_editorial_retirado` o `consulta_en_chat_con_dato_preservado`. Evitar marcar bloques como revisados por el simple hecho de extraerlos o buscar palabras.

Distinguir el dato del modo de expresarlo. Conservar una fecha o un resultado aportado; reconstruir la oración que lo presenta si incumple el estilo. La instrucción «mantener el original» se refiere al contenido factual mientras falte una corrección confirmada. Retirar aclaraciones del editor aunque estén dentro del original.

Ante «audita y aplica», revisar toda la expresión del documento. La autorización comprende reformular párrafos y celdas. Evitar limitar la tarea a corregir sumas o conciliaciones cronológicas.

Clasificar las frases por su función. Un resultado como «prueba no ejecutada» comunica un estado técnico. Una frase como «no acredita por sí solo la aceptación» comenta la suficiencia de una evidencia. Llevar esa evaluación al chat cuando se edite un informe descriptivo. En un informe de auditoría expresamente encargado, desarrollar los hallazgos que constituyan su tema.

Completar además un registro por negación conforme a NEGACIONES_Y_PARAFRASIS.md. Mantener el dato y evaluar la paráfrasis de su oración. Evitar conservar la construcción solo por tratarse de un estado técnico.

### Revisar por propósito, incluso sin coincidencias en el auditor

Determinar qué tarea cumple el apartado y qué información necesita su lector. Leer la figura con su título, nota y párrafo de presentación. Leer las celdas con los encabezados y el resto de la fila. Buscar en el cuerpo y los anexos si la misma información aparece en varios lugares. Evaluar cada frase con esta pregunta: «¿Qué información necesaria se perdería si la quito?». Aplicar el criterio a todo el informe, aunque el auditor devuelva cero coincidencias.

| Caso | Decisión en el informe |
|---|---|
| Detalle visible o repetido por el título, como un encabezado, banner, campos de acceso o aviso de directorio vacío | Resumir el estado que documenta una nota existente en una frase directa. Conservar la fuente y el código de actividad si aportan trazabilidad. Evitar dejar solo el código cuando la nota contiene una descripción factual. |
| Comportamiento de interfaz requerido por el encargo | Describir el hecho con lenguaje directo. Si se documenta una condición de búsqueda, conservar «El buscador pide al menos dos caracteres». Un aviso visible en la interfaz no permite inferir el estado de la base de datos. |
| Imagen reutilizada, rótulos distintos u otra diferencia visible | Describir únicamente lo que el apartado necesita. Consultar en el chat si la diferencia exige una decisión. Evitar convertirla en una incidencia o una tarea pendiente. |
| Salvedad sobre lo que acredita una captura, un vídeo, una planilla o un repositorio | En un informe descriptivo identificar el material pertinente y quitar la salvedad. Una evaluación de evidencia forma parte del informe cuando se encargó expresamente. |
| Consulta sobre fechas, recuentos, actas, guardado o permisos de acceso | Tramitar la consulta en el chat. Conservar el dato aportado en su registro mientras falte una corrección confirmada. Suprimir etiquetas del revisor y recapitulaciones. Si un campo admite quedar vacío y el dato falta, dejarlo vacío. Respetar los códigos de datos faltantes exigidos por el formato. |
| Tarea del revisor, como «capturas por seleccionar» o «acceso pendiente de confirmar» | Retirar el recordatorio del entregable. Mantener un estado pendiente únicamente cuando esté documentado como parte del proyecto. |
| Estado real de una prueba, un manual o una validación | Conservar el estado y su alcance. Un build sin ejecutar, un manual excluido del paquete y un acta que el revisor no localizó describen situaciones distintas. La última queda como consulta si corresponde. |
| Atribución genérica, como «según la fuente» o «el borrador señala» | Conservar o precisar la atribución cuando sostenga el dato o delimite su certeza. Retirar las fórmulas repetitivas que solo narren el trabajo editorial. |
| Oposición innecesaria, calificativos vagos, conectores formales o nominalizaciones como «mensaje de ausencia de registros» | Quitar la frase si es accesoria. Cuando el dato sea necesario, reconstruir la frase con lenguaje directo desde las ideas clave. Preservar las relaciones y las negaciones técnicas que determinan el significado. |

Asignar un lugar principal a cada dato y mantener las remisiones que ayuden a navegar el documento. Eliminar repeticiones en otros bloques cuando carezcan de función propia. En el registro interno indicar qué se retiró, qué dato se conservó y qué decisión corresponde consultar. Mantener ese registro fuera del entregable.

## 4. Reformular el contenido

Escribir directamente desde la voz del autor. Eliminar moldes de oposición y amplificaciones prefabricadas. Dar a las ideas su extensión necesaria. Retirar tríadas ornamentales y generalidades vacías.

Evitar sustituir una advertencia por otra redacción que conserve su función editorial. Retirar también las notas que recapitulan incidencias de auditoría con lenguaje aparentemente descriptivo. Conservar datos en sus registros de origen; evitar reconstruir una nota para proteger cada repetición numérica. Ejemplo recibido: «Las imágenes ilustran interfaces; no prueban por sí solas funcionamiento integral ni aceptación». Redacción para una relación de evidencias: «Vistas públicas, móviles y administrativas de los anexos 6–13». Tratar la aceptación en el chat si necesita una decisión.

Conservar el significado de los estados técnicos aportados aplicando NEGACIONES_Y_PARAFRASIS.md. En «El build no se ejecutó», puede expresarse «El build quedó sin ejecutar». Usar «pendiente de ejecución» cuando ese estado esté documentado. Para un acta no localizada, consultar su estado en el chat; evitar convertir la falta de localización en la afirmación de que no existe o no fue firmada.

## 5. Guardar y volver a comprobar

Abrir el archivo de salida guardado. Ejecutar sobre él el mismo inventario y auditor. Cotejar el texto extraído con las decisiones del registro interno. Resolver cada coincidencia contextual; evitar usar cero coincidencias como objetivo o certificado. Revisar las apariciones RN-41 y justificar internamente cada negación conservada en la salida.

Revisar de nuevo las celdas modificadas y los anexos. Cotejar en conjunto el texto que presenta cada figura, su título y su nota. Retirar observaciones editoriales duplicadas o reformuladas como comparaciones visuales. Aplicar el caso del Anexo 8 de SALIDA_LIMPIA.md. Buscar también equivalentes de las aclaraciones retiradas, aunque usen palabras distintas. Comprobar la fidelidad de fechas y cifras. Verificar que los enlaces y las imágenes se mantengan cuando se haya pedido conservarlos. Renderizar el documento y comprobar su presentación mediante la herramienta del formato.

## 6. Criterio de cierre

Concluir la revisión cuando cada bloque incluido en el alcance tenga una decisión editorial y el archivo de salida refleje esas decisiones. Tratar cualquier componente inaccesible en el chat. Evitar la afirmación «revisión completa» si el registro contiene bloques sin examinar.

Entregar el texto final limpio. Comunicar los hallazgos solicitados en la conversación. Un número de intervenciones describe cambios realizados; la cobertura se acredita con el recorrido documentado de los bloques.
