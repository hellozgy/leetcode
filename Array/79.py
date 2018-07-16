class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board)==0:return False
        state = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    state[i][j]=1
                    tag = self.find(board, i, j, word, 1, [[i, j]], state)
                    if tag:return True
        return False
                    
    def find(self, data, x, y, word, index, stack, state):
        if index==len(word):return True
        if x-1>=0 and state[x-1][y]==0 and data[x-1][y]==word[index]:
            state[x-1][y]=1
            stack.append([x-1,y])
            tag = self.find(data, x-1, y, word, index+1, stack, state)
            if tag:return True
        if x+1<len(data) and state[x+1][y]==0 and data[x+1][y]==word[index]:
            state[x+1][y]=1
            stack.append([x+1,y])
            tag = self.find(data, x+1, y, word, index+1, stack, state)
            if tag:return True
        if y-1>=0 and state[x][y-1]==0 and data[x][y-1]==word[index]:
            state[x][y-1]=1
            stack.append([x,y-1])
            tag = self.find(data, x, y-1, word, index+1, stack, state)
            if tag:return True
        if y+1<len(data[0]) and state[x][y+1]==0 and data[x][y+1]==word[index]:
            state[x][y+1]=1
            stack.append([x,y+1])
            tag = self.find(data, x, y+1, word, index+1, stack, state)
            if tag:return True
        
        if len(stack)==0:return False
        last = stack.pop()
        state[last[0]][last[1]]=0
            
board =[["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
so = Solution()
print(so.exist(board, word))
        