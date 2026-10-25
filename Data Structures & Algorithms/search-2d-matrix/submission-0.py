class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows-1
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] <= target <= matrix[row][cols-1]:
                l, r = 0, cols-1
                while l <= r: 
                    m = (r+l) // 2
                    if matrix[row][m] == target: return True
                    elif matrix[row][m] > target: r = m - 1
                    else: l = m + 1
                return False
            elif target < matrix[row][0]: bottom = row - 1
            else: top = row + 1
        return False
        # Time O(log (n * m))
        # Space O(1)