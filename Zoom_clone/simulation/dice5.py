import random

# Simulate rolling a 6-sided die 200 times
simulations = 200
results = []

for toss_number in range(123, 123 + simulations):
    # Simulate a die roll (1 to 6)
    die_result = random.randint(1, 6)
    
    # Store the result along with the toss number
    results.append({'Toss Number': toss_number, 'Die Result': die_result})

# Count the number of times the die shows a five
count_fives = sum(result['Die Result'] == 5 for result in results)

# Print the results
print("Results:")
for result in results:
    print(result)

print("\nNumber of times the die showed a five:", count_fives)
