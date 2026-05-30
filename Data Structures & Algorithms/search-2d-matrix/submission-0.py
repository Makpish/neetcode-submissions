class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1
        col = len(matrix[0])-1

        while l<r:
            m = (l+r)//2
            if matrix[m][col] == target:
                return True
            if matrix[m][col]<target:
                l=m+1
            else:
                r=m
        
        row = l
        l,r = 0,col

        while l<=r:
            m = (l+r)//2
            if matrix[row][m] == target:
                return True
            if matrix[row][m]>target:
                r=m-1
            else:
                l=m+1
        return False

        