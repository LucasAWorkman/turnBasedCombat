import tbc

def main():
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 1

    monster = tbc.Character("Monster", 20, 35, 5, 1)

    hero.printStats()
    monster.printStats()

    fight = tbc.fight(hero, monster)
    fight.startFight()
if __name__ == "__main__":
    main()
