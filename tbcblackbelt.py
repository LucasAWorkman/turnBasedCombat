import random
import json
import os
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

class inventory(object):
    
    def __init__(self, ):
        super().__init__()
        self.file = "inventory.json"
        self.inv = self.loading() 

    def saving(self):
        with open("inventory.json", "w") as filefilefile:
            data = json.dump(self.inv, filefilefile, indent=3)
        return data
    def loading(self):
        if os.path.exists(self.file): # had to look up how to figure out the error i was having, as it was originally the json deleting its data on run, then i got to this resolution without the os but a new error would occur if inventory.json wasnt already made, but i found out os is very helpful for finding if a file exists
            with open("inventory.json", "r") as filefilefile:
                d = json.load(filefilefile) 
                return d
        else:
            return {"items": []}

    def add_item(self,item):
        self.inv["items"].append(item)
        self.saving()
        
    def tier2Armor(self):
        if "Tier 2 Armor" in self.inv["items"]:
            print("Tier 2 armor dropped but you already own this")
        else:
            self.add_item("Tier 2 Armor")
    def tier2Sword(self):
        if "Tier 2 Sword" in self.inv["items"]:
            print("Tier 2 Sword dropped but you already own this")
        else:
            self.add_item("Tier 2 Sword")


class fight(object):

    def __init__(self,player1,player2):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
    

    def startFight(self):
        inventory_class = inventory()
        inventory_save = inventory_class.saving()
        inventory_loading = inventory_class.loading()
        keepGoing = True
        if "Tier 2 Sword" in inventory_class.loading()["items"]:
            print("Tier 2 Sword equipped, +3 damage")
        if "Tier 2 Armor" in inventory_class.loading()["items"]:
            print("Tier 2 Armor equipped, +3 Armor")
            self.player1.armor += 3
        while keepGoing:
            keepPlaying = input("Press enter for another round")
            if keepPlaying == "":
                rollHitPlayer1  = random.randint(1, 100)
                rollHitPlayer2 = random.randint(1, 100)   
                if rollHitPlayer1 < self.player1.hitChance:
                    print(f"{self.player1.name} hit {self.player2.name}...")  
                    rollHitPlayer1Dmg = random.randint(1, self.player1.maxDamage)  
                    if "Tier 2 Sword" in inventory_class.loading()["items"]:
                        rollHitPlayer1Dmg += 3
                    print(f"for {rollHitPlayer1Dmg} points of damage")
                    if self.player2.armor >= 1:
                        print(f"{self.player2.name} armor can absorb {self.player2.armor}")
                        totalDmgplr1 = rollHitPlayer1Dmg - self.player2.armor
                        if totalDmgplr1 < 0:
                            totalDmgplr1
                        self.player2.hitPoints -= totalDmgplr1
                    else:
                        print(f"{self.player2.name} has no armor")
                        self.player2.hitPoints -= rollHitPlayer1Dmg
                if rollHitPlayer2 < self.player2.hitChance:
                    print(f"{self.player2.name} hit {self.player1.name}...") 
                    rollHitPlayer2Dmg = random.randint(1, self.player2.maxDamage)
                    print(f"for {rollHitPlayer2Dmg} points of damage")
                    if self.player1.armor >= 1:
                        print(f"{self.player1.name} armor can absorb {self.player1.armor}")
                        totalDmgplr2 = rollHitPlayer2Dmg - self.player1.armor
                        if totalDmgplr2 < 0:
                            totalDmgplr2
                        self.player1.hitPoints -= totalDmgplr2
                    else:
                        print(f"{self.player1.name} has no armor")
                        self.player1.hitPoints -= rollHitPlayer2Dmg
            print(f"{self.player1.name}: {self.player1.hitPoints} HP")
            print(f"{self.player2.name}: {self.player2.hitPoints} HP")
            if self.player1.hitPoints <= 0:
                print(f"{self.player1.name} has died") 
                keepGoing = False
            elif self.player2.hitPoints <= 0:
                print(f"{self.player2.name} has died")
                keepGoing = False
                dropItem = random.randint(1,100)
                if dropItem >= 50:
                    print("Dropped tier 2 armor")
                    inventory_class.tier2Armor()
                else:
                    print("Dropped tier 2 Sword")
                    inventory_class.tier2Sword() 
                    
def main():
    c = Character()
    c.printStats()
    f = fight()
    f.startFight()
if __name__ == "__main__":
    main()