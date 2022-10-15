import unittest
import LAB1


class test_lab1 (unittest.TestCase):
    def test_value(self):
        self.assertEqual(LAB1.f(52), 5)
        self.assertEqual(LAB1.f(634), 6)
        self.assertEqual(LAB1.f(0), 0)



