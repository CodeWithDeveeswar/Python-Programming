# Simple Match Case Statement
num = int(input("Enter a number (1-3): "))

match num:
    case 1:
        print(1) 
    case 2:
        print(2)
    case 3:
        print(3)
    case _:
        print("Invalid Number")
# Enter a number (1-3): 4
# Invalid Number

# Enter a number (1-3): 2
# 2

print() # New line

# Example: Even Odd Number using Match Case
N = int(input("Enter a number to check Even or Odd: "))

def even_odd(N):
    match N % 2:
        case 0:
            print(N,"is Even Number")
        case 1:
            print(N,"is Odd Number")
            
even_odd(N)
# Enter a number to check Even or Odd: 7
# 7 is Odd Number
 
# Enter a number to check Even or Odd: 10
# 10 is Even Number

