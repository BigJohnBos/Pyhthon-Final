# JD, AK, BB, JL 7th 



# Adventure Game Final

game = "running"

# Archie




def Right():
    print("you went right!")
    print(f"{name}, as you were walking the skety path you stumble into a portal and teleport to the midieval times!")
    print("you see Ms. LaRosa milking a cow")
    Left = print("left = you help her milk it")
    Right = print("right = you push the cow over")
    Middle = print("middle = you go back and jump back into the portal")

    choice = input("Do you go Left, Right, or Middle? ").capitalize()    
    if choice == "Left":
        print("you go Left!")
        print("she says thank you and gives you 5 silver coins")
        print("you give up and live in the village and live happily ever after")        
    elif choice == "Right":
        print("you go Right!")
        print("the cow flips over and shoots milk in your face!")
        print("you get squished from the weightand DIE")
    elif choice == "Middle":
        print("you go Middle!")
        print("you fall through a hole and DIE")
    else:
        print("enter a valid answer")   

# Jesus Durannd

def Thief():
        global game
        print("You run out and follow the thief for a while and even though you get tired and think about giving up, a strange adrenaline invades you and you decide to keep running to catch him without realizing that you have reached a forest.")
        
        print("Suddenly, the thief stops and turns around, and when you see that he has no face and red liquid is coming out of what appear to be his eyes, you try to look at the dog, but the dog has no head. ")
    
        print("You run away with your heart racing, but you don't know where you are. All you see are trees around you, and when you think you're safe, you stop, but when you turn around, the creature hits you on the head and you pass out.")
        
        print("When you wake up, you are in a white room with absolutely nothing, just your existence as empty and simple as the wall. *We'll see if you change that.*")
        
        print("Suddenly, an image appears on the screen that says, Which is stronger: Water, Earth, Fire, Air?")
        
        # Conditionals
        
        while True:
            Elements = input("Water Earth Fire Air ")
            
            if Elements == "Water":
                print("Good choice, the element of change... But not enough. Suddenly, the white room starts to fill with water until you drown, and when you wake up, you're just water inside a bottle. GAME OVER")
            elif Elements == "Earth":
                print("Mmm, basic, just because you're firm doesn't mean you're strong. GAME OVER")
            elif Elements == "Fire":
                print("Interesting, the most aggressive element is a lethal flame that, if left unchecked, is a sharp-edged dagger. But it's not the strongest. GAME OVER")
            elif Elements == "Air":
                print("Mmmm... CONGRATULATIONS! You chose the correct option. Many people think that air is very weak or simple, but the truth is that air is everywhere. You control it and you control everything. Congratulations! You are now the avatar. Be one better than Korra. Thanks for playing.")
            else:
                print("Chose one of the opptions not other thing >.<")
        




    # Second Loop
def Forward():
    
    
    # Start of path Forwoard

    # Print staments
    
    print("When you go out of school you decide to forward to walmart ")
    print("Suddenly, as you leave Walmart, you see a thief stealing a husky puppy from an old man. What will you do? Go after the thief, or do nothing, as you have done your whole life?" )
    
    # Loop
    
    while True:
        desition = input("What you gonna do theif or nothing?:\n").capitalize()
        
        if desition == "Theif":
            Thief(game)
            break
        elif desition == "nothing":
            print("You continue on your way, ignoring the problem, but when you cross the street, you have a heart attack and die. GAME OVER")
            break
        else:
            print("Put theif or nothing")


        
            



# Jovie Lineback

# Def code is a function to allow player to move from each location

def Left():
    # Print statements to output info

    print(f"You get out of school and turn left to go go your friends house!")
    print(f"As you're walking to your friends house when you accidently trip and everything goes black")
    print(f"you wake up and realize you got kidnapped into someones basement and have to find a way out!")
    

    
    print(f"you look around to see if theres anything to help you escape. All you see is a brick, a stick, and a lamp.")
    
    #input that allows the user to input information to use later
    
    choice = input("what item do you choose to help escape?:\n").capitalize().strip()
    

    # conditional if statement that takes in user input and depending on what you say if it's true or false it will do it
    # if they choose brick then this will run
    if choice == "Brick":
        
        print("you grab the brick and throw it at the window, the window breaks and you start to climb out!")
        print("Unfortunetly the kidnapper heard you and caught you before you could climb out, you lose")
    
    #if they choose stick this will run sin
    
    elif choice == "Stick":
        
        print("you reach for the stick and right as you grab it you see a dog coming for it")
        
        dog_choice = input("do you try and befriend the dog or ignore it (1 to befriend the dog and 2 to ignore it):\n").strip()
        
        if dog_choice == "1":
            print("YAY you successfully befriended the dog! the dog gives you a key to the door to your escape!")
            print("you successfully escaped the kidnapper!")
        elif dog_choice == "2":
            print("uh oh the dog started to bark and attack you. You lose")
        
    
    elif choice == "Lamp":
        print("Once you grab the lamp it was actually a magic lamp and a genie comes out!")
        print("this is your chance to finally escape, all you have to do is tell the genie you want to go home!")
        print("I want to go home genie!!")
        print("Uh oh the genie didn't know where your home was and sent you into his home in the lamp!")
        print("you lose and are stuck eternally in the lamp")   

    game = "dead"
    
    
# Boston

while game == "running":
    print("The crazy adventures of Ms. LaRosa")
    name = input("What is your name:\n")
    print(f"Welcome {name} to The crazy adventures of Ms. LaRosa!")
    print("School just got out and you are wandering what you are going to do.")
    print("You come to a crossroad and you can go Forward, Left, or Right")
    print("Forward is go to walmart,")
    print("Left is you go to your friend's house,")
    print("Right is go down a sketchy path")
    

    while True:
        direction_1 = input("Forward, Left, or Right :\n")
        if direction_1 == "Right":
            Right()
            break
        elif direction_1 == "Forward":
            Forward()
            break
        elif direction_1 == "Left":
            Left()
        else:
            print("Enter a valid answer ")
