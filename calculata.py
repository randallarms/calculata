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

# Input the expression
i = input("\nEnter expression:  ");

# Evaluate the expression
print("\nEvaluating expression: ")

# Turn string into list of integers & symbols
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
    else:
        print(str_error + str_error_char + str_again)
        exit()
    exp_position += 1
    
# Check that a number comes first
if not int_check(exp_holder[0]):
    print(str_error + str_error_int + str_again)
    exit()

# Iterate through list and evaluate
result = int(exp_holder[0])
new_exp_position = 0

for d in exp_holder:
    if symbol_check(d):
        result = math_func(d, result, int(exp_holder[new_exp_position+1]))
    new_exp_position += 1

# Debugging printing on expression parts

exp_str = ""
for d in exp_holder:
    exp_str += str(d)
print(exp_str + " = " + str(result))
    
# Print result

print(str(result))