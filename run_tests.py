import unittest
import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)


def run_tests():
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")

    # Configure test runner with verbose output
    runner = unittest.TextTestRunner(verbosity=2)

    print("\nRunning Tests...")
    print("=" * 50)

    # Run tests and store results
    result = runner.run(suite)

    # Print summary
    print("\nTest Summary:")
    print(f"Ran {result.testsRun} tests")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")


if __name__ == "__main__":
    run_tests()
