import random
import pandas as pd
import matplotlib.pyplot as plt

# Simulate tossing of a coin 1000 times
toss = 1000
result_of_coin= []   

# Count the number of times the coin shows heads
count_heads = sum(result['Coin Result'] == 'Heads' for result in result_of_coin)
count_tails=sum(result['Coin Result']=='Tails' for result in result_of_coin)

# Print the results
print("Side_shown:")
for result in result_of_coin:
    print(result)

#print("\nNumber of times the coin showed heads:", count_heads)
#print("\nNumber of times the coin showed tails:", count_tails)
