class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {"":[{},None]}
        for w in words:
            tt = trie[""]
            for i in range(len(w)):
                if w[i] not in tt[0]:
                    tt[0][w[i]] = [{}, None]
                tt = tt[0][w[i]]
            tt[1] = w
        # print(trie)
        
        dirx = [-1,0,1,0]
        diry = [0,-1,0,1]

        res = []
        vis = set()

        def dfs(i,j,curr):
            # print(curr)
            if (i,j) in vis or not curr or board[i][j] not in curr[0]:
                return
            vis.add((i,j))
            curr = curr[0][board[i][j]]
            if curr[1]:
                res.append(curr[1])
                curr[1] = None
            for k in range(4):
                newi = i+dirx[k]
                newj = j+diry[k]
                if newi>=0 and newi<len(board) and newj>=0 and newj<len(board[0]):
                    dfs(newi,newj,curr)
            vis.remove((i,j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,trie[""])
        return res



        