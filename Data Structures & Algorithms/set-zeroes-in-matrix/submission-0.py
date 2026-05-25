class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rs = set()
        cs = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rs.add(i)
                    cs.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rs or j in cs:
                    matrix[i][j] = 0
        
        