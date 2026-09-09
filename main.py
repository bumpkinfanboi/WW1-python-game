import string
import functions
import introsequence

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
    def getHPTotal(self):
        running_total = 0
        for i in self.stats["health"]:
            running_total += self.stats["health"][i]
        print(running_total)
user = player()
user.intro()
print(user.stats["class"])
print(user.stats)
print(user.perks)
print(difficulty)
print(user.stats["name"])
user.getHPTotal()