'''
https://leetcode.com/problems/word-search/?envType=study-plan-v2&envId=top-interview-150

'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board), len(board[0])

        def dfs(r: int, c: int,i:int):
            if i == len(word):
                return True
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i]):
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                if dfs(r+dr,c+dc,i+1):
                    return True

            board[r][c] = temp
            return False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        return False