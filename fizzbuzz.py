# add your code here

numbers = list(range(1,101))

for x in numbers:
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)