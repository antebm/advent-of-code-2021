from bingo_board import BingoBoard

FILE_NAME = "input.txt"
BOARD_SIZE = 5

input = open(FILE_NAME, "r")

def convert_to_integers(values):
    integers = []
    for value in values:
        integers.append(int(value))

    return integers


numbers = input.readline().strip().split(',')
numbers = convert_to_integers(numbers)

boards = input.readlines()
boards.remove('\n')
boards.append('')

board = []
board_objects = []

for line in boards:
    board_row = line.strip().split()
    if(board_row):
        board_row = convert_to_integers(board_row)
        board.append(board_row)
    else:
        board_object = BingoBoard(board)
        board_objects.append(board_object)
        board = []


winning_points = 0
winning_points_list = []

for number in numbers:
    if not board_objects:
        break
    
    turn_over = False
    for board_object in board_objects:
        board_object.update_descriptor(number)
        if (board_object.check_winning() and not board_object.board_done()):
            points = board_object.calculate_points()
            winning_points = number * points
            winning_points_list.append(winning_points)
            board_object.close_board()
            turn_over = True
  

# part 1 solution
print(winning_points_list[0])

# part 2 solution
print(winning_points_list[-1])