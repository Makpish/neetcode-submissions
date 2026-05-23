class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = {}#{i: [] for i in wordList}
        # adj[beginWord] = []
        wordList.append(beginWord)

        # def distance(a,b):
        #     l1 = [0] * 26
        #     l2 = [0] * 26

        #     for i in range(len(a)):
        #         l1[ord(a[i])-97]+=1
        #         l2[ord(b[i])-97]+=1
            
        #     c = 0
        #     for i in range(26):
        #         c += abs(l1[i] - l2[i])
            
        #     return c==2
        
        for i in wordList:
            for j in range(len(i)):
                p = i[:j] + "*" + i[j+1:]
                if p not in adj:
                    adj[p] = []
                adj[p].append(i)
        
        print(adj)

        q = deque([beginWord])
        res= 1
        vis = set()
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for j in range(len(w)):
                    p = w[:j] + "*" + w[j+1:]
                    for k in adj[p]:
                        if k not in vis:
                            vis.add(k)
                            q.append(k)
            res+=1
        return 0

        