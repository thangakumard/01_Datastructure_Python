'''
https://leetcode.com/problems/majority-element/submissions/1857230705/?envType=study-plan-v2&envId=top-interview-150
Boyer-Moore Voting Algorithm

'''
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        candidate = counter = 0

        for num in nums:
            if counter == 0:
                candidate = num
            if candidate == num:
                counter += 1
            else:
                counter -= 1
        return candidate

if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,3]
    print(sol.majorityElement(nums))  # Output: 3
