import random

# pokemon
class Pokemon:
    def __init__(self, name, type, level, moves):
        self.name = name
        self.type = type
        self.level = level
        self.moves = moves


class Move:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power


pikachu = Pokemon("Pikachu", "Electric", 10, [Move(
    "Thunderbolt", "Electric", 90), Move("Quick Attack", "Normal", 40)])
charmander = Pokemon("Charmander", "Fire", 10, [Move(
    "Flamethrower", "Fire", 90), Move("Scratch", "Normal", 40)])


def battle(pokemon1, pokemon2):
    print(f"{pokemon1.name} vs {pokemon2.name}")
    while pokemon1.level > 0 and pokemon2.level > 0:
        # Pokemon 1 attacks
        move1 = random.choice(pokemon1.moves)
        print(f"{pokemon1.name} used {move1.name}!")
        pokemon2.level -= move1.power
        print(
            f"{pokemon2.name} lost {move1.power} level. Level remaining: {pokemon2.level}")

        # Check if Pokemon 2 is still alive
        if pokemon2.level <= 0:
            print(f"{pokemon2.name} fainted!")
            break

        # Pokemon 2 attacks
        move2 = random.choice(pokemon2.moves)
        print(f"{pokemon2.name} used {move2.name}!")
        pokemon1.level -= move2.power
        print(
            f"{pokemon1.name} lost {move2.power} level. Level remaining: {pokemon1.level}")

        # Check if Pokemon 1 is still alive
        if pokemon1.level <= 0:
            print(f"{pokemon1.name} fainted!")
            break


battle(pikachu, charmander)
