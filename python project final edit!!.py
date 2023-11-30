import sys
player_name = ""
title="THE CURSED CASTLE"
x=title.center(100)
print(x)
print("\n")
print("outside the cursed castle lived a knight just as old as time.")
print("he howled 'STAY AWAY! STAY AWAY! IF YOU WANT TO LIVE' the mother told her children")
print("go to sleep now! or the old knight will take you to the cursed castle! ")
print("the lore of the cursed castle goes beyond mere tales that mortals tell each other")
print("treasure or tragedy what will it be?")
print("will there ever be an adventurer who seeks the cursed castle and returns alive? only time can tell.")
print("\n")


def stage1():
    global player_name  
    print("\n")
    print("STAGE 1: THE ESCAPE")
    print("\n")
    print("Welcome to the Adventure Game!")
    print("As a professional adventurer, you have decided to visit the cursed castle but find yourself in the maze of doom.")
    print("However, during your exploration, you find yourself utterly lost.")
    print("You see a signboard that states that there exists an escape route.")
    print("With newfound hope, you start moving, and you now find multiple routes in front of you.")
    print("\n")
    if not player_name:
        player_name = input("Let's start with your name:\n")
        print(f"Good luck, adventurer {player_name}.")
    
    intro_scene()

def intro_scene():
    print("You find yourself at crossroads, and you can choose to go down any of the four pathways. Remember your life depends on your choice. Now where would you like to go?")
    
    while True:
        user_input = input("Options: left/right/forward\n")
        if user_input == "left":
            show_shadow_figure()
            break
        elif user_input == "right":
            show_skeletons()
            break
        elif user_input == "forward":
            haunted_room()
            break
        else:
            print("Option invalid! Please enter a valid option.")


def show_shadow_figure():
    print("You see a dark shadowy figure appear in the distance. your insticts scream at you telling you to get away from the monster. You need to make a quick decision. Where would you like to go?")
    
    while True:
        user_input = input("Options: right/backward\n")
        if user_input == "right":
            sign_scene()
            break
        elif user_input == "backward":
            intro_scene()
            break
        else:
            print("Option invalid! Please enter a valid option.")

def sign_scene():
    print("You see a broken sign that has been dropped on the ground. Someone has been here recently. you solve the puzzel and the puzzle leads you ahead .Where would you like to go?")
    
    while True:
        user_input = input("Options: forward/backward\n")
        if user_input == "forward":
            print("You made it! You've found an exit.")
            print("you think to yourself 'I MADE IT! I MADE IT I am finally out of that godforsaken place!' but it looks like fate had other plans")
            stage2()
            break
        elif user_input == "backward":
            show_shadow_figure()
            break
        else:
            print("Option Invalid! Please enter a valid option.")

def show_skeletons():
    print("You see a wall of bones and skulls as you walk into the room. what's going on? you think to yourself . Someone is watching you.... but aren't you the only one in this cursed place?. How eerie!. Where would you like to go?")
    
    while True:
        user_input = input("Options: backward/forward\n")
        if user_input == "backward":
            intro_scene()
            break
        elif user_input == "forward":
            strange_creature()
            stage2()
            break
        else:
            print("Option Invalid. Please enter a valid option.")

def haunted_room():
    print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
    
    while True:
        user_input = input("Options: right/left/backward\n")
        if user_input == "right":
            print("Multiple starving beasts start emerging from the shadows as you enter the room. You are now a scrumptious feast.")
            print(".......")
            print(".......????!!!!")
            print("how stange you are still alive and kicking you find yourself at cross roads")
            print("You are now at the place where this helish nightmare began")
            stage1()
        elif user_input == "left":
            print("You made it! You've found an exit.")
            print("you think to yourself 'I MADE IT! I MADE IT I am finally out of that godforsaken place!' but it looks like fate had other plans")
            stage2()
            break
        elif user_input == "backward":
            intro_scene()
            break
        else:
            print("Option Invalid. Please enter a valid option.")

