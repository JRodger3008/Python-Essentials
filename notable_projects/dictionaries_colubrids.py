"""
Colubrid Snake Dictionary and Operations

This program demonstrates various operations and manipulations on Python dictionaries
using a small collection of Colubridae snake species. It covers:

    - Basic dictionary creation and pretty-printing (pprint()).
    - Display species information (common and scientific names) with formatted output.
    - Reverse the dictionary (colubrid_species) using comprehension.
    - Safe dictionary searches using the .get() method, and .casefold() to normalise string case.
    - CRUD Operations (Create, Read, Update, Delete) on dictionary entries.
    - Working with nested dictionaries for more detailed species data.
    - Interactive user input to query the dictionary.

This is intended as an educational exploration of dictionary handling and data 
structures in Python, with real-world inspired herpetological data. Snakes and reptiles 
have always been close to my heart, fueling a deep fascination and passion since my childhood.

Author: Jordan Rodger
Date: 18/05/2025 (Last Edit: 21/05/2025)
"""


from pprint import pprint # 'Pretty print' for formatted data structures
from typing import Any # Represents any data type, useful for nested dictionaries and JSON-like data


# Original dictionary definition {Common name: Scientific name} for a small collection
# of Colubridae snake species.
colubrid_species = {"grass snake": "Natrix natrix", 
                    "western hognose snake": "Heterodon nasicus", 
                    "boomslang": "Dispholidus typus",
                    "aesculapian snake": "Zamenis longissimus", 
                    "bull snake": "Pituophis catenifer sayi"} 

print("====== Collection of Colubrid species ======")
# 'Pretty print' - though the dictionary object itself isn't changed, it's reformatted
# for readability, which can change the displayed order.
# However, you can side-step this by using sort_dicts=False.
pprint(colubrid_species, sort_dicts=False)
print()


# ====== FUNCTION DEFINITIONS ======
def display_species(species_dict: dict[str, str]) -> None:
    """Prints all species in the dictionary with a clean formatted message."""
    for common, scientific in species_dict.items():
        print(f"{common.title()}'s scientific name is {scientific}")



# Reverse dictionary using dictionary comprehension (Scientific -> Common).
# Note: Assumes all values are unique, since dictionary keys must be unique.
# If duplicate values exist, the reversal will cause data loss as later keys overwrite
# earlier ones.
# Syntax: reverse_dict = {key: value for value, key in dict.items()}
def reverse_dictionary(original_dict: dict[str, str]) -> dict[str, str]:
    """Return a dictionary with keys and values reversed."""
    return {value: key for key, value in original_dict.items()}



# .get() method to access default value safely without throwing an error
# Syntax: dict.get(key, default=None) - This returns the value associated with the key, or None.
def get_scientific_name(species_dict: dict[str, str], common_name: str, default: str = "Species not found") -> str:
    """Return the scientific name or a default message if not found."""
    # .casefold() is a stronger and more aggressive method than .lower(),
    # making it ideal for case-insensitive comparisons.
    # It handles more Unicode characters ('ß' (Eszett) -> 'ss') and ensures
    # consistent and robust comparisons (e.g., user input vs dictionary keys).
    return species_dict.get(common_name.casefold(), default)



def print_detailed_species(species_info: dict[str, dict[str, Any]]) -> None:
    """Prints detailed information for each species in a nested dictionary.

    Each entry should map a common name to a nested dictionary containing:
        - 'scientific': the scientific name (str)
        - 'venomous': a boolean indicating if the species is venomous (medically significant)
            (though technically, all squamate reptiles (and even humans) are venomous to some extent)
            Out of ~2000 species of Colubrids, only around 40 have medically significant 
            venom, with the Boomslang being particularly dangerous due to its potent haemotoxic 
            venom, leading to uncontrolled internal and external bleeding.
        - 'region': the species' native region (str)

    Example output:
    Boomslang (Dispholidus typus) - Venomous, found in sub-Saharan Africa
    """
    for common, data in species_info.items():
        venom = "Venomous" if data["venomous"] else "Non-venomous"
        print(f"{common.title()} ({data['scientific']}) - {venom}, found in {data['region']}")



# Searching for keys
print("Scientific name of Boomslang:", end = " ")
print(colubrid_species["boomslang"]) # Dispholidus typus
print('"Zamenis longissimus" in colubrid_species:', end = " ")
print("Zamenis longissimus" in colubrid_species) # False because it's checking keys, not values
print('"Zamenis longissimus" in colubrid_species.values():', end = " ")
print("Zamenis longissimus" in colubrid_species.values()) # True
print()


# Displays species, cleanly formatted
display_species(colubrid_species)
print()


# Find a specified key-value pair
pair = ("grass snake", "Natrix natrix")
print('"grass snake", "Natrix natrix" in colubrid_species.items():', end = " ")
print(pair in colubrid_species.items()) # True

