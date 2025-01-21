#import python libraries for linear regression
import pandas as pd
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
#loading dataset
df = pd.read_csv('output.csv')
#splitting dataset into training and testing
X = df['Rainfall'].values.reshape(-1,1)
y = df['Yield'].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#fitting the model
model = LinearRegression()
model.fit(X_train, y_train)
#predicting the model
y_pred = model.predict(X_test)
#plotting the model
plt.bar(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.title('Production')
plt.xlabel('Rainfall')
plt.ylabel('Yield')
plt.show()



