Manager.py 

main()

   Main in the second py file provided by andy but it makes hero and monster with the properties from the tbc.character() class

   Also prints the stats

   Also starts the fight

   –update added startFight() for better organization and not having everything under def init



tbc.py

Class character(object)

   Do the def init and pass through all the values we want for the characters, being name, hitpoints, hitchance, maxdamage, and armor

   printStats(self)
   Print the parameters of the def init function

Class fight(object)

   Do the def init passing self but also player1 and player2 as we pass hero and monster from the manager script

   Startfight(self)

      Keepgoing to make a while loop that always makes the fight and use input of enter to keep it going

      Get random numbers 1,100 and if its lower than the player1 hitchance or the roll for player2 hitchance is lower than they dont land a hit

      Use another roll for each to determine the damage 1 to maxDamage then apply to hitpoints

      If they have armor subtract the damage then apply it to the hitpoints

      Print hps of each player at the bottom and if lower or equal to zero end the loop
