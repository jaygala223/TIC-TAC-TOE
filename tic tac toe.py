from IPython.display import clear_output

def display_board(board):
    print(board[1]+"  |  "+board[2]+"  |  "+board[3])
    print("-"*14)
    print(board[4] + "  |  "+board[5]+"  |  "+board[6])
    print("-"*14)
    print(board[7] + "  |  "+board[8]+"  |  "+board[9])

test_board = [1,"X","O","X","O","X","O","X","O","X"]
display_board(test_board)

def player_input():
    print("PLAYER1 ENTER CHOICE: X or O")
    choice = input()

    while choice!="X" and choice!="O":
         choice = choice.upper()

    if choice=="X":
        return ("X","O")
    if choice=="O":
        return ("O","X")

def place_choice(board,choice,position):
    board[position]=choice

def space_check(board,position):
    return board[position]==" "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def win_check(board,mark):
    if ((board[1] == board[2] == board[3] == mark) or
       (board[4] == board[5] == board[6] == mark) or
       (board[7] == board[8] == board[9] == mark) or
       (board[1] == board[4] == board[7] == mark) or
       (board[2] == board[5] == board[8] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark) or
       (board[3] == board[6] == board[9] == mark)):
       return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("choose a number from 1 to 9: "))

        return position

def replay():
    choice = input("play again? y or n? ")
    return choice=="y"

import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 1:
        return "PLAYER1"
    else:
        return "PLAYER2"

print("welcome to TIC TAC TOE")

while True:
    the_board = [" "]*10
    player1_choice,player2_choice = player_input()

    turn = choose_first()
    print(turn+"will go first")

    play_game = input("READY? YES OR NO? ")
    if play_game == "YES" or play_game == "yes":
        game_on= True
    else:
        game_on=False



    while game_on:
        if turn== "PLAYER1":
            display_board(the_board)
            position= player_choice(the_board)
            place_choice(the_board,player1_choice,position)

            if win_check(the_board,player1_choice):
                display_board(the_board)
                print("WE HAVE A WINNER!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("IT'S A DRAW!")
                    break
                else:
                    turn="PLAYER2"
        else:
            display_board(the_board)
            position= player_choice(the_board)
            place_choice(the_board,player2_choice,position)

            if win_check(the_board,player2_choice):
                display_board(the_board)
                print("WE HAVE A WINNER!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("IT'S A DRAW!")
                    break
                else:
                    turn="PLAYER1"
    if not replay():
        break








