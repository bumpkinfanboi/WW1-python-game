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
user = player()
user.intro()
print(user.stats["class"])
print(user.perks)
print(difficulty)
print(user.stats["name"])