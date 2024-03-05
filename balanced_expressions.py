# Create a program that checks whether parentheses, braces and square brackets
# of an expression are balanced.
# - Balanced means that these delimiters open and close in order 
# and correctly.
# - Parentheses, braces and square brackets are of equal prioritary.
# There is no one more important than the other.
# - Balanced expression: { [ a * ( c + d ) ] - 5 }
# - Unbalanced expression: { a * ( c + d ) ] - 5 }

def check_banlanced_expression (expression):
    symbols_position = {}
    symbols_id = {
        "{" : 1,
        "}" : 1,
        "[" : 2,
        "]" : 2,
        "(" : 3,
        ")" : 3
    }

    for position, character in enumerate(expression.replace(" ", "")):
        id_symbol = symbols_id.get(character)

        if character in ("{", "[", "("):
            if id_symbol in symbols_position: # Check if the symbol identifier 
            # had been regitered previously.
                symbols_position[id_symbol].append(position)
            else:
                symbols_position[id_symbol] = [position]
        elif character in ("}", "]", ")"):
            if id_symbol in symbols_position: # Check if the symbol identifier 
            # had been regitered previously.
                symbols_position[id_symbol].append(position)
            else:
                print("Unbalanced expression")
                return False
    
    for key, positions in symbols_position.items():
        if not(len(positions) == 2):
            print("Unbalanced expression")
            return False
        
    print("Balanced expression")
    return True


check_banlanced_expression("a * { [ a * ( c + d ) ] - 5 }")
check_banlanced_expression("{ [ a * ( c + d ] - 5 }")
check_banlanced_expression("a * { [ a * ( c + d ) ]](}} }")
check_banlanced_expression("a(")
check_banlanced_expression("} a * 10 + (b) {")