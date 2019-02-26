from random import randint

# creatin a 5X5 board

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)


#Hidding a battleship

def random_row(board):
  return randint(1, len(board))

def random_col(board):
  return randint(1, len(board[0]) )

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col


#Gameplay

for turn in range(4):
  print "Turn", turn + 1
  #user input
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  #win
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break

  #out of range
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."

    #attempt to check same coordinates
    elif board[guess_row - 1][guess_col -1] == "X":
      print( "You guessed that one already." )

    #missed / try again
    else:
      print "You missed my battleship!"
      board[guess_row -1][guess_col-1] = "X"
    print_board(board)

  #game over
  if turn == 3:
    print "Game Over"
