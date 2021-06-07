board = [ 
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]

# print(board[0][1])
# print(board[2][2])

while True:

    row_index = 0
    for row in board:
        col_index = 0
        for col in row:
            if col == " _ ":
                print(row_index, col_index, end=" ")
                
            else:
                print(col, end=" _ ")
            col_index += 1
        print(' ')
        print(' ')
        row_index += 1

    pos_row = int(input("Which row? "))
    pos_col = int(input("Which column? "))

    board[pos_row][pos_col] = "X"