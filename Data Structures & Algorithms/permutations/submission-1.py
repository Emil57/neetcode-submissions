class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations, tracks = [], []
        used = set()
        def backtracking():
            if len(tracks) == len(nums):
                permutations.append(tracks[:])
                return
            
            for n in nums:
                if n not in used:
                    used.add(n)
                    tracks.append(n)
                    backtracking()
                    tracks.pop()
                    used.remove(n)
        backtracking()
        return permutations

        # Time O(n * n!)
        # Space O(n * n!)
        