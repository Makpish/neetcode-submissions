class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # adj = {}
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            j=0
            while j<len(words[i]) and j<len(words[i+1]):
                if words[i][j] != words[i+1][j]:
                    break
                j+=1
            if j==len(words[i]):
                continue
            if j==len(words[i+1]):
                return ""
            adj[words[i+1][j]].add(words[i][j])
        # s.add(w[-1])
        
        vis = {}
        x = []

        def dfs(i):
            if i in vis:
                return vis[i]
            vis[i] = True
            for j in adj[i]:
                if dfs(j):
                    return True
            vis[i] = False
            x.append(i)
        
        for i in adj.keys():
            if dfs(i):
                return ""
        return ''.join(x)

        


        