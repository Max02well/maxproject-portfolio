import pandas as pd
import random

# i. (6 marks)
data = []
for i in range(200):
    roll =random.randint(1,6)
    d = {'roll':roll}
    data.append(d)

# ii. (3 marks)
df = pd.DataFrame(data) #important so as to use pandas in inserting column

num = pd.Series(range(1,201)) #the column to be inserted
df.insert(0,'num',num)#note the 0, try with 1 and note the results.
print(df)

# iii. (3 marks)
count = df['roll'].value_counts()[5]

print(f'The number of 5s is: {count}')


