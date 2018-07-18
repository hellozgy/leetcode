class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1) and board[i][j]=='O':
                    self.f(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='A':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'

    def f(self, board, i, j):
        if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]=='O':
            board[i][j]='A'
            self.f(board, i-1, j)
            self.f(board, i+1, j)
            self.f(board, i, j-1)
            self.f(board, i, j+1)

