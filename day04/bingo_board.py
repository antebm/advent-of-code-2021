class BingoBoard:
    """Models Bingo board"""

    # initialize board and board descriptor
    def __init__(self, board):
        self.board = board
        self.descriptor = [[False]*5,[False]*5, [False]*5, [False]*5, [False]*5]
        self.done = False
    
    # update descriptor
    def update_descriptor(self, number):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if self.board[i][j] == number:
                    self.descriptor[i][j] = True

    # check for winning condition
    def check_winning(self):
        winning = False
        for row in range(0, len(self.board)):
            winning = True
            for column in range(0, len(self.board[row])):
                if self.descriptor[row][column] == False:
                    winning = False
                    break

            if winning:
                return winning

        for column in range(0, len(self.board[0])):
            winning = True
            for row in range(0, len(self.board)):
                if self.descriptor[row][column] == False:
                    winning = False
                    break

            if winning:
                return winning

        return False

    # calculate points
    def calculate_points(self):
        points = []
        point_sum = 0
        for row in range(0, len(self.board)):
            for column in range(0, len(self.board[0])):
                if self.descriptor[row][column] == False:
                    points.append(self.board[row][column])

        for point in points:
            point_sum = point_sum + point

        return point_sum

    def close_board(self):
        self.done = True

    def board_done(self):
        return self.done

    def print_board(self):
        print(self.board)

    def print_descriptor(self):
        print(self.descriptor)