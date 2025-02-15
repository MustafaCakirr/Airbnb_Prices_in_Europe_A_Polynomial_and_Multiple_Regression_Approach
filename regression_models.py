import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
from data_preprocessing import * 
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from train_test_preprocessing import *
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


# City list
cities = ["amsterdam","barcelona", "berlin", "london", "paris"]

# Store data for all cities in one list
x_train_list = [ax_train_scaled, barx_train_scaled, berx_train_scaled, lx_train_scaled, px_train_scaled]
y_train_list = [ay_train, bary_train, bery_train, ly_train, py_train]

x_test_list = [ax_test_scaled, barx_test_scaled, berx_test_scaled, lx_test_scaled, px_test_scaled]
y_test_list = [ay_test, bary_test, bery_test, ly_test, py_test]

# Polynomial Regression  for London and Paris
degree = 2  

# Dictionary where we will store models for all cities
models = {}

def train_and_evaluate():
    
    for city, x_train_data, y_train_data, x_test_data, y_test_data in zip(cities, x_train_list, y_train_list,x_test_list,y_test_list):
        
        print(f"\nŞehir: {city.upper()}")
      
        if isinstance(x_train_data, pd.Series):
            x_train_data = x_train_data.to_frame()  #  Series -> DataFrame

        # Polynomial Regression  for London and Paris
        if city in ["london", "paris"]:
            # print(f"{city.upper()} için Polynomial Regression uygulanıyor..")
            poly = PolynomialFeatures(degree=degree, include_bias=False)
            x_train_poly = poly.fit_transform(x_train_data)
            x_test_poly = poly.transform(x_test_data)

            # Find the best Alpha value for Ridge Regression  (Grid Search)
            param_grid = {'alpha': [0.01, 0.1, 1, 10, 100]}
            ridge_cv = GridSearchCV(Ridge(), param_grid, scoring='r2', cv=5)
            ridge_cv.fit(x_train_poly, y_train_data)

            # Train Ridge Model with Best Alpha
            ridge_model = Ridge(alpha=ridge_cv.best_params_["alpha"])
            ridge_model.fit(x_train_poly, y_train_data)

            y_train_pred = ridge_model.predict(x_train_poly)
            y_test_pred = ridge_model.predict(x_test_poly)
            print("Model Katsayıları:", ridge_model.coef_)
            print("Dönüştürülmüş X_train Shape:", x_train_poly.shape)
                         
        else:
            print(f"{city.upper()} için Multiple Linear Regression")
            model = LinearRegression()
            model.fit(x_train_data, y_train_data)

            y_train_pred = model.predict(x_train_data)
            y_test_pred = model.predict(x_test_data)
            
        mse_train = mean_squared_error(y_train_data, y_train_pred)
        r2_train = r2_score(y_train_data, y_train_pred)

        mse_test = mean_squared_error(y_test_data, y_test_pred)
        r2_test = r2_score(y_test_data, y_test_pred)
        
        print(f"Train MSE: {mse_train:.4f}, R²: {r2_train:.4f}")
        print(f"Test MSE: {mse_test:.4f}, R²: {r2_test:.4f}")
       
        plt.figure(figsize=(8, 5))
        plt.scatter(y_test_data, y_test_pred, alpha=0.5, color="blue", label="Tahminler")
        plt.plot([y_test_data.min(), y_test_data.max()], [y_test_data.min(), y_test_data.max()], 'r', lw=2, label="Identity Line")
        plt.xlabel("Gerçek Değerler")
        plt.ylabel("Tahmin Edilen Değerler")
        plt.legend()
        plt.title(f"{city.upper()} - Gerçek vs Tahmin Edilen Değerler")
        plt.show()
            

    