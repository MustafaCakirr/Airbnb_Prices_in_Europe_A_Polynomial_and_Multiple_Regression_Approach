import pandas as pd 
import numpy as np
from remove_outliers import remove_outliers 
from sklearn.preprocessing import StandardScaler

## Importing CSV files
amsterdam_data = pd.read_csv("C:/Users/MUSTAFA ÇAKIR/OneDrive/Masaüstü/Projeler/PolynomialLR/amsterdam_weekdays.csv", encoding="utf-8")
barcelona_data = pd.read_csv("C:/Users/MUSTAFA ÇAKIR/OneDrive/Masaüstü/Projeler/PolynomialLR/barcelona_weekdays.csv", encoding="utf-8")
berlin_data = pd.read_csv("C:/Users/MUSTAFA ÇAKIR/OneDrive/Masaüstü/Projeler/PolynomialLR/berlin_weekdays.csv", encoding="utf-8")
london_data = pd.read_csv("C:/Users/MUSTAFA ÇAKIR/OneDrive/Masaüstü/Projeler/PolynomialLR/london_weekdays.csv", encoding="utf-8")
paris_data = pd.read_csv("C:/Users/MUSTAFA ÇAKIR/OneDrive/Masaüstü/Projeler/PolynomialLR/paris_weekdays.csv", encoding="utf-8")


## Preprocessing files
list = [amsterdam_data,barcelona_data,berlin_data,london_data,paris_data]
for i in list:
    i.drop(["Unnamed: 0"],axis=1,inplace = True)

# Categorical to Numeric (One-Hot Encoding)
city_data_list = [amsterdam_data, barcelona_data, berlin_data, london_data, paris_data]
city_data_list = [pd.get_dummies(city, drop_first=True) for city in city_data_list]
amsterdam_data, barcelona_data, berlin_data, london_data, paris_data = city_data_list


# Removing Outliers
city_data_list = [remove_outliers(city, "realSum") for city in city_data_list]
amsterdam_data, barcelona_data, berlin_data, london_data, paris_data = city_data_list

# Remove realSum label 
x_amsterdam_data = amsterdam_data.drop(["realSum"],axis=1)
x_barcelona_data = barcelona_data.drop(["realSum"],axis=1)
x_berlin_data    = berlin_data .drop(["realSum"],axis=1)
x_london_data    = london_data .drop(["realSum"],axis=1)
x_paris_data     = paris_data .drop(["realSum"],axis=1)


# Determining the dependent variable
y_amsterdam_data = amsterdam_data["realSum"] 
y_barcelona_data = barcelona_data["realSum"]
y_berlin_data    = berlin_data["realSum"]   
y_london_data    = london_data["realSum"]   
y_paris_data     = paris_data["realSum"]       


