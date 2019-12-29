#prompt the user for a positive at least once
while True:
    number = int(input("Height: "))
    if number>0:
        break
    
#loop and another nested loop for the width and the height
for h in range(number):
    for w in range(number):
        if w >= number-h-1:
            print("#",end="")
        else:
            print(" ",end="")
    print()