class Solution:
    def __init__(self) -> None:
        self.max_length = 0
        self.start = 0
        
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            self.max_substring(s, i, i)
            self.max_substring(s, i, i + 1)
        return s[self.start : self.start + self.max_length]
            
    def max_substring(self, s: str, l: int, r: int) -> None:
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        if self.max_length < r - l - 1:
            self.max_length = r - l - 1
            self.start = l + 1
        
        