class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrow = points[0][1]
        number_arrows = 0
        for point in points:
            if arrow < point[0] or arrow > point[1]:
                number_arrows+=1
                arrow = point[1]
        return number_arrows+1
        # Time O(n log n)
        # Space O(1)
