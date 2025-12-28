#https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        for i in nums:
            if i != val:
                nums[pointer] = i
                pointer += 1
        return pointer
    if __name__ == "__main__":
        nums1 = [3, 2, 3, 3, 1, 0]
        result = removeElement(nums1, 3)
        print(result)
    