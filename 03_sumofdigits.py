print("Please enter a number.")
number = input()
digits = [int(d) for d in str(number)]
result = 0
for digit in digits:
    result = result + digit
print(result)