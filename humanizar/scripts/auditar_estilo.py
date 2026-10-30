#!/usr/bin/env python3
"""Auditor heurístico de muletillas en español, NO detector de IA.

Lee solamente .md/.txt. No reescribe el archivo. Sus hallazgos son
observaciones de superficie que un editor debe confirmar en contexto.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

RULES = [
    ("RN-09", "prefacio vacío", "media", r"\b(?:es de vital importancia|es importante (?:mencionar|destacar|señalar)|cabe (?:destacar|resaltar|mencionar))\b", "¿Puede comenzar directamente con la afirmación?"),
    ("RN-10", "léxico grandilocuente", "contextual", r"\b(?:pilar fundamental|panorama dinámico|en el dinámico panorama|papel crucial|experiencia enriquecedora|un análisis exhaustivo|transformación revolucionaria)\b", "Solicitar dato concreto o simplificar; conservar si se justifica."),
    ("RN-11", "conector ritual", "contextual", r"\b(?:en este sentido|en ese sentido|por otra parte|aunado a ello|en conclusión|en definitiva)\b", "Comprobar que la transición tiene función lógica."),
    ("RN-12", "contraste reiterable", "contextual", r"\b(?:no solo\b.{0,100}?\bsino (?:también|que)|no (?:es|se trata de)\b.{0,100}?\bsino)\b", "Revisar si existe una oposición real; no prohibir la estructura."),
    ("RN-14", "generalización temática", "media", r"\b(?:en la sociedad actual|en el mundo actual|hoy más que nunca|en el contexto actual de constante cambio)\b", "Sustituir por contexto verificable o eliminar."),
    ("RN-19", "tono publicitario", "media", r"\b(?:solución revolucionaria|a la vanguardia de la innovación|amplia gama de beneficios|marca un antes y un después)\b", "Reformular como evidencia concreta."),
    ("RN-23", "voz conversacional", "alta", r"\b(?:espero que (?:te|le|les) (?:sea|haya sido) útil|si (?:quieres|deseas),? puedo|como (?:modelo de lenguaje|inteligencia artificial))\b", "Eliminar respuesta de asistente ajena al género documental."),
    ("RN-28", "marcador pendiente", "alta", r"\[(?:nombre del autor|insertar (?:información|texto|dato)|referencia pendiente|fuente pendiente|resultado pendiente)[^\]]*\]", "Completar únicamente con información comprobada."),
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archivo", type=Path, help=".txt o .md codificado en UTF-8")
    parser.add_argument("--json", action="store_true", help="Reporte JSON")
    args = parser.parse_args()
    if args.archivo.suffix.lower() not in (".md", ".txt"):
        parser.error("Solo archivos .md y .txt; no se analizan documentos Word/PDF.")
    content = args.archivo.read_text(encoding="utf-8-sig")
    report = audit(content)
    if args.json:
        print(json.dumps({"archivo": str(args.archivo), "hallazgos": report,
            "advertencia": "Coincidencias heurísticas; no detecta ni cuantifica autoría por IA."},
            ensure_ascii=False, indent=2))
    else:
        print(f"Revisión heurística de {args.archivo}: {len(report)} coincidencia(s)")
        for x in report:
            print(f"L{x['linea']} · {x['regla']} · {x['severidad']} · «{x['fragmento']}»")
            print(f"  {x['sugerencia']}")
        print("Importante: no atribuye origen IA ni evalúa la calidad global.")


if __name__ == "__main__":
    main()
