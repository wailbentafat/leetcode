
def numb_exist_coloumn(coloumn_num, board):
    all_col = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = []
    for b in board:
        a.append(b[coloumn_num - 1])
    for num in a:
        if num in all_col:
            all_col.remove(num)
    return all_col

def numb_exist_row(row_num, board):
    all_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in board[row_num - 1]:
        if num in all_row:
            all_row.remove(num)
    return all_row

def numb_exist_box(row_num, coloumn_num, board):
    all_box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = []
    for i in range(3):
        for j in range(3):
            a.append(board[row_num + i][coloumn_num + j])
    for num in a:
        if num in all_box:
            all_box.remove(num)
    return all_box
def can_place(num, row_num, coloumn_num, board):
    if num in board[row_num - 1]:
        return False
    if num in numb_exist_coloumn(coloumn_num, board):
        return False
    if num in numb_exist_row(row_num, board):
        return False
    if num in numb_exist_box(row_num, coloumn_num, board):
        return False
    return True


def sudoku_solver(board):
    for row in board:
        for col in row :
            if col == '.':
                for num in range(1, 10):
                    if can_place(num, board.index(row) + 1, row.index(col) + 1, board):
                        board[board.index(row)][row.index(col)] = str(num)
                        if sudoku_solver(board):
                            return True
                        else:
                            board[board.index(row)][row.index(col)] = '.'
                return False
    return True