import random
import sys

def main():

    input1 = input("Do you wanna flip a coin? [Y/N]:  ")

    if input1:
        if input1 in [ "Y", 'y']:
            coinface = random.randint(0, 1)

            input2 = input("Heads or Tails? ")

            if input2 in [ "heads", "Heads" ]:
                if coinface == 0:
                    print("You Win! The coin was heads!")
                    print(coinface)
                else:
                    print("You Lose! The coin was tails!")
                    print(coinface)
            elif input2 in [ "tails", "Tails" ]:
                if coinface == 0:
                    print("You Lose! The coin was heads!")
                    print(coinface)
                else:
                    print("You Win! The coin was tails!")
                    print(coinface)
            else:
                print("Invalid Input! Input Y or N.")
                sys.exit(0)

        elif input1 in [ "N", 'n']:
            print("Quitting...")
            sys.exit(0)
        else:
            print("Invalid Input! Input Y or N.")
            sys.exit(0)

main()
