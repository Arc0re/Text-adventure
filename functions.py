#this module will contain some functions for the game.

import variables

#Pokemon style fight, the parameter is the enemy type (rat, spider... see globals)
def combat(enemy):
    damage = enemy[1]
    print "An enemy appears! Its a wild %s!" %enemy
    print "You have 3 choices."
    action = raw_input("---------- Attack \n ---------- Cast \n ---------- Block \n")
