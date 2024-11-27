
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
