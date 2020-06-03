# Problem Statement : 

# 5.2 Write a program that repeatedly prompts a user for integer numbers until
# the user enters 'done'. Once 'done' is entered, print out the largest and
# smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the
# number. Enter 7, 2, bob, 10, and 4 and match the output below.

 # Code is Written By Krishna

# The code below almost works

largest=None
smallest=None
while True:
    try:
        num =input("Enter a number: ")
        if num == "done" :
            break
        istr=int(num)
        if istr > largest:
            largest=istr
        if smallest==None:
            smallest=istr
        if istr < smallest:
            smallest=istr
    except:
        print("Invalid input")
    
        

print("Maximum is", largest)
print("Minimum is", smallest)

# Thank u so much
