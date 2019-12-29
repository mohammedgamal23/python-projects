#prompt the user for a positive at least once
while True:
    try:
        number = int(input("Height: "))
    except (ValueError):
        print("Invalid input")
    if number>0:
        break
    

#loop and another nested loop for the width and the height
for h in range(number):

    #loop for the left pyramid
    for w in range(number):
        if w >= number-h-1:
            print("#",end="")
        else:
            print(" ",end="")
    
    #loop for the between spaces
    for space in range(number):
        print("  ",end="")

    #loop for the right pyramid
    for second_width in range(number):
        if second_width <=h:
            print("#",end="")
        else:
            print(" ",end="")
            
    print()
    