def strange_creature():
    print("As you walk further into the passage, you encounter a strange creature blocking your way.")
    print("The creature has a rotting body and is twice your size. It seems like its going to attack any moment.")
    print("you need to brace yourself adventurer")

    choice = input("Do you have a weapon to defend yourself? (yes/no):\n")
    
    if choice.lower() == "yes":
        print("How strong! With your weapon, you manage to defend yourself and move forward.")
        print("You made it! You've found an exit.")
        print("you think to yourself 'I MADE IT! I MADE IT I am finally out of that godforsaken place!' but it looks like fate had other plans")
        stage2()
        
    elif choice.lower()=="no":
        print("Without a weapon, you try to escape, but the creature catches up to you. It has mauled you to death. How painful!")
        print(".......")
        print(".......????!!!!")
        print("how stange you are still alive and kicking you find yourself at crossroads")
        print("You are now at the place where this helish nightmare began")
        stage1()
         
    else:
        print("Oh no! Looks like you couldn't make a decison the creature has caught upto you because of this! you died")
        print(".......")
        print(".......????!!!!")
        print("how stange you are still alive and kicking you find yourself at cross roads, Finding the escape route is the only choice you have it appears")
        print("You are now at the place where this helish nightmare began")
        stage1()

def stage2():
    print("\n")
    print("STAGE 2: THE EXPLORATION")
    print("\n")
    print("Oh no, looks like escaping the maze of doom alone was not enough! We have ended up in the cursed castle after finding the exit.")
    print("right when you fear that your worst nightmares are going to come true. you hear a wisper 'TrEaSuReS AwAiT To ThOsE WhO OvErCoMe TrIAiLs'.")
    print("I pray you stay safe, adventurer. May the gods show you light!")
    print("okay? you thought and read a sign that said....")
    print("Find the exit out of multiple rooms in the cursed castle.")
    print("\n")
    print("P.S go in order specified to uncover a mysterious story about the cured castle (However it is not necessary to do so )")
    print("Let the journey begin.")
    print("\n")
    magicwords()
    


def magicwords():
    while True:
        print("\n")
        print("Say the magic words to enter the teleportation portal (EtheriaNexus): ")
        words = input()
        if words =="EtheriaNexus":
            print("Let the journey begin!")
            level2()
            return
        else:
            print("\n")
            print("looks like you got it wrong")
            print("Please try again.")

    

def level2():
    print("You can go to multiple places through the teleportation portal and discover the mysteries of the cursed castle.")
    print("\n")
    directions = ["Hall of Paintings", "The Great Weapon Room", "Enchanted Ballroom", "Mesmerizing Gardens"]
    
    print("You are now at the teleportation room, and you can enter the portal to reach any of the four mysterious places. Where would you like to go?")
    
    while True:
        user_input = input(f"Options: {' / '.join(directions)}\n")
        if user_input in directions:
            explore_room(user_input)
        else:
            print("Please enter a valid option.")

def explore_room(room):
    print(f"You have entered the {room}.")
    
    if room == "Hall of Paintings":
        show_hall_of_paintings()
    elif room == "The Great Weapon Room":
        show_the_great_weapon_room()
    elif room == "Enchanted Ballroom":
        show_enchanted_ballroom()
    elif room == "Mesmerizing Gardens":
        show_mesmerizing_gardens()

def show_hall_of_paintings():
    print("You find the paintings staring at you. How creepy.")
    print("why do i feel the preasence of so many people when i'm all alone?")
    user_input = get_user_input(["inspect", "leave"])
    
    if user_input == "inspect":
        print("you go towards a painting, the woman in the painting seems to be the queen of the castle")
        print("You found an old paper that reads 'It was The most fragnant place i went to It was my most beloved gift, why did it have to be destroyed?.WHY!???'")
        print("as you read the paper you start hearing wails of a woman, Let us leave this place soon....... you think and suddenly a voice rings in your head")
        print("You have found a clue to treasure. Let's get back to the starting point to explore more rooms and find unimaginable treasure.")
        print("\n")
        level2()
    elif user_input == "leave":
        print("What rotten luck! Let's head back quickly.")
        level2()

