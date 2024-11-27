import unittest
from src.task_01 import Solution

class TestWordCounter(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_sample.txt"
        with open(self.test_file, "w") as f:
            f.write("Hello world!")
            f.write("This is a sample text file.")
            f.write("Hello Python world.")
            f.write("1231 is again 1231.")
    
    def cleanup(self):
        os.remove(self.test_file)
    
    def test_word_count():


    if __name__ == "__main__":
    unittest.main()
