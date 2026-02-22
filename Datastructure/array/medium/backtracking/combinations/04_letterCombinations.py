'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''
# Time complexity O(4^n) * O(n) = O(n. 4 ^n)
# Space complexity O(n)
'''
In the worst case, all digits are 7 or 9, giving 4 choices per digit.
At each of the n positions, we branch up to 4 times. Therefore, the total number of combinations generated is:4^n
'''
from typing import List

class Solution:
    MAP = [
        "", "", "abc", "def",
        "ghi", "jkl", "mno", "pqrs",
        "tuv", "wxyz"
    ]

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        self.backtrack(digits, 0, [], result)
        return result

    def backtrack(self, digits: str, idx: int, path: list, result: List[str]):
        if idx == len(digits):
            result.append("".join(path))# O(n)
            return

        letters = self.MAP[int(digits[idx])]

        for ch in letters:
            path.append(ch)
            self.backtrack(digits, idx + 1, path, result)
            path.pop()

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))