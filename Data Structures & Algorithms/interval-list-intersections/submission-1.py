class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]

            start = max(first[0], second[0])
            end = min(first[1], second[1])
            if start <= end:
                res.append([start,end])
            
            if first[1] < second[1]: i+=1
            else: j+=1
        return res
        # Time O(n)
        # Space O(n)