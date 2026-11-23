import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from auditar_estilo import audit, audit_docx, negation_summary


class NegacionesTest(unittest.TestCase):
    def markers(self, text):
        return [h for h in audit(text) if h['regla'] == 'RN-41']

    def test_ejemplos_del_usuario_localizados(self):
        for text in ['No se realizó la prueba de carga.', 'No se afirma la aceptación.', 'No se encontraron diferencias estadísticamente significativas.']:
            with self.subTest(text=text):
                self.assertEqual(len(self.markers(text)), 1)

    def test_cada_aparicion_y_contexto(self):
        text = 'No se realizó. No se afirma. No hay registros.'
        hits = self.markers(text)
        self.assertEqual([h['columna'] for h in hits], [1, 16, 30])
        self.assertTrue(all('No se realizó.' in h['contexto'] for h in hits))

    def test_variantes_y_mayusculas(self):
        hits = self.markers('NO. Nunca. JAMÁS. Tampoco. Ni. Sin.')
        self.assertEqual([h['fragmento'].lower() for h in hits], ['no', 'nunca', 'jamás', 'tampoco', 'ni', 'sin'])

    def test_limites_de_palabra(self):
        self.assertEqual(self.markers('Nodo normal. Sincronizar. Nivel nominal. Sinopsis.'), [])

    def test_sustitucion_sin_sigue_en_revision(self):
        hits = self.markers('La prueba quedó sin ejecutar.')
        self.assertEqual(hits[0]['fragmento'], 'sin')
        self.assertEqual(hits[0]['severidad'], 'contextual')

    def test_cuantificadores_localizados_sin_reescribir(self):
        text = 'No todos completaron la tarea. No necesariamente ocurre siempre.'
        self.assertEqual(len(self.markers(text)), 2)
        self.assertIn('No todos', self.markers(text)[0]['contexto'])
        self.assertIn('No necesariamente', self.markers(text)[1]['contexto'])

    def test_codigo_excluido_y_reanudacion(self):
        text = '```txt\nNo se realizó.\n```\nNo se afirma.'
        self.assertEqual([h['linea'] for h in self.markers(text)], [4])

    def test_citas_y_terminos_necesitan_contexto(self):
        text = '«No se realizó». Prueba no paramétrica. Sigla NO.'
        hits = self.markers(text)
        self.assertEqual(len(hits), 3)
        self.assertTrue(all(h['severidad'] == 'contextual' for h in hits))

    def test_resumen_no_dicta_decision(self):
        summary = negation_summary(audit('No se realizó. Tampoco se afirma.'))
        self.assertEqual(summary['apariciones'], 2)
        self.assertEqual(summary['por_marcador'], {'no': 1, 'tampoco': 1})
        self.assertEqual(summary['decision_semantica'], 'pendiente_de_revision_contextual')

    def test_runs_divididos_y_celda(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'caso.docx'
            xml = '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:tbl><w:tr><w:tc><w:p><w:r><w:t>N</w:t></w:r><w:r><w:t>o se realizó.</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:body></w:document>'
            with ZipFile(path, 'w') as z:
                z.writestr('word/document.xml', xml)
            before = path.read_bytes()
            result = audit_docx(path)
            hit = next(h for h in result['hallazgos'] if h['regla'] == 'RN-41')
            self.assertIn('tabla 1, fila 1, celda 1', hit['ubicacion'])
            self.assertEqual(result['revision_negaciones']['apariciones'], 1)
            self.assertEqual(path.read_bytes(), before)

    def test_cli_json_integra_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'caso.md'
            path.write_text('No se realizó.\nNo se afirma.', encoding='utf-8')
            program = Path(__file__).resolve().parents[1] / 'scripts' / 'auditar_estilo.py'
            result = subprocess.run([sys.executable, str(program), str(path), '--json'], capture_output=True, text=True, check=True)
            data = json.loads(result.stdout)
            self.assertEqual(data['revision_negaciones']['apariciones'], 2)
            self.assertEqual(path.read_text(encoding='utf-8'), 'No se realizó.\nNo se afirma.')


if __name__ == '__main__':
    unittest.main()
