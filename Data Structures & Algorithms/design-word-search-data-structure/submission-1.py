class WordDictionary:

    def __init__(self):
        self.t = [False,{}]
        

    def addWord(self, word: str) -> None:
        t = self.t
        for i in range(len(word)):
            if word[i] not in t[1]:
                t[1][word[i]] = [False, {}]
            t = t[1][word[i]]
        t[0] = True
        

    def search(self, word: str) -> bool:
        def s(t,i):
            c = t
            for j in range(i,len(word)):
                x = word[j]
                if x == ".":
                    for n in c[1].keys():
                        if s(c[1][n],j+1):
                            return True
                    return False
                else:
                    if x not in c[1]:
                        return False
                    c = c[1][x]
            return c[0]
        return s(self.t, 0)


        
