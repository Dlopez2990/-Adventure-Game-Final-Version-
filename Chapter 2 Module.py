import random

def handle_banshee_encounter():
    print("You follow the whisper and face a Banshee.")
    print("Player Actions:")
    print("1. Stand your ground and face the Banshee.")
    print("2. Attempt to flee.")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        outcome = random.choice(["win", "lose"])
        
        if outcome == "win":
            print("You defeat the Banshee and find a key.")
            follow_key_option()
        else:
            print("The Banshee's power overwhelms you.")
            print("Player Actions:")
            print("1. Try again.")
            print("2. Return to Thornfall.")
            
            choice_try_again = input("Enter your choice: ")
            
            if choice_try_again == "1":
                print("You gather your resolve and face the Banshee again.")
                handle_banshee_encounter()
            elif choice_try_again == "2":
                print("You retreat and return to Thornfall.")
            else:
                print("Invalid choice.")
            
    elif choice == "2":
        print("You attempt to flee but the Banshee's wail follows you.")
        print("Player Actions:")
        print("1. Turn back and retrace your steps.")
        print("2. Look into the mist.")
        
        choice_flee = input("Enter your choice: ")
        
        if choice_flee == "1":
            print("You turn back and retrace your steps.")
            original_spot_options()
        elif choice_flee == "2":
            print("You look into the mist and see large shadows.")
            print("Your instincts tell you it's not wise to continue.")
            original_spot_options()
        else:
            print("Invalid choice.")

def follow_key_option():
    choice = input("The key is shaking. Do you want to follow it? (y/n): ")
    
    if choice.lower() == "y":
        print("The key leads you through dense undergrowth and mysterious paths.")
        print("As you go deeper, the forest seems to become even more enchanted and eerie.")
        print("Continue the story with the deeper forest section.")
    elif choice.lower() == "n":
        original_spot_options()
    else:
        print("The key leads you through dense undergrowth and mysterious paths.")
        print("As you go deeper, the forest seems to become even more enchanted and eerie.")
        print("Continue the story with the deeper forest section.")

def original_spot_options():
    print("Player Actions:")
    print("1. Follow the mysterious whisper (encounter Banshee fight - win or lose).")
    print("2. Attempt to head East (leads to a dead end on a cliffside).")
    print("3. Head North to return to Thornfall.")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        handle_banshee_encounter()
    elif choice == "2":
        print("You head east but find a dead end on a cliffside.")
        original_spot_options()
    elif choice == "3":
        print("You return to Thornfall.")
    else:
        print("Invalid choice.")

def chapter_two_journey():
    print("Chapter 2: Journey to the Forgotten Forest")
    print("Intro: The player ventures into the dense and eerie Forgotten Forest.")
    original_spot_options()

chapter_two_journey()