# Prior to Python 3.7, dictionaries did not preserve order, so you previously had no control over this aspect.
# Convert dict items to a list (snapshot) to allow indexing
second_entry = list(colubrid_species.items())[1]
print(f"Index[1], after converting dict to list: {second_entry}") # ('western hognose snake', 'Heterodon nasicus')

# Tuple unpacking - Indexed to last element
key, value = list(colubrid_species.items())[-1]
print(f"Common name: {key.title()}, Scientific name: {value}") # Common name: Bull Snake, Scientific name: Pituophis catenifer sayi
print()


# ====== CRUD Operations ======
print("====== CRUD OPERATIONS ======")

# Add a new species (added to the END of colubrid_species dict)
colubrid_species["garter snake"] = "Thamnophis sirtalis"
print(f"Added Garter snake to colubrid_species: {colubrid_species['garter snake']}")
# Added Garter snake to colubrid_species: Thamnophis sirtalis

# Add new species using .update() method
colubrid_species.update({"corn snake": "Pantherophis guttatus"})

# Update an existing dict entry
colubrid_species["grass snake"] = "Natrix natrix cypriaca" # Cyprus Grass Snake
print(f"Updated Grass snake scientific name: {colubrid_species['grass snake']}") 
# Updated Grass snake scientific name: Natrix natrix cypriaca

# Delete an entry, and use .keys() method to display dict keys
del colubrid_species["bull snake"]
print(f"Deleted Bull snake. Keys are now: {list(colubrid_species.keys())}") 
# ['grass snake', 'western hognose snake', 'boomslang', 'aesculapian snake', 'garter snake']

# Another deletion method is the .popitem() method, which removes the last inserted item (LIFO: Last In, First Out).
# Note: Prior to Python 3.7, .popitem() would remove an arbitrary item due to unordered dicts.
# A copy is used here to preserve the original dictionary.
temp_species = colubrid_species.copy()
removed = temp_species.popitem()
print(f"Demonstration of .popitem() method: removed {removed}") # removed ('corn snake', 'Pantherophis guttatus')

# To clear all entries from the dictionary (the object remains, but becomes empty), use the .clear() method.
temp_species.clear()
print(f"Demonstration of .clear() method: temp_species = {temp_species}") # temp_species = {}
print()


print("====== Updated colubrid_species dict ======")
# 'Pretty print'
pprint(colubrid_species, sort_dicts=False)
print()


# ====== Dictionary reversal ======
reverse_dict = reverse_dictionary(colubrid_species) # Scientific name becomes the new key, common becomes new value
print("====== Reverse dictionary ======")

# Loop to format output
for sci, common in reverse_dict.items():
    print(f"{sci} is commonly known as {common.title()}")
print()


# Count species / display all keys or values
print(f"Total species in dictionary: {len(colubrid_species)}") # Total species in dictionary: 6

print(f"All common names: {list(colubrid_species.keys())}") 
# ['grass snake', 'western hognose snake', 'boomslang', 'aesculapian snake', 'garter snake', 'corn snake']

print(f"All scientific names: {list(colubrid_species.values())}") 
# ['Natrix natrix cypriaca', 'Heterodon nasicus', 'Dispholidus typus', 'Zamenis longissimus', 'Thamnophis sirtalis', 'Pantherophis guttatus']
print()


# Search for keys in dictionary using get_scientific_name()
get_species = get_scientific_name(colubrid_species, "tiger snake")
print(get_species) # Species not found
get_species_suc = get_scientific_name(colubrid_species, "western hognose snake")
print(get_species_suc) # Heterodon nasicus
print()


# Nested dictionaries
detailed_species = {"boomslang": {"scientific": "Dispholidus typus", "venomous": True, "region": "sub-Saharan Africa"},
                    "grass snake": {"scientific": "Natrix natrix cypriaca", "venomous": False, "region": "Cyprus"}
                    }

print_detailed_species(detailed_species) 
# Prints common name (scientific name) - {Venomous/Non-venomous}, found in {region}
# Boomslang (Dispholidus typus) - Venomous, found in sub-Saharan Africa
# Grass Snake (Natrix natrix cypriaca) - Non-venomous, found in Cyprus

# Display venomous species in dict
venomous = [name for name, data in detailed_species.items() if data['venomous']]
print(f"Venomous species: {venomous}") # Venomous species: ['boomslang']


# Get user input to search dictionary
if __name__ == "__main__":
    try:
        search = input("Enter a common snake name to get its scientific name: ").strip() # Example: BoOmSlAnG
        print(f"{search.title()}'s scientific name is: {get_scientific_name(colubrid_species, search)}") 
        # Boomslang's scientific name is: Dispholidus typus
    
    # Option for Ctrl+C Keyboard Interrupt
    except KeyboardInterrupt:
        print("\nInput Cancelled.")