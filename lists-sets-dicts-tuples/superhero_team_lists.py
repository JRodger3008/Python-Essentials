# Scenario: Building a Superhero Team
# I asked ChatGPT to construct a scenario with list manipulation for me to solve.


# Step 1: Creates an empty list named justice_defenders.
justice_defenders = []

# Step 2: Adds the founding members using append().
justice_defenders.append("Captain Strong")
justice_defenders.append("Shadow Lynx")
justice_defenders.append("Quantum Blaze")

print(f"Founding members: {justice_defenders}")

# Step 3: Add two recruits via user input
for name in ["Iron Pulse", "Night Specter"]:
    input(f"Press Enter to add {name} to list: ") # User input to confirm addition
    justice_defenders.append(name) # Add new recruits to team

print(f"After adding recruits: {justice_defenders}")

# Step 4: Remove the last two recruits
del justice_defenders[-1]  # Remove Night Specter (Last entry)
del justice_defenders[-1]  # Remove Iron Pulse (2nd to last entry)
print(f"After removing recruits: {justice_defenders}")

# Step 5: Insert Mystic Nova at index 1
justice_defenders.insert(1, "Mystic Nova")
print(f"Final team lineup: {justice_defenders}")
    

