import random

# Chapter 3: Deep Roots
def chapter_3():
    print("Chapter 3: Deep Roots")
    print("Intro:")
    print("The player is deep into the Forgotten Forest, and the ground is covered in fog, creating an eerie atmosphere.")
    
    player_has_key = random.choice([True, False])  # Simulating whether the player has the key or not
    
    if player_has_key:
        print("Scene:")
        print("You feel a peculiar sensation as you continue through the dense mist.")
        print("The key you acquired earlier begins to shake, as if it's leading you somewhere.")
        print("The fog swirls around you, and a path starts to form before you, guided by the shaking key.")
        
        choice = input("\nPlayer Actions:\n"
                       "1. Follow the shaking key towards the artifact (Chapter 4)\n"
                       "2. Head South to cut waves of vines and encounter a poison Ivy plant\n"
                       "3. Head North to return to Thornfall (Chapter 2)\n"
                       "Choose your action (1, 2, or 3): ")

        if choice == "1":
            print("You decide to follow the shaking key towards the artifact. You're one step closer to uncovering the mysteries of the forest.")
            
            friendly_banshee()
            
        elif choice == "2":
            print("You head South, ready to cut through waves of vines. As you progress, you encounter a menacing poison Ivy plant.")
            fight_poison_ivy()
            
        elif choice == "3":
            print("You decide to head North, back towards Thornfall. Your journey takes you back through familiar terrain.")
            chapter_2()
            
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

    else:
        print("Scene:")
        print("As you continue through the dense mist, an unsettling howl slices through the air.")
        print("The spectral figure of the Banshee reappears before you, her mournful eyes fixed on yours.")
        print("She is a creature of both beauty and sorrow, her voice echoing with tales of a tragic past.")
        
        choice = input("\nPlayer Actions:\n"
                       "1. Engage the Banshee in conversation\n"
                       "2. Attempt to move past the Banshee and continue your journey\n"
                       "Choose your action (1 or 2): ")

        if choice == "1":
            print("You decide to engage in conversation with the Banshee, hoping to learn more about her and the forest's history.")
            banshee_conversation()
            
        elif choice == "2":
            print("You choose to attempt to move past the Banshee and continue your journey through the mist-shrouded woods.")
            continue_journey()
            
        else:
            print("Invalid choice. Please choose 1 or 2.")


def chapter_2():
    print("Chapter 2 content goes here.")
    
def chapter_4():
    print("Chapter 4 content goes here.")
    
def fight_poison_ivy():
    print("Fight with the poison Ivy plant begins!\n")
    
    player_health = 100
    poison_ivy_health = 50  # poison Ivy's health to be weaker
    poison_ivy_attack = 10  
    
    while player_health > 0 and poison_ivy_health > 0:
        print("Your Health:", player_health)
        print("Poison Ivy's Health:", poison_ivy_health)
        print("\nOptions:")
        print("1. Attack")
        print("2. Defend")
        
        choice = input("Choose your action (1 or 2): ")
        
        if choice == "1":
            player_damage = random.randint(15, 30)  # Player's damage range
            
            print("You attack the Poison Ivy plant and deal", player_damage, "damage!")
            poison_ivy_health -= player_damage
            
            if poison_ivy_health > 0:
                poison_ivy_damage = random.randint(5, 15)  # Poison Ivy's damage range
                print("The Poison Ivy plant attacks you and deals", poison_ivy_damage, "damage!")
                player_health -= poison_ivy_damage
            
        elif choice == "2":
            poison_ivy_damage = random.randint(5, 15)  # Poison Ivy's damage range
            player_damage_reduction = random.randint(5, 15)
            
            print("You choose to defend against the Poison Ivy's attack.")
            print("The Poison Ivy plant attacks you and deals", poison_ivy_damage, "damage!")
            print("Your defense reduces the damage by", player_damage_reduction)
            
            player_health -= max(0, (poison_ivy_damage - player_damage_reduction))
            
        else:
            print("Invalid choice. Please choose 1 or 2.")
    
    if player_health <= 0:
        print("You have been defeated by the Poison Ivy plant.")
    else:
        print("You have defeated the Poison Ivy plant!")
        chapter_4()

def banshee_conversation():
    print("Banshee conversation content goes here.")
    
def continue_journey():
    print("Continuation of the journey content goes here.")
    
def friendly_banshee():
    print("You continue to follow the shaking key through the forest. Suddenly, a friendly Banshee appears before you.")
    print("She smiles gently and speaks in a soothing voice.")
    print("Friendly Banshee: 'Fear not, traveler. The key you have found is leading you to your destined path.")
    print("You will find glory and honor, or perhaps a more peaceful end. Embrace the journey.'")
    
    choice = input("\nPlayer Actions:\n"
                   "1. Thank the Banshee and continue on the path\n"
                   "2. Ask the Banshee for more guidance\n"
                   "Choose your action (1 or 2): ")
    
    if choice == "1":
        print("You thank the Banshee for her words and continue following the shaking key with renewed determination.")
        chapter_4()
    elif choice == "2":
        print("You ask the Banshee for more guidance, seeking a clearer understanding of your path.")
        print("Friendly Banshee: 'The journey holds its mysteries, and I can only offer cryptic guidance.'")
        print("Friendly Banshee: 'Remember, every choice shapes your destiny. Embrace the unknown.'")
        choice = input("\nPlayer Actions:\n"
                       "1. Thank the Banshee and continue on the path\n"
                       "Choose your action (1): ")
        if choice == "1":
            print("You thank the Banshee and continue following the shaking key, your heart and mind focused on the adventure ahead.")
            chapter_4()
        else:
            print("Invalid choice. Please choose 1.")
    else:
        print("Invalid choice. Please choose 1 or 2.")


chapter_3()
