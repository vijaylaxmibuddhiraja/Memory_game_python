import os
import random 
import time

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_intro():

    score = 0

    # Display the welcome message
    while True:   
        clear_screen()
        print("=====================================")
        print (" Welcome to the Memory Game!")
        print("=====================================")

        # Select levels
        print("\nSelect a level:")
        print("A. Beginner")
        print("B. Intermediate")
        print("C. Expert")
        print("D. Quit")

        choice = input("\nEnter your choice: ").upper()

        # WHEN QUIT the game 
        if choice == "D" or choice == "":
             confirm = input("Are you sure you want to quit? (Y/N): ").upper()
             if confirm == "Y":
                 print(f"\nYour final score is: {score}")
                 print("Thank you for playing! Goodbye!")
                 break
             else:
                 continue
             
        # START THE GAME
        #Set variables based on level
        # BEGINNER LEVEL
        if choice == "A" or choice.lower() == "beginner":
            letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            count = 5
            wait_time = 5

        # INTERMEDIATE LEVEL
        elif choice == "B" or choice.lower() == "intermediate":
            letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            count = 7
            wait_time = 7  

        # EXPERT LEVEL
        elif choice == "C" or choice.lower() == "expert":
             letter_list = ["DRAGON", "MAMOTH", "PHOENIX", "MOUNTAIN", "FOREST", "ISLAND",
             "RIVER", "OCEAN", "DESERT", "CANYON", "VALLEY", "GLACIER"]
             count = 5
             wait_time = 10   

        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)
            continue
            

        # Generate random sequence
        
        original_sequence = random.sample(letter_list, count)
        clear_screen()

        print(f"\nYour score is: {score}")
        print("===============================")

        print("\nMemorize this sequence:")
        print(" ".join(original_sequence))

        print(f"\nYou have {wait_time} seconds to memorize the sequence.")
        time.sleep(wait_time)
        clear_screen()

        #make the shuffling
        mixed_sequence = list(original_sequence)
        random.shuffle(mixed_sequence)

        #Ask the user to input the sequence
        user_input = input("Enter the correct sequence (with spaces): ").upper().split()
        
        if user_input == original_sequence:
            print("Yeyy!! You entered the correct sequence.")
            score += 10
            print(f"\nYou gained 10 points! Your total score is now: {score}")
        else:
            print("Oops! Wrong answer.")
            print(f"\nThe correct sequence was: { ' '.join(original_sequence)}")

            score -= 5
            print(f"\nYou lost 5 points. Your total score is now: {score}")
            
        time.sleep(3)
     
            
    #to test if it works
    #print(f"You selected {choice} level.")  
    
if __name__ == "__main__":
    display_intro()



