import random
secret_num = random.randint(1, 100) #the computer thinks a number
guesses = 0
a = 1
b = 100
my_guess = int(input("Guess the number: "))
while secret_num != my_guess:
    if secret_num > my_guess:
        print(f"{my_guess} is too small!")
    if secret_num < my_guess:
        print(f"{my_guess} is too big!")
    my_guess = int(input("Guess the number: "))
    guesses += 1

print(f"You guessed in {guesses} trials!")