import pandas as pd 
import csv
filename = 'test.csv'
df = pd.read_csv('test.csv')
print(df.head())
print(df.tail())





# count no. of rows in csv file and print first n rows 