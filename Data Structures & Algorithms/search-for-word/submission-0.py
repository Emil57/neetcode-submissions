class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtracking(r,c,i):
            if i == len(word): return True
            if not (r in range(rows) and c in range(cols) and board[r][c] == word[i]): return False

            char = board[r][c]
            board[r][c] = '.'

            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr,nc = dr+r, dc+c
                if backtracking(nr,nc,i+1):
                    board[r][c] = char
                    return True
            board[r][c] = char
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtracking(r,c,0):
                        return True
        return False

        # Time O((m*n)*3^(L-1)), L = length of word
        # Space O(L)