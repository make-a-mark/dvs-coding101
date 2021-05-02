''' 
Before you begin week 2 tasks, replace your print_board with our new one attached below:
'''

def print_board(self):
  print("   A  B  C  D  E  F  G  H")
  counter = 8
  for row in range(len(self.board)):
    print(str(counter), end=' ')
    for column in range(len(self.board)):
      piece = self.board[row][column]
      if (piece == "--"):
        print ("--", end=' ')
      else:
        print(piece.print_name(), end=' ')
    print(str(counter) + " ")
    counter -= 1
  print("   A  B  C  D  E  F  G  H")

'''
TASK 1: Movement 
We will now be working on movement! Within the class Gamestate, Create a function called move with the parameters:
self
start_square
end_square

start_square and end square should both be strings of length 2 where the first character is a letter from a-h (file/column of sqaure) and the second character is a number from 1-8 (row of the square).

Refer to the link below for square names.
https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/SCD_algebraic_notation.svg/1200px-SCD_algebraic_notation.svg.png

For now, lets assume that these parameters are in the correct format. Below we defined a dictionary which maps the file to the corresponding index in a row and the row to the corresponding index in the board. 
Your job is to change the gamestate/board to move the piece on start_square to the given end_square.

Hints: store a piece using avariable? what happens to the square that the piece started on?


'''

#file_index = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
#row_index = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0}

'''
TASK 2:
We now need to include some checks within our move function. The checks are:
- If someone inputs more or less characters than necessary (eg: ab2 to ab4)
- If someone inputs characters outside of the actual squares on our board (eg: m99 to z50)
- If someone tries to move from a square that is empty (no piece on the square)
- If it is not the side's turn

For each of the checks, if they are invalid, return False so that the program does not make an invalid move.
'''


'''
TASK 3: Interactivity
We are now going to create a way to accept user input and make moves. 

Create a start_game function at the bottom of GameState that takes in parameter just self. It will ask for user input and then take that input and plug it into move. (use "input()" and the function split() may be helpful) Then we want to reprint the board to see if the correct move was made. For now, we can just have this function loop infinitely (even if a user wins). 

At the bottom of your repl create a main function with no parameters that just instantiates a GameState, then call main(). 

'''