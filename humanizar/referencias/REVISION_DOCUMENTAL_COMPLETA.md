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

## 4. Reformular el contenido

Escribir directamente desde la voz del autor. Eliminar moldes de oposición y amplificaciones prefabricadas. Dar a las ideas su extensión necesaria. Retirar tríadas ornamentales y generalidades vacías.

Evitar sustituir una advertencia por otra redacción que conserve su función editorial. Retirar también las notas que recapitulan incidencias de auditoría con lenguaje aparentemente descriptivo. Conservar datos en sus registros de origen; evitar reconstruir una nota para proteger cada repetición numérica. Ejemplo recibido: «Las imágenes ilustran interfaces; no prueban por sí solas funcionamiento integral ni aceptación». Redacción para una relación de evidencias: «Vistas públicas, móviles y administrativas de los anexos 6–13». Tratar la aceptación en el chat si necesita una decisión.

Conservar completos los estados técnicos aportados. En «El build no se ejecutó», puede expresarse «Build pendiente de ejecución». Para un acta no localizada, consultar su estado en el chat; evitar convertir la falta de localización en la afirmación de que no existe o no fue firmada.

## 5. Guardar y volver a comprobar

Abrir el archivo de salida guardado. Ejecutar sobre él el mismo inventario y auditor. Cotejar el texto extraído con las decisiones del registro interno. Resolver cada coincidencia contextual; evitar usar cero coincidencias como objetivo o certificado.

Revisar de nuevo las celdas modificadas y los anexos. Buscar también equivalentes de las aclaraciones retiradas, aunque usen palabras distintas. Comprobar la fidelidad de fechas y cifras. Verificar que los enlaces y las imágenes se mantengan cuando se haya pedido conservarlos. Renderizar el documento y comprobar su presentación mediante la herramienta del formato.

## 6. Criterio de cierre

Concluir la revisión cuando cada bloque incluido en el alcance tenga una decisión editorial y el archivo de salida refleje esas decisiones. Tratar cualquier componente inaccesible en el chat. Evitar la afirmación «revisión completa» si el registro contiene bloques sin examinar.

Entregar el texto final limpio. Comunicar los hallazgos solicitados en la conversación. Un número de intervenciones describe cambios realizados; la cobertura se acredita con el recorrido documentado de los bloques.
