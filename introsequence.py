import functions

def start(): # return must be list, 1 = stats, 2 = perks, 3 = inventory
    outputList = {}
    print("""CLASSES:
Rifleman:
    Basic infantry. Comes equipped with a rifle and a gas mask.
Raider:
    Trench Raider. Equipped with a carbine and a club.
Medic:
    Medical specialist. Issued with a handgun and basic medical equipment.
Officer:
    High ranking commander. Has a whistle for rallying troops and a sabre.
Spotter:
    Artillery fire director. Assigned a radio backpack and a handgun.""")
    _selectedClass = functions.query("Select a class.\n", ["rifleman", "raider", "medic", "officer", "spotter"])

    print("""PERKS:
Scav:
    Always the opportunist, you pilfer whatever you can, even if it's not the best.
    Containers have 10% more items but at 0-30% reduced durability.
Insomniac:
    The artillery sounds are getting to you. You find it hard to stay asleep.
    You wake up one hour early but you have -1 move range and a random 10% negative modifier on accuracy)
Underage:
    Eager for the supposed spoils and glory of war, you did whatever you could to join the military. You lied on your recruitment papers.
    You have a 19% mental health boost and you require 15% less rations. Your carry capacity is reduced by 20%, you are +30% succeptable to addictions, and you take +10% damage.
Flat_Footed:
    A hereditary condition. Your flat feet help against the sea of mud. You cannot run like the others.
    Immune to terrain move debuffs like mud. You only have 80% base movement speed. Injuries to the legs take much longer to heal.
Immunocomprimised:
    You got sick. Very sick. The scars of the disease still haunt you. Now your either variolated and recover quickly, or completely crippled until the sickness burns through you.
    Infections give permenant scarring. +40% infection chance, but +25% wound healing speed if not infected.
Institutionalized:
    They saw you as diseased. They locked you away from society, chained and starved. They never truly broke you.
    10% morale boost, +15% melee hit chance, but you start without a weapon.
Far_Sighted:
    Spending your days watching birds, you can't see up close as well as you used to.
    -20% melee hit chance, +10% accuracy. 5% morale boost when outdoors.
Pack_Mule:
    Your hoarding has led to a compulsion to collect what you find. Your back has grown stronger, but your legs struggle against the strain.
    Carry capacity is increased 20% and containers have increased capacity. Base movement speed is 70%.
Cigarette_Addict:
    War is hell. Healthy coping mechanisms are in short supply. You've grown reliant on Nicotine.
    When craving Nicotine, you have a 20% accuracy debuff and hunger drains 30% faster. When not craving Nicotine, gain +1 perception range. Gain a permenant Nicotine addiction.
Alcohol_Addict:
    You hate it here. Everything gives you nightmares. Alcohol stops the bad thoughts.
    When not on Alcohol, your mental health drains 5% per hour. Alcohol's positive effect on your mood is doubled. Gain a permenant Alcohol addiction.

Type complete when finished.""")
    _selectedPerks = []
    _picked_list = []
    while True:
        _dont_append = False
        _selected = functions.query("Select 2 or more perks.\n", ["scav", "insomniac", "underage", "flat_footed", "immunocomprimised", "insititutionalized", "far_sighted", "pack_mule", "cigarette_addict", "alcohol_addict", "complete"])
        for i in _picked_list:
            if _selected in i:
                _dont_append = True
                print("Already picked "+i+". Try another.")
        if _selected == "complete":
            if len(_selectedPerks) >= 2:
                print("Confirmed selection of these perks:")
                print(_selectedPerks)
                break
            else:
                print("Not enough perks selected! Selected perks are:")
                print(_selectedPerks)
                _dont_append = True
        if _dont_append == False:
            _selectedPerks.append(_selected)
            _picked_list.append(_selected)

    print("""DIFFICULTIES:
    Easy
    Medium
    Hard""")
    _selected_difficulty = functions.query("Select a difficulty.\n", ["easy", "medium", "hard"])

    _selected_name = functions.query("What is your name?\n", None, True)
    
    outputList["difficulty"] = _selected_difficulty
    outputList["stats"] = {"class" : _selectedClass}
    outputList["perks"] = _selectedPerks
    outputList["inventory"] = 'list3'
    outputList["stats"]["name"] = _selected_name
    return outputList