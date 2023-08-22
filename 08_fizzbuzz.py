def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

list = []
for i in range(1,101):
    list.append(i)
    
def fizz_buzz():
    for element in list:
        result = []
        for element in range(1, 101):
            if is_prime(element):
                result.append("Prime")
            else:
                current = ""
                if element % 3 == 0:
                    current += "Fizz"
                if element % 5 == 0:
                    current += "Buzz"
                if not current:
                    current = element
                result.append(current)
        return result
 
result = fizz_buzz()
print(result)

    


# print(list)