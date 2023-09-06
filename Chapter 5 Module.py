# Chapter 5: The Fate of Thornfall
def chapter_5():
    print("Chapter 5: The Fate of Thornfall")
    print("Intro:")
    print("The player returns to Thornfall to warn the townsfolk about the impending danger.")
    
    print("Scene:")
    print("As you re-enter Thornfall, you can sense a heightened tension in the air.")
    print("The townsfolk go about their business, but there's an unease that lingers beneath their expressions.")
    print("With the golden sword at your side and the artifact key in hand, you make your way through the town.")
    
    choice = input("\nPlayer Actions:\n"
                   "1. Head to the main castle to alert the king of the great danger to come\n"
                   "2. Head towards the tavern to warn the townsfolk\n"
                   "3. Leave town\n"
                   "Choose your action (1, 2, or 3): ")
    
    if choice == "1":
        print("You decide to head to the main castle to alert the king of the great danger approaching Thornfall.")
        alert_king()
    elif choice == "2":
        print("You choose to head towards the tavern to warn the townsfolk about the impending threat.")
        warn_townsfolk()
    elif choice == "3":
        print("With a heavy heart, you decide to leave town. Your journey ends here.")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

def alert_king():
    print("You make your way to the main castle, where the guards are on high alert.")
    print("As you approach the front gate, the guards stop you and demand to know your business.")
    
    print("You show the guards the artifact key and explain that you've returned from the Forgotten Forests with dire news.")
    print("The guards understand the gravity of the situation and immediately allow you to enter the castle.")
    
    print("Inside the castle, you are granted an audience with the king. He eyes you with curiosity and asks, 'Who let you in and why are you here?'")
    
    print("You respectfully explain the situation, detailing the impending attack from the Lizard men and the need for Thornfall to prepare for the threat.")
    print("The king listens attentively, and a heavy silence hangs in the air as the weight of your words sinks in.")
    print("After a moment, the king speaks, 'We shall not take this threat lightly. We will rally our forces and make the necessary preparations.'")
    print("He looks at you with newfound respect, 'You have done a great service to Thornfall, and we are in your debt.'")
    print("With that, the king stands and gestures towards you, 'Join us in our preparations. We could use someone of your skills.'")
    
    join_choice = input("Will you join the preparations? (yes or no): ")
    if join_choice.lower() == "yes":
        print("With a determined nod, you accept the king's invitation to join the preparations.")
        print("The night is long as you work together with the townsfolk and soldiers, fortifying the defenses of Thornfall.")
        print("As dawn breaks, the sky starts to light up, and you can feel a sense of anticipation in the air.")
        print("Suddenly, a chorus of screams and the sound of battle erupt from the outskirts of the town.")
        print("The lizard men have arrived.")
        
        battle_choice = input("Options:\n"
                              "1. Show your skills and push ahead alone\n"
                              "2. Stay with the soldiers and fight together\n"
                              "Choose your action (1 or 2): ")
        
        if battle_choice == "1":
            print("You draw your golden sword and rush ahead, taking down several lizard men with precision and speed.")
            print("As you charge, the soldiers rally around you, covering your flanks with a volley of arrows.")
            print("However, you spot a soldier about to be ambushed from a blind spot.")
            save_choice = input("Will you save the soldier? (yes or no): ")
            if save_choice.lower() == "yes":
                print("You react swiftly, striking down the lizard man about to attack the soldier.")
                print("The soldier nods his thanks, and you continue to fight side by side.")
                print("The battle is intense, but your combined efforts are paying off.")
                print("As the last lizard man falls, you realize it's daytime, and the town is safe.")
                print("The soldiers cheer, and you all head back to town victorious.")
                celebration()
            else:
                print("The soldier's cry for help goes unanswered as you focus on the larger battle.")
                print("After the battle, the soldier approaches you, looking disappointed, and yells, 'We're a team, stop showing off and help us next time!'")
                print("The battle eventually comes to an end, and the town is safe.")
                print("The soldiers cheer and thank you for your help.")
                celebration()
        elif battle_choice == "2":
            print("You choose to stay with the soldiers, fighting side by side against the incoming lizard men.")
            print("The battle is fierce, but with your combined efforts, you manage to hold the line.")
            print("As the last lizard man falls, the sun rises, and the town is safe.")
            print("The soldiers cheer, and you all head back to town victorious.")
            celebration()
        else:
            print("Invalid choice. Please choose 1 or 2.")
    else:
        print("You politely decline the king's offer and take your leave from the castle.")
        chapter_6()  # to be continued

def warn_townsfolk():
    print("You choose to head towards the tavern to warn the townsfolk about the impending threat.")
    print("As you explain the situation to the townsfolk, you can see the fear in their eyes.")
    print("They believe you, but their morale is low, and they don't seem to have the will to fight.")
    print("Despite your warnings, the lizard men attack the town.")
    print("You and the villagers put up a valiant effort, but the odds are against you.")
    print("Unfortunately, you're overwhelmed by the lizard men's onslaught, and the town falls.")
    print("The last thing you see is the destruction around you before everything goes dark.")
    
    reset_choice = input("The town has fallen, and your journey has come to a tragic end. Do you want to reset and try again? (yes or no): ")
    if reset_choice.lower() == "yes":
        chapter_5()  # Restart Chapter 5
    else:
        print("Thank you for playing!")

def celebration():
    print("As you return to town, the townsfolk greet you with cheers and applause.")
    print("They hoist you up on their shoulders, celebrating you as the hero of Thornfall.")
    print("Tears of joy are shed, and the town bursts into a festive celebration.")
    print("You've saved Thornfall from the impending danger, and the townsfolk are eternally grateful.")
    print("The game ends, thanking you for playing.")


def chapter_6():
    print("Chapter 6 to be continued.")


chapter_5()
