from sys import argv,exit
#from cs50 import get_string

#checking if the command-line length is valid
if len(argv) != 2:
    print("Usage: python caesar.py k")
    exit(1)

#assigning the key to a variable
key = argv[1]

#checking if the key is positive integer
if not key.isalpha():
    print("k must be an alphabetic")
    exit(1)

#dict for uppercase characters
upper_pairs = {
    'A' : '0', 'B' : '1', 'C' : '2', 'D' : '3', 'E' : '4', 'F' : '5', 'G' : '6', 'H' : '7', 'I' : '8', 'J' : '9', 'K' : '10',
    'L' : '11', 'M' : '12', 'N' : '13', 'O' : '14', 'P' : '15', 'Q' : '16', 'R' : '17', 'S' : '18', 'T' : '19', 'U' : '20', 'V' : '21',
    'W' : '22', 'X' : '23', 'Y' : '24', 'Z' : '25'  
}

#dict for lowercase characters
lower_pairs = {
    'a' : '0', 'b' : '1', 'c' : '2', 'd' : '3', 'e' : '4', 'f' : '5', 'g' : '6',
    'h' : '7', 'i' : '8', 'j' : '9', 'k' : '10', 'l' : '11', 'm' : '12', 'n' : '13', 'o' : '14', 'p' : '15', 'q' : '16',
    'r' : '17', 's' : '18', 't' : '19', 'u' : '20', 'v' : '21', 'w' : '22', 'x' : '23', 'y' : '24', 'z' : '25'
}

#prompt the user for the plaintext
plaintext=input("plaintext: ")
#plaintext=get_string("plaintext: ")

#print ciphertext
print("ciphertext: ",end="")

#empty list for assigning the converted value of the given key
key_converter = []

#loop for converting key's characters into its equivalent values
for k in range(len(key)):
    if key[k].isupper():
        key_converter.append(upper_pairs.get(key[k]))
    if key[k].islower():
        key_converter.append(lower_pairs.get(key[k]))
 

#variable to iterate through the key
j=0

#loop for iterating through the plaintext and convert it
for i in range(len(plaintext)):
    
    if j==len(key):
        j=0
    
    if plaintext[i].isalpha():
        if plaintext[i].isupper():
            cipher_value = (int(upper_pairs.get(plaintext[i])) + int(key_converter[j]) ) % 26
            print(list(upper_pairs.keys())[list(upper_pairs.values()).index(str(cipher_value))],end="")
            j+=1
        
        if plaintext[i].islower():
            cipher_value = (int(lower_pairs.get(plaintext[i])) + int(key_converter[j]) ) % 26
            print(list(lower_pairs.keys())[list(lower_pairs.values()).index(str(cipher_value))],end="")
            j+=1
    
    else:
        print(plaintext[i],end="")

    