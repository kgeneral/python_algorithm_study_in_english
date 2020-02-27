# https://leetcode.com/problems/game-of-life/submissions/
# elapsed time : 44 min
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nextState = {}
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                neighbors = sum(self.neighbors(board, i, j))
                if board[i][j] == 1:
                    if neighbors < 2: nextState[(i,j)] = 0
                    elif neighbors > 3: nextState[(i,j)] = 0
                else:
                    if neighbors == 3: nextState[(i,j)] = 1
        
        for coord in nextState:
            board[coord[0]][coord[1]] = nextState[coord]
   

    def neighbors(self, board, i, j):
        m = len(board)
        n = len(board[0])
        adj=[]
        
        for it1 in range(max(i-1,0), min(i+2,m)):
            for it2 in range(max(j-1,0), min(j+2,n)):
                if it1==i and it2==j: continue
                adj.append(board[it1][it2])
        
        return adj
