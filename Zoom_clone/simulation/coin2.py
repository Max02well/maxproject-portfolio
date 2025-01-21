import random
import pandas as pd
import matplotlib.pyplot as plt

def coin():
   toss = random.randint(1, 2)
   return toss

data = []
x = 1
while x <= 60:
    results = coin()
    data.append({'Toss': results, 'Toss_number': x})
    x += 1

# Create a DataFrame
df = pd.DataFrame(data)

# Count occurrences of 2
count2 = df['Toss'].eq(2).sum()
print("Count of 2 is:", count2)

# Count occurrences of 1
count1 = df['Toss'].eq(1).sum()
print("Count of 1 is:", count1)

# Display the DataFrame
print(df)

# Plot the 'Toss' column
df['Toss'].plot(kind='bar', title='Coin Toss Results')
plt.xlabel('Toss Number')
plt.ylabel('Toss Result')
plt.show()