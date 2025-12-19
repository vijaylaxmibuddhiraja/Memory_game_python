import os
import random 
import time

def clear_screen():
   #Clears the terminal screen.
    os.system('cls' if os.name == 'nt' else 'clear')

def display_intro():

    # Display the welcome message  
        clear_screen()
        print("=====================================")
        print("=====================================")
        print (" Welcome to the Memory Game!")
        print("=====================================")
        print("=====================================")

       # Display player name 
        player_name = input("\nEnter your name: ").strip()

        clear_screen()
        print(f"\nHello, {player_name}! Get ready to test your memory skills.")
  
        time.sleep(2)

        score = 0  # Initialize score
    
        while True:
            clear_screen()
            # Select levels
            print(f"\n{player_name}, Let's begin the game!")
            print(f"Select your level")     
            print("A. Beginner")
            print("B. Intermediate")
            print("C. Expert")
            print("D. Quit")

            choice = input("\nEnter your choice: ").upper()
            
            # WHEN QUIT the game 
            if choice == "D" or choice == "":
                confirm = input("Are you sure you want to quit? (Y/N): ").upper()
             
                if confirm == "Y":
                    clear_screen()
                    print(f" Goodbye, {player_name}!")
                    print(f"\nYour final score is: {score}")
                    print("Thank you for playing!")
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
                letter_list = ["DRAGON", "MAMMOTH", "PHOENIX", "MOUNTAIN", "FOREST", "ISLAND",
                "RIVER", "OCEAN", "DESERT", "CANYON", "VALLEY", "GLACIER"]
                count = 5
                wait_time = 10   

            else:
               print("Invalid choice. Please try again.")
               time.sleep(2)
               continue

            # Start the game loop for the selected level
            while True:    
                # Generate random sequence
                original_sequence = random.sample(letter_list, count)
                clear_screen()

                #print(f"\nYour score is: {score}")
                #print("===============================")

                print("\nThe original sequence is:")
                print(" ".join(original_sequence))

                print(f"\nYou have {wait_time} seconds to memorize the sequence.")
                # time.sleep(wait_time)
        
                #countdown timer
                for i in range(wait_time, 0, -1):
                    print(f"Time remaining: {i} seconds", end='\r')
                    time.sleep(1)

                clear_screen()

                #make the shuffling
                mixed_sequence = list(original_sequence)
                random.shuffle(mixed_sequence)

                #Ask the user to input the sequence with option to quit
                print("\nEnter the correct sequence (with spaces): ")
                user_input = input("\nYour answer: ").upper()

                # Process user input
                user_input_list = user_input.split()

                clear_screen()
           
                # Check if the user's input matches the original sequence
                if user_input_list == original_sequence:
                    print("Yeyy!! You entered the correct sequence.")
                
                    score += 10  # Add 10 points
                
                    print(f"\nYou gained 10 points! Your total score is now: {score}")

                else:
                    print("Oops! Wrong answer.")
                    print(f"\nThe correct sequence was: { ' '.join(original_sequence)}")

                    score -= 5 # Deduct 5 points
                
                    print(f"\nYou lost 5 points. Your total score is now: {score}")

                print("\n===================================")

                # Ask to continue to the next round
                print(f"\n{player_name}, What would you like to do next?")
                print("1.Play next round")
                print("2. Return to main menu")
           
                next_choice = input("\nEnter your choice: ")
            
                if next_choice == "2":
                    print(f"\nReturning to main menu...")
                    time.sleep(3)
                    break 
           
                elif next_choice == "1":
                    print("\nGet ready for the next round!")
                    time.sleep(3)
                    continue
                else:
                    print("Invalid choice. Continue playing..")
                    time.sleep(3)
                    continue
          

    #to test if it works
    #print(f"You selected {choice} level.")  
    
if __name__ == "__main__":
    display_intro()



