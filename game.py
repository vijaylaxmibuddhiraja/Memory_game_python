import os
import random 
import time

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_intro():
    # Display the welcome message
    while True:   
        clear_screen()
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

        # QUITTING the game 
        if choice == "D" or choice.lower() == "quit":
             confirm = input("Are you sure you want to quit? (Y/N): ").lower()
             if confirm == "y":
                 print("Thank you for playing! Goodbye!")
                 break
             else:
                 continue
             

        # BEGINNER LEVEL
        if choice == "A" or choice.lower() == "beginner":
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            count = 5
            wait_time = 5

        # INTERMEDIATE LEVEL
        elif choice == "B" or choice.lower() == "intermediate":
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            count = 7
            wait_time = 7  

        # EXPERT LEVEL
        elif choice == "C" or choice.lower() == "expert":
            alphabet = "DRAGON", "MAMOTH", "PHOENIX", "MOUNTAIN", "FOREST", "ISLAND",
            "RIVER", "OCEAN", "DESERT", "CANYON", "VALLEY", "GLACIER"
            count = 5
            wait_time = 10     
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)
            continue

        original_sequence = random.sample(alphabet, count)

        clear_screen()

        print("\nMemorize this sequence:")
        print(" ".join(original_sequence))


        print("\nYou have {wait_time} seconds to memorize the sequence.")
        time.sleep(wait_time)
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

        input("\nPress Enter to return to main menu..")       
        #print("Time's up!Please enter the sequence.")


    
    
    #to test if it works
    #print(f"You selected {choice} level.")  
    
if __name__ == "__main__":
    display_intro()



