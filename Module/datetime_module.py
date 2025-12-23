import datetime

x = datetime.datetime.now()
print(x)                # prints current date and time 

print(x.year)           # prints year

print(x.strftime("%Y")) # prints year with century

print(x.strftime("%y")) # prints year without century

print(x.strftime("%A")) # Full weekday name

print(x.strftime("%a")) # prints short weekday name

print(x.strftime("%B")) # Full month name    

print(x.strftime("%b")) # prints short month name

print(x.strftime("%d")) # Day of the month

print(x.strftime("%m")) # Month as a number


