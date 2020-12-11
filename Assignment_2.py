# Create the below pattern using nested for loop in Python.
#                         *
#                         * *
#                         * * *
#                         * * * *
#                         * * * * *
#                         * * * *
#                         * * *
#                         * *
#                         *

# HERE WE ARE USING THE FOR LOOP FOR PRINTING THE FIRST 5 ROWS
for i in range(1,6):
    # HERE WE ARE USING FOR LOOP FOR PRINTING THE STARTS IN EACH AND EVERY ROW ACCORDING TO THEIR ROW NUMBER
    for j in range(0,i):
        print("*",end=" ")
    print() 

# HERE WE ARE USING THE FOR LOOP FOR PRINTING MORE 4 ROWS 
for i in range (5, 1, -1):
    # HERE WE ARE USING FOR LOOP FOR PRINTING THE STARS IN EACH AND EVERY ROWS WITH DECREASING ORDER
    for j in range(0, i -1):
        print("*", end=" ")
    print()







# WEITR A PROGRAM TO REVERSE A WORD

# HERE WE ARE TAKING THE INPUT FROM USER BY USING "INPUT" KEYWORD 
a = input("Enter the name that you want to Reverse :")

# HERE WE ARE PRINTING THE WORD THAT WE WANT TO REVERSE
print(f"NAME IS : {a}")

# HERE WE ARE PRINTING REVERSE ORDER
print(f"REVERSE OF NAME IS : {a[::-1]}")