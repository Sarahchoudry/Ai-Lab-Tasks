#!/usr/bin/env python
# coding: utf-8

# In[14]:


import math
class TicTacToe:
    def __init__(self):
        self.board = [
            [0, 0, 0], 
            [0, 0, 0],
            [0, 0, 0]
        ]
    def is_winner(self, player):
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]) or all([self.board[j][i] == player for j in range(3)]):
                return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def is_full(self):
        return all(self.board[i][j] != 0 for i in range(3) for j in range(3))
    
    def evaluate_board(self):
        if self.is_winner(1): 
            return 10
        if self.is_winner(-1): 
            return -10
        return 0  
    def minimax(self, depth, is_maximizing):
        score = self.evaluate_board()
        if score == 10 or score == -10:
            return score - depth if score == 10 else depth - 10
        if self.is_full():
            return 0
        
        if is_maximizing:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == 0:
                        self.board[i][j] = 1 
                        best_score = max(best_score, self.minimax(depth + 1, False))
                        self.board[i][j] = 0
            return best_score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == 0:
                        self.board[i][j] = -1
                        best_score = min(best_score, self.minimax(depth + 1, True))
                        self.board[i][j] = 0
            return best_score
    
    def get_best_move(self):
        best_value = -math.inf
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0: 
                    self.board[i][j] = 1 
                    move_value = self.minimax(0, False)
                    self.board[i][j] = 0  
                    if move_value > best_value:
                        best_value = move_value
                        best_move = (i, j)
        return best_move

game = TicTacToe()
game.board = [
    [1, -1, 1],
    [0, -1, 0],
    [1, 0, 0]
] 
best_move = game.get_best_move()
print(f"Best move for AI: Row {best_move[0]}, Column {best_move[1]}")


# In[ ]:





# In[ ]:





# In[ ]:




