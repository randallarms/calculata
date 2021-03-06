#======================================#
#             Calculata                #
#          by Randall Arms             #
#  @ github.com/randallarms/calculata  #
#======================================#

# Opening text
print("\n\n===================")
print(" C A L C U L A T A ")
print("===================")

# General info
VERSION = "0.7.12"

# Error strings
STR_DEBUG = "[DEBUG] "
STR_WARNING = "[WARNING] "
STR_ERROR = "[ERROR] "
STR_ERROR_START = "Expression must begin with an integer or open parenthesis."
STR_ERROR_SYMBOL = "Extraneous symbols were detected."
STR_ERROR_CHAR = "One of the characters in your query is not valid."
STR_ERROR_ZERO = "Division by zero detected."
STR_ERROR_PARENTHESES = "Parentheses not properly closed."
STR_AGAIN = " Please try again."
STR_EXIT = " Now exiting."
        
#===========#
# FUNCTIONS #
#===========#

# Get the last integer
def make_int(int_holder):

    int_str = ""
    
    for n in int_holder:
        int_str += str(n)
    return int(int_str)

# Checks that the input n is an integer
def int_check(n):

    try:
        integer = int(n)
        return True
    except ValueError:
        return False
        
# Checks that the input c is an acceptable operation symbol  
def symbol_check(c):

    symbols = ["+", "-", "*", "/"]
    
    if (c in symbols):
        return True
    else:
        return False
        
# Checks that the input p is an open or close parenthesis
def parenthesis_check(p):

    if p == "(" or p == ")":
        return True
    else:
        return False
        
# Performs a math function based on the parameters
def math_func(symbol, n1, n2):

    if symbol == "+":
        return n1+n2
    elif symbol == "-":
        return n1-n2
    elif symbol == "*":
        return n1*n2
    elif symbol == "/":
        if n2 == 0:
            print(STR_ERROR + STR_ERROR_ZERO + STR_AGAIN)
            exit()
        return n1/n2
        
# Exit message
def exit_msg():
    
    print("\nThank you for using Calculata, v" + VERSION + "!")
    print("This version of Calculata is in development ")
    print("and is for debugging purposes only! ")
    print("For more info, please visit ")
    print("https://www.github.com/randallarms/calculata")
    return
        
# Turn string into list of integers & symbols
def listify(i):

    int_holder = list()
    exp_holder = list()
    exp_position = 0
    
    for c in i:
        if (int_check(c)):
            print(STR_DEBUG + "Int check: " + str(c))
            int_holder.append(c)
            if exp_position+1 == len(i):
                exp_holder.append(make_int(int_holder))
        # Check for symbol
        elif (symbol_check(c)):
            print(STR_DEBUG + "Symbol check: " + str(c))
            exp_size = len(exp_holder)
            # Make sure symbols aren't back-to-back
            if exp_size > 1 and symbol_check(exp_holder[len(exp_holder)-2]):
                print(STR_ERROR + STR_ERROR_SYMBOL + STR_AGAIN)
                exit()
            # Add the last integer and symbol to the expression
            exp_holder.append(make_int(int_holder))
            exp_holder.append(c)
            int_holder = list()
        # Check for parentheses
        elif (parenthesis_check(c)):
            print(STR_DEBUG + "Parenthesis check: " + str(c))
            exp_size = len(exp_holder)
            # Make sure parentheses aren't back-to-back
            if exp_size > 1 and parenthesis_check(exp_holder[exp_size-2]):
                print(STR_ERROR + STR_ERROR_CHAR + STR_AGAIN)
                exit()
            # Account for closing parentheses to compile and flush int_holder
            elif exp_size > 1 and int_check(exp_holder[exp_size-2]):
                exp_holder.append(make_int(int_holder))
                int_holder = list()
            # Add the parentheses to the expression
            exp_holder.append(c)
        else:
            print(STR_ERROR + STR_ERROR_CHAR + STR_AGAIN)
            exit()
        exp_position += 1
        
    print(STR_DEBUG + "Exp_holder: " + str(exp_holder))
    
    # Check that a number or open parenthesis comes first
    if int_check(exp_holder[0]) or exp_holder[0] == "(":
        return exp_holder
    else:
        print(STR_ERROR + STR_ERROR_START + STR_AGAIN)
        exit()
        
# Iterate through list and evaluate
def evaluate(exp_holder):

    # Check that expression begins with an integer or open parenthesis
    if int_check(exp_holder[0]):
        result = int(exp_holder[0])
    elif exp_holder[0] == "(":
        result = 0
    else:
        print(STR_ERROR + STR_ERROR_START + STR_AGAIN)
        
    # Evaluation
    
    group_results = list()
    eval_exp_position = 0
    current_exp_position = 0
    pemdas_phase = "p" # (p) parantheses, (e) exponents, (md) multiplication/division, (as) addition/subtraction
    
    # Iterate through expression
    for d in exp_holder:
    
        # Check that loop is caught up
        if current_exp_position >= eval_exp_position:
            # Evaluate current expression
            if symbol_check(d):
                next_d = int(exp_holder[eval_exp_position+1])
                result = math_func(d, result, next_d)
            # Parentheses detection
            elif d == "(":
                # Get inner expression
                next_exp = list()
                next_exp_position = current_exp_position
                for e in exp_holder:
                    if (next_exp_position >= eval_exp_position):
                        if (e == ")"):
                            break
                        elif (next_exp_position >= len(exp_holder)-1):
                            print(STR_ERROR + STR_ERROR_PARENTHESES + STR_AGAIN)
                        else:
                            next_exp.append(e)
                            next_exp_position += 1
                # Evaluate inner expression
                inner_result = evaluate(listify(next_exp))
                result = math_func(d, result, inner_result)
            # Increment loop counters
            current_exp_position += 1
            eval_exp_position += 1
        else:
            current_exp_position += 1
        
    # Return the result
    return result
        
#=======#
# INPUT #
#=======#

i = ""

while i != "exit":

    # Input the expression
    i = input("\nEnter expression:  ");
    
    if i == "exit":
        exit_msg()
        break
    else:
        # Evaluate the expression
        print("\nEvaluating expression...")
        exp = listify(i)
        result = evaluate(exp)
        # Print result
        print("Your result is: " + str(result))