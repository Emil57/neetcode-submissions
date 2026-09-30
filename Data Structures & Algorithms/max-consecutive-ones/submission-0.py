class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        curr = 0
        # [1,1,0,1,1,1]
        for v in nums:
            if v == 1: curr +=1
            else: 
                maxx = max(maxx, curr)
                curr = 0 
            print(f'Curr: {curr}')
        return max(curr,maxx)