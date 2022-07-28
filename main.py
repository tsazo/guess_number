import random

def guess(x):
  random_number = random.randint(1, x)
  guess = 0

  while guess != random_number:
    guess = int(input(f"Guess a whole number between 1 and {x}: "))
    print(guess)

    if guess < random_number:
      print("Sorry, guess again. Too low.")
    elif guess > random_number:
      print("Sorry, guess again. Too high.")
  
  print(f"You got it right! You guessed the number {random_number} correctly!")

def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  
  while feedback != 'c':
    guess = random.randint(low, high)
    feedback = input(f"is {guess} too high (H), too low (L), or correct (C)? ").lower()

    if feedback == 'h':
      high = guess - 1
      guess = random.randint(low, high)
    elif feedback == 'l':
      low = guess + 1
      guess = random.randint(low, high)

  print(f'Computer guessed your number {guess}!')


def main():
  print("First, you guess the computer's number.")
  randint = random.randint(10,50)
  guess(randint)

  num = input("Now, your turn! Your number is between 1 and what other number?: ")
  computer_guess(int(num))

if __name__ == "__main__":
  main()