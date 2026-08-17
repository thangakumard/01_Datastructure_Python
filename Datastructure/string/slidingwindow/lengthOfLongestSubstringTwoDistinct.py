'''
 * https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
 * 
 * Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

	Example 1:
	Input: "eceba"
	Output: 3
	Explanation: t is "ece" which its length is 3.

	Example 2:
	Input: "ccaabbb"
	Output: 5
	Explanation: t is "aabbb" which its length is 5.
 '''
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0

        char_count = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len