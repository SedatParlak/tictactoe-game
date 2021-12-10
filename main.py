
board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]

user = True
turns = 0


# display the board
def display_board(input_board):
    for row in input_board:
        for slot in row:
            print(slot + " | ", end="")
        print()


# quit game
def quit_game(is_quit):
    if is_quit == "q":
        print("Thanks for gaming")
        return True
    else:
        return False


# check the user input is a number
def is_num(input_isnum):
    if not input_isnum.isnumeric():
        print("This is a not valid number")
        return True
    else:
        return False


# check the user input between 1-9
def check_num(num):
    if 1 <= int(num) <= 9:
        return False
    return True


def coordinates(user_int):
    row = int(user_int / 3)
    col = int(user_int % 3)
    return row, col


def is_taken(coords, boards):
    row = coords[0]
    column = coords[1]
    if boards[row][column] != "-":
        print("Position already taken. Please try another position.")
        return True
    return False


def current_user(user_):
    if user_:
        return "X"
    else:
        return "O"


def add_to_board(coords, boards):
    row = coords[0]
    col = coords[1]
    boards[row][col] = active_user


def current_user(user_):
    if user_:
        return "X"
    else:
        return "O"


def is_win(act_user, boards):
    if check_rows(act_user, boards):
        return True
    if check_column(act_user, boards):
        return True
    if check_diagonal(act_user, boards):
        return True
    return False


def check_rows(act_user, boards):
    for row in boards:
        completed_row = True
        for slot in row:
            if slot != act_user:
                completed_row = False
                break
        if completed_row:
            return True
    return False


def check_column(act_user, boards):
    for col in range(3):
        completed_col = True
        for row in range(3):
            if boards[row][col] != act_user:
                completed_col = False
                break
        if completed_col:
            return True
    return False


def check_diagonal(act_user, boards):
    if boards[0][0] == act_user and boards[1][1] == act_user and boards[2][2] == act_user:
        return True
    elif boards[0][2] == act_user and boards[1][1] == act_user and boards[2][0] == act_user:
        return True
    return False


# game loop
while turns < 9:
    active_user = current_user(user)
    display_board(board)
    print(f"'{active_user.upper()}' turn")
    user_input = input("Please enter a position from 1-9 : \nEnter 'q' to quit. ").lower()

    if quit_game(user_input):
        break

    if is_num(user_input):
        print("Please try again.")
        continue

    if check_num(user_input):
        print("This number is out of range. Please try again")
        continue

    user_input = int(user_input) - 1
    coord = coordinates(user_input)

    if is_taken(coord, board):
        print("Please try again")
        continue
    else:
        add_to_board(coord, board)

    if is_win(active_user, board):
        display_board(board)
        print(f"{active_user.upper()} won !")
        break

    turns += 1
    if turns == 9:
        print("Tie !")
        break

    user = not user
