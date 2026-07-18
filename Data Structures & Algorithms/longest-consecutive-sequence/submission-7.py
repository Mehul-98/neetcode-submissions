class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        if nums == []:
            return 0
        length = 1
        for i in range(len(nums)):
            if nums[i] - 1 in numset:
                continue
            else:
                start = nums[i]
                l = 0
                while(start in numset):
                    l += 1
                    start += 1
                length = max(length,l)
        return length
                    
        