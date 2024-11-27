import unittest
from src.task_01 import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_example2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

    def test_example3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_negative_numbers(self):
        nums = [0, -3, 4, 3, 90]
        target = 0
        self.assertEqual(self.solution.twoSum(nums, target), [1, 3])

    def test_multiple_solutions(self):
        nums = [2, 5, 5, 11]
        target = 10
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])


if __name__ == "__main__":
    unittest.main()
