class PrefixTree:
    class Node:
        def __init__(self, e):
            self.e = e
            self.n = {}

    def __init__(self):
        self.t = self.Node(False)
        

    def insert(self, word: str) -> None:
        t = self.t
        for i in range(len(word)):
            if word[i] not in t.n:
                t.n[word[i]] = self.Node(False)
            t = t.n[word[i]]
            if i==len(word)-1:
                t.e = True


    def search(self, word: str) -> bool:
        t = self.t
        for i in range(len(word)):
            # print("search",t.n)
            if word[i] not in t.n:
                return False
            t = t.n[word[i]]
            if i==len(word)-1:
                return t.e
        return False
        

    def startsWith(self, prefix: str) -> bool:
        t = self.t
        for i in range(len(prefix)):
            # print("startsWith",t.n)
            if prefix[i] not in t.n:
                return False
            t = t.n[prefix[i]]
        return True
        
        