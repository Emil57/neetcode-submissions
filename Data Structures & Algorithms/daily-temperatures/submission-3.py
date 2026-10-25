class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_stack = []
        res = [0] * len(temperatures)

        for r in range(len(temperatures)):
            while mon_stack and temperatures[mon_stack[-1]] < temperatures[r]:
                l = mon_stack.pop()
                res[l] = r-l
            mon_stack.append(r)
        return res
        # Time O(n)
        # Space O(n)