import random

#Guess a number game

random_num = random.randint(1, 20)
def guess_number():
    num_of_guesses = 0
    while num_of_guesses <= 5:
        user_num = int(input("Enter a number between 1 and 20: "))
        num_of_guesses += 1
        if user_num == random_num:
            print("Congratulations, you guessed the right number in this amount of guesses:", num_of_guesses)
            break
        elif user_num < 0 or user_num > 20:
            print("Your number is outside the required range.")
        elif user_num > random_num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
    else:
        print("Sorry, you ran out of guesses. The correct number is", random_num)
    return num_of_guesses

guess_number()


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