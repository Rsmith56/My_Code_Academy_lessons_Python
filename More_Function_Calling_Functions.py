# More Functions Calling Functions
def cube(number):
    return number**3
# The "by_three" function calls the "cube(number)" function below 
# Note the "%" modulo yields the remainder. If no remainder == 0 (10 % 5 == 2)
# "%" means find the remainder of a division operation
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False  

# Addtional notes: don't forget indentation and : after def, if, and else statements
