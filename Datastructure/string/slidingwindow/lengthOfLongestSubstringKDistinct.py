'''
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k:int) -> int:
        if not s:
            return 0

        char_count = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len