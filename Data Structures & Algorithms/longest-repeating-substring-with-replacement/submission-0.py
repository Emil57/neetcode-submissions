class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = [0] * 26
        l=0
        longest = 0
        for r in range(len(s)):
            letters[ord(s[r])-ord('A')]+=1
            
            while ((r-l+1) - max(letters)) > k:
                letters[ord(s[l])-ord('A')]-=1
                l+=1
            
            longest = max(r-l+1, longest)
        return longest
        