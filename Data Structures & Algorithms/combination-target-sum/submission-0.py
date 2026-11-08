class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combinations = []

        def backtracking(i, summ):
            if summ == target:
                result.append(combinations[:])
                return
            elif summ > target or i == len(nums): return

            # no pick 
            backtracking(i+1, summ)
            #pick
            combinations.append(nums[i])
            backtracking(i, summ+nums[i])
            combinations.pop()
        backtracking(0,0)
        return result

        # Time O(n^(T/M))
        # M = Smallest Candidate, T = Target