class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        length = 0
        for n in numset:
            if n-1 in numset:
                continue
            else:
                l = 0
                while n+l in numset:
                    l +=1
                length = max(l,length)
        return length
                    
        