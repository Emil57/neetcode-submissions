class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        mon_stack = []

        for r in range(len(temperatures)):
            while mon_stack and temperatures[r] > temperatures[mon_stack[-1]]:
                l = mon_stack.pop()
                out[l] = r-l
            mon_stack.append(r)
        
        return out

