
from hero import Hero
from goblin import Goblin


"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    hero = Hero(10, 5)
    goblin = Goblin(6,2)
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while goblin.alive() and hero.alive() :
        #print("You have %d health and %d power." % (hero.health, hero.power))
        hero.print_status()
        #print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            # goblin_health -= hero_power
            # print("You do %d damage to the goblin." % hero_power)
            hero.attack(goblin)
            if not goblin.alive():
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive():
            # Goblin attacks hero
            # hero_health -= goblin_power
            # print("The goblin does %d damage to you." % goblin_power)
            goblin.attack(hero)
            if not hero.alive():
                print("You are dead.")

main()
