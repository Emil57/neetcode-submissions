class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, maxx = 0, float('-inf')
        for n in nums:
            curr+=n
            maxx = max(curr, maxx)
            if curr < 0: curr = 0
        return maxx
        # Time O(n)
        # Space O(1)