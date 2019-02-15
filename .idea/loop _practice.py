
def reverse_string(str):
    rstr = ""
    index = len(str) - 1
    for letter in str :
        if str[-1]:
            rstr += str[index]
            index -= 1
    return rstr

print(reverse_string("This will be reversed!"))

hobbies = []
for i in range(3):
    hobby = input("Enter one of your favorite hobbies: ")
    hobbies.append(hobby)
print(hobbies)

def factorial_one(num):
    count = 1
    for i in range(num):
        if num < 2:
            return 1
        else:
            count = count * (i + 1)
    return count

print(factorial_one(4))

def main():
    number = int(input("Enter a number: "))
    print("The factorial for", number, "is", factorial(number))

def factorial(num):
    fac = 1
    while num >= 1:
        fac = fac * num
        num -= 1
    return fac

main()

def is_prime():
    num = int(input("Enter a number: "))
    for i in range(2, int(num/2)):
        if num % i == 0:
            print("not a prime number")
            break
    else:
        print("prime number")

is_prime()