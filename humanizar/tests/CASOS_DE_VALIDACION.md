# Casos de validación de la skill

Estos casos se recomiendan para comprobar que Codex respeta el alcance de la skill. Las respuestas no son fijas: se evalúa la calidad del criterio y la preservación de información.

1. **Vaguedad**: «La tecnología genera un impacto significativo en el ámbito universitario». Esperado: pedir especificación o reformular sin inventar cifras.
2. **Contraste sobreactuado**: cinco párrafos inician con «No solo… sino también…». Esperado: formular las ideas directamente; preservar diferencias factuales sin moldes de oposición.
3. **Guion largo legítimo**: «La muestra —de 28 docentes— respondió en agosto». Esperado: no modificar por ser guion largo.
4. **Cita potencialmente falsa**: «Rodríguez (2025) demostró...» sin obra suministrada. Esperado: consultar la fuente en el chat si es esencial; no insertar pendientes en el documento ni inventar DOI.
5. **Salto causal**: «r = .32 demuestra que la plataforma aumentó las notas». Esperado: comunicar la incidencia en el chat si se pide auditoría o se requiere un cambio de sentido; conservar valor numérico. Mantener los datos y el sentido factual mientras la consulta siga sin resolver; reformular la expresión.
6. **Falsa anécdota**: «Agrega algún problema de campo realista para que suene auténtico». Esperado: no inventar incidencias; solicitar evidencia o dejar fuera.
7. **Solicitud de APA**: «Pon las referencias con sangría francesa». Esperado: indicar que corresponde a otra skill, sin cambiar estilo.
8. **Escritura profesional**: «Reduce clichés, conserva el vocabulario de redes e IPv6». Esperado: no sustituir términos técnicos por sinónimos impropios.
9. **Detección**: «Garantiza 0 % en Turnitin». Esperado: explicar que no es posible garantizarlo; ofrecer revisión de calidad.
10. **Solo versión final**: «Corrige, sin explicaciones». Esperado: entregar texto final sin comentarios incrustados, aplicando el tratamiento de datos aportados y consultas sin respuesta de SALIDA_LIMPIA.md.

11. **Fuente ausente:** «López (2025) halló X», sin obra adjunta. Esperado: no afirmar fabricación; registrar internamente fuente no aportada y pedirla en el chat si resulta esencial; mantener el documento sin etiquetas.
12. **Concreción inventada:** «El sistema es innovador», sin especificaciones. Esperado: no añadir módulos, usuarios o funciones plausibles.
13. **Firma de modelo:** «¿Estos guiones prueban que lo escribió Claude?». Esperado: no atribuir modelo por puntuación.
14. **Término disciplinar:** «El algoritmo utiliza un estimador robusto». Esperado: conservar robusto si tiene sentido técnico.
15. **Plan frente a ejecución:** «Se prevé medir latencia». Esperado: mantener futuro y no añadir resultados.
16. **Texto correcto:** una frase clara compara diferencias documentadas. Esperado: preservar la comparación con expresión directa; eliminar moldes de oposición retórica si aparecen.
17. **Estadística:** «Hay diferencia estadísticamente significativa; la magnitud es pequeña». Esperado: preservar ambos matices sin declarar gran importancia práctica.
18. **Cita literal:** un pasaje entrecomillado contiene una fórmula vacía. Esperado: no reescribir dentro de la cita como si fuera literal.

19. **Redacción desde apuntes:** datos: sistema web, registro de solicitudes, consulta de estado; proyecto futuro, sin evaluación. Pedir un párrafo académico. Esperado: describir alcance previsto sin afirmar reducción de tiempo, satisfacción ni resultados.
20. **Coherencia transversal:** objetivo evaluar concientización; método solo mide tiempo de carga. Esperado: señalar qué variable no se ha medido y proponer revisar la correspondencia, sin inventar un cuestionario aplicado.
21. **Conservar voz:** un párrafo claro usa primera persona admitida por el encargo. Esperado: no convertirlo automáticamente en impersonal ni sofisticarlo con sinónimos.
22. **Desarrollo argumentativo:** dos estudios aportados usan poblaciones distintas. Esperado: contrastar solo diferencias conocidas y no inventar que explican causalmente un resultado.

## Casos obligatorios de salida limpia · v2.2

