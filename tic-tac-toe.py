# Create a function that analyzes a 3x3 matrix composed by "X" and "O"
# and returns the following:
# - "X" if the "X" have won.
# - "O" if the "O" have won.
# - "Draw" if there has been a tie.
# - "Null" if the proportion of "X", "O", or of the matrix is not correct.
# Or if both have won. 
# Note: The matrix may not be completely covered.
# It could be represented with an empty "", for example.

# abs() => Is a method that obtains the absolute value of a number without
# considering it's sign (Convert a number to a positive number).

def tic_tac_toe (matrix):
    number_words = {
        "": 0,
        "X": 0,
        "O": 0
    }

    # Empty.
    if matrix == [[], [], []] or matrix == [['', '', ''], ['', '', ''], ['', '', '']]:
        return ""

    # Null.
    for row in matrix:
        for word in row:
            try:
                number_words[word] += 1
            except KeyError:
                return "Null."
    
    diff_movements = number_words["X"] - number_words["O"]
    if not(abs(diff_movements) <= 1):
        return "Null." 
    
    # Win.
    line_three = []
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            word = matrix[row][column]

            try:
                # Search for line of three vertically.
                if word == matrix[row][column + 1] and word == matrix[row][column + 2]: 
                    line_three.append(word)
            
                # Search for line of three diagonally.
                if word == matrix[row + 1][column + 1] and word == matrix[row + 2][column + 2]:
                    line_three.append(word)
            except IndexError: 
                pass

            try:
                # Search for line of three horizontally.
                if word == matrix[row + 1][column] and word == matrix[row + 2][column]:
                    line_three.append(word)
            except IndexError:
                pass
    
    if set(line_three) == {"X"} or set(line_three) == {"O"}:
        return line_three[0]

    # Draw.
    elif line_three == [] or line_three == [''] or set(line_three) == {"X", "O"}:
        return "Draw."
    
    
print(tic_tac_toe([["", "", ""],
                   ["", "", ""], 
                   ["", "", ""]]))

print(tic_tac_toe([["X", "X", "O"],
                   ["X", "X", "O"], 
                   ["X", "O", "O"]]))

print(tic_tac_toe([["X", "X", "O"], 
                   ["X", "X", "O"],
                   ["X", "X", "O"]]))

print(tic_tac_toe([["X", "", ""], 
                   ["", "X", "O"], 
                   ["O", "", "X"]]))

print(tic_tac_toe([["O", "X", "X"],
                   ["X", "O", "O"], 
                   ["X", "O", "O"]]))