class GameState:

  def __init__(self):
    '''
    TASK 1:
    Create/Initialize an 8x8 board by making 8 lists within 1 list (nested list), can just have the values as "--" for now

    Name of this property/attribute/member/variable should be "board"
    Hint: how do you reference a class' variable? maybe use self!
    '''

    
'''
TASK 2:
Create a new class called "Piece" with 2 extra parameters on top of self: color and board. 

We want the Piece to know what color it is to know who it can capture, and we want it to know the board as well so it knows where it can go and what other pieces are around.

Then initialize the properties:
"side" (this will be the same as the color of the piece)
"board" (the parameter board passed in)
"made_move" (this is going to be used later on to determine if this is the piece's first move, so for now, set it to False)
"name" (name of the piece, but within the Piece class, we can set this to anything (you can use "--"))

In addition, create a function called "print_name" that will return the piece's name
'''

'''
TASK 3:
Create a new class for each specific chess piece
i.e. 
Pawn
Rook
Knight
Bishop
Queen
King

It should inherit the properties of class "Piece". Refer to the slides or search class inheritance for how to do this. Hint: it is done in the parameters of the class.

Additionally, the specific piece has its own init, which has the same parameters as Piece.

Within this init, initialize the property: name which is the name of the specific piece

For formatting purposes, we recommend but not mandatory to name your pieces as such:

Pawn = PN
Rook = RK
Knight = KT
Bishop = BP
Queen = QN
King = KG


Each chess piece has a function method caled: valid_move
Valid move has 5 parameters:
self
fr_row
fr_col
to_row
to_col
We will be implementing the movement functionality the following week, but create the functions for now and it can just return without doing anything
'''


'''
TASK 4:
Let's go back into the GameState class to begin setting up our board.
The first thing we want to do is use all of the above classes to construct our rows of pieces. One way to approach this is to create the 4 rows of ordered pieces outside of our board array and then assign them into our board array.
By the end of this task, if you use the GameState.print_board() function (don't forget to initialize a new GameState) you should get:

RK KT BP QN KG BP KT RK 
PN PN PN PN PN PN PN PN 
-- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- 
PN PN PN PN PN PN PN PN 
RK KT BP KG QN BP KT RK 
'''