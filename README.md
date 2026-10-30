# Humanizar 2.0

Humanizar ayuda a redactar y revisar textos académicos y profesionales en español con claridad y una voz natural. Conserva los hechos y la intención del autor, y mejora la forma de desarrollar y conectar las ideas.

**Autor y responsable del proyecto:** Jan Stevenson Galarreta Pocito ([JanGP17](https://github.com/JanGP17)).

**Repositorio de origen:** [JanGP17/Skill-Textos-naturales](https://github.com/JanGP17/Skill-Textos-naturales).

## Qué hace

- Redacta desde apuntes y fuentes, manteniendo el contenido dentro de la evidencia disponible.
- Reduce relleno, clichés y expresiones ornamentales; revisa las estructuras repetitivas según su función.
- Fortalece la argumentación y la relación entre problema, objetivos, metodología, resultados y conclusiones.
- Conserva la voz del autor y los términos técnicos que aportan precisión.
- Entrega texto final limpio: las dudas esenciales se resuelven en el chat antes de finalizar el fragmento.

Incluye un inventario de 89 asuntos de revisión, ejemplos y un auditor opcional para archivos de texto. APA 7 se trabaja con una habilidad independiente.

## La regla central de la versión 2.0

El documento final contiene únicamente el texto destinado a su lector. Esta regla comprende los párrafos, las notas, los pies de figura y los anexos. Las observaciones editoriales accesorias se omiten; cuando falta un dato indispensable, la habilidad hace una consulta en el chat. Las limitaciones del estudio y los resultados negativos se mantienen cuando forman parte del contenido.

## Instalar por comando en Codex

Necesitas Node.js 22.20 o posterior y Git. En la terminal de VS Code, PowerShell o tu terminal habitual, ejecuta:

```bash
npx skills add JanGP17/Skill-Textos-naturales --skill humanizar --agent codex --global --copy
```

La instalación global permite usarla en distintos proyectos. Para instalarla solo en el proyecto actual:

```bash
npx skills add JanGP17/Skill-Textos-naturales --skill humanizar --agent codex --copy
```

Puedes consultar las habilidades instaladas y actualizar Humanizar con:

```bash
npx skills list --global
npx skills update humanizar --global
```

Los comandos utilizan el instalador [skills de Vercel Labs](https://github.com/vercel-labs/skills). Sus opciones se documentan en la [referencia de comandos](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

## Instalar desde el ZIP en Windows

1. Descomprime `humanizar-v2.0.zip`.
2. Copia la carpeta completa `humanizar` en `%USERPROFILE%\.agents\skills\`.
3. Comprueba que exista `%USERPROFILE%\.agents\skills\humanizar\SKILL.md`.
4. En Codex, abre `/skills` o escribe `$humanizar` para seleccionarla. Si aún no aparece, abre una nueva sesión.

Para actualizar una instalación manual, guarda una copia de la carpeta anterior y reemplázala por la nueva. Usa un solo método de instalación para mantener una única copia activa.

## Cómo usarla

```text
$humanizar Revisa este apartado de mi tesis. Mejora la claridad y la
argumentación; conserva los datos, las fuentes y los términos técnicos.
Entrega la versión final limpia. Consulta en el chat cualquier dato
esencial que necesites antes de finalizar.
```

También puedes pedir un primer borrador:

```text
$humanizar Redacta una introducción a partir de estos apuntes.
Usa un tono académico natural y desarrolla solo lo que pueda
sostenerse con la información que te comparto.
```

## Archivos incluidos

- `SKILL.md`: instrucciones de la habilidad.
- `referencias/`: reglas de redacción, investigación de respaldo, ejemplos y salida limpia.
- `scripts/auditar_estilo.py`: revisión opcional de expresiones en `.txt` y `.md`.
- `tests/`: pruebas del script y casos para revisar el comportamiento.
- `agents/` y `assets/`: datos de presentación e icono.
- `LICENSE.txt`: condiciones de uso del material propio del proyecto.

El auditor requiere Python 3. Desde la carpeta de la habilidad:

```bash
python scripts/auditar_estilo.py borrador.md
python scripts/auditar_estilo.py borrador.md --json
python -B -m unittest discover -s tests -v
```

Las coincidencias del script orientan la revisión en contexto. La calidad se evalúa por precisión y utilidad, no por el número de coincidencias. Humanizar no mide autoría ni promete resultados en detectores de IA.

## Autoría y permisos

Puedes descargar, instalar y utilizar Humanizar para tus propios trabajos, incluidos los académicos y profesionales. Conserva la autoría, este README y el enlace al repositorio de origen en tu copia de la habilidad.

Para recomendarla, comparte el [enlace al repositorio](https://github.com/JanGP17/Skill-Textos-naturales), donde se mantiene la versión del proyecto. La redistribución de los archivos, la publicación de versiones modificadas y la comercialización de la habilidad requieren autorización previa del responsable a través de ese repositorio.

Estas condiciones se aplican a los archivos propios de Humanizar; no imponen una mención del proyecto en los textos que redactes con ella. Las fuentes y los materiales de terceros conservan sus respectivas condiciones de uso. Consulta [LICENSE.txt](https://github.com/JanGP17/Skill-Textos-naturales/blob/main/humanizar/LICENSE.txt) para los términos completos.

## Fuentes de consulta

Las referencias incluidas distinguen estudios empíricos, observaciones comunitarias y decisiones editoriales. El inventario de 89 asuntos reúne criterios para revisar textos; no es una lista oficial de señales de Turnitin. Las fuentes y sus límites se detallan en [la investigación de respaldo](https://github.com/JanGP17/Skill-Textos-naturales/blob/main/humanizar/referencias/TAXONOMIA_FORENSE_Y_EVIDENCIA.md).
