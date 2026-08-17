'''
Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

 

Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
 

Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.
'''
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        oddChar = 0

        for key, value in freq.items():
            if value%2 == 1:
                oddChar += 1
            if oddChar > 1:
                return False
        
        return True
