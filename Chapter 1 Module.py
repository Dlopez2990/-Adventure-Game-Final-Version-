import random

# Function to interact with a villager
def interact_with_villager():
    # List of possible responses from the villager
    greetings = ["Hi", "Hello there", "Greetings"]
    questions = ["What brings you to our village?", "Are you here on a quest?", "Can I help you with something?"]
    offers = ["Say, are you looking to earn some coin?", "I've got a task that might pay well, if you're interested."]
    
    # List of randomly chosen villager names
    npc_name_choices = ["Dexter", "Ryan", "Dawn", "Andie"]
    
    # Randomly select a villager name
    npc_name = random.choice(npc_name_choices)
    
    print(f"{npc_name}: {random.choice(greetings)}, I am {npc_name}. {random.choice(questions)}")
    
    answer = input(f"{npc_name}: {random.choice(offers)} (Press 'y' for yes, any other key for no): ")
    
    if answer.lower() == "y":
        task = "deliver a package"  # Actual task description
        reward = random.randint(10, 50)  # Random coin reward
        print(f"{npc_name}: Excellent! I need someone to {task}. I'll reward you with {reward} coins.")
        
        package_delivered = input("Did you successfully deliver the package? (Press 'y' for yes, any other key for no): ")
        
        if package_delivered.lower() == "y":
            follow_up = input(f"{npc_name}: Well done! You've proven yourself reliable. So, what brings you here? Are you on a quest to help with the trouble in our town? (Press 'y' to tell your quest, any other key to decline): ")
            if follow_up.lower() == "y":
                print(f"{npc_name}: A hero, eh? That's impressive. We could use all the help we can get.")
                visit_options = input(f"{npc_name}: Would you like to:\n1. Visit the local tavern to gather information from townspeople?\n2. Take on tasks to earn money and supplies?\n3. Rest at the inn.\n(Press '1', '2', '3', or any other key to decline): ")
            
                if visit_options == "1":
                    print("You decided to visit the local tavern to gather information from townspeople.")
                    tavern_info = ["They say there's a dense and eerie Forgotten Forest to the east.", "Legends speak of mythical creatures and hidden dangers in the Forgotten Forest."]
                    for info in tavern_info:
                        print(f"Local Villager: {info}")
                    
                    forest_option = input("Would you like to head to the Forgotten Forest? (Press 'y' for yes, any other key to decline): ")
                    if forest_option.lower() == "y":
                        print("You've decided to head to the Forgotten Forest.")
                       
                    else:
                        print("You've chosen not to venture into the Forgotten Forest for now.")
                elif visit_options == "2":
                    print("You chose to take on tasks to earn money and supplies.")
                    task_choice = input("Here's a task for you: Gather some herbs from the nearby forest. It's a dangerous place, but the reward is worth it. Will you accept? (Press 'y' for yes, any other key to decline): ")
                    if task_choice.lower() == "y":
                        herbs_collected = random.randint(2, 5)  # Random number of herbs collected
                        herbs_reward = herbs_collected * 5  # Reward based on the number of herbs collected
                        print(f"You ventured into the forest and collected {herbs_collected} herbs. You earned {herbs_reward} coins.")
                    else:
                        print("You've declined the task for now.")
                    
                elif visit_options == "3":
                    print("You opted to rest at the inn to regain your strength.")
                    inn_option = input("While resting, you overhear tales of a dense and eerie Forgotten Forest to the east. Legends speak of mythical creatures and hidden dangers. Would you like to head to the Forgotten Forest? (Press 'y' for yes, any other key to decline): ")
                    if inn_option.lower() == "y":
                        print("You've decided to head to the Forgotten Forest.")
                        
                    else:
                        print("You've chosen not to venture into the Forgotten Forest for now.")
                else:
                    print(f"{npc_name}: Alright, let me know if you change your mind.")
            else:
                print(f"{npc_name}: Fair enough. Let me know if you change your mind.")
        else:
            print(f"{npc_name}: Oh well, maybe next time. Let me know if you decide to help.")
    else:
        quest_response = input(f"{npc_name}: Oh? What's your business here? Are you here to help with the trouble that's been plaguing our town? (Press 'y' to tell your quest, any other key to decline): ")
        if quest_response.lower() == "y":
            print(f"{npc_name}: A hero, eh? That's impressive. We could use all the help we can get.")
            visit_options = input(f"{npc_name}: Would you like to:\n1. Visit the local tavern to gather information from townspeople?\n2. Take on tasks to earn money and supplies?\n3. Rest at the inn.\n(Press '1', '2', '3', or any other key to decline): ")
            
            if visit_options == "1":
                print("You decided to visit the local tavern to gather information from townspeople.")
                tavern_info = ["They say there's a dense and eerie Forgotten Forest to the east.", "Legends speak of mythical creatures and hidden dangers in the Forgotten Forest."]
                for info in tavern_info:
                    print(f"Local Villager: {info}")
                
                forest_option = input("Would you like to head to the Forgotten Forest? (Press 'y' for yes, any other key to decline): ")
                if forest_option.lower() == "y":
                    print("You've decided to head to the Forgotten Forest.")
                    
                else:
                    print("You've chosen not to venture into the Forgotten Forest for now.")
            elif visit_options == "2":
                print("You chose to take on tasks to earn money and supplies.")
                task_choice = input("Here's a task for you: Gather some herbs from the nearby forest. It's a dangerous place, but the reward is worth it. Will you accept? (Press 'y' for yes, any other key to decline): ")
                if task_choice.lower() == "y":
                    herbs_collected = random.randint(2, 5)  # Random number of herbs collected
                    herbs_reward = herbs_collected * 5  # Reward based on the number of herbs collected
                    print(f"You ventured into the forest and collected {herbs_collected} herbs. You earned {herbs_reward} coins.")
                else:
                    print("You've declined the task for now.")
                
            elif visit_options == "3":
                print("You opted to rest at the inn to regain your strength.")
                inn_option = input("While resting, you overhear tales of a dense and eerie Forgotten Forest to the east. Legends speak of mythical creatures and hidden dangers. Would you like to head to the Forgotten Forest? (Press 'y' for yes, any other key to decline): ")
                if inn_option.lower() == "y":
                    print("You've decided to head to the Forgotten Forest.")
                    
                else:
                    print("You've chosen not to venture into the Forgotten Forest for now.")
            else:
                print(f"{npc_name}: Alright, let me know if you change your mind.")
        else:
            other_reason = input(f"{npc_name}: No worries. If you don't mind me asking, what are you doing here in our town? (Press 'y' to answer, any other key to decline): ")
            if other_reason.lower() == "y":
                player_reason = input("Please tell me more about your purpose here: ")
                print(f"{npc_name}: I see, thank you for sharing. Safe travels.")
            else:
                print(f"{npc_name}: Fair enough. Let me know if you change your mind or need assistance.")


interact_with_villager()


