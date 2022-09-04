class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(0,(n+1)//2):
            for j in range(0,n//2):
                temp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp
        return matrix

ans = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(ans.rotate(matrix))