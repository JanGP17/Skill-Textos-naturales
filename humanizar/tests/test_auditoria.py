import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from auditar_estilo import audit

class AuditorTest(unittest.TestCase):
    def test_encuentra_muletillas(self):
        rows = audit('Es de vital importancia mencionar este asunto.\n')
        self.assertTrue(any(x['regla'] == 'RN-09' for x in rows))
    def test_salta_codigo(self):
        rows = audit('```md\nEs de vital importancia\n```\n')
        self.assertEqual(rows, [])
    def test_texto_neutro(self):
        self.assertEqual(audit('Se aplicó el instrumento y se registraron las respuestas.'), [])
    def test_lineas(self):
        rows = audit('Línea normal\nEn conclusión, se revisó el dato.')
        self.assertEqual(rows[0]['linea'], 2)

    def test_salta_cercas_tilde(self):
        self.assertEqual(audit('~~~txt\nEn conclusión\n~~~'), [])
    def test_delimitador_distinto_no_cierra(self):
        self.assertEqual(audit('````txt\n```\nEn conclusión\n````'), [])
    def test_reanuda_despues_de_cierre(self):
        rows = audit('~~~txt\nEn conclusión\n~~~\nEn conclusión')
        self.assertEqual([r['linea'] for r in rows], [4])
    def test_advertencia_no_es_puntuacion(self):
        self.assertEqual(audit('La muestra —de 28 docentes— respondió en agosto.'), [])

    def test_calificativos_ornamentales_en_plural(self):
        hits = audit('Presentaron soluciones innovadoras y resultados excepcionales.')
        self.assertEqual([h['fragmento'] for h in hits if h['regla'] == 'RN-10'],
                         ['innovadoras', 'excepcionales'])
        self.assertEqual(audit('El resultado preliminar fue estadísticamente significativo.'), [])

    def test_conectores_formales_son_contextuales(self):
        hits = audit('Asimismo, hubo una demora. Por consiguiente, se amplió el plazo.')
        self.assertEqual([h['fragmento'] for h in hits if h['regla'] == 'RN-11'],
                         ['Asimismo', 'Por consiguiente'])
        self.assertTrue(all(h['severidad'] == 'contextual' for h in hits))

    def test_figura_localiza_comentario_y_comparacion_descriptiva(self):
        rows = audit('Se observa una discrepancia visual por revisar.\n'
                     'Nota. El encabezado identifica Antropología, mientras que el banner lleva el rótulo Arqueología.')
        hits = [row for row in rows if row['clase'] == 'posible anotación editorial sobre una figura']
        self.assertEqual([row['linea'] for row in hits], [1, 2])
        self.assertTrue(all(row['severidad'] == 'contextual' for row in hits))
        self.assertEqual(audit('Portada del micrositio de Antropología'), [])

if __name__ == '__main__':
    unittest.main()
