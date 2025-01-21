from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import pickle
import numpy as np

#load dataset
df1=pd.read_csv('output.csv')
df1.head(10)
#feature selection
x = df1[["Area", "Rainfall", "Fertilizer", "Production"]]
y=df1[["Yield"]]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
#initialize the model
model=LinearRegression()
#train the model
model.fit(x_train,y_train)
#test model
y_pred=model.predict(x_test)
#score
accuracy=r2_score(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print("Mean Squared Error:",mse)
print("R2 Score:",r2)
#print("Accuracy:",accuracy)
#Save the trained model as a pickle file
with open('trained_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
user_input = []
for column in x.columns:
    value = float(input(f"Enter value for {column}: "))
    user_input.append(value)

# Reshape user input for prediction
user_input_array = np.array([user_input])

# Predict using the model
y_pred = model.predict(user_input_array)
print(f"Predicted value: {y_pred[0]}")

