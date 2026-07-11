class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsetmap = {i:set() for i in range(9)}
        colsetmap = {i:set() for i in range(9)}
        gridsetmap = {i:set() for i in range(9)} 

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rowsetmap[i]:
                        return False
                    rowsetmap[i].add(board[i][j])

                    if board[i][j] in colsetmap[j]:
                        return False
                    colsetmap[j].add(board[i][j])

                    if board[i][j] in gridsetmap[(i//3)*3 + j//3]:
                        return False
                    gridsetmap[(i//3)*3 + j//3].add(board[i][j])
        return True

                    
        