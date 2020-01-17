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
str_error_symbol = "Extraneous symbols were detected."
str_error_char = "One of the characters in your query is not valid."
str_again = " Please try again."

# Checks that the input n is an integer
def int_check(n):
    try:
        integer = int(n)
        return true
    except ValueError:
        return false
        
# Checks that the input c is an integer
        
def symbol_check(c):
    symbols = ["+", "-", "*", "/"]
    if (c in symbols):
        return true
    else:
        return false
        
# Performs a math function based on the parameters

def math_func(symbol, n1, n2):
    if symbol == "+":
        return n1+n2
    elif symbol == "-":
        return n1-n2
    elif symbol == "*":
        return n1*n2
    elif symbol == "/":
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
    # Check for integer
    if (int_check(c)):
        int_holder.append(c)
    # Check for symbol
    elif (symbol_check(c)):
        exp_size = len(exp_holder)
        # Make sure symbols aren't back-to-back
        if exp_size > 0 && symbol_check(exp_holder[exp_position-1]):
            print(str_error + str_error_symbol + str_again)
            exit()
        # Get the last integer
        int_str = ""
        for n in int_holder:
            int_str += n
        integer = int(int_str)
        # Add the last integer and symbol to the expression
        exp_holder.append(integer + c)
        int_holder = list()
    else:
        print(str_error + str_error_char + str_again)
        exit()
    exp_position += 1

# Iterate through list and evaluate
new_int_holder = 0
new_exp_holder = list()
new_exp_position = 0
result = 0
        
for d in exp_holder:
    if int_check(d):
        new_int_holder = d
    elif symbol_check(d):
        new_exp = math_func(d, exp_holder[new_exp_position-1], exp_holder[new_exp_positon+1])
        new_exp_holder.append(new_exp)
        new_int_holder = 0
    new_exp_position += 1
    
print(str(result))