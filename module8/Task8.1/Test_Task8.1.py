import unittest
import Task_full


class TestTask(unittest.TestCase):

    def test_discriminant(self):
        print("Discriminant testing:")
        self.assertEqual(Task_full.discriminant(1, -2, -3), 16)
        self.assertEqual(Task_full.discriminant(1, -6, 9), 0)
        self.assertEqual(Task_full.discriminant(5, 3, 7), -131)

    def test_roots(self):
        print("Roots testing:")
        self.assertEqual(Task_full.roots(16, 1, -2, -3), (3.0, -1.0))
        self.assertEqual(Task_full.roots(0, 1, -6, 9), 3.0)
        self.assertEqual(Task_full.roots(-131, 5, 3, 7), None)

    def test_solve_square(self):
        print("Solve square testing:")
        self.assertEqual(Task_full.solve_square(1, -2, -3), (3.0, -1.0))
        self.assertEqual(Task_full.solve_square(1, -6, 9), 3.0)
        self.assertEqual(Task_full.solve_square(5, 3, 7), None)








