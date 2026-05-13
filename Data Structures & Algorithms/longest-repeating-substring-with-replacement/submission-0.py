class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            # Update the count for the character entering the window
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Update the max frequency found in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # If replacements needed > k, shrink window from left
            # Window Length = (right - left + 1)
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            # Update result with the size of the largest valid window
            res = max(res, right - left + 1)
            
        return res
