#=====================================#
#             Calculata               #
#          by Randall Arms            #
#  @ github.com/randallarms/calculata #
#=====================================#

# Opening text
print("\n\n=========")
print("CALCULATA")
print("=========")

# Checks that the input n is an integer
def int_check(n):
    try:
        integer = int(n)
		return true
    except ValueError:
		return false
		
def symbol_check(c):
	symbols = []
	if (c in symbols):
		return true
	else:
		return false

# Input the expression
i = input("\nEnter expression:  ");

# Evaluate the expression
print("\nEvaluating expression: ")

int_holder = 0
exp_holder = 0
result = 0

for c in i:
	if (int_check(c)):
		d = int(c)
		if (int_holder == 0):
			int_holder = d
		else:
			int_holder += d
	elif (symbol_check(c)):
		if (exp_holder == 0):
			exp_holder = int_holder
		else:
			exp_holder = str(exp_holder) + c
	else:
		print("[ERROR] One of the characters in your query is not valid. Please try again. ")
		exit()
	print(result)