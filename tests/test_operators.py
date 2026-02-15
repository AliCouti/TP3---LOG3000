import unittest
from src.operators import add, subtract, multiply, divide

class TestOperators(unittest.TestCase):
    """
    Suite de tests unitaires pour les opérations mathématiques de base.
    """

    def test_add(self):
        """
        Teste l'addition de deux nombres.
        """
        # Ces tests vérifient que l'addition de deux nombres donne le résultat attendu.
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        """
        Teste la soustraction standard.
        """
        # Ces tests visent à vérifier la soustraction normale qui est (a - b).
        self.assertEqual(subtract(10, 5), 5) 
        self.assertEqual(subtract(5, 10), -5)

    def test_multiply(self):
        """
        Teste la multiplication standard.
        """
        # Ces tests vérifient la multiplication normale (a * b) et la multiplication par zéro.
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(2, 0), 0)

    def test_divide(self):
        """
        Teste la division standard.
        """
        # Ces tests vérifient la division normale (a / b) qui inclut des réponses décimales.
        self.assertEqual(divide(5, 2), 2.5) 
        
    def test_divide_by_zero(self):
        """
        Devrait lever une erreur ou gérer la division par zéro.
        """
        # Ces tests vérifient que la division par zéro est correctement gérée.
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()