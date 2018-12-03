import pandas as pd #importing pandas
data=pd.read_csv('https://raw.githubusercontent.com/Sridhar-S-G/Databetics-Using-Logistic-Regression/master/diabetes.csv') #reading data from csv 
df=pd.DataFrame(data) #Converting data to DataFrame
print(df.head()) #Print head of df(printing first 5 rows of data)
