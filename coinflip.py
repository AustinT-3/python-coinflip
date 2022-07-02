import random
import sys

def main():

    input1 = input("Do you wanna flip a coin? [Y/N]:  ")

    if input1:
        if input1 in [ "Y", 'y']:
            coinface = random.randint(0, 1)

            input2 = input("\nHeads or Tails? ")

            if input2 in [ "heads", "Heads" ]:
                if coinface == 0:
                    print("\nYou Win! The coin was heads!")
                else:
                    print("\nYou Lose! The coin was tails!")
            elif input2 in [ "tails", "Tails" ]:
                if coinface == 0:
                    print("\nYou Lose! The coin was heads!")
                else:
                    print("\nYou Win! The coin was tails!")
            else:
                print("Invalid Input! Input Y or N.")
                sys.exit(0)
            
            quitgame = input("Play Again? [Y/N]:  ")
            if quitgame in [ "Y", 'y']:
                print("\n")
                main()
            else:
                print("Quitting...")
                sys.exit(0)

        elif input1 in [ "N", 'n']:
            print("\nQuitting...")
            sys.exit(0)
        else:
            print("\nInvalid Input! Input Y or N.")
            sys.exit(0)

main()
