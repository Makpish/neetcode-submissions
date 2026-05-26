class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws = set()
        ms = 0
        for i in wordDict:
            ws.add(i)
            ms = max(ms, len(i))
        ms = [ms]
        dp = {"": True}

        def dfs(so):
            # print(so)
            if so in dp:
                return dp[so]
            dp[so] = False
            for i in range(1,min(len(so), ms[0])+1):
                # print(so[:i])
                if so[:i] in ws and dfs(so[i:]):
                    dp[so] = True
                    break
            return dp[so]

        return dfs(s)