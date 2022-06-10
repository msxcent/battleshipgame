import random
import os
# dictionary for ships:
ships = {'A': 5, 'B': 4, 'C': 3, 'S': 3, 'D': 2}
decorator = 'X'

# Checks if ships are completely hit
player_miss = 0
player_hit = 0

opponent_hit = 0
opponent_miss = 0


def p_miss_tracker():
	global player_miss
	player_miss += 1

def p_hit_tracker():
	global player_hit
	player_hit += 1   


def display_num_pmiss_phit(v_board):
    print('\033[1;33mCOMPUTER BOARD: \033[0m')
    print('-------------------------------------------')
    print_v_board(v_board)
    print('-------------------------------------------')
    print('Move Summary')
    print('Hits: ' , player_hit, ' / 17')  
    print('Miss: ' , player_miss)

def c_miss_tracker():
	global opponent_miss
	opponent_miss += 1

def c_hit_tracker():
	global opponent_hit
	opponent_hit += 1  
  
def display_num_cmiss_chit(p_board):
    print('\033[1;33mPLAYER BOARD: \033[0m')
    print('-------------------------------------------')
    print_p_board(p_board)
    print('-------------------------------------------')
    print('Move Summary')
    print('Hits: ' , opponent_hit, ' / 17')  
    print('Miss: ' , opponent_miss)
    
def check_player_win():
    if player_hit == 17:
        print(' ')
        print("\033[1;33mCongratulations!!\033[0m")
        print("\033[1;33mYou Won the Battleship Game!\033[0m")
        print(' ')
        input("Press Enter to Continue...")
        os.system('clear')
        play_again()
        
def check_opponent_win():
    if opponent_hit == 17:
        print(' ')
        print("\033[1;33mOh No! You Lost.\033[0m")
        print("\033[1;33mThe Computer has won the Battleship Game!\033[0m")
        print(' ')
        input("Press Enter to Continue...")
        os.system('clear')
        play_again()
        
    

