from datetime import date
import sys 

today = date.today()

print(today)
print(today.day)
print(today.year)
print(date.weekday(today))

# Getting name
name = sys.argv[1]

# Getting phone
phone = sys.argv[2]

# Getting email
email = sys.argv[3]

# Getting salary
print(sys.argv[4])
salary = int(sys.argv[4])

# Getting percent to incremet
percent = int(sys.argv[5])
increment =  salary * (percent) / 100


print(f"User data: Name: {name}, phone: {phone}, email: {email}, salary: {salary}, percent to increment: {percent}%")

#Calculating new salary
salary += increment
print(f"New salary: {salary}")