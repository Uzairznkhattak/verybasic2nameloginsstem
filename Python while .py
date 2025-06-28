print('name')      #prints the string name 
name = input().lower()     #asks for input from the user and saves it in the variable name
while True:        #makes the while statement True for ever until made false
    if name == 'Uzair':    # check if the string variable is equal to the string uzair
        print('welcome back ' + name + ', please write down your password')  # if its equal to uzair, prints this
        password = input()   # asks for input
        if password == 'uzair123':    # checks if the string password equals uzair123
            print("you've successfully login") # if equal to it, prints this
            break         # when it was success, it breaks out the while loop here and goes out
        else:     #   if the password variable string is not equal to uzair123, it prints this.
            print('wrong password')
    elif name == 'Umair': # checks if the string in the variable given by the user is this
        print('welcome back' + name + ' please write down your password') # prints if equal
        password = input()  # asks for the input and saves in variable
        if password == 'umair123': #if true, prints the following line
            print("you've' logged in")
            break # breaks the while loop 
        else:
            print('wrong password')
    else: # if the name wasnt uzair or Umair, prints the following line and goes back to the while loop until the string matches
        print(name, 'Username not available, please write again')
        name = input().lower()
        