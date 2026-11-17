class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        ps = 1

        for i in range(len(nums)):
            res[i] = ps
            ps *= nums[i]
        ps = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*= ps
            ps*=nums[i]
        
        return res