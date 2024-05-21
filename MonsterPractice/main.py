def move(speed):
    print("The monster has moved")
    print(f"It has a speed of {speed}")


class Monster:
    # attributes
    health = 90
    energy = 40

    # methods
    def attack(self, amount):
        print("The monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 20
        print(self.energy)


monster = Monster()
monster.attack(40)
move(10)
