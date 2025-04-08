# The expression to be tokenized
expr = "x + (M * 56) = k / 2"

# Initialize variables for token processing
token = ""          # Stores the current token being built
current_char = ""    # Current character being examined
current_class = 0    # Numeric code representing the current token type
current_pos = 0      # Current position in the expression string

# Define token type constants with their numeric codes
IDENTIFIER = 11      # Token Code for variable names (starts with letter)
INTEGER = 10         # Token Code for integer numbers
ADD_OPER = 21        # Token Code for + operator
MINUS_OPER = 22      # Token Code for - operator
MULTIP_OPER = 23     # TokenCode for * operator
DIVIDE_OPER = 24     # Token Code for / operator
EQUAL_OPER = 20      # Token Code for = operator
L_PAREN = 25         # Token Code for left parenthesis (
R_PAREN = 26         # Token Code for right parenthesis )
DONE = -1            # Token Code indicating end of input

def read_char():
    #"""Reads the next character from the expression and classifies its type"""
    global current_char, current_class, current_pos
    if current_pos < len(expr):  # If we haven't reached the end
        current_char = expr[current_pos]  # Get current character
        current_pos += 1         # Move to next position
        # Classify the character type
        if current_char.isalpha():
            current_class = IDENTIFIER
        elif current_char.isdigit():
            current_class = INTEGER
        elif current_char == '(':
            current_class = L_PAREN
        elif current_char == ')':
            current_class = R_PAREN
        elif current_char == '+':
            current_class = ADD_OPER
        elif current_char == '-':
            current_class = MINUS_OPER
        elif current_char == '*':
            current_class = MULTIP_OPER
        elif current_char == '/':
            current_class = DIVIDE_OPER
        elif current_char == '=':
            current_class = EQUAL_OPER
        else:
            current_class = -2    # Unknown character type
    else:
        current_char = ''         # End of input
        current_class = DONE

def skip_spaces():
    #"""Skips over any whitespace characters in the input"""
    while current_char.isspace():  # While current character is space
        read_char()               # Keep reading next character

def scan():
    #"""Scans and returns the next token from the input"""
    global token
    token = ""                   # Reset token buffer
    skip_spaces()                # Skip any leading whitespace

    # Handle IDENTIFIER tokens (variable names)
    if current_class == IDENTIFIER:
        token += current_char     # Start with first letter
        read_char()
        # Continue while we have letters or numbers
        while current_char.isalnum():
            token += current_char
            read_char()
        print(f"Token: IDENTIFIER ({IDENTIFIER}), Lexeme: {token}")
        return IDENTIFIER

    # Handle INTEGER tokens (numbers)
    elif current_class == INTEGER:
        while current_char.isdigit():  # While we have digits
            token += current_char
            read_char()
        print(f"Token: INTEGER ({INTEGER}), Lexeme: {token}")
        return INTEGER

    # Handle all operator types
    elif current_class in [ADD_OPER, MINUS_OPER, MULTIP_OPER, DIVIDE_OPER, EQUAL_OPER]:
        token = current_char      # Operators are single characters
        # Get operator name and code for output
        oper_info = {
            ADD_OPER: ("ADD_OPER", ADD_OPER),
            MINUS_OPER: ("MINUS_OPER", MINUS_OPER),
            MULTIP_OPER: ("MULTIP_OPER", MULTIP_OPER),
            DIVIDE_OPER: ("DIVIDE_OPER", DIVIDE_OPER),
            EQUAL_OPER: ("EQUAL_OPER", EQUAL_OPER)
        }[current_class]
        print(f"Token: {oper_info[0]} ({oper_info[1]}), Lexeme: {token}")
        read_char()
        return current_class

    # Handle left parenthesis
    elif current_class == L_PAREN:
        token = current_char
        print(f"Token: L_PAREN ({L_PAREN}), Lexeme: {token}")
        read_char()
        return L_PAREN

    # Handle right parenthesis
    elif current_class == R_PAREN:
        token = current_char
        print(f"Token: R_PAREN ({R_PAREN}), Lexeme: {token}")
        read_char()
        return R_PAREN

    # Handle end of input
    elif current_class == DONE:
        print("End of expression.")
        return DONE

    # Handle unknown characters
    else:
        print(f"Unknown character: {current_char}")
        read_char()
        return -1

def main():
    """Main function that drives the tokenization process"""
    read_char()          # Initialize by reading first character
    while scan() != DONE:  # Keep scanning until end of input
        pass

if __name__ == "__main__":
    main()  # Entry point when run as a script