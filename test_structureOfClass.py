import unittest

#Exemple d’une classe de test avec unitest
class ClasseDeTest(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(True)
#Pour exécuter une classe de test, il faut utiliser la fonction unittest.main() 
if __name__ == '__main__':
    unittest.main()
