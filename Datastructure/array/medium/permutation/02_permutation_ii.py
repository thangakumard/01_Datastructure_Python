'''
https://leetcode.com/problems/permutations/
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''
from typing import List
class Solution:
    def permute_ii(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        nums.sort()
        self._backtracking(nums, result, [], used)
        return result
    def _backtracking(self, nums: List[int], result: List[List[int]], temp: List[int], used: List[bool]):
        if(len(nums) == len(temp)):
            result.append(temp.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i>0 and nums[i] == nums[i-1] and used[i-1] == False:
                continue
            used[i] = True
            temp.append(nums[i])
            self._backtracking(nums, result, temp, used)
            temp.pop()
            used[i] = False

if __name__ == "__main__":
    sol = Solution()
    input = [1,2,3]
    print(sol.permute_ii(input))
