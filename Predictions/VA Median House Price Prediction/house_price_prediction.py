import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#csv import
csv = "VA Median House Prices 2000-2010.csv"
houseData = pd.read_csv(csv)

#Print Description
#print(houseData.describe())

#Plot Data in 2-D Graph
#houseData.plot(x='Year', y='Median_Price', style='o')  
#plt.title('Year vs Median_Price')  
#plt.xlabel('Year')  
#plt.ylabel('Median_Price')  
#plt.show()

x_train = houseData['Year'].values.reshape(-1,1)
y_train = houseData['Median_Price'].values.reshape(-1,1)


regressor = LinearRegression()
regressor.fit(x_train, y_train)

#Print slope
#print(regressor.coef_)

#Print predictions versus actual data
#y_pred = regressor.predict(x_test)
#df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
#print(df)

#Input and predict
yearInput = int(input("Enter a year: "))
yearInputReshape = np.reshape(yearInput, (1,-1))

y_pred = regressor.predict(yearInputReshape)
y_predInt = int(y_pred)

print("Expected Median House Price in " + str(yearInput) + " is: " + str(y_predInt))