import unittest

#Ici on teste les exceptions 

class ExceptionTest(unittest.TestCase):

    def test_valeurAbsolue(self):
        with self.assertRaises(TypeError):
            abs("a")


if __name__ == '__main__':
    unittest.main()
