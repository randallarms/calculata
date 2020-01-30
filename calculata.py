#=====================================#
#             Calculata               #
#          by Randall Arms            #
#  @ github.com/randallarms/calculata #
#=====================================#

# Opening text
print("\n\n=========")
print("CALCULATA")
print("=========")

str_error = "[ERROR] "
str_error_int = "Expression must begin with an integer."
str_error_symbol = "Extraneous symbols were detected."
str_error_char = "One of the characters in your query is not valid."
str_error_zero = "Division by zero detected."
str_again = " Please try again."


# Get the last integer
def make_int(int_holder):
    int_str = ""
    for n in int_holder:
        int_str += n
    return int(int_str)

# Checks that the input n is an integer
def int_check(n):
    try:
        integer = int(n)
        return True
    except ValueError:
        return False
        
# Checks that the input c is an integer  
def symbol_check(c):
    symbols = ["+", "-", "*", "/"]
    if (c in symbols):
        return True
    else:
        return False
        
# Checks that the input p is a parenthesis
def paranthesis_check(p):
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
            print(str_error + str_error_zero + str_again)
            exit()
        return n1/n2
        
# Turn string into list of integers & symbols
def listify(i):
    int_holder = list()
    exp_holder = list()
    exp_position = 0
    for c in i:
        if (int_check(c)):
            int_holder.append(c)
            if exp_position+1 == len(i):
                exp_holder.append(make_int(int_holder))
        # Check for symbol
        elif (symbol_check(c)):
            exp_size = len(exp_holder)
            # Make sure symbols aren't back-to-back
            if exp_size > 0 and symbol_check(exp_holder[len(exp_holder)-2]):
                print(str_error + str_error_symbol + str_again)
                exit()
            # Add the last integer and symbol to the expression
            exp_holder.append(make_int(int_holder))
            exp_holder.append(c)
            int_holder = list()
        # Check for parantheses
        elif (paranthesis_check(c)):
            exp_size = len(exp_holder)
            # Make sure symbols aren't back-to-back
            if exp_size > 0 and int_check(exp_holder[exp_size-2]):
                print(str_error + str_error_char + str_again)
                exit()
            # Add the parantheses to the expression
            exp_holder.append(c)
        else:
            print(str_error + str_error_char + str_again)
            exit()
        exp_position += 1
        
    # Check that a number comes first
    if not int_check(exp_holder[0]):
        print(str_error + str_error_int + str_again)
        exit()
    else:
        return exp_holder
        
# Iterate through list and evaluate
def evaluate(exp_holder):
    result = int(exp_holder[0])
    group_results = list()
    eval_exp_position = 0
    current_exp_position = 0
    for d in exp_holder:
        # Check that loop is caught up
        if current_exp_position >= eval_exp_position:
            # Evaluate current expression
            if symbol_check(d):
                next_d = int(exp_holder[eval_exp_position+1])
                if next_d == ")":
                    # Evaluate inner expression
                    next_exp = list()
                    next_exp_position = 0
                    for e in exp_holder:
                        if (next_exp_position > eval_exp_position):
                            if (e == ")"):
                                break
                            elif (next_exp_position >= len(exp_holder)-1):
                                print(str_error + str_error_parantheses + str_again)
                            else:
                                next_exp.append(e)
                        # Increment expression counters
                        next_exp_position += 1
                        eval_exp_position += 1
                    inner_result = evaluate(listify(next_exp))
                    result = math_func(d, result, inner_result)
                else:
                    eval_exp_position += 1
                    result = math_func(d, result, next_d)
                
            # Increment loop counter
            current_exp_position += 1
        
        # Return the result
        return result

# Input the expression
i = input("\nEnter expression:  ");

# Evaluate the expression
print("\nEvaluating expression: ")

exp = listify(i)
result = evaluate(exp)

# Debugging printing on expression parts
exp_str = ""
for d in exp:
    exp_str += str(d)
print(exp_str + " = " + str(result))
    
# Print result
print(str(result))