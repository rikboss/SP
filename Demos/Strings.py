# manual increase/decrease - adding spaces and characters for each line using a loop
mystring = ''  # initial string
size = 4  # size, could also be input from user
for i in range(0, size):  # loop first part
    for j in range(i, size - 1):
        mystring += ' '  # adding a space to the string
    for j in range(0, i + 1):
        mystring += '*'  # adding a * to the string
    print(mystring)  # printing string
    mystring = ''  # resetting string
for i in range(size - 1, 0, -1):  # loop second part
    for j in range(i, size):
        mystring += ' '  # adding a space to the string
    for j in range(0, i):
        mystring += '*'  # adding a * to the string
    print(mystring)  # printing string
    mystring = ''  # resetting string

# using str.format() to add padding, manually building the main string
mystring = '' #initial string
size = 4 #size, could also be input from user
for i in range(0,size): #loop first part
    mystring += '*' #adding a * to the string
    print('{:>{}}'.format(mystring,size)) # printing with padding
for i in range(size-1,0,-1): #loop second part
    mystring = mystring[:-1] #removing a character * from the string
    print('{:>{}}'.format(mystring,size)) # printing with padding

# using f-strings to add padding, manually building the main string
mystring = '' #initial string
size = 4 #size, could also be input from user
for i in range(0,size): #loop first part
    mystring += '*' #adding a * to the string
    print(f'{mystring:>{size}}') # printing with padding
for i in range(size-1,0,-1): #loop second part
    mystring = mystring[:-1] #removing a character * from the string
    print(f'{mystring:>{size}}') # printing with padding