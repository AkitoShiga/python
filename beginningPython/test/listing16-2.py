import unittest, my_math2
from subprocess import Popen, PIPE

class ProductTestCase(unittest.TestCase):
    def test_integers(self):
        for x in range(-10, 20):
            for y in range(-10, 10):
                p = my_math2.product(x,y)
                self.assertEqual(p, x * y,' Integerの乗算に失敗しました')


    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10
                y = y / 10
                p = my_math2.product(x, y)
                self.assertEqual(p, x * y, 'Floatの乗算に失敗しました')

    def test_with_PyChecker(self):

        cmd = 'pychecker', '-Q', my_math2.__file__.rstrip('c')
        pychecker = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pychecker.stdout.read(), '')

    def test_with_PyLint(self):
        cmd = 'pylint', '-rn', 'my_math2'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pylint.stdout.read(), '')

if __name__ == '__main__':
    unittest.main()