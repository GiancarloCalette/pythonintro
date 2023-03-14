print("Hello world!")
name = "Giancarlo"
last_name ="Calette"
age = 101
total = 15.22
found = False
print(name)
print(last_name)
print(age)
print(total)
print(found)

print(name + last_name)

if age<100:
    print("Dont worry you are young")
    print("We still in the if statement")
elif age == 100:
    print("Congratulations, you got to live a century")
else:
    print("Sorry, you are getting old")
print("Outside of the if")

def say_Hello():
    print("Hello there")
    print("print a function")

say_Hello()

def say_hi(name):
    print("Hi" + name)

def get_day():
    return "Friday"
say_hi("Luis")
say_hi(name)

day = get_day()
print("Today is " + day)
