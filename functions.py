import json

def query(toask, acceptableinputs=None, charonly=False, numonly=False):
    queryanswr = input(toask)
    if acceptableinputs != None:
        for i in acceptableinputs:
            print("INPUTCHECKING: "+i)
            if queryanswr.lower() in i:
                return queryanswr.lower()
        print("ERROR: NOT FOUND IN ACCEPTABLEINPUTS")
        queryanswr = query(toask, acceptableinputs, charonly, numonly)
    if charonly == True:
        if queryanswr.isalpha() == True:
            return queryanswr
        else:
            print("ERROR: NOT ALPHABETIC")
            query(toask, acceptableinputs, charonly, numonly)
    if numonly == True:
        if queryanswr.isnumeric() == True:
            return queryanswr
        else:
            print("ERROR: NOT NUMERIC")
            query(toask, acceptableinputs, charonly, numonly)
    return queryanswr

class item:
    def __init__(self, name, weight, type, itemstats, equip_slot=None, container=False, container_allowed_items=None):
        self.name = name
        self.weight = weight # IMPORTANT NOTE: WEIGHT IS IN KILOGRAMS! 0.2 = 200 grams! 1 = 1 kilogram!
        self.type = type
        self.itemstats = itemstats
        self.max_item_stats = itemstats
        if equip_slot != None:
            self.equip_slot = equip_slot
        else:
            self.equip_slot = None
        if container == True:
            self.container_space = itemstats["containerspace"]
            self.encumbrance_reduction = itemstats["encumbrance_reduction"]
        else:
            self.container_space = None
            self.encumbrance_reduction = None
        if container_allowed_items != None:
            self.allowed_items = container_allowed_items
    def use_item(self, itemstat, amount): #amount can be negative to add to an itemstat
        if self.itemstats[itemstat]:
            if isinstance(self.itemstats[itemstat], int):
                if self.itemstats[itemstat] < amount:
                    self.itemstats[itemstat] = 0
                    self.item_empty() # TODO: ADD THIS TO MAKE A NEW ITEM IF THIS ITEM IS USED COMPLETELY
                elif -self.itemstats[self.itemstats] > amount:
                        self.itemstats[itemstat] = self.max_item_stats[itemstat]
                else:
                    self.itemstats[itemstat] -= amount
            else:
                self.itemstats[itemstat] = amount # failsafe
                print("WARNING: itemstat is not an integer, falling back to itemstat=amount.")
        else:
            return "ERROR: NO ITEM FOUND"
        return self.itemstats[itemstat]