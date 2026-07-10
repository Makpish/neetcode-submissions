class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ["()"]
        p = self.generateParenthesis(n-1)
        s=set()
        for i in p:
            s.add("(" + i + ")")
            for j in range(len(i)):
                s.add(i[:j] + "()" + i[j:])
        return list(s)
        