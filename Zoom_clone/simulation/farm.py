import pandas as pd
import random
import numpy as np
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import csv
import matplotlib.pyplot as plt

def years():
    return random.randint(2003, 2022)

def area():
    return random.randint(10, 1000)

def rainfall():
    return random.randint(200, 5000)

def production():
    return random.randint(1000, 25000)

def fertilizer():
    return random.randint(1, 1000)

def yield_():
    return random.randint(1, 10)

# Simulate the code for 500 times
results = []
for _ in range(10000):
    data = {
        'Year': years(),
        'Area': area(),
        'Rainfall': rainfall(),
        'Production': production(),
        'Fertilizer': fertilizer(),
        'Yield': yield_()
    }
    results.append(data)

# Create a DataFrame from the results    
df = pd.DataFrame(results)


# Display the DataFrame
print("DataFrame:")
print(df)

# Save the DataFrame to a CSV file
csv_filename = 'output.csv'
df.to_csv(csv_filename, index=False)

print(f"\nDataFrame saved to {csv_filename}")

