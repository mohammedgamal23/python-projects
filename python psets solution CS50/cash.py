# prompt the user for a positive at least once and catching a potential error
try:
    while True:
        number = float(input("Change owed: "))
        if number > 0:
            break
except(ValueError):
    print("Invalid input, please use numerical values")

# making it big int
number_modified = int(number *100) 

# some helper variables
quarter = 25
dime = 10
nickel = 5
penny = 1
coins_counter = 0

# check for how many quarters available
while(number_modified >= quarter):
    coins_counter += 1
    number_modified = number_modified - quarter

# check for how many dimes available
while(number_modified >= dime):
    coins_counter += 1
    number_modified = number_modified - dime

# check for how many nickels available
while(number_modified >= nickel):
    coins_counter += 1 
    number_modified = number_modified - nickel

# check for how many pennies available
while(number_modified >= penny):
    coins_counter += 1
    number_modified = number_modified - penny

# print the number of coins
print(coins_counter)