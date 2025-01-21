import random
import matplotlib.pyplot as plt





# Model a coin with two faces: heads and tails
coin = ["heads", "tails"]

# Simulate tossing the coin 1000 times
tosses = [random.choice(coin) for i in range(1000)]

# Count the number of times the coin landed on heads
heads_count = sum(1 for toss in tosses if toss == "heads")

# Visualize the results
plt.bar(["heads", "tails"], [heads_count, 1000 - heads_count])
plt.xlabel("Outcome")
plt.ylabel("Frequency")
plt.title("Coin Toss Simulation (1000 Tosses)")
plt.show()