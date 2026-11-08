class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        tracks = []

        def backtracking():
            if len(tracks) == len(nums):
                permutations.append(tracks[:])
            
            for n in nums:
                if n not in tracks:
                    tracks.append(n)
                    backtracking()
                    tracks.pop()
        backtracking()
        return permutations

        # Time O(n!)
        # Space O(n!)
        