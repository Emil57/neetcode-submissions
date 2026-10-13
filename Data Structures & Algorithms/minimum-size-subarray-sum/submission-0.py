class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        summ = 0
        minn = float('inf')
        for r in range(len(nums)):

            summ+= nums[r]

            while summ >= target: 
                minn = min(minn, r-l+1)
                summ -= nums[l]
                l+=1
            
        return minn if minn != float('inf') else 0 