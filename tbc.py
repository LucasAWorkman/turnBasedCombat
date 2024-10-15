import random

# there was probably an easier way to do startFight with properties and returning values but it worked first try with my logic

class Character(object):

    def __init__(self, name = "Goober", hitPoints = 10, hitChance = 50, maxDamage = 5, armor = 2):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor

    def printStats(self):
        print(self.name)
        print("===========")
        print(f"Hit points: {self.hitPoints}")
        print(f"Hit chance: {self.hitChance}")
        print(f"Max damage: {self.maxDamage}")
        print(f"Armor: {self.armor}")

class fight(object):

    def __init__(self,player1,player2):
        super().__init__()
        self.player1 = player1
        self.player2 = player2


    def startFight(self):
        keepGoing = True
        while keepGoing:
            keepPlaying = input("Press enter for another round")
            if keepPlaying == "":
                rollHitPlayer1  = random.randint(1, 100)
                rollHitPlayer2 = random.randint(1, 100)   
                if rollHitPlayer1 < self.player1.hitChance:
                    print(f"{self.player1.name} hit {self.player2.name}...")  
                    rollHitPlayer1Dmg = random.randint(1, self.player1.maxDamage)  
                    print(f"for {rollHitPlayer1Dmg} points of damage")
                    if self.player2.armor >= 1:
                        print(f"{self.player2.name} armor can absorb {self.player2.armor}")
                        totalDmgplr1 = rollHitPlayer1Dmg - self.player2.armor
                        self.player2.hitPoints -= totalDmgplr1
                    else:
                        print(f"{self.player2.name} has no armor")
                        self.player2.hitPoints - rollHitPlayer1Dmg
                elif rollHitPlayer2 < self.player2.hitChance:
                    print(f"{self.player2.name} hit {self.player1.name}...") 
                    rollHitPlayer2Dmg = random.randint(1, self.player2.maxDamage)
                    print(f"for {rollHitPlayer2Dmg} points of damage")
                    if self.player1.armor >= 1:
                        print(f"{self.player1.name} armor can absorb {self.player1.armor}")
                        totalDmgplr2 = rollHitPlayer2Dmg - self.player1.armor
                        self.player1.hitPoints -= totalDmgplr2
            print(f"{self.player1.name}: {self.player1.hitPoints} HP")
            print(f"{self.player2.name}: {self.player2.hitPoints} HP")
            if self.player1.hitPoints <= 0:
                print(f"{self.player1.name} has died") 
                keepGoing = False
            elif self.player2.hitPoints <= 0:
                print(f"{self.player2.name} has died")
                keepGoing = False
def main():
    c = Character()
    c.printStats()
    f = fight()
    f.startFight()
if __name__ == "__main__":
    main()