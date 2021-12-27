with open("input.txt", "r") as f:
    data = f.read().split()

drawn_numbers = data[0].split(",")
boards = [data[i + 1:i + 26] for i in range(0, len(data[1:]), 25)]  # Split input data into groups of 25 (5x5 boards)

def checkrow(rownum, board):
    return 'XXXXX' == ''.join(board[rownum:rownum+5])

def checkcol(colnum, board):
    return 'XXXXX' == ''.join(board[colnum::5])

winning_boards = []

for turn, number in enumerate(drawn_numbers):
    for bindex, board in enumerate(boards):
        if bindex in winning_boards:
            continue
        if number in board:
            board[board.index(number)] = "X"
            for i in range(5):
                if checkrow(i*5, board) or checkcol(i, board):
                    nums = [int(j) for j in board if j != 'X']
                    print(turn, sum(nums) * int(number))
                    if bindex not in winning_boards:
                        winning_boards.append(bindex)