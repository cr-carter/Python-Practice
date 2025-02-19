'''
This function takes an array of strings as an input
representing a minesweeper board. Example:
['  *',
 ' * ',
 '  *']
Output should be the solution to the board. Example:
['-2*',
 '1*3',
 '-1*']
Raise an exception if the input board is invalid.
An invalid board is one with rows of different lengths,
or a character other than a '*' or a space.
'''

def minesweeper_solver(board):
    #Check if valid board was passed
    try:
        column_count = len(board[0])
        row_count = len(board)
        for row in board:
            if len(row) != column_count:
                raise ValueError
            if any(c not in " *" for c in row):
                raise ValueError
    except ValueError:
        return "The board is invalid with current input."
    except IndexError:
        return "The board is invalid with current input."

    solution = []
    directions = [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    for row in range(row_count):
        solution_row = ''
        for col in range(column_count):
            count = 0
            if board[row][col] == '*':
                solution_row += '*'
            else:
                for i in directions:
                    if 0 <= col + i[0] <= column_count - 1 and 0 <= row + i[1] <= row_count - 1:
                        if board[row + i[1]][col + i[0]] == '*':
                            count += 1
                solution_row += ('-' if count == 0 else str(count))
        solution.append(solution_row)
    return solution


#Test code below
board = [" *  * ", "  *   ", "    * ", "   * *", " *  * ", "      "]
result = minesweeper_solver(board)
print(result)
