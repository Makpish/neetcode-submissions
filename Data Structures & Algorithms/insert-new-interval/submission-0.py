class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i=0
        flag = 1
        while i<len(intervals):
            if flag and newInterval[0]<intervals[i][0]:
                res.append(newInterval)
                flag = 0
            res.append(intervals[i])
            i+=1
        
        if flag:
            res.append(newInterval)
        # print(res)
        
        newres = [res[0]]
        i=1
        while i < len(res):
            if res[i][0]>newres[-1][1]:
                newres.append(res[i])
            else:
                newres[-1][0] = min(res[i][0], newres[-1][0])
                newres[-1][1] = max(res[i][1], newres[-1][1])
            i+=1
        return newres
        
        

        