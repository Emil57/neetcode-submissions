class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, tracks = [], []

        def backtracking(i):
            if i == len(nums):
                subsets.append(tracks[:])
                return
            backtracking(i+1)

            tracks.append(nums[i])
            backtracking(i+1)
            tracks.pop()
        
        backtracking(0)
        return subsets
        #Time O(2^n)
        # Space O(2^n)