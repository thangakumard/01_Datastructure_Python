#https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x, y, z = m-1, n-1, m + n -1

        while y >= 0:
            if x >= 0 and nums1[x] >= nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1
            z -= 1

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3

    nums2 = [2, 5, 6]
    n = 3

    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]