def computer_choose_board():
    # Premade boards for computer
    board1 = [['A', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' '], ['A', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' '],
              ['A', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' '], ['A', ' ', ' ', 'C', 'C', 'C', ' ', ' ', ' ', ' '],
              ['A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', 'D', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'D', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['B', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ']]

    board2 = [[' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', 'D'], [' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', 'D'],
              [' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' '], ['S', 'S', 'S', ' ', ' ', 'C', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' '],
              ['B', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    board3 = [['C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', 'A', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' '], [' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', 'A', ' '],
              [' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', 'A', ' '], ['B', 'B', 'B', 'B', ' ', 'S', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'D', 'D', ' ']]

    board4 = [['B', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', 'C'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C'],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C'], [' ', ' ', 'D', 'D', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' '],
              ['S', 'S', 'S', ' ', ' ', ' ', 'A', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ']]

    board5 = [[' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', 'A', ' '], [' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', 'A', ' '],
              [' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', 'A', ' '], [' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', 'A', ' '],
              [' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', 'A', ' '], [' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', 'D', 'D', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['B', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    board6 = [[' ', 'A', ' ', ' ', ' ', ' ', ' ', 'S', 'S', 'S'], [' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', 'D', ' '], [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', 'D', ' '],
              [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' '], ['B', 'B', 'B', 'B', ' ', 'C', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Computer choose board
    x = random.randint(1, 6)

    if x == 1:
        board = board1
    elif x == 2:
        board = board2
    elif x == 3:
        board = board3
    elif x == 4:
        board = board4
    elif x == 5:
        board = board5
    elif x == 6:
        board = board6
    return board


board = computer_choose_board()
computer_choose_board


# Print board only for development testing
def print_board(board):
    # Print labels
    column_numbers = '0123456789'
    print('   |' + ' | '.join(column_numbers) + ' | ')
    for number, row in enumerate(board):
        print(number, '| ' + ' | '.join(row) + ' |')


# Visual board for Player
def visual_board():
    v_board = []
    for row in range(10):
        row = []
        for col in range(10):
            row.append(' ')
        v_board.append(row)
    return v_board


v_board = visual_board()


# Print Visual board for Player
def print_v_board(v_board):
    # Print labels
    column_numbers = '0123456789'
    print('   |' + ' | '.join(column_numbers) + ' | ')
    for number, row in enumerate(v_board):
        print(number, '| ' + ' | '.join(row) + ' |')


def player_board():
    p_board = []
    for row in range(10):
        row = []
        for col in range(10):
            row.append(' ')
        p_board.append(row)
    return p_board
p_board = player_board()


# Print Visual board for Player
def print_p_board(p_board):
    #Print labels
    column_numbers = '0123456789'
    print('   |' + ' | ' .join(column_numbers) + ' | ')
    for number, row in enumerate(p_board):
        print(number, '| ' + ' | '.join(row) + ' |')


# Player place ships
def p_place_ships(p_board, ships):
    ship_names = ['Aircraft Carrier Ship ( 5 squares )', 'Battleship ( 4 squares )', 'Cruiser ( 3 squares )', 'Submarine ( 3 squares )', 'Destroyer ( 2 squares )']
    i=0
    for key,value in ships.items():
        ship_not_placed = True
        while ship_not_placed:
            try:
                print("\033[93;36m \n! Note that you only need to input the location of the first square ! \033[0m")
                print("\033[93;36m!    The program will automatically add the rest of the squares     ! \033[0m ")
                print(' ')
                print_p_board(p_board)
                print(' ')
                print('\033[1;33mPlace your ', ship_names[i],'\033[0m')
                i = i+1
                x = int(input('Enter First Square row: '))
                y = int(input('Enter First Square column: ' ))
                ori = input('Please enter orientation [H][V] : ')
                
                for ship in range(value):
                    if x <= 9 and y <= 9:
                    
                        if ori.upper() == 'V':
                            if p_board[x+ship][y]  == ' ' :
                                p_board[x+ship][y] = key
                                ship_not_placed = False
                                
                        elif ori.upper() == 'H':
                            if p_board[x][y+ship] == ' ':
                                p_board[x][y+ship] = key 
                                ship_not_placed = False  
                      
                    else:
                        raise IndexError
                        
            except (IndexError,ValueError):
                i = i-1
                print(' ')
                print(' ')
                print('\033[31mInvalid Input. Try Again.\033[0m')
                print(' ')
                print(' ')
                input('Press enter to continue...')
                os.system('clear')
                ship_not_placed = True
        
        ship_not_placed = True
        os.system('clear')

# Player guess ships placement
def p_guess(board, v_board):
    play_guess = True
    while play_guess:
        try:
            print("\033[31m! Please strictly input values ranging from 0-9 only to avoid error !\033[0m")
            print(' ')
            print('\033[1;33mCOMPUTER BOARD: \033[0m')
            print('-------------------------------------------')
            print_v_board(v_board)
            print('-------------------------------------------')
            print(' ')
            print('\033[1;33mPLAYER TURN \033[0m')
            x = int(input('Guess ROW    [0-9]: '))
            y = int(input('Guess COLUMN [0-9]: '))
            #print('-------------------------------------------')
        
            # MISS
            if board[x][y] == ' ':
                p_miss_tracker()
                print(' ')
                print('\033[31mYou missed!\033[0m')
                print(' ')
                print(' ')
                input("Press Enter to Continue...")
                os.system('clear')
                v_board[x][y] = 'O'
                display_num_pmiss_phit(v_board)
                play_guess = False
                print(' ')
                print('\033[1;33mOpponents Turn\033[0m')
                input("Press Enter to Continue...")
                os.system('clear')
                c_guess(p_board)
                
                
            # HIT
            elif board[x][y] == 'A':
                p_hit_tracker()
                print(' ')
                print('\033[33mYou hit a ship!\033[0m')
                board[x][y] = 'X'
                v_board[x][y] = '\u03BB'
                check_player_win()
                play_guess = True
                print(' ')
                print(' ')
                input("Press Enter to Continue...")
                os.system('clear')
                
                    
            elif board[x][y] == 'B':
                p_hit_tracker()
                print(' ')
                print('\033[33mYou hit a ship!\033[0m')
                board[x][y] = 'X'
                v_board[x][y] = '\u03B2'
                check_player_win()
                play_guess = True
                print(' ')
                print(' ')
                input("Press Enter to Continue...")
                os.system('clear')
                
                    
            elif board[x][y] == 'C':
                p_hit_tracker()
                print(' ')
                print('\033[33mYou hit a ship!\033[0m')
                board[x][y] = 'X'
                v_board[x][y] = '\u0398'
                check_player_win()
                play_guess = True
                print(' ')
                print(' ')
                input("Press Enter to Continue...")
                os.system('clear')
                
            elif board[x][y] == 'D':
                p_hit_tracker()
                print(' ')
                print('\033[33mYou hit a ship!\033[0m')
                board[x][y] = 'X'
                v_board[x][y] = '\u0394'
                check_player_win()
                play_guess = True
                print(' ')
                print(' ')
                input("Press Enter to Continue...")
                os.system('clear')

            elif board[x][y] == 'S':
                p_hit_tracker()
                print(' ')
                print('\033[33mYou hit a ship!\033[0m')
                board[x][y] = 'X'
                v_board[x][y] = '\u03B6'
                check_player_win()
                play_guess = True
                print(' ')
                print(' ')
                input("Press Enter to Continue...")
                os.system('clear')
        
        except (IndexError,KeyboardInterrupt,ValueError):
            print(' ')
            print(' ')
            print('\033[31mInvalid Input. Try again.\033[0m')
            print(' ')
            print(' ')
            input("Press Enter to continue...")
            os.system('clear')
            play_guess = True
            
    # play_guess = True


# Computer guess ship placement
def c_guess(p_board):
    comp_guess = True
    while comp_guess:
        print('\033[1;33mPLAYER BOARD: \033[0m')
        print('-------------------------------------------')
        print_p_board(p_board)
        print('-------------------------------------------')
        print('\033[1;33mCOMPUTER TURN \033[0m')
        print(' ')
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if p_board[x][y] == 'A':
            c_hit_tracker()
            print('\033[31mYour Opponent hit your Airship!\033[0m')
            print(' ')
            print(' ')
            p_board[x][y] = 'X'
            check_opponent_win()
            input("Press Enter to Continue...")
            os.system('clear')
            comp_guess = True
            

        elif p_board[x][y] == 'B':
            c_hit_tracker()
            print('\033[31mYour Opponent hit your Battleship!\033[0m')
            print(' ')
            print(' ')
            p_board[x][y] = 'X'
            check_opponent_win()
            input("Press Enter to Continue...")
            os.system('clear')
            comp_guess = True
            

        elif p_board[x][y] == 'C':
            c_hit_tracker()
            print('\033[31mThe Computer hit your Carrier!\033[0m')
            print(' ')
            print(' ')
            p_board[x][y] = 'X'
            check_opponent_win()
            input("Press Enter to Continue...")
            os.system('clear')
            comp_guess = True
            

        elif p_board[x][y] == 'S':
            c_hit_tracker()
            print('\033[31mThe Computer hit your Submarine!\033[0m')
            print(' ')
            print(' ')
            p_board[x][y] = 'X'
            check_opponent_win()
            input("Press Enter to Continue...")
            os.system('clear')
            comp_guess = True
           

        elif p_board[x][y] == 'D':
            c_hit_tracker()
            print('\033[31mThe Computer hit your Destroyer!\033[0m')
            print(' ')
            print(' ')
            p_board[x][y] = 'X'
            check_opponent_win()
            input("Press Enter to Continue...")
            os.system('clear')
            comp_guess = True
            

        elif p_board[x][y] == ' ':
            c_miss_tracker()
            print('\033[33mYour opponent missed.\033[0m')
            print(' ')
            print(' ')
            input("Press Enter to Continue...")
            os.system('clear')
            p_board[x][y] = 'O'
            display_num_cmiss_chit(p_board)
            comp_guess = False
            print(' ')
            print('\033[1;33mPlayers Turn\033[0m')
            input("Press Enter to Continue...")
            os.system('clear')
            p_guess(board, v_board)
    
def print_player_board(p_board):
    print('\033[1;33mPLAYER BOARD: \033[0m')
    print('-------------------------------------------')
    print_p_board(p_board)
    print('-------------------------------------------')
    print(' ')

def print_cheatsheet(board):
    print('\033[1;33mCOMPUTER BOARD: [CHEAT SHEET] \033[0m')
    print('-------------------------------------------')
    print_board(board)
    print('-------------------------------------------')
    print(' ')
    
# Main game loop
def game_loop():
    # Computer choose board
    computer_choose_board()
    print('\nThe Computer has now placed the ships. Your turn!\n')
    p_place_ships(p_board, ships)
    print_player_board()
    print("All Ships have been placed.")
    print(' ')
    print(' ')
    print('\033[1;33m\nLet the game begin!\n\033[0m')
    input("Press Enter to Continue...")
    os.system('clear')
    stop = True
    while (stop):
        ineedtheboard = True
        while(ineedtheboard):
            print_player_board()
            #remove '#' below to view the computer's ship placement
            print_cheatsheet(board)
            p_guess(board, v_board)
        stop = False    


def instructions():
    os.system('clear')
    print('\033[1;33m----------------------------------------------------------')
    print('|             HOW TO PLAY THE BATTLESHIP GAME             |')
    print('|---------------------------------------------------------|')
    print('|                                                         |')
    print('|  This is a Player vs. Computer game.                    |')
    print('|  Each player have a 10x10 board where you can place     |')
    print('|  5 ships. The ships you can place are as follows:       |')
    print('|  1. Airship - 5 spots                                   |')
    print('|  2. Battleship - 4 spots                                |')
    print('|  3. Carrier - 3 spots                                   |')
    print('|  4. Submarine - 3 spots                                 |')
    print('|  5. Destroyer -2 spots                                  |')
    print('|  In placing row and column value, you only need to      |')
    print('|  input the value for the first square. Type H for       |')
    print('|  Horizontal Placement and V for Vertical Placement.     |')
    print('|  If you hit an opponent ship, you can still take        |')
    print('|  another turn. If you miss, you will see your number    |')
    print('|  of hits and miss then it will be the computers turn.   |')
    print('|                                                         |')
    print('-----------------------------------------------------------')
    print('\n')
    user = input('Are you Ready to Start the Game? Y for yes, N for no: \033[0m')
    if user.upper() == 'Y':
        os.system('clear')
        game_loop()
    elif user.upper() == 'N':
        print(' ')
        print('\033[1;33mOkay, returning you to the menu.\033[0m ')
        print(' ')
        input('Press Enter to continue...')
        os.system('clear')
        main()

def quit_game():
  os.system('clear')
  print(' ')
  print("\033[1;33mThank you for playing.\033[0m")
  print(' ')
  input("Press Enter to continue...")
  quit()

def main():
    print("\033[1;33m-------------------------------------")
    print("|       THE BATTLESHIP GAME!        |")
    print("-------------------------------------")
    print("|                                   |")
    print("|                [1]                |")
    print("|             A B O U T             |")
    print("|                                   |")
    print("|                [2]                |")
    print("|             S T A R T             |")
    print("|                                   |")
    print("|                [3]                |")
    print("|              E X I T              |")
    print("|                                   |")
    print("-------------------------------------")
    
    print(' ')
    print('Welcome, Player!\033[0m')
    user_input = int(input('What would you like to do? [1-3]: '))
    if user_input == 1:
        instructions()
    
    elif user_input == 2:
        os.system('clear')
        game_loop()
    
    elif user_input == 3:
        quit_game()
    
    else:
        print(' ')
        print(' ')
        print('\033[31mPlease try again!\033[0m')
        print(' ')
        print(' ')
        input('Press Enter to Continue... ')
        os.system('clear')
        main()

def play_again():
    print('\033[1;33m----------------------------------------')
    print('| Do you want to play again?           |')
    print('|--------------------------------------|')
    print('| [Y] Yes                              |')
    print('| [N] No                               |')
    print('----------------------------------------\033[0m')
    print(' ')
    choice = input("Enter Choice: ")
    if choice.upper() == 'Y':
        print(' ')
        print('\033[1;33mStarting the game...\033[0m')
        print(' ')
        input("Press Enter to start new game")
        os.system('clear')
        game_loop()
        
    elif choice.upper() == 'N':
        print(' ')
        print('\033[1;33mThank you for playing!\033[0m')
        print(' ')
        input("Press Enter to go back to menu")
        os.system('clear')
        main()
    
main()
