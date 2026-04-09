'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n
'''
#Time complexity O (k.C(n,k))
#Space Complexity O(k)
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n:
            return []
        result = []
        def backtracking(current, start):
            if len(current) == k:
                result.append(current[:])
                return
            remaining = k - len(current)# remainingLen = 2-1 = 1
            # last start value that still allows filling 'remainingLen' numbers
            end = n - remaining + 1 # 5 - 1 + 1 = 5
            for i in range(start, end + 1):
                current.append(i)
                backtracking(current, i+1)
                current.pop()
        backtracking([],1)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(5,2))
