import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
agrupa_multiplos = getattr(undertest, 'agrupa_multiplos', None)

class PublicTests(unittest.TestCase):

   def test_adicional_1(self):
        seq = [6, 15, 12, 6, 8, 3, 25, 14, 1, 10, 7]

        agrupa_multiplos(seq, 5)
        assert seq == [15, 25, 10, 6, 12, 6, 8, 3, 14, 1, 7]

        agrupa_multiplos(seq, 2)
        assert seq == [10, 6, 12, 6, 8, 14, 15, 25, 3, 1, 7]

        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
