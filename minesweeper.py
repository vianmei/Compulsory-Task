"""
Create a function that takes a grid of # and -, where each hash (#) represents a
mine and each dash (-) represents a mine-free spot.
Return a grid, where each dash is replaced by a digit, indicating the number of
mines immediately adjacent to the spot i.e. (horizontally, vertically, and
diagonally)

Example of an input:
[ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]
Example of the expected output:
[ ["1", "1", "2", "#", "#"],
["1", "#", "3", "3", "2"],
["2", "4", "#", "2", "0"],
["1", "#", "#", "2", "0"],
["1", "2", "2", "1", "0"] ]
"""

grid_list = [["-", "-", "-", "#", "#"],
             ["-", "#", "-", "-", "-"],
             ["-", "-", "#", "-", "-"],
             ["-", "#", "#", "-", "-"],
             ["-", "-", "-", "-", "-"]]


# Calculate the number of mines immediately adjacent to the spot
# current_row :  current row index
# current_col :  current column index
# sign : current element value
# g_cols : number of grid cols
# g_rows : number of grid rows
def get_mines_count(current_row, current_col, sign, g_cols, g_rows):
    adjacent_list = [-1, 0, 1]
    hash_count = 0
    for row_num in adjacent_list:
        for col_num in adjacent_list:
            next_row = current_row + row_num
            next_col = current_col + col_num
            if next_row in range(g_rows) and next_col in range(g_cols) and sign != "#":
                try:
                    next_sign = grid_list[next_row][next_col]
                    if next_sign == "#":
                        hash_count += 1
                except Exception as error_str:
                    print("get_count", error_str)
    return hash_count


# The enumerate function in Python to keep track of the index points and values
def enumerate_function(values):
    for count, value in enumerate(values, start=0):
        print(f'Index {count} contains the value {value}')


# Start the program
print("--- Print the input grid list --- ")
for row_list in grid_list:
    print(row_list)

print()
print("--- Start Minesweeper --- ")
rows = len(grid_list)
minesweeper_grid = []  # Store minesweeper value list

for row in range(rows):
    cols = len(grid_list[row])  # now the number of cols depends on each row’s length
    each_row_list = []
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        try:
            num = 0
            current_value = grid_list[row][col]
            if current_value == "-":
                num = get_mines_count(row, col, current_value, cols, rows)
                each_row_list.append(str(num))
            else:
                each_row_list.append(current_value)
        except Exception as error:
            print(error)
    # Add row to minesweeper grid list
    minesweeper_grid.append(each_row_list)

    # keep track of the index points and values for each row list
    enumerate_function(each_row_list)

print()
# Print result
print("--- Minesweeper --- ")
for row_list in minesweeper_grid:
    print(row_list)
