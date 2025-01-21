import random

# Simulate rolling a 6-sided die 200 times
rolls = [random.randint(1, 6) for i in range(200)]

# Add a column to the list to store the number of each tossing of the die
rolls_with_numbers = [(roll, i + 123) for i, roll in enumerate(rolls)]

# Count the number of times the dice showed a five
count_fives = sum(1 for roll, _ in rolls_with_numbers if roll == 5)

print(f"The dice showed a five {count_fives} times.")