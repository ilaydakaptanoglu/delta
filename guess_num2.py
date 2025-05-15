guesses = 0
ok = False
a = 1
b = 100

print("H: Guess the number")
guess = 50
while ok == False:
    print(f"C: {guess}")
    human_answer = input("H: (S/B/Q): ").lower()
    if human_answer == 's':
        a = (a+b)//2
    elif human_answer == 'b':
        b = (a+b)//2
    else: ok = True
    guess =  (a+b)//2
    guesses += 1
print(f"You Guessed in {guesses} trials! ")