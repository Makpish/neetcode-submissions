class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()

        def dfs(i,x,y):
            if x<0 or x==len(board) or y<0 or y==len(board[0]):
                return False
            
            if word[i] != board[x][y]:
                return False
            
            if i == len(word)-1:
                return True
            
            vis.add((x,y))

            f = False
            
            if (x-1,y) not in vis:
                f = f or dfs(i+1, x-1, y)
            if (x+1,y) not in vis:
                f = f or dfs(i+1, x+1, y)
            if (x,y-1) not in vis:
                f = f or dfs(i+1, x, y-1)
            if (x,y+1) not in vis:
                f = f or dfs(i+1, x, y+1)
            

            vis.remove((x,y))

            return f
        
        for a in range(len(board)):
            for b in range(len(board[0])):
                if dfs(0,a,b):
                    return True
        return False
        