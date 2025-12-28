class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        last_index = {}      # char -> last seen index
        left = 0
        max_length = 0

        for right, ch in enumerate(s):
            if ch in last_index and last_index[ch] >= left:
                left = last_index[ch] + 1

            last_index[ch] = right
            max_length = max(max_length, right - left + 1)

        return max_length
    
    def lengthOfLongestSubstring_II(self, s: str) -> int:
        counter = [0] * 256
        left = right = 0
        max_length = 0

        while right < len(s):
            if counter[ord(s[right])] == 0:
                counter[ord(s[right])] += 1
                right += 1
            else:
                counter[ord(s[left])] -= 1
                left += 1

            max_length = max(max_length, right - left)
    
        return max_length


if __name__ == "__main__":
    solution = Solution()
    test_string = "abcabcbb"
    print(solution.lengthOfLongestSubstring(test_string))  # Output: 3

'''
“If the input is guaranteed to be standard ASCII or a very small fixed alphabet,
 I might use an array of fixed size for maximum speed and constant memory. 
 But if the character set could be larger, 
 like full Unicode, or not clearly bounded, 
 or if I want clearer and more robust code, 
 I’d use a dictionary mapping each character to its count or last index. 
 The time complexity is still O(n),
   but a dictionary generalizes better and avoids assumptions about the character set.”
'''