import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from auditar_estilo import audit, audit_docx, read_docx

NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def part(body, root='document'):
    return f'<w:{root} xmlns:w="{NS}">{body}</w:{root}>'


class WordAuditTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'informe.docx'

    def write(self, content, extra=None):
        with ZipFile(self.path, 'w') as z:
            z.writestr('word/document.xml', part('<w:body>' + content + '</w:body>'))
            for name, content in (extra or {}).items():
                z.writestr(name, content)

    def test_tabla_y_runs_fragmentados(self):
        self.write('<w:tbl><w:tr><w:tc><w:p><w:r><w:t>No acre</w:t></w:r><w:r><w:t>dita por sí solo la aceptación.</w:t></w:r></w:p></w:tc></w:tr></w:tbl>')
        result = audit_docx(self.path)
        self.assertEqual(result['cobertura']['tablas'], 1)
        self.assertEqual(result['cobertura']['celdas'], 1)
        self.assertTrue(any('tabla 1, fila 1, celda 1' in h['ubicacion'] for h in result['hallazgos']))

    def test_partes_perifericas(self):
        self.write('<w:p><w:r><w:t>Cuerpo.</w:t></w:r></w:p>', {
            'word/header1.xml': part('<w:p><w:r><w:t>Fecha inválida.</w:t></w:r></w:p>', 'hdr'),
            'word/footer2.xml': part('<w:p><w:r><w:t>Requiere verificación.</w:t></w:r></w:p>', 'ftr'),
            'word/footnotes.xml': part('<w:footnote w:id="1"><w:p><w:r><w:t>Según la fuente.</w:t></w:r></w:p></w:footnote>', 'footnotes'),
            'word/comments.xml': part('<w:comment w:id="0"><w:p><w:r><w:t>Comentario.</w:t></w:r></w:p></w:comment>', 'comments'),
        })
        result = audit_docx(self.path)
        self.assertEqual(len(result['cobertura']['partes']), 5)
        self.assertEqual(len(result['bloques']), 5)
        self.assertEqual(len({h['parte'] for h in result['hallazgos']}), 3)

    def test_cuadro_texto_una_vez(self):
        self.write('<w:p><w:r><w:t>Exterior.</w:t></w:r><w:r><w:pict><w:txbxContent><w:p><w:r><w:t>Fecha inválida.</w:t></w:r></w:p></w:txbxContent></w:pict></w:r></w:p>')
        result = audit_docx(self.path)
        self.assertEqual([b['texto'] for b in result['bloques']], ['Exterior.', 'Fecha inválida.'])
        self.assertEqual(result['cobertura']['cuadros_texto'], 1)
        self.assertEqual(len(result['hallazgos']), 1)

    def test_tablas_anidadas(self):
        self.write('<w:tbl><w:tr><w:tc><w:p><w:r><w:t>Exterior.</w:t></w:r></w:p><w:tbl><w:tr><w:tc><w:p><w:r><w:t>Requiere conciliación.</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:tc></w:tr></w:tbl>')
        result = audit_docx(self.path)
        self.assertEqual(result['cobertura']['tablas'], 2)
        self.assertEqual(result['cobertura']['celdas'], 2)
        self.assertIn('tabla 2, fila 1, celda 1', result['hallazgos'][0]['ubicacion'])

    def test_extraccion_no_aprueba_revision(self):
        self.write('<w:p><w:r><w:t>Texto.</w:t></w:r></w:p><w:p/>')
        result = read_docx(self.path)
        self.assertEqual(result['cobertura']['parrafos_xml'], 2)
        self.assertEqual(result['cobertura']['parrafos_vacios'], 1)
        self.assertTrue(all(b['revision_editorial'] == 'sin_registrar' for b in result['bloques']))

    def test_original_inmutable(self):
        self.write('<w:p><w:r><w:t>Fecha inválida 35/10/2026.</w:t></w:r></w:p>')
        before = hashlib.sha256(self.path.read_bytes()).hexdigest()
        result = audit_docx(self.path)
        self.assertTrue(result['hallazgos'])
        self.assertIn('35/10/2026', result['bloques'][0]['texto'])
        self.assertEqual(before, hashlib.sha256(self.path.read_bytes()).hexdigest())

    def test_resultado_negativo_y_estado_tecnico(self):
        text = 'No se encontraron diferencias estadísticamente significativas. El build no se ejecutó. El instrumento tiene tres dimensiones: acceso, uso y satisfacción.'
        self.assertEqual(audit(text), [])

    def test_cambio_controlado_eliminado(self):
        self.write('<w:p><w:del><w:r><w:delText>Fecha inválida.</w:delText></w:r></w:del><w:ins><w:r><w:t>Texto vigente.</w:t></w:r></w:ins></w:p>')
        result = audit_docx(self.path)
        self.assertEqual(result['bloques'][0]['texto'], 'Texto vigente.')
        self.assertEqual(result['cobertura']['revisiones_pendientes'], 2)
        self.assertEqual(result['hallazgos'], [])

    def test_oposicion_recomienda_reformular(self):
        result = audit('No es una solución, sino un proceso.')
        hit = next(h for h in result if h['regla'] == 'RN-12')
        self.assertIn('Reformular directamente', hit['sugerencia'])
        self.assertNotIn('no prohibir', hit['sugerencia'])

    def test_advertencia_fecha_en_celda(self):
        self.assertTrue(any(h['regla'] == 'RN-39' for h in audit('Aprobada; salida 0. La fecha requiere verificación.')))


if __name__ == '__main__':
    unittest.main()
