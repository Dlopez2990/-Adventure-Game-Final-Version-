import random

# Chapter 4: Unraveling the Secrets
def chapter_4():
    print("Chapter 4: Unraveling the Secrets")
    print("Intro:")
    print("The player unravels the mysteries surrounding the artifact and the dark shadow, heading towards ancient ruins.")
    
    print("Scene:")
    print("You stand before the entrance of the ancient ruins, the air heavy with a sense of history and foreboding.")
    print("The path ahead is dimly lit, and shadows dance on the walls, whispering secrets of bygone eras.")
    
    choice = input("\nPlayer Actions:\n"
                   "1. Explore the ancient ruins\n"
                   "2. Head out of the ancient ruins to return to the Forgotten Forest (Chapter 3)\n"
                   "Choose your action (1 or 2): ")
    
    if choice == "1":
        print("You cautiously step into the ancient ruins, your heart racing as you delve deeper into the unknown.")
        explore_ruins()
    elif choice == "2":
        print("You decide to head out of the ancient ruins and return to the Forgotten Forest, your instincts guiding you back.")
        chapter_3()
    else:
        print("Invalid choice. Please choose 1 or 2.")


def chapter_3():
    print("Chapter 3 content goes here.")
    
def explore_ruins():
    print("As you explore the ancient ruins, you feel an uneasy tension in the air.")
    print("The passages wind and twist, revealing murals of forgotten legends and inscriptions in a language you can't decipher.")
    
    quiet_option = input("\nOptions:\n"
                         "1. Move as quietly as possible\n"
                         "2. Keep walking without being cautious\n"
                         "Choose your action (1 or 2): ")
    
    if quiet_option == "1":
        print("You move as quietly as possible, trying to avoid alerting any potential dangers within the ruins.")
        ambush_warning()
    elif quiet_option == "2":
        print("You continue walking without being cautious, hoping to uncover the secrets of the ruins.")
        ambush()
    else:
        print("Invalid choice. Please choose 1 or 2.")

def ambush_warning():
    print("As you stealthily navigate the ruins, you pick up on subtle sounds and vibrations.")
    print("Your instincts warn you of an impending danger.")
    print("You gain knowledge that a surprise attack from the Lizard men is being planned to target Thornfall.")
    
    choice = input("\nOptions:\n"
                   "1. Follow the key deeper into the ruins\n"
                   "2. Leave the ruins to return to Thornfall and warn the townsfolk\n"
                   "Choose your action (1 or 2): ")
    
    if choice == "1":
        print("You decide to follow the key deeper into the ruins, determined to uncover more secrets.")
        continue_deeper()
    elif choice == "2":
        print("With the knowledge of the impending attack, you choose to leave the ruins and hurry back to Thornfall.")
        print("Your heart heavy with the weight of the impending danger, you make your way back to the town.")
        chapter_3()
    else:
        print("Invalid choice. Please choose 1 or 2.")

def continue_deeper():
    print("You follow the key as it leads you through the intricate passageways of the ruins.")
    print("The air grows colder and more suffused with ancient magic.")
    print("As you venture deeper, the secrets of the ruins and the artifact become more palpable.")
    print("Suddenly, the key in your pocket starts to glow faintly.")
    print("Before you can react, the key flies out of your pocket and hovers in front of you.")
    print("It then connects to a small, ornate slot in the wall.")
    
    choice = input("\nOptions:\n"
                   "1. Turn the key\n"
                   "2. Leave the key and leave the ruins\n"
                   "Choose your action (1 or 2): ")
    
    if choice == "1":
        print("With a deep breath, you turn the key in the slot.")
        print("A faint rumbling echoes through the ruins as the key turns, and a hidden passage is revealed.")
        print("You step through the passage and find a treasure chest.")
        print("Inside the chest, you discover a magnificent golden sword and a pouch containing 1,000 coins.")
        print("Feeling triumphant, you leave the ruins with your newfound treasure.")
        print("As you exit the ruins, you race back to Thornfall to warn the townsfolk of the impending danger.")
        
    elif choice == "2":
        print("You decide to leave the key for now and leave the ruins, your curiosity held at bay.")
        print("The key returns to your side, and you make your way out of the ruins.")
        chapter_3()
    else:
        print("Invalid choice. Please choose 1 or 2.")


chapter_4()
