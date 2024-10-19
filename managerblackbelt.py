import tbcblackbelt as tbc

def main():
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 100
    hero.maxDamage = 20
    hero.armor = 1

    monster = tbc.Character("Monster", 20, 35, 5, 1)

    hero.printStats()
    monster.printStats()

    fight = tbc.fight(hero, monster)
    fight.startFight()
    inventorysys = tbc.inventory()
    inventorysys.saving()
    inventorysys.loading()

if __name__ == "__main__":
    main()