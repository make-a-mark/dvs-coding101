
#**Put these two functions in your Piece class, make sure to indent properly**
def find_direction_NWSE(self, fr_row, fr_col, to_row, to_col):
    if (fr_row - to_row == 0) or (fr_col - to_col == 0):
      if (fr_col > to_col):
        #moving left
        return "Left"
      if (to_col > fr_col):
        #moving right
        return "Right"
      
      if (fr_row > to_row):
        #moving down
        return "Down"
      if (to_row > fr_row):
        #moving Up
        return "Up"

def are_pieces_between_DIG(self, start, end, dir):
  if dir == "Left Down":
    sq = start
    sq[0] += 1
    sq[1] -= 1
    while (sq != end):
      if GameState.get_piece(self, sq[0], sq[1]) != "--":
        return False
      sq[0] += 1
      sq[1] -= 1
    return True
  elif dir == "Left Up":
    sq = start
    sq[0] -= 1
    sq[1] -= 1
    while (sq != end):
      if GameState.get_piece(self, sq[0], sq[1]) != "--":
        return False
      sq[0] -= 1
      sq[1] -= 1
    return True
  elif dir == "Right Down":
    sq = start
    sq[0] += 1
    sq[1] += 1
    while (sq != end):
      if GameState.get_piece(self, sq[0], sq[1]) != "--":
        return False
      sq[0] += 1
      sq[1] += 1
    return True
  elif dir == "Right Up":
    sq = start
    sq[0] -= 1
    sq[1] += 1
    while (sq != end):
      if GameState.get_piece(self, sq[0], sq[1]) != "--":
        return False
      sq[0] -= 1
      sq[1] += 1
    return True
  else:
    return False

#This is the entire Pawn Class, for the sake of time, we gave it to you
class Pawn(Piece):
  def __init__(self, color, board):
    super().__init__(color, board)
    self.name = "PN"


  def is_attack(self, col_dif, row_dif, to_piece):
    # using abs because of different colors.
    if abs(col_dif) != 1:
      return False
    # attack is always a single diagonal move where diff_row and col is 1
    elif abs(row_dif) != 1:
      return False
    # cannot attack an empty sqaure
    elif to_piece == "--":
      return False
    # cannot attack your own team
    elif to_piece.side == self.side:
      return False
    else:
      return True
      
    
  def correct_direction(self, row_dif):
    #Not vertical movement
    if (row_dif == 0):
      return False
    # black piece moiving up the board
    elif (row_dif > 0 and self.side == "black"):
      return True
    #white piece moving down the board
    elif (row_dif < 0 and self.side == "white"):
      return True
    else:
      return False

    
  def valid_move(self, fr_row, fr_col, to_row, to_col):
    col_dif = (to_col - fr_col)
    row_dif = (to_row - fr_row)
    to_piece = self.board[to_row][to_col]



    #make sure pawns move in the correct direction
    if not(self.correct_direction(row_dif)):
      print("Pawn does not move that way")
      return False

    #srefer to is_attack function
    if self.is_attack(col_dif, row_dif, to_piece):
      return True

    #Standard single column move
    if to_piece == "--" and abs(row_dif) == 1 and col_dif == 0:
      return True

    #First move
    if (abs(row_dif) == 2 and not self.made_move):
      int_square = None
      direction = self.find_direction_NWSE(fr_row, fr_col, to_row, to_col)
      return self.are_pieces_between_NWSE([fr_row, fr_col], [to_row, to_col], direction)
      if (self.side == "black"):
        int_square = self.board[to_row + 1][to_col]
      else:
        int_square = self.board[to_row - 1][to_col]
      if int_square == "--" and to_piece == "--":
        return True
    else:
      return False
    return True



'''
Tasks Begin Here:

Task #1: Checking if path is clear.

We gave you the implementation of find_direction_DIG. Well that is for diagnol movements, we need something for the pieces that only move in non-diagnol directions (Left, Right, Up, Down). The code should look very similar to the one we have provided.

'''


'''
Task #2: Determining the direction for diagnol movement!

Some pieces (Bishop & Queen) move in a diagnol direction (Left up/down, Right up/down) and we need to determine that direction. Using the starting row/col and end row/col make a function that will return a string with the direction the piece is moving. (Hint: Look at find_direction_NWSE!)
'''

'''
Task #3: King Movement
The King moves pretty freely compared to other pieces, it can move in any direction as long as it is one space away. And due to this, we won't even need to check if pieces are between because it is only a space away. So the only thing that needs to be done here is implement a function ("one_square_away") that just checks to make sure that the king is in fact moving one square away from its original spot in any direction. We will then check if it is attacking a piece of its own in valid_move.

In the King's valid_move, all we need to do is check if the square that the king is moving to has a piece of the same color. For example, if the White King moves forward one but there is a White Pawn there, then that is an invalid move.

Hint: Use GameState.get_piece(self, row, col).side to get the color piece that is there. However, if the space is empty, you can't get it's side therefore it will error. How can you get around this? (Hint within a hint: if the space is empty, lets set its side to something other than Black or White)
'''


'''
Task #4: Rook Valid Move

Now that you have all the code for directional movement as well as pieces in between, the valid_move function for these piece should be very, simple (two lines of code). All you need to do here is get the direction and then check if they're are pieces in between in that direction. 
'''


'''
Task #5: Implmenting Bishop and Queen

Now that you have written the code to check for directional movement as well as if pieces are between, the valid_move function for these two pieces should be very simple (ours was 2 for bishop and 3 for queen). All you need to do here is get the direction the piece is moving, then check if there are pieces in between in that direction.
'''


''' 
Task #6: Implmenting the Knight

At first, this may seem like a difficult task because of the "different" way that the knight moves but it turns out to be a lot simpler than you think. The knight moves in an L pattern (if you are not familiar: https://www.masterclass.com/articles/what-is-the-knight-in-chess#how-do-knights-move)
Read this part closely because it breaks down exactly what you should be checking for to ensure a knight is moving in an L shape. (Hint: It'll always be 2 in one way and 1 in the other)

Since the knight can jump over other pieces, we won't need to check if there are pieces in the way, the only other thing that needs to be done is ensure that the knight isn't landing on a piece of its own color. (Hint: GameState.get_piece(self, row, col) will return the Piece object and adding .side to the end of it returns the color, however, don't forget that an empty square can't return a color to you and will error, how can you get around this?)
'''