def show_the_great_weapon_room():
    print("Even with how old the castle is, the weapons are surprisingly sharp.")
    user_input = get_user_input(["inspect", "leave"])
    
    if user_input == "inspect":
        print("You found a shining dagger. Upon inspection, you find strange scriptures on it.")
        print("Impossible! You can read the scriptures even when you don't recognize the language.")
        print("You have found a new clue that says 'She was only out for a stroll she loved the open space WHY DID SHE HAVE TO DIE? she only loved the nature' Is this perhaps the king's Dagger you thought")
        print("You were still in your thoughts as the weapons started falling from the nails?.....oh no run!")
        print("as you run, a voice rings in your head it says....")
        print("Let's get back to the starting point to explore more rooms and find unimaginable treasure.")
        print("what is going on?")
        print("\n")
        level2()
    elif user_input == "leave":
        print("What rotten luck! Let's head back quickly.")
        level2()

def show_enchanted_ballroom():
    print("Even with how old the castle is, the ballroom is still enchanting.")
    user_input = get_user_input(["inspect", "leave"])
    
    if user_input == "inspect":
        print("You found strange writings on a curtain.")
        print("Impossible! You can read the strange writings even when you don't recognize the language.")
        print("You have found a new clue that says 'the place where the four elements sun earth water and wind meet lies a great fortune.'")
        print("You start hearing a ballroom music that signifies a start to dance and as you are creeped out you hear a voice ringing in your head that says....")
        print("Let's get back to the starting point to explore more rooms and find unimaginable treasure.")
        print("\n")
        level2()
        
    elif user_input == "leave":
        print("What rotten luck! Let's head back quickly.")
        level2()
def replay():
    print("\n")
    print(f"The End Is Just A New Beginning {player_name}.")
    print("would you like to relive the adventure?"+"\n"+"(yup/nah)")
    decision=input("enter yup or nah  : ")
    if decision.lower()=='yup':
        print("\n"+"yay! let us explore more!")
        stage1()
    else:
        print("thankyou for being there with ous on the journey")
        sys.exit()

def show_mesmerizing_gardens():
    print("How beautiful! How have the flowers not wilted?")
    user_input = get_user_input(["inspect", "leave"])
    
    if user_input == "inspect":
        print("You found a signboard that leads you to the greenhouse.")
        print("You arrive at the greenhouse and see strange writings. Impossible! You can read the strange writings even when you don't recognize the language.")
        print("You have found a new clue that says 'the place where the worst tragedy started ... The place where the flowers lie in eternal bloom'")
        print("You found unimaginable treasure filled with gold, gemstones a dagger a curtain and an oldpaper?.... and so much more.!")
        print("You here a strange ringing voice in your head  'the lore of the great castle is not something meant for mere mortals. Adventurer, LEAVE NOW AND NEVER RETURN ELSE BE PREPARED TO DIE!!!!!'")
        print("Not wanting to die, you leave the green house quickly.")
        print("you see a portal ahead, it has a sign reading exit, it takes you home")
        print("I was never killed in the cursed castle why did the people who went to uncover the secrets of castle never return?")
        print("you wake up next day to find no treasure around you..... 'WAIT NO TREASURE?????' You find a note by your bed that reads 'Evidence is the only way to plead the truth'and then... you hear hysterical laughter HAHAHAHA ")
        print("THE END THANK YOU FOR PLAYING THE CURSED CASTLE A NEW ADVENTURE AWAITS YOU")
        replay()
        
    elif user_input == "leave":
        print("What rotten luck! Let's head back quickly.")
        level2()

def get_user_input(options):
    while True:
        user_input = input(f"Options: {'/'.join(options)}\n").lower()
        if user_input in options:
            return user_input
        else:
            print("Option Invalid! Please enter a valid option.")
stage1()
