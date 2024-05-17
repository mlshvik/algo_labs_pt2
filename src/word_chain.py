class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=len)
        dp = {}
        for word in words:
            for i in range(len(word)):
                dp[word] = max(dp.get(word[:i] + word[i + 1:], 0) + 1, dp.get(word, 0))
        return max(dp.values())


def read_input(file_name):
    with open(file_name, 'r') as file:
        N = int(file.readline().strip())
        words = [file.readline().strip() for _ in range(N)]
    return N, words


def write_output(file_name, result):
    with open(file_name, 'w') as file:
        file.write(str(result) + '\n')


def main():
    input_file = r'D:\унік\гіти\algo_labs_pt2\tests\wchain.in'
    output_file = r'D:\унік\гіти\algo_labs_pt2\tests\wchain.out'

    N, words = read_input(input_file)
    solution = Solution()
    result = solution.longestStrChain(words)
    write_output(output_file, result)


if __name__ == '__main__':
    main()
