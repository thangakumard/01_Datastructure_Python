'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
# Time complexity O(nCn)
# Space Complexity O(n)
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []
        path: List[str] = []

        def backtracking(open: int, close: int):
            if(len(path) == 2 * n):
                result.append(''.join(path)) #O(n)
                return
            if open < n:
                path.append('(')
                backtracking(open+1, close)
                path.pop()
            if close < open:
                path.append(')')
                backtracking(open, close+1)
                path.pop()

        backtracking(0,0) # O(Cn) * O(n) = O (nCn)
        return result 
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(5))