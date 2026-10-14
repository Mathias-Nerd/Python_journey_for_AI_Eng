import random

secret_number = random.randint(1,100)

def play_game(target=None, max_attempts=None):
    attempt = 0
    if not target:
        target = random.randint(1,100)

    while True:
        while True:
            try:
                guess = int(input("Guess a number between 1 and 100: ").strip())
            except ValueError:
                print("Invalid input")
                continue
            if 1 <= guess <= 100:
                break
            else:
                print("Number outside 1 - 100")
                continue
        attempt += 1
        if guess > target:
            print("too high")
        elif guess < target:
            print("too low")
        else:
            print(f"correct! you got it in {attempt} guesses")
            break
    



# Do not modify below this line
if __name__ == "__main__":
    play_game(25)
