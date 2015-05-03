#Written for Python 2.X, will not work on 3.X because of raw_input()
#Main game file
import variables

def start():
    print "Welcome into the best text-adventure game ever made."
    print "This adventure will take you to a mysterious cave, and ya' better take a pen and a piece of paper to draw a map."
    variables.name = raw_input("First of all, what is your name, you filthy rat? ")
    print "So, your name is %s. Not everybody has nice parents..." %variables.name

    print "Next, there will be your class. What? You don't now what 'a class' is? Hum. I guess not everybody has a brain, after all...\n"
    print "You need to choose between 1.Warrior \n 2.Wizard \n 3.Undead."
    
    
    while (variables.skill != "warrior" or  variables.skill != "wizard" or  variables.skill != "undead"):
        prov = raw_input("Just type in the one you want. Careful, it's case sensitive bacause I'm lazy. Don't you dare complain. ")
        
        if (prov.lower()  == "warrior"):
            variables.skill = "warrior"
            print "So, you think you are the true man. Hum. We'll see that.\n"
            break
        elif (prov.lower()  == "wizard"):
            variables.skill = "wizard"
            print "Magic, huh ? Pussy.\n"
            break
        elif (prov.lower() == "undead"):
            variables.skill = "undead"
            print "Oh, you smell a little. Just a little...\n"
            break
        else:
            print "Can't you read?"


    print "\n(That was a joke, for the 'case sensitive' thing. Lol.)"
    print "Nice. Now that we now that you are a %s, more or less, lets go on. If you want to see your class's skills, just open the classes.txt file located on the same folder.\n" %variables.skill

    return
def game_loop():
    loop = 1

    while loop == 1:
        print "You awake on top of a high tower. The sky is rainy and its night. You can see a stairway which leads inside the tower. The only thing that you have is a knife."
        first = raw_input("Where do you go?")
        if first.lower() == ("go downstairs"):
            print "You climb down the stairs.\n"
            loop = 2
        else:
            print "I don't understand this command. Want me to speak in bytecode, just to see?\n"
            loop = 1


    while loop == 2:
        print "You enter in a dark room, where the air smell like a dead body. A great library covers an entire wall. There is a table and a door."
        second = raw_input("What do you do?")
        
        if second.lower() == ("go to table") or second.lower() == ("table"):
            print "On the table, you see an open book which title is 'Necronomicon'. Next to it, you see a weird stick."
            table = raw_input("What do you do?")
            
            if table.lower() == ("take book"):
                print "You put the book in your bag."
                variables.inventory.append("necronomicon")
                loop = 2
            elif table.lower() == ("take stick") or table.lower() == ("take weird stick"):
                print "You put the stick in your inventory. A strange glow is emanating from one extremity..."
                variables.inventory.append("magic staff")
                
                if variables.skill == "wizard" or variables.skill == "undead":
                    equip = raw_input("Do you want to equip the staff to use it as a weapon? Answer by 'yes' or 'no', that shouldn't be too hard.")
                    if equip.lower() == ("yes"):
                        variables.equipped_weapon = "staff"
                        print "You have equipped the staff."
                    elif equip.lower() == ("no"):
                        print "You don't want to fight ? Fine..."
                        loop = 2
                    else:
                        print "I don't know that command..."
                        loop = 2
                        
                else:
                    print "Huh, it looks like you cannot equip that. Too bad..."
                    loop = 2

            loop = 2

       #  elif second.lower() == ("library") or second.lower()== ("go to librairy"):
             

            
    

    

    return

start()
game_loop()
