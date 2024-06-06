import random

class Dice:
    def dice_k6(self):
        min_value = 1
        max_value = 6
        roll = random.randint(min_value, max_value)
        return roll
    def dice_k10(self):
        min_value = 1
        max_value = 10
        roll = random.randint(min_value, max_value)
        return roll
    def dice_k12(self):
        min_value = 1
        max_value = 12
        roll = random.randint(min_value, max_value)
        return roll
    def dice_k20(self):
        min_value = 1
        max_value = 20
        roll = random.randint(min_value, max_value)
        return roll
    def dice_k100(self):
        min_value = 1
        max_value = 100
        roll = random.randint(min_value, max_value)
        return roll
my_dice = Dice()
while True:
    dice_type = input ("Please, chose your dice:\n1 - k6\n2 - k10\n3 - k12\n4 - k20\n5 - k100\n")
    if dice_type not in ("1", "2", "3", "4", "5"):
        print("Error! Please choose a number from 1 to 5")
        continue

    if dice_type == "1":
        while True:
            print("YOu rolled a d6:\n",my_dice.dice_k6())
            choice = input("Do you want to roll again with the same dice (Y/N)?")
            if choice.lower() != "y":
                break
    elif dice_type == "2":
        while True:
            print("You rolled a d10:\n",my_dice.dice_k10())
            choice = input("Do you want to roll again with the same dice (Y/N)?")
            if choice.lower() != "y":
                break
    elif dice_type == "3":
        while True:
            print("You rolled a d12:\n",my_dice.dice_k12())
            choice = input("Do you want to roll again with the same dice (Y/N)?")
            if choice.lower() != "y":
                break
    elif dice_type == "4":
        while True:
            print("You rolled a d20:\n",my_dice.dice_k20())
            choice = input("Do you want to roll again with the same dice (Y/N)?")
            if choice.lower() != "y":
                break
    elif dice_type == "5":
        while True:
            print("You rolled a d100:\n", my_dice.dice_k100())
            choice = input("Do you want to roll again with the same dice (Y/N)?")
            if choice.lower() != "y":
                break
    else:
        print("error! Try again!")
        continue


