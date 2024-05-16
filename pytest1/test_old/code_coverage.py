import unittest
import coverage

cov = coverage.Coverage()
cov.start()

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)

    def test_add_negative(self):
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-1, 1), 0)

cov.stop()
cov.save()

if __name__ == '__main__':
    cov.html_report()