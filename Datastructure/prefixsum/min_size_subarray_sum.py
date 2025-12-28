#https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=prefix-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1
        return res if res != float('inf') else 0
    
from typing import List 
if __name__ == "__main__":
    solution = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(solution.minSubArrayLen(target, nums))  # Output: 2

    target = 4
    nums = [1,4,4]
    print(solution.minSubArrayLen(target, nums))  # Output: 1