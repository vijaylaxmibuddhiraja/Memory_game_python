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
    print(" Beginner")
    print(" Intermediate")
    print(" Expert")
    print(" Quit")

    choice = input("\nEnter your choice: ")

    if choice.lower == "quit":
        print("Thanks for playing! Goodbye!")
        return
    
    #to test if it works
    print(f"You selected {choice} level.")  
    
if __name__ == "__main__":
    display_intro()



