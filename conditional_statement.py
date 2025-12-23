# If, Elif, Else
marks = 45 # Fail

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

print() # New line

# Nested If
age = 18
has_licence = 'yes' # you can drive

if age >= 18:
    if has_licence == 'yes':
        print("you can drive")
    else:
        print("go and take licence")
else:
    print("you are too young to drive")

print() # New line

# If, Else using 'and'
mark = 55
attendance = 76 # Alloweded for exam

if mark >= 55  and attendance >= 70:
    print("Alloweded for exam")
else:
    print("Not alloweded for exam")

print() # New line

# Use case 1
recharge_amount = 200
data_balance = 1.5 # you are eligible for bonus data

if recharge_amount >= 399 or data_balance >= 1:
    print("you are eligible for bonus data")
else:
    print("you are not eligible")

print() # New line

# Use case 2
# Hard Code
order_amount = 1000
days = 'mon'
membership = 'gold' # 20% discount

if (order_amount >= 1000 and days in ['sat', 'sun']) or membership =='gold':
    print("20% discount")
else:
    print("No discount")



