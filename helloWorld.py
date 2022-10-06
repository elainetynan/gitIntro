import datetime
# My first python program in Programming for Data Analysis
print("Check if it is a Tuesday")

today = datetime.datetime.today()
dayOfWeek = today.weekday()
if dayOfWeek == 0:
    print("It is Monday")
elif dayOfWeek == 1:
    print("It is Tuesday")
elif dayOfWeek == 2:
    print("It is Wednesday")
elif dayOfWeek == 3:
    print("It is Thursday")
elif dayOfWeek == 4:
    print("It is Friday")
elif dayOfWeek == 5:
    print("It is Saturday")
elif dayOfWeek == 6:
    print("It is Sunday")
else:
    print("What happened????")