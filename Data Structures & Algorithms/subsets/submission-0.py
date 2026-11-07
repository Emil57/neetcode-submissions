class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        tracks =[]
        result = []
        n = len(nums)

        def backtracking(i):
            if i == n:
                result.append(tracks[:])
                return
            
            backtracking(i+1)

            tracks.append(nums[i])
            backtracking(i+1)
            tracks.pop()
        backtracking(0)
        return result
        # Time O(n 2^n)
        # Space O(n 2^n)
