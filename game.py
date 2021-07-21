# print board in prettier way
#store state of board and player turn
#check whose turn it is
#ask for input
#update the board
#check for win
#change whose turn it is

def print_board(board):
    """This function prints the tic tac toe game board."""
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def play_tictactoe():
    """This function runs the tic tac toe game."""
    board = {'1': '1', '2': '2', '3': '3', 
            '4': '4', '5': '5', '6': '6', 
            '7': '7', '8': '8', '9': '9'}
    player_turn = "X"
    total_turns = 0

    while(True):
        print_board(board)
        print(f"It's your turn, {player_turn}.")
        print("Pick a numbered space to move to.")
        move = input("Which number space will your move be on?  ")
        
        try:
            if board[move] != "X" and board[move] != "O":
                board[move] = player_turn
                total_turns += 1
            else:
                print('Invalid move.  That space is already taken.')
                continue
        except KeyError:
            print('Invalid input.  You must pick a number on the board.')
            continue

        if board['7'] == board['8'] == board['9']:
            print_board(board)
            print(f'\n Game Over! \n {player_turn} won! \n')
            break
        elif board['4'] == board['5'] == board['6']:
            print_board(board)
            print(f'\n Game Over! \n {player_turn} won! \n')
            break
        elif board['1'] == board['2'] == board['3']:
            print_board(board)
            print(f'\n Game Over! \n {player_turn} won! \n')
            break
        elif board['1'] == board['4'] == board['7']:
            print_board(board)
            print(f'\n Game Over! \n {player_turn} won! \n')
            break
        elif board['2'] == board['5'] == board['8']:
            print_board(board)
            print(f'\n Game Over! \n {player_turn} won! \n')
            break
        elif board['3'] == board['6'] == board['9']:
            print_board(board)
            print(f'\n Game Over! \n {player_turn} won! \n')
            break
        elif board['3'] == board['5'] == board['7']:
            print_board(board)
            print(f'\n Game Over! \n {player_turn} won! \n')
            break
        elif board['1'] == board['5'] == board['9']:
            print_board(board)
            print(f'\n Game Over! \n {player_turn} won! \n')
            break
        
        if total_turns == 9:
            print_board(board)
            print('\n Game over! \n You tied!')
            break

        if player_turn == "X":
            player_turn = "O"
        else: 
            player_turn = "X"

play_tictactoe()
