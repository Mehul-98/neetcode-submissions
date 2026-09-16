class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        have = 0
        currmap,targetmap = {},{}
        for char in t:
            targetmap[char] = targetmap.get(char,0) + 1
        need = len(targetmap)
        l = 0
        best_start = 0
        res_len = float("inf")
        for r in range(len(s)):
            currmap[s[r]] = currmap.get(s[r],0) + 1
            if s[r] in targetmap and currmap[s[r]] == targetmap[s[r]]:
                have += 1
            while have == need:
                size = r - l + 1
                if res_len > size:
                    res_len = size
                    best_start = l
                
                currmap[s[l]] -= 1
                if s[l] in targetmap and currmap[s[l]] < targetmap[s[l]]:
                    have -= 1
                l += 1
        if res_len == float("inf"):
            return ""
        return s[best_start:best_start+res_len]

