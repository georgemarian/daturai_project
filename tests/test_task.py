import unittest
import os
from src.task_01 import Solution


class TestWordCounter(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_sample.txt"
        with open(self.test_file, "w") as f:
            f.write("Hello world!\n")
            f.write("This is a sample text file.\n")
            f.write("Hello Python world.\n")
            f.write("1231 is again 1231.\n")

    def tearDown(self):
        os.remove(self.test_file)

    def test_word_count(self):
        # Instantiate the WordCounter with the test file
        word_counter = Solution()
        result = word_counter.word_count(self.test_file)

        # Expected output
        expected = {
            "hello": 2,
            "world": 2,
            "this": 1,
            "is": 2,
            "a": 1,
            "sample": 1,
            "text": 1,
            "file": 1,
            "python": 1,
            "1231": 2,
            "again": 1,
        }

        # Assert the result matches the expected output
        self.assertEqual(result, expected)


# Run the tests
if __name__ == "__main__":
    unittest.main()
