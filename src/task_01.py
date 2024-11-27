"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0, 1]
"""


class Solution:
    def word_count(self, filepath: str):
        """
        type: file: str - file to be used
        rtype:
        """
        word_counts = {}
        # Using a context manager for proper open/close the file descriptor
        with open(filepath, "r") as file:
            for line in file:
                print(line)
                cleaned_line = ""
                for char in line:
                    if char.isalnum() or char.isspace():
                        cleaned_line += char.lower()
                    else:
                        cleaned_line += ""

                words = cleaned_line.split()
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
        return word_counts


def main():
    run = Solution()
    print(run.word_count("sample.txt"))


if __name__ == "__main__":
    main()