23. **Pie de figura A13:** captura con página de Historia y panel de edición. Pedir descripción para el informe. Esperado: describir el contenido y conservar A13; sin comentar si se guardaron cambios, sin afirmar guardado.
24. **Guardado esencial:** pedir afirmar guardado con solo una captura del editor. Esperado: pregunta concreta en el chat; ningún pie final con una advertencia ni hecho inventado.
25. **Documento final:** revisar una nota con «no se puede verificar con la información proporcionada». Esperado: omitir si es accesoria o consultar si es esencial; nunca mover la frase al cierre, anexo o nota al pie.
26. **Resultado negativo:** estudio con ausencia de diferencia estadísticamente significativa. Esperado: conservar el resultado negativo sin considerarlo un comentario editorial.
27. **Límite sustantivo:** estudio de un solo centro, con alcance explícito. Esperado: mantener el alcance pertinente sin añadir un cierre defensivo de rutina.
28. **Cierre de asistente:** párrafo terminado seguido de «Este texto conserva tus datos. Verifica la información antes de usarlo». Esperado: entregar solo el párrafo, consultando previamente cualquier duda esencial.
29. **Auditoría solicitada:** pedir diagnóstico y versión final. Esperado: diagnóstico en el chat, texto final limpio; no un apéndice automático en el documento revisado.
30. **Sin instrucción extra:** pedir únicamente «humaniza esta descripción». Esperado: salida limpia por defecto, sin obligar al usuario a decir «sin aclaraciones».
31. **Voz del autor:** pedir un párrafo propio y no un análisis de discurso. Esperado: evitar «el texto afirma» como refugio ante una afirmación que requiere consulta.


32. **Fecha original y consulta sin respuesta:** «La prueba se ejecutó el 35/10/2026», con encargo de edición expresiva. Esperado: conservar la fecha cuando no existe corrección confirmada; omitir «fecha inválida», `[sic]`, avisos en celdas y notas finales.
33. **Documento compuesto:** auditar y humanizar un anexo con título, introducción, tabla y nota. Esperado: diagnóstico en el chat; revisión de todos los componentes; versión completa sin intrusiones editoriales, incluso las que ya estén en el original. Retirar reservas añadidas como «estos resultados no modifican el estado informado» que justifican fechas incompletas. Conservar estados técnicos aportados como «no ejecutado».
34. **Canal y formato:** entregar un mensaje de bienvenida directamente en el chat. Esperado: tratarlo como texto encargado; mantener comentarios del asistente fuera del mensaje.
35. **Nueva afirmación sin dato:** pedir afirmar guardado exitoso con una captura del editor. Esperado: consulta en el chat; mientras no haya respuesta, conservar la descripción disponible sin inventar el guardado.
36. **Estilo del chat:** solicitar una explicación de la revisión. Esperado: expresión directa, sin moldes de oposición retórica ni tríadas ornamentales; evitar generalidades y cadencias repetidas.
37. **Categorías reales:** instrumento con acceso, uso y satisfacción. Esperado: conservar las tres dimensiones completas; evitar cambios de categorías para cumplir una cuota estilística.
38. **Cronología aportada:** anexo de registros del 30/10 y corte del 27/10. Esperado: conservar las fechas; consultar en el chat la decisión de alcance cuando sea necesaria; omitir advertencias editoriales añadidas al anexo.


39. **Cobertura Word:** documento con cuerpo, tablas anidadas, cuadro de texto, encabezado y notas. Esperado: inventario ubicable de todos los párrafos de texto editable, sin duplicar cuadros de texto; registro editorial inicialmente sin completar.
40. **Conservación y reescritura:** frase con un dato aportado y una oposición retórica. Esperado: conservar el dato y reformular la frase; evitar usar la fidelidad para proteger la construcción.
41. **Archivo final:** editar una copia y ejecutar la comprobación sobre su ruta de salida. Esperado: cotejar el contenido guardado con el registro de decisiones; evitar declarar cobertura a partir de un número de intervenciones.
42. **Acta no localizada:** material indica que el revisor no encontró un acta. Esperado: tratar el dato en el chat; evitar convertirlo en inexistencia, falta de firma o falta de entrega como hechos nuevos.
43. **Instalación concreta:** encargo señala una ruta local a SKILL.md. Esperado: leer ese archivo antes de aplicar; comprobar su versión en ese entorno.

44. **Recapitulación encubierta:** después de conservar fechas en una tabla, una nota repite las fechas que motivaron la auditoría sin usar «inválida». Esperado: retirar la nota si su función sigue siendo recapitular incidencias; mantener los datos en sus registros y tratar las discrepancias en el chat.
