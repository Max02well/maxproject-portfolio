import random
import pandas as pd
import matplotlib.pyplot as plt

def coin():
   toss = random.randint(1, 2)
   return toss

data = []
x = 1
while x <= 1000:
    results = coin()
    data.append({'Toss': results, 'Toss_number': x})
    x += 1

# Create a DataFrame
df = pd.DataFrame(data)

# Count occurrences of tail-count2
count2 = df['Toss'].eq(2).sum()
print("Count of Tail is:", count2)

# Count occurrences of head-count1
count1 = df['Toss'].eq(1).sum()
print("Count of Head is:", count1)

# Display the DataFrame
print(df)

# Plot the 'Toss' column
plt.bar(["heads", "tails"], [count1, 1000 - count1])
plt.xlabel("Outcome")
plt.ylabel("Frequency")
plt.title("Coin Toss Simulation (1000 Tosses)")
plt.show()
#df['Toss'].plot(kind='bar', title='Coin Toss Results')
#plt.xlabel('Toss Number')
#plt.ylabel('Toss Result')
#plt.show()