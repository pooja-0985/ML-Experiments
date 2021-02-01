# -*- coding: utf-8 -*-
"""Linear Regression Example

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y29quNoghkoT8xcOJCwiAVC8OS6Rk0BA
"""

# # Data Preprocessing
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')




# Extracting dependent and independent variables:
# Extracting independent variable:
X = dataset.iloc[:, :-1].values
# Extracting dependent variable:
y = dataset.iloc[:, 1].values



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)



# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)


# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, y_pred, color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

print("Regressor slope:  %2.f  "%( regressor.coef_[0]))
print("Regressor intercept:%2.f  "% regressor.intercept_)

YearsExperience= 10
print("Salary for given Years of Experience is :     %.f"    %(regressor.predict([[YearsExperience]])))

from sklearn import metrics
print("MAE %2.f" %(metrics.mean_absolute_error(y_test,y_pred)))

from sklearn import metrics
print("RMSE %2.f" %(np.sqrt(metrics.mean_absolute_error(y_test,y_pred))))

print('Train Score: %f' %(regressor.score(X_train, y_train))) 
print('Test Score: %f' % (regressor.score(X_test, y_test)) )

import pickle 
  
# Save the trained model as a pickle string. 
saved_model = pickle.dumps(regressor) 
# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))  
