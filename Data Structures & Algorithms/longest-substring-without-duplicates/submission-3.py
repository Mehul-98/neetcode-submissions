class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = 0 
        charmap = set()
        start = 0
        for i in range(len(s)):
            while s[i] in charmap:
                charmap.remove(s[start])
                start += 1
            charmap.add(s[i])
            currlen = i - start + 1
            long = max(long,currlen)
        return long

        

        