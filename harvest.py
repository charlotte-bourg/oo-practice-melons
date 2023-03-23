############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code 

def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []
    musk = MelonType("musk",1998,"green",True,True,"Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    casaba = MelonType("cas",2003,"orange",True,False,"Casaba")
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberries")
    all_melon_types.append(casaba)
    crenshaw = MelonType("cren",1996,"green",True,False,"Crenshaw")
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)  
    yellow_watermelon = MelonType("yw",2013,"yellow",False,True,"Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)  
    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon_type in melon_types:
        print(f"{melon_type.name} pairs well with")
        for pairing in melon_type.pairings:
            print(f"- {pairing}")
        print()

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    
    melon_dict = {}
    for melon_type in melon_types:
        melon_dict[melon_type.code] = melon_type
    return melon_dict


############
# Part 2   #
############


class Melon():
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvest_field, harvester): 
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvester = harvester

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field != 3:
            return True
        else:
            return False 

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    all_melons = []
    melons_types_by_id = make_melon_type_lookup(melon_types)
    melon_1 = Melon(melons_types_by_id['yw'], 8, 7, 2, "Sheila")
    all_melons.append(melon_1)
    melon_2 = Melon(melons_types_by_id['yw'], 3, 4, 2, "Sheila")
    all_melons.append(melon_2) 
    melon_3 = Melon(melons_types_by_id['yw'], 9, 8, 3, "Sheila")
    all_melons.append(melon_3)
    melon_4 = Melon(melons_types_by_id['cas'], 10, 6, 35, "Sheila")
    all_melons.append(melon_4) 
    melon_5 = Melon(melons_types_by_id['cren'], 8, 9, 25, "Michael")
    all_melons.append(melon_5)
    melon_6 = Melon(melons_types_by_id['cren'], 8, 2, 35, "Michael")
    all_melons.append(melon_6)  
    melon_7 = Melon(melons_types_by_id['cren'], 2, 3, 4, "Michael")
    all_melons.append(melon_7)
    melon_8 = Melon(melons_types_by_id['musk'], 6, 7, 4, "Michael")
    all_melons.append(melon_8)     
    melon_9 = Melon(melons_types_by_id['yw'], 7, 10, 3, "Sheila")
    all_melons.append(melon_9)
    return all_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        
        if melon.is_sellable():
            selling_string = "(CAN BE SOLD)"
        else: selling_string = "(NOT SELLABLE)"
        print(f"Harvested by {melon.harvester} from Field {melon.harvest_field} {selling_string}")

def read_harvest_log():
    harvest_log_list = []
    melon_types_list = make_melon_types()
    melon_types_by_id = make_melon_type_lookup(melon_types_list)
    with open("harvest_log.txt") as f:
        for line in f:
            line = line.strip()
            line = line.split()
            melon_type = melon_types_by_id[line[5]]
            shape = line[1]
            color = line[3]
            harvest_field = line[11]
            harvester = line[8]
            harvest_log_list.append(Melon(melon_type, shape, color, harvest_field, harvester))
    return harvest_log_list

