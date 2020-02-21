class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        result = [[0 for i in range(n)] for j in range(m)]
        
        hasChanges = True
        while hasChanges:
            hasChanges = False
            for i in range(m):
                for j in range(n):
                    if matrix[i][j]==0: 
                        continue
                    minAdjacentDist = min(self.adjacents(matrix, i, j))
                    #print(i, j, matrix[i][j], minAdjacentDist)
                    if matrix[i][j] <= minAdjacentDist:
                        hasChanges = True
                        matrix[i][j] = minAdjacentDist + 1
        
        return matrix
                
    def adjacents(self, grid, i, j):
        m=len(grid)
        n=len(grid[0])
        
        adjacents = []
        if i>0: adjacents.append(grid[i-1][j])
        if i<m-1: adjacents.append(grid[i+1][j])
        if j>0: adjacents.append(grid[i][j-1])
        if j<n-1: adjacents.append(grid[i][j+1])
            
        return adjacents
