import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#csv import
csv = "VA Unemployment Percent 1976-2019.csv"
data = pd.read_csv(csv)

#Print Description
print(data.describe())

#Plot Data in 2-D Graph
data.plot(x='Year', y='Unemployment_Rate', style='o')  
plt.title('Year vs Unemployment_Rate')  
plt.xlabel('Year')  
plt.ylabel('Unemployment_Rate')  
plt.show()

x_train = data['Year'].values.reshape(-1,1)
y_train = data['Unemployment_Rate'].values.reshape(-1,1)


regressor = LinearRegression()
regressor.fit(x_train, y_train)

#Print slope
#print(regressor.coef_)

#Print predictions versus actual data
#y_pred = regressor.predict(x_train)
#df = pd.DataFrame({'Actual': y_train.flatten(), 'Predicted': y_pred.flatten()})
#print(df)

#Input and predict
yearInput = int(input("Enter a year: "))
yearInputReshape = np.reshape(yearInput, (1,-1))

y_pred = regressor.predict(yearInputReshape)
y_predInt = int(y_pred)

print("Expected Unemployment Rate in " + str(yearInput) + " is: " + str(y_predInt))