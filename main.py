import string
import functions
import introsequence
import os
import keyboard

difficulty = ""
class player:
    def __init__(self):
        self.position = {}
        self.inventory = []
    def intro(self):
        global difficulty
        introOutput = introsequence.start()
        self.stats = introOutput["stats"]
        self.perks = introOutput["perks"]
        self.inventory = introOutput["inventory"]
        difficulty = introOutput["difficulty"]
    def getHPTotal(self, outof=False):
        running_total = 0
        for i in self.stats["health"]:
            running_total += self.stats["health"][i]
        if outof == True:
            print(str(running_total) + "/" + str(self.stats["health_max"]["total"]))
            return running_total, self.stats["health_max"]["total"]
        else:
            print(running_total)
            return running_total
    def damage_organ(self, organ, amount):
        if amount > self.stats["health"][organ]:
            self.stats["health"][organ] = 0
            print("ORGAN " + str(organ) + " NOW HAS 0 HEALTH")
            print(str(organ) + " has " + str(self.stats["health"][organ]) + " health")
        elif -self.stats["health_max"][organ] > amount:
            self.stats["health"][organ] = self.stats["health_max"][organ]
            print("ORGAN " + str(organ) + " HAS " + str(self.stats["health"][organ]))
        else:
            print("AMOUNT = "+ str(amount))
            print("OLD HEALTH = " + str(self.stats["health"][organ]))
            self.stats["health"][organ] -= amount
            print("NEW HEALTH = " + str(self.stats["health"][organ]))
        
user = player()
user.intro()
print(user.stats["class"])
print(user.stats)
print(user.perks)
print(difficulty)
print(user.stats["name"])
user.getHPTotal()
user.damage_organ("head", 10)
user.damage_organ("head", -10)
user.getHPTotal(True)
print(user.stats["health"])