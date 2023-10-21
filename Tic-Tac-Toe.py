#importing necessary modules: tkinter for GUI and random for the computer movement on the board

import tkinter as tk
from tkinter import messagebox
import random

#declare functions

def winner(board,player):
    """
    :param board: receives the current board(the matrix where X and 0 will appear) which may be empty,partially occupied or full
    :param player: receives the current player, whether it is the user or the computer)
    :return: True if any of the players won: a row/column/one of the diagonals has all elements equal), False otherwise
    """
    for i in range(3):
        if all(board[i][j]==player for j in range(3)) or all(board[j][i]==player for j in range(3)):
            return True
    return all(board[i][i]==player for i in range(3)) or all(board[i][2-i]==player for i in range(3))

def full(board):
    """
    :param board: receives the current board(the matrix where X and 0 will appear) which may be empty,partially occupied or full
    :return: True if all the cells in the board are occupied, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell=="":
                return False
    return True

def computer_choice(board):
    """
    This functions gives the positions of O on the board.
    :param board: receives the current board(the matrix where X and 0 will appear) which may be empty,partially occupied or full
    :return: a random position out of the ones that are not occupied, where 0 will appear from now on. The position is randomly selected using the random.choice() method.
    """
    available=[]
    for r in range(3):
        for c in range(3):
            if board[r][c]=="":
                available.append((r,c))
    return random.choice(available)

#creating a class for the GUI

class TicTacToeGUI:
    def __init__(self,root):
        """
        This function initializes the tkinter frame and buttons for each cell.
        """
        self.root=root
        self.root.title("Tic-Tac-Toe")
        tk.messagebox.showinfo("Welcome", f"Welcome to Tic-Tac-Toe\nYour fighter:X\n!!GAME ON!!")
        self.board=[["" for _ in range(3)]for _ in range(3)]
        self.user="X"
        self.current_player=self.user
        self.buttons=[[None for _ in range(3)]for _ in range(3)]
        for i in range(3):
            for j in range(3):
                #each button press enables the function self.make_move(row,col) that tries to put an X/0 on the board in the row and column(col) given.
                self.buttons[i][j]=tk.Button(root,text="",width=10,height=3,bg="white",command=lambda row=i, col=j: self.make_move(row,col))
                self.buttons[i][j].grid(row=i,column=j)
    def make_move(self,row,col):
        """
        :param row: receives the row where the user/computer tries to put an X/0
        :param col: receives the column where the user/computer tries to put an X/0
        :return: this function "populates" the board with X and 0`s on the positions chosen, where possible.
        """
        if self.board[row][col]=="" and winner(self.board,self.current_player)==False:
            self.board[row][col]=self.current_player
            if self.current_player=="X":
                # the button & board cell that is now occupied will have a new content(text=the player that chose that cell) and a new colour depending on the player that occupies the cell.
                self.buttons[row][col].config(text=self.current_player, bg="lightblue")
            else:self.buttons[row][col].config(text=self.current_player,bg="lightgreen")
            if winner(self.board,self.current_player)==True:
                self.printwinner(self.current_player)
                #game ended, current player won
            elif full(self.board):
                self.tie()
                #game ended with a tie
            else:
                #changing the player and asking the computer to make a move
                if self.current_player=="0":
                    self.current_player="X"
                else: self.current_player="0"
                if self.current_player!=self.user:
                    self.computer_choice()

    def computer_choice(self):
        """
        This function calls the computer_choice functioned declared previously and then calls the self.make_move function that adds an 0 element on the board.
        """
        row,col=computer_choice(self.board)
        self.make_move(row,col)

    def printwinner(self,player):
        """
        :param player: the winning player(user/computer)
        :return: a message announcing the winner of the game that just ended
        """
        tk.messagebox.showinfo("Game Over",f"\n Player {player} wins!")
        self.reset_board()

    def tie(self):
        """
        :return: a message announcing the game ended in a draw/tie
        """
        tk.messagebox.showinfo("Game Over","\n It`s a tie!")
        self.reset_board()
    def reset_board(self):
        """
        This function cleans the board, emptying it of the previous elements and also restarts the buttons representing each cell of the board
        """
        self.board=[["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="",bg="white")
        self.current_player=self.user

if __name__=="__main__":
    #initialising the GUI
    root=tk.Tk()
    app=TicTacToeGUI(root)
    root.mainloop()











