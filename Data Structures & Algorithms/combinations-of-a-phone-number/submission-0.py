class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        combinations, tracks = [], []

        mapp = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def backtrack(i):
            if i == len(digits):
                combinations.append("".join(tracks))
                return
            
            for c in mapp[digits[i]]:
                tracks.append(c)
                backtrack(i+1)
                tracks.pop()
        
        backtrack(0)
        return combinations

        # Time O(4**n)
        # Space O(n)