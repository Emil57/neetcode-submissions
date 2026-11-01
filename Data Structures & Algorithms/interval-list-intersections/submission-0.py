class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]

            if second[0] <= first[1] <= second[1] or first[0] <= second[1] <= first[1]:
                interval = [max(first[0],second[0]), min(first[1],second[1])]
                res.append(interval)
            
            if first[1] < second[1]: i+=1
            else: j+=1
        return res