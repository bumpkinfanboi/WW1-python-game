import json
import functions

item_info = {
    "enfieldmk3" : {
        "name" : "Lee Enfield Mk. III",
        "weight" : 5,
        "type" : "weapon",
        "itemstats" : {"range" : 500, "containerspace":5, "encumbrance_reduction":0,}, # range is measured in meters
        "equip_slot" : "primary", # TODO: make equipment slots in player inventory, have them reduce the weight of an item if equipped (like Project Zomboid)
        "container" : True,
        "allowed_items" : ["303spitzer"],
    },
    "303spitzer" : {
        "name" : ".303 Spitzer",
        "weight" : 0.025,
        "type" : "ammunition",
        "itemstats" : {"caliber" : ".303", "bullet_shape" : "spitzer"}
    }
}
with open("data.json", "w+") as file:
    json.dump(item_info, file, indent=3)

template = {
    "item_devname" : {
        "name" : "real name",
        "weight" : 1, # use int or float here
        "type" : "devitem",
        "itemstats" : {"containerspace" : 999, "encumbrance_reduction":100, "whatever" : "goes here"},
        "equip_slot" : "back", # TODO: make equipment slots in player inventory, have them reduce the weight of an item if equipped (like Project Zomboid)
        "container" : True,
        "allowed_items" : None, # if allowed items == None, all items ALLOWED. otherwise, make a list of all the dev item names (or item categories) to allow.
    }
}