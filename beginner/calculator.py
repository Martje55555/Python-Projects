import os

# Calculator
def addition ():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0 #Total number enter
    ans = 0

    while n != 0:
        ans += n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

def subtraction ():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Subtraction")
    n = float(input("Enter the number: "))
    t = 0 #Total number enter
    ans = n
    n = float(input("Enter another number (0 to calculate): "))
    while n != 0:
        if n == 0.0: return [ans,t]
        ans = ans - n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
        print('this is n: ', n)
    return [ans,t]

def multiplication ():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0 #Total number enter
    ans = 1

    while n != 0:
        ans = ans * n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

def average():
    os.system('cls' if os.name=='nt' else 'clear')
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

# main...

while True:
    list = []
    print(" Simple Calculator in python!")
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")

    c = input(" ")

    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, invilid character")
    else:
        break