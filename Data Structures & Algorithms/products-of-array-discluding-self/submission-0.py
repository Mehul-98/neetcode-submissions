class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        pre = nums[0]
        for i in range(1,len(nums)):
            res[i] = nums[i-1] * res[i-1]
        post = nums[-1]
        for i in range(len(nums) - 2,-1,-1):
            res[i] = res[i] * post
            post = post * nums[i]
        return res
            



        