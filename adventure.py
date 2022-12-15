import random
import time

PLAYGROUNDS = [
    {
        "place": "field",
        "properties": "grass and yellow wildflowers",
        "enemy": "troll",
        "enemy_property": "terrifying the nearby village",
        "enemy_place": "a house",
        "weapon_place": "a dark cave",
        "weapon_spec_place": "behind a rock"
    },
    {
        "place": "battleship deck",
        "properties": "cannons and gunpowder",
        "enemy": "pirate",
        "enemy_property": "invading the battleship for the food and treasure",
        "enemy_place": "the bridge",
        "weapon_place": "the funnel",
        "weapon_spec_place": "on the floor"
    },
    {
        "place": "castle bailey",
        "properties": "soldier's death bodies kill by the evil witch",
        "enemy": "witch",
        "enemy_property": "murderring soldiers with her spell \
            and terroring the king for treasure",
        "enemy_place": "the tower",
        "weapon_place": "an arrow loop",
        "weapon_spec_place": "in a broken cabinet"
    }
]

WEAPONS = {
    "primitive": ["dagger", "sickle", "pickaxe", "cleaver", "blade"],
    "ultimate": [
        "Stormrazor", "Harrowing Cresent", "Navori Quickblades",
        "Black Cleaver", "Infinity Edge Blade"
    ],
    "ultimate_property": ["awesome attack speed", "incredible strength"]
}


def play_game():
    while True:
        playground = random.choice(PLAYGROUNDS)
        primitive_weapon = random.choice(WEAPONS["primitive"])
        ultimate_weapon = None
        start_place(primitive_weapon, playground, start_game=True)
        selection = get_user_input()
        while True:
            if selection == "1":
                get_in_enemy_place(
                    primitive_weapon,
                    playground,
                    ultimate_weapon
                )
                enemy_selection = get_user_input()
                if enemy_selection == "2":
                    run_away(playground)
                    start_place(primitive_weapon, playground, start_game=False)
                    selection = get_user_input()
                    continue
                else:
                    fight(primitive_weapon, playground, ultimate_weapon)
                    break
            elif selection == "2":
                ultimate_weapon = get_in_weapon_place(
                    primitive_weapon,
                    playground,
                    ultimate_weapon
                )
                start_place(primitive_weapon, playground, start_game=False)
                selection = get_user_input()
        print_pause("Game ended! \
            Would you like to play again (1) or quit (2)?")
        replay = get_user_input()
        if replay == "1":
            print("Game is restarting......")
            continue
        else:
            print("See you later :)")
            break


def get_user_input():
    print("(Please enter 1 or 2.)")
    selection = input().strip()
    while True:
        if selection != "1" and selection != "2":
            print("Wrong command! (Please enter 1 or 2 only.)")
            selection = input().strip()
        else:
            break
    return selection


def print_pause(text):
    words = text.split()
    print(" ".join(words))
    time.sleep(2)


def start_place(primitive_weapon, playground, start_game=True):
    if start_game:
        print_pause(f"You find yourself standing in an open \
            {playground['place']}, filled with {playground['properties']}.")
        print_pause(f"Rumor has it that a {playground['enemy']} \
            is somewhere around here, \
            and has been {playground['enemy_property']}.")
        print_pause(f"In front of you is {playground['enemy_place']}.")
        print_pause(f"To your right is {playground['weapon_place']}.")
        print_pause(f'In your hand you hold your trusty \
            (but not very effective) {primitive_weapon}.')
        print()
    print_pause(f"Enter 1 to knock on the door and enter the \
        {playground['enemy_place'].split()[-1]}.")
    print_pause("Enter 2 to get into the "
                + " ".join(playground['weapon_place'].split()[1:]) + ".")
    print_pause("What would you like to choose?")
    return


def get_in_weapon_place(primitive_weapon, playground, ultimate_weapon=None):
    if ultimate_weapon is not None:
        print_pause("You've walked here before and \
            have collected all good stuff. There is nothing left.")
    else:
        print_pause("You peer cautiously into the "
                    + " ".join(playground['weapon_place'].split()[1:])+".")
        print_pause(f"Your eye catches a glint of rare materials \
            (metals, ...) {playground['weapon_spec_place']}.")
        print_pause(f"You use these materials to upgrade your current \
            {primitive_weapon} to a legendary items.")
        ultimate_weapon = random.choice(WEAPONS['ultimate'])
        print_pause(f"BOOOM. Your crafted weapon is called {ultimate_weapon}, \
            legend has it that gives the owner \
            {random.choice(WEAPONS['ultimate_property'])}")
    print_pause(f"You walk back out to the {playground['place']} \
        with the {ultimate_weapon} in your hand.")
    return ultimate_weapon


def get_in_enemy_place(primitive_weapon, playground, ultimate_weapon=None):
    print_pause("You approach the door of the "
                + " ".join(playground['enemy_place'].split()[1:]) + ".")
    print_pause(f"Suddenly, the door is open and you see the \
        {playground['enemy']}.")
    print_pause(f"OMG! The {playground['enemy']} is here.")
    print_pause(f"The {playground['enemy']} start to attack you.")
    if ultimate_weapon is not None:
        print_pause(f"You feel confident with the crafted \
            legendary {ultimate_weapon}.")
    else:
        print_pause(f"With the little {primitive_weapon} in hand, \
            you feel insecure....")
    print_pause("Would you like to fight back (1) or get away (2)?")


def fight(primitive_weapon, playground, ultimate_weapon=None):
    if ultimate_weapon is not None:
        print_pause(f"With the legendary {ultimate_weapon} crafted from the "
                    + " ".join(playground['weapon_place'].split()[1:])+", ")
        print_pause(f"you easily dominate the {playground['enemy']}.")
        print_pause(f"After few minutes of engaging, the \
            {playground['enemy']} starts to lose and begs you for mercy.")
        print_pause("You agree to spare his life \
            and force him to leave forever.")
        print("You are vitorious!!")
    else:
        print_pause("You choose to fight back with all you got. \
            However, the difference in strength is huge.")
        print_pause(f"Your little {primitive_weapon} \
            cannot help you win the evil.")
        print_pause("You were defeated :(")


def run_away(playground):
    print_pause(f"You run quickly back to the {playground['place']}. \
        Luckily, the {playground['enemy']} cannot follow your speed.")


if __name__ == "__main__":
    play_game()
