
#%% Imports

import time


#%% 

def empty_board():
    """ Returns the empty board list """

    board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
    
    return board

#%% 

def reference_board():
    """ Returns a board with valid symbol positions for player reference """
    board = [["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"]]
    
    return board

#%%

def print_board(board):
    """ Prints the TicTacToe board """

    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("---+---+---")


#%%

def choose_player():
    """ Asks players to choose player numbers for the game"""

    print("Player 1: X\nPlayer 2: O\n\n")
    choice = input("Choose which player you want to be (1 or 2): ")

    if choice not in ['1', '2']:
        print("Please enter a valid player number (1 or 2 only)!")

    else:
        if choice == '1': 
            print("Okay! You are Player '1' and your friend is Player 2")

        else:
            print("Okay! You are Player '2' and your friend is Player 1")


#%% 

def player_input(number):
    """ Asks for player's desirable position input, returns the position"""

    valid_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_position = input(f"Please enter the position Player {number} (1-9): ")

    if player_position not in valid_positions:
        print("Enter a valid position (1-9): ")

    else:
        pass
        
    return player_position


#%%

def player_moves(board, player_position, player_num):
    """ Adds the relevant symbols (X or O) at player's chosen position"""

    if player_num == '1':
        symbol = 'X'

    else:
        symbol = 'O'



    if player_position == '7':
        board[0][0] = symbol

    elif player_position == '8':
        board[0][1] = symbol

    elif player_position == '9':
        board[0][2] = symbol

    elif player_position == '4':
        board[1][0] = symbol

    elif player_position == '5':
        board[1][1] = symbol

    elif player_position == '6':
        board[1][2] = symbol
    
    elif player_position == '1':
        board[2][0] = symbol

    elif player_position == '2':
        board[2][1] = symbol

    else:
        board[2][2] = symbol


    return board


#%%

def replay():
    """ Asks if players want to play again and returns True if players want to play again"""
    
    choice = input("Do you want to play again? (y/n): ")

    if choice.lower() == 'y':
        return True

    else:
        return False


#%% Game logic

def main():
    """ Conatins the main logic of the game """

    print("Welcome to the TIC TAC TOE game! Hope you will have fun!")
    time.sleep(3)
    print("Choose which player you would like to be.")
    choose_player()
    time.sleep(3)
    print("Player 1 goes first")
    time.sleep(2)
    print("Here is the position reference for your convenience:")
    ref_board = reference_board()
    print_board(ref_board)
    time.sleep(2)
    print("The game begins in 5 seconds....\n\n")
    time.sleep(8)
    print("LET THE GAME BEGIN!!\n\n")

    new_board = empty_board()
    print_board(new_board)
    print("\n\n\n")

    position_list = []

    for i in range(0,9):

        if (i % 2) == 0:
            player_number = '1'
            print("Choose a position Player 1\n")

            while True:

                position = player_input(player_number)

                if position in position_list:
                    print("Position already taken before.")
                    continue

                else:
                    break

            
            updated_board = player_moves(new_board, position, player_number)
            print_board(updated_board)
            print("\n\n")

            position_list.append(position)


        else:
            player_number = '2'
            print("Choose a position Player 2\n")

            while True:

                position = player_input(player_number)

                if position in position_list:
                    print("Position already taken before.")
                    continue

                else:
                    break

            updated_board = player_moves(new_board, position, player_number)
            print_board(updated_board)
            print("\n\n")

            position_list.append(position)


        new_board = updated_board

        stop_game = False


        for j in range(0,3):
            
            if ((updated_board[j][0] == 'X') and (updated_board[j][1] == 'X') and (updated_board[j][2] == 'X')):
                print(f"END OF THE GAME!\n")
                print("Player 1 is the winner!")
                stop_game = True
                break

            elif ((updated_board[j][0] == 'O') and (updated_board[j][1] == 'O') and (updated_board[j][2] == 'O')):
                print(f"END OF THE GAME!\n")
                print("Player 2 is the winner!")
                stop_game = True
                break

            else:
                pass
        
        if stop_game:
            break



        for k in range(0,3):

            if ((updated_board[0][k] == 'X') and (updated_board[1][k] == 'X') and (updated_board[2][k] == 'X')):
                print(f"END OF THE GAME!\n")
                print("Player 1 is the winner!")
                stop_game = True
                break

            elif ((updated_board[0][k] == 'O') and (updated_board[1][k] == 'O') and (updated_board[2][k] == 'O')):
                print(f"END OF THE GAME!\n")
                print("Player 2 is the winner!")
                stop_game = True
                break

            else:
                pass

        if stop_game:
            break




        if ((updated_board[0][0] == 'X') and (updated_board[1][1] == 'X') and (updated_board[2][2] == 'X')) or ((updated_board[0][2] == 'X') and (updated_board[1][1] == 'X') and (updated_board[2][0] == 'X')): 
                
            print(f"END OF THE GAME!\n")
            print("Player 1 is the winner!")
            stop_game = True
            break   

        elif ((updated_board[0][0] == 'O') and (updated_board[1][1] == 'O') and (updated_board[2][2] == 'O')) or ((updated_board[0][2] == 'O') and (updated_board[1][1] == 'O') and (updated_board[2][0] == 'O')):
                
            print(f"END OF THE GAME!\n")
            print("Player 2 is the winner!")
            stop_game = True
            break

        else:
            pass



        if stop_game:
            break

        if i == 8 and not stop_game:
            print("It's a draw!")


    print("\n")
    print("END OF THE GAME!")

    print("Do you want to play again (y / n)? ")
    replay_choice = replay()

    return replay_choice

# %%

replay_choice  = True

if __name__ == "__main__":

    while True:
        replay_choice = main()

        if not replay_choice:
            print("Thanks for playing! Bye bye.")
            break

# %%
