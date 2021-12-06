import unittest


class ExceptionTest(unittest.TestCase):

    def valeurAbsolue(self):
        with self.assertRaises(TypeError):
            abs("a")


if __name__ == '__main__':
    unittest.main()
