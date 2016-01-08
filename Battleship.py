# import the random integer generator
from random import randint

#------Functions to setup/update the board ------#

# functions to generate the position of the battleships
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# a function for printing the board
def print_board(board):
    for row in board:
        print " ".join(row)
   
# a function to clear the screen
def clear_screen():
    print ("\n" * 50)

# a function that checks if coordinate input is valid
def valid_coordinate_input(coord_input):
    for numbers in valid_inputs:
        if coord_input == numbers:
            return True
    return False
    
# a function to check if the number of ships is valid
def check_ship_num(num):
    for numbers in valid_ship_num:
        if num == numbers:
            return True
    return False
    
# a function to check if a ship is hit by player 2
def check_if_hit_player1(coordinate):
    if player1_ships.count(coordinate) == 1:
            return True
    return False
    
# a function to check if a ship is hit by player 1
def check_if_hit_player2(coordinate):
    if player2_ships.count(coordinate) == 1:
            return True
    return False

#------Setting up the initial board ------#
# start with an empty board variable
board = []
board2 = []
player1_ships = []
player2_ships = []
valid_inputs = ["1", "2", "3", "4", "5", "6"]
valid_ship_num = ["1", "2", "3", "4"]

# fill in the board with intial O
for x in range(6):
    board.append(["O"] * 6)
    board2.append(["O"] * 6)

# print opening statment for the game
print "Let's play Battleship!"
print "Type 'quit' to gave up when asked if you're ready \n"

num_ship = raw_input("How many ships do you want to play with up to 4: ")
while check_ship_num(num_ship) == False:
    num_ship = raw_input("Please enter valid number of ships 1, 2, 3, or 4: ")
num_ship = int(num_ship)

# store the rows and cols for the battleships
for ship_num in range(num_ship):
    ship_row = random_row(board)
    ship_col = random_col(board)
    ship_coord = [ship_row, ship_col]
    while player1_ships.count(ship_coord) != 0:
        ship_row = random_row(board)
        ship_col = random_col(board)
        ship_coord = [ship_row, ship_col]
    player1_ships.append(ship_coord)
    
    ship2_row = random_row(board2)
    ship2_col = random_col(board2)
    ship2_coord = [ship2_row, ship2_col]
    while player2_ships.count(ship2_coord) != 0:
        ship2_row = random_row(board2)
        ship2_col = random_col(board2)
        ship2_coord = [ship2_row, ship2_col]
    player2_ships.append(ship2_coord)

print player1_ships
print player2_ships
print "\n"
#------ The Games Begin, Good Luck------#
for turn in range(37):
    # Asking if player 1 is ready to play
    is_ready = raw_input("Are you ready, Player 1? y or n: ")
    if is_ready == "quit":
        print "Player 1 gave up. Player 2 is the winner!"
        break
    while is_ready != "y":
        is_ready = raw_input("Are you ready now, Player 1? y or n: ")
    clear_screen()
    
    # Starts player1's turn
    print "Turn ", turn + 1
    print "Player 1 Turn:"
    print " "
    print_board(board)
    # Prompts player 1 to choice a coordinate to attack
    guess_row = raw_input("Guess Row:")
    while valid_coordinate_input(guess_row) == False:
        guess_row = raw_input("Please enter a valid Row Coordinate: ")
    guess_col = raw_input("Guess Col:")
    while valid_coordinate_input(guess_col) == False:
        guess_col = raw_input("Please enter a valid Column Coordinate: ")

    guess_row = int(guess_row) - 1
    guess_col = int(guess_col) - 1
    guess_coord = [guess_row, guess_col]
    # Checks if player 1 hit anything
    if check_if_hit_player2(guess_coord) == True:
        player2_ships.remove(guess_coord)
        if len(player2_ships) == 0:
            print "Congratulations! You sunk Player2's battleship!"
            print "Player1 is the winner!"
            break
        else:
            print "\n"
            print "You sunk one of Player2's ship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print "\n"
            print "Oops, that's not even in the ocean."
        elif (board[guess_row][guess_col] == "*"):
            print "You guessed that coordinate already."
        elif (board[guess_row][guess_col] == "X"):
            print "\n"
            print "You have already hit the ship there."
        else:
            print "\n"
            print "You missed Player2's battleships!"
            board[guess_row][guess_col] = "*"
            print_board(board)
            print " "
    # Asks if player 2 is ready
    is_ready = raw_input("Are you ready, Player 2? y or n: ")
    if is_ready == "quit":
        print "Player 2 gave up. Player 1 is the winner!"
        break
    while is_ready != "y":
        is_ready = raw_input("Are you ready now, Player 2? y or n: ")
    
    # starts player2's turn    
    clear_screen()
    print "Turn ", turn + 1
    print "Player 2 Turn:"
    print " "
    print_board(board2)
    # Prompts player 2 to choice coordinate to attack
    guess2_row = raw_input("Guess Row:")
    while valid_coordinate_input(guess2_row) == False:
        guess2_row = raw_input("Please enter a valid Row Coordinate: ")
    guess2_col = raw_input("Guess Col:")
    while valid_coordinate_input(guess2_col) == False:
        guess2_col = raw_input("Please enter a valid Column Coordinate: ")

    guess2_row = int(guess2_row) - 1
    guess2_col = int(guess2_col) - 1
    guess_coord = [guess2_row, guess2_col]
    
    # Checks if player 2 hit anything
    if check_if_hit_player1(guess_coord) == True:
        player1_ships.remove(guess_coord)
        if len(player1_ships) == 0:
            print "Congratulations! You sunk Player1's battleship!"
            print "Player2 is the winner!"
            break
        else:
            print "\n"
            print "You sunk one of Player1's ship!"
            board2[guess2_row][guess2_col] = "X"
            print_board(board2)   
    else:
        if (guess2_row < 0 or guess2_row > 5) or (guess2_col < 0 or guess2_col > 5):
            print "\n"
            print "Oops, that's not even in the ocean."
        elif(board2[guess2_row][guess2_col] == "*"):
            print "\n"
            print "You guessed that one already."
        elif (board2[guess2_row][guess2_col] == "X"):
            print "\n"
            print "You have already hit the ship there."
        else:
            print "\n"
            print "You missed Player1's battleship!"
            board2[guess2_row][guess2_col] = "*"
            print_board(board2)
            print " "
            
        if turn == 36:
            print "Game Over "