import os
from pdb import main
import random 
import time

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_intro():
    # Display the welcome message
    print("=====================================")
    print (" Welcome to the memory game!")
    print("=====================================")

    # Select levels
    print("\nSelect a difficulty level:")
    print("A. Beginner")
    print("B. Intermediate")
    print("C. Expert")
    print("D. Quit")

    choice = input("\nEnter your choice: ")

    if choice == "A" or choice.lower() == "beginner":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        original_sequence = random.sample(alphabet, 5)

        clear_screen()

        print("\nMemorize this sequence:")
        print(" ".join(original_sequence))


        print("\nYou have 5 seconds to memorize the sequence.")
        time.sleep(5)
        clear_screen()

        #make the shuffling
        mixed_sequence = list(original_sequence)
        random.shuffle(mixed_sequence)

        #Ask the user to input the sequence
        user_input = input("Enter the correct sequence (with spaces): ").upper().split()
        if user_input == original_sequence:
            print(" You entered the correct sequence.")
        else:
            print("Oops! Wrong answer.")
            print(f"\nThe correct sequence was: { ' '.join(original_sequence)}")
        #print("Time's up!Please enter the sequence.")


    #if choice == "D" or choice.lower() == "quit":
      #  print("Thanks for playing! Goodbye!")
      #  return
    
    #to test if it works
    #print(f"You selected {choice} level.")  
    
if __name__ == "__main__":
    display_intro()



