import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(suma(1, 2), 3)

    def test_suma_negativa(self):
        self.assertEqual(suma(-1, -2), -3)

if __name__ == '__main__':
    unittest.main()
