from sys import argv, exit
#from cs50 import get_string

def main():

    # check if the command line arguments are correct
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    # assign the file to a variable
    banned_file = argv[1]

    # open the file to perform operations
    f = open(banned_file, "r")
    
    # empty set to accept the words in the file
    container_set = set()

    # loop to assign every line to a set
    for line in f:
        container_set.add(line.rstrip("\n"))
    
    # prompt the user for a message
    user_message = input("What message would you like to censor?")

    # make every word in the message as a separated member in a list 
    words = user_message.split(" ")
    items = "*"

    # iterate through every word in the list to check if it's in the file or not
    for word in words:
        if word.lower() in container_set:
            
            #assignment with no reason :'D
            tmp_length = len(word)
            
            tmp_items = items * len(word)
            user_message = user_message.replace(word, tmp_items)
    
    # print the censored word
    print(user_message)


if __name__ == "__main__":
    main()