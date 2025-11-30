#load data
import pandas as pd
df = pd.read_csv('C:/Users/Admin/OneDrive/Desktop/ML_Practice/model/delaney_solubility_with_descriptors.csv')

#Data separation in x and y
y = df['logS']
x = df.drop('logS', axis = 1)

#Data Spliting
from sklearn.model_selection import train_test_split
X_train, X_test,Y_train, Y_test = train_test_split(x,y,test_size=0.2,random_state=100)
# print(X_train)
# print(X_test)
 
#Model Building (using Linear Regression)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, Y_train)
y_lr_train_pred = lr.predict(X_train)
y_lr_test_pred = lr.predict(X_test)
# print(y_lr_train_pred)

#Evaluating Model Performance
from sklearn.metrics import mean_squared_error,r2_score
lr_train_mse = mean_squared_error(Y_train, y_lr_train_pred)
lr_train_r2 = r2_score(Y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(Y_test, y_lr_test_pred)
lr_test_r2 = r2_score(Y_test, y_lr_test_pred)
# print("LR MSE(Train) : ",lr_train_mse)
# print("LR R2(Train) : ",lr_train_r2)
# print("LR MSE(Test) : ",lr_test_mse)
# print("LR R2(Test) : ",lr_test_r2)
lr_results = pd.DataFrame(['Linear Regression',lr_train_mse,lr_train_r2,lr_test_mse,lr_test_r2]).transpose()
lr_results.columns = ['Method   ', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
print(lr_results)

#Visual
import matplotlib.pyplot as plt

plt.scatter(Y_test, y_lr_test_pred)
plt.xlabel("Actual logS")
plt.ylabel("Predicted logS")
plt.title("Actual vs Predicted (Test Set)")
plt.show()
