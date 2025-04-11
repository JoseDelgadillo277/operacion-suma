import unittest
from operaciones_aritmeticas import OperacionesAritmeticas

class TestSuma(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
    # Arrange
        operando1 = 10
        operando2 = 15
        resultadoEsperado = 25
        objSuma = OperacionesAritmeticas(operando1, operando2)

    # Act
        resultadoActual = objSuma.calcularSuma()

    # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, msg= "Fallo la suma")

    def test_suma_operadorNoNumerico_lanzaExepcion(self):
        objSuma = OperacionesAritmeticas(operando1=3, operando2="a")
        with self.assertRaises(ValueError):
            objSuma.calcularSuma()


    def test_division_dosNumeros_retornaDivision(self):
            # Arrange
            dividendo = 10
            divisor = 15
            resultadoEsperado = 0.667
            objSuma = OperacionesAritmeticas(dividendo, divisor)

            # Act
            resultadoActual = objSuma.calcular_division()

            # Assert
            self.assertAlmostEqual(resultadoEsperado, resultadoActual, places=2,msg="Fallo la division")

    def test_division_operadorNoNumerico_lanzaExepcion(self):
        objSuma = OperacionesAritmeticas(operando1=3, operando2="a")
        with self.assertRaises(ValueError):
            objSuma.calcular_division()

    def test_division_operadorNoNumerico_lanzaExepcion(self):
        objSuma = OperacionesAritmeticas(operando1=3, operando2=0)
        with self.assertRaises(ZeroDivisionError):
            objSuma.calcular_division()

if __name__ == '__main__':
    unittest.main()
