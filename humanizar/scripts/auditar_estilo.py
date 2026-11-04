#!/usr/bin/env python3
"""Auditor heurístico de muletillas en español, NO detector de IA.

Lee .md/.txt y texto editable de .docx. No reescribe el archivo. Sus hallazgos son
observaciones de superficie que un editor debe confirmar en contexto.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
from zipfile import ZipFile, BadZipFile
from xml.etree import ElementTree as ET

RULES = [
    ("RN-09", "prefacio vacío", "media", r"\b(?:es de vital importancia|es importante (?:mencionar|destacar|señalar)|cabe (?:destacar|resaltar|mencionar))\b", "¿Puede comenzar directamente con la afirmación?"),
    ("RN-10", "léxico grandilocuente", "contextual", r"\b(?:pilar fundamental|panorama dinámico|en el dinámico panorama|papel crucial|experiencia enriquecedora|un análisis exhaustivo|transformación revolucionaria)\b", "Solicitar dato concreto o simplificar; conservar si se justifica."),
    ("RN-11", "conector ritual", "contextual", r"\b(?:en este sentido|en ese sentido|por otra parte|aunado a ello|en conclusión|en definitiva)\b", "Comprobar que la transición tiene función lógica."),
    ("RN-12", "oposición retórica", "alta", r"\b(?:no solo\b.{0,100}?\bsino (?:también|que)|no (?:es|se trata de)\b.{0,100}?\bsino)\b", "Reformular directamente; preservar diferencias factuales y citas literales."),
    ("RN-14", "generalización temática", "media", r"\b(?:en la sociedad actual|en el mundo actual|hoy más que nunca|en el contexto actual de constante cambio)\b", "Sustituir por contexto verificable o eliminar."),
    ("RN-19", "tono publicitario", "media", r"\b(?:solución revolucionaria|a la vanguardia de la innovación|amplia gama de beneficios|marca un antes y un después)\b", "Reformular como evidencia concreta."),
    ("RN-23", "voz conversacional", "alta", r"\b(?:espero que (?:te|le|les) (?:sea|haya sido) útil|si (?:quieres|deseas),? puedo|como (?:modelo de lenguaje|inteligencia artificial))\b", "Eliminar respuesta de asistente ajena al género documental."),
    ("RN-28", "marcador pendiente", "alta", r"\[(?:nombre del autor|insertar (?:información|texto|dato)|referencia pendiente|fuente pendiente|resultado pendiente)[^\]]*\]", "Consultar en el chat; conservar los datos aportados mientras falte corrección confirmada. Retirar marcadores del entregable."),
    ("RN-39", "reserva editorial de evidencia", "alta", r"\bno\s+(?:se\s+)?(?:acredita[n]?|prueba[n]?|certifica[n]?|equivale|significa|permite[n]?)\b", "Determinar la función. Retirar reservas del editor del entregable y describir su objeto directamente; tratar la evaluación en el chat. Preservar resultados y estados técnicos sustantivos."),
    ("RN-39", "aclaración de verificación", "alta", r"\b(?:fecha[s]?\s+(?:inválida[s]?|imposible[s]?)|requiere[n]?\s+(?:verificación|conciliación|confirmación|respaldo|sustento)|según\s+la\s+fuente|la\s+fuente\s+(?:informa|consigna|registra|indica)|por\s+(?:verificar|confirmar))\b", "Tratar la incidencia en el chat. Preservar el dato aportado sin etiqueta de invalidez ni aviso en el documento."),
    ("RN-39", "comentario de conservación de evidencia", "alta", r"\bse\s+conserva\b.{0,160}?\bcomo\s+evidencia\b", "Describir el contenido directamente y resolver el comentario editorial en el chat."),
]


def audit(text: str) -> list[dict]:
    reports = []
    fence_char = None
    fence_len = 0
    for lineno, line in enumerate(text.splitlines(), 1):
        # Cerrar solo con el mismo delimitador y longitud suficiente.
        if fence_char is not None:
            if re.fullmatch(r" {0,3}" + re.escape(fence_char) +
                            "{" + str(fence_len) + r",}\s*", line):
                fence_char = None
            continue
        opening = re.match(r" {0,3}(`{3,}|~{3,})(.*)$", line)
        if opening and not (opening[1][0] == "`" and "`" in opening[2]):
            fence_char, fence_len = opening[1][0], len(opening[1])
            continue
        for rid, label, severity, regex, advice in RULES:
            for hit in re.finditer(regex, line, flags=re.IGNORECASE | re.UNICODE):
                reports.append({"linea": lineno, "regla": rid,
                                "clase": label, "severidad": severity,
                                "fragmento": hit.group(0), "sugerencia": advice})
    return reports



W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
STORY = re.compile(r"word/(?:document|header[0-9]*|footer[0-9]*|footnotes|endnotes|comments)\.xml$")


def read_docx(path: Path) -> dict:
    """Inventariar texto OOXML, sin OCR ni evaluación semántica automática.

    Los identificadores son estables dentro de cada versión del archivo.
    Cada párrafo de una celda o cuadro de texto se cuenta una sola vez.
    Los párrafos vacíos se cuentan por separado, sin simular su revisión.
    """
    blocks = []
    coverage = {"partes": [], "parrafos_xml": 0, "bloques_con_texto": 0,
                "parrafos_vacios": 0, "tablas": 0, "celdas": 0,
                "imagenes_archivo": 0, "cuadros_texto": 0,
                "textos_ocultos": 0, "revisiones_pendientes": 0}
    with ZipFile(path) as archive:
        parts = sorted(n for n in archive.namelist() if STORY.fullmatch(n))
        if "word/document.xml" not in parts:
            raise ValueError("El archivo carece de word/document.xml")
        coverage["imagenes_archivo"] = sum(n.startswith("word/media/") and not n.endswith("/") for n in archive.namelist())
        for part in parts:
            root = ET.fromstring(archive.read(part))
            parent = {child: node for node in root.iter() for child in node}
            def ancestors(node):
                while node in parent:
                    node = parent[node]
                    yield node
            def owner_paragraph(node):
                return next((a for a in ancestors(node) if a.tag == W + "p"), None)
            tables = {node: i for i, node in enumerate(root.iter(W + "tbl"), 1)}
            coverage["partes"].append(part)
            coverage["tablas"] += len(tables)
            coverage["celdas"] += sum(1 for _ in root.iter(W + "tc"))
            coverage["cuadros_texto"] += sum(1 for _ in root.iter(W + "txbxContent"))
            coverage["revisiones_pendientes"] += sum(1 for n in root.iter() if n.tag in (W + "ins", W + "del"))
            section = ""
            for i, paragraph in enumerate(root.iter(W + "p"), 1):
                coverage["parrafos_xml"] += 1
                fragments = []
                for n in paragraph.iter():
                    # Un cuadro de texto anidado tiene sus propios párrafos.
                    if owner_paragraph(n) is not paragraph:
                        continue
                    lineage = list(ancestors(n))
                    if any(a.tag == W + "del" for a in lineage):
                        continue
                    if n.tag == W + "t":
                        fragments.append(n.text or "")
                    elif n.tag in (W + "tab", W + "br", W + "cr"):
                        fragments.append(" ")
                text = " ".join("".join(fragments).split())
                if not text:
                    coverage["parrafos_vacios"] += 1
                    continue
                lineage = list(ancestors(paragraph))
                table = next((n for n in lineage if n.tag == W + "tbl"), None)
                cell = next((n for n in lineage if n.tag == W + "tc"), None)
                row = next((n for n in lineage if n.tag == W + "tr"), None)
                style_node = paragraph.find("./" + W + "pPr/" + W + "pStyle")
                style = style_node.get(W + "val", "") if style_node is not None else ""
                if style.lower().startswith(("heading", "ttulo", "titulo", "título")):
                    section = text
                location = f"párrafo {i}"
                if table is not None and row is not None and cell is not None:
                    rows = [n for n in table.iter(W + "tr") if next((a for a in ancestors(n) if a.tag == W + "tbl"), None) is table]
                    cells = [n for n in row.iter(W + "tc") if next((a for a in ancestors(n) if a.tag == W + "tr"), None) is row]
                    location = f"tabla {tables[table]}, fila {rows.index(row)+1}, celda {cells.index(cell)+1}, párrafo {i}"
                box = any(n.tag == W + "txbxContent" for n in lineage)
                hidden = bool(paragraph.findall(".//" + W + "vanish"))
                coverage["textos_ocultos"] += int(hidden)
                blocks.append({"id": f"{part}:p{i}", "parte": part,
                               "ubicacion": location, "seccion": section,
                               "tipo": "cuadro_texto" if box else "tabla" if table is not None else "parrafo",
                               "texto": text, "revision_editorial": "sin_registrar"})
    coverage["bloques_con_texto"] = len(blocks)
    return {"cobertura": coverage, "bloques": blocks}


def audit_docx(path: Path) -> dict:
    inventory = read_docx(path)
    findings = []
    for block in inventory["bloques"]:
        for finding in audit(block["texto"]):
            findings.append({**finding, "id": block["id"], "parte": block["parte"],
                             "ubicacion": block["ubicacion"], "seccion": block["seccion"]})
    return {**inventory, "hallazgos": findings}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archivo", type=Path, help=".txt/.md UTF-8 o .docx")
    parser.add_argument("--json", action="store_true", help="Reporte JSON")
    parser.add_argument("--inventario", action="store_true", help="Incluir bloques de texto DOCX y registro de revisión vacío en JSON")
    args = parser.parse_args()
    suffix = args.archivo.suffix.lower()
    if suffix not in (".md", ".txt", ".docx"):
        parser.error("Formatos admitidos: .md, .txt y .docx. Para PDF se requiere extracción y revisión visual independientes.")
    try:
        if suffix == ".docx":
            result = audit_docx(args.archivo)
            if not args.inventario:
                result.pop("bloques")
        else:
            result = {"hallazgos": audit(args.archivo.read_text(encoding="utf-8-sig"))}
    except (OSError, BadZipFile, ET.ParseError, ValueError) as exc:
        parser.error(f"No se pudo leer el archivo: {exc}")
    result["archivo"] = str(args.archivo)
    result["advertencia"] = "Coincidencias heurísticas. El inventario acredita extracción, no revisión semántica. Las imágenes requieren inspección visual. No detecta ni cuantifica autoría por IA."
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Revisión heurística de {args.archivo}: {len(result['hallazgos'])} coincidencia(s)")
        if "cobertura" in result:
            c = result["cobertura"]
            print(f"Inventario: {c['bloques_con_texto']} bloques, {c['tablas']} tablas, {c['celdas']} celdas, {c['imagenes_archivo']} imágenes de archivo.")
        for finding in result["hallazgos"]:
            location = finding.get("ubicacion", f"L{finding['linea']}")
            print(f"{location} · {finding['regla']} · «{finding['fragmento']}»")
            print(f"  {finding['sugerencia']}")
        print(result["advertencia"])


if __name__ == "__main__":
    main()
