#=====================================#
#             Calculata               #
#          by Randall Arms            #
#  @ github.com/randallarms/calculata #
#=====================================#

# Opening text
print("\n\n===================")
print(" C A L C U L A T A ")
print("===================")

# Error strings
STR_ERROR = "[ERROR] "
STR_ERROR_START = "Expression must begin with an integer or open paranthesis."
STR_ERROR_SYMBOL = "Extraneous symbols were detected."
STR_ERROR_CHAR = "One of the characters in your query is not valid."
STR_ERROR_ZERO = "Division by zero detected."
STR_ERROR_PARANTHESES = "Parantheses not properly closed."
STR_AGAIN = " Please try again."


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
            print(STR_ERROR + STR_ERROR_ZERO + STR_AGAIN)
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
                print(STR_ERROR + STR_ERROR_SYMBOL + STR_AGAIN)
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
                print(STR_ERROR + STR_ERROR_CHAR + STR_AGAIN)
                exit()
            # Add the parantheses to the expression
            exp_holder.append(c)
        else:
            print(STR_ERROR + STR_ERROR_CHAR + STR_AGAIN)
            exit()
        exp_position += 1
        
    # Check that a number or open paranthesis comes first
    if int_check(exp_holder[0]) or exp_holder[0] == "(":
        return exp_holder
    else:
        print(STR_ERROR + STR_ERROR_START + STR_AGAIN)
        exit()
        
# Iterate through list and evaluate
def evaluate(exp_holder):

    # Check that expression begins with an integer or open paranthesis
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
	
	# Iterate through expression
    for d in exp_holder:
	
        # Check that loop is caught up
        if current_exp_position >= eval_exp_position:
            # Evaluate current expression
            if symbol_check(d):
                next_d = int(exp_holder[eval_exp_position+1])
                result = math_func(d, result, next_d)
                eval_exp_position += 1
			# Parantheses detection
			elif d == "(":
				# Get inner expression
				next_exp = list()
				next_exp_position = 0
				for e in exp_holder:
					if (next_exp_position > eval_exp_position):
						if (e == ")"):
							break
						elif (next_exp_position >= len(exp_holder)-1):
							print(STR_ERROR + STR_ERROR_PARANTHESES + STR_AGAIN)
						else:
							next_exp.append(e)
							next_exp_position += 1
					# Evaluate inner expression
					inner_result = evaluate(listify(next_exp))
					result = math_func(d, result, inner_result)
					# Increment expression counter
					eval_exp_position += 1
                
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