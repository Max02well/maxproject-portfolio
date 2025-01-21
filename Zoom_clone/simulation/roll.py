import random

# Get the number of rolls from the user
num_rolls = int(input("Enter the number of rolls: "))

# Create a list to store the results of the rolls
rolls = []

# Roll the dice the specified number of times
for i in range(num_rolls):
    # Generate a random number between 1 and 6
    roll = random.randint(1, 6)

    # Add the roll to the list of results
    rolls.append(roll)

# Print the results of the rolls
print("The results of the rolls are:", rolls)