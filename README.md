# Airbnb_Prices_in_Europe_A_Polynomial_and_Multiple_Regression_Approach
# Predicting Airbnb Prices in Europe: A Polynomial and Multiple Regression Approach

##  Project Description
This project aims to **predict Airbnb prices** in various European cities using **Linear Regression, Polynomial Regression, and Ridge Regression** models.  
The dataset is sourced from **Kaggle** and contains various features related to rental properties.  

**Dataset Source:**  
[Kaggle - Airbnb Price Determinants in Europe](https://www.kaggle.com/datasets/thedevastator/airbnb-price-determinants-in-europe/data)

---

##  Dataset Information
**Columns in the dataset:**  
- **realSum** → Price of the listing (Target variable)  
- **room_shared, room_private** → Whether the room is shared or private  
- **person_capacity** → Maximum capacity of guests  
- **host_is_superhost** → Whether the host is a "superhost"  
- **cleanliness_rating** → Cleanliness rating  
- **guest_satisfaction_overall** → Overall guest satisfaction rating  
- **bedrooms** → Number of bedrooms  
- **dist, metro_dist** → Distance to city center and metro  
- **attr_index, attr_index_norm** → Attraction index and its normalized version  
- **rest_index, rest_index_norm** → Restaurant index and its normalized version  
- **lng, lat** → Location data (longitude and latitude)  
- **room_type_Private room, room_type_Shared room** → Room type categories (One-Hot Encoded)  

The dataset includes properties from **Amsterdam, Barcelona, Berlin, London, and Paris**.  

---

##  Models Used  
Three different regression models were used in this project:  
**Linear Regression (Multiple Linear Regression)** → Applied to Amsterdam, Barcelona, and Berlin.  
**Polynomial Regression + Ridge Regression** → Applied to London and Paris (Degree: 2).  

---

##  Model Results  

Below are the **Mean Squared Error (MSE)** and **R² score** values.  
**A higher R² score indicates a better fit of the model to the data.**  

### ** Amsterdam (Linear Regression)**
- **Train MSE:** 18,451.44 | **Train R²:** 0.6517  
- **Test MSE:** 21,570.14 | **Test R²:** 0.5673  

### ** Barcelona (Linear Regression)**
- **Train MSE:** 4,393.50 | **Train R²:** 0.6501  
- **Test MSE:** 4,022.55 | **Test R²:** 0.7013  

### ** Berlin (Linear Regression)**
- **Train MSE:** 3,510.25 | **Train R²:** 0.5087  
- **Test MSE:** 3,047.31 | **Test R²:** 0.5591  

### ** London (Polynomial Regression + Ridge)**
- **Train MSE:** 7,963.63 | **Train R²:** 0.7249  
- **Test MSE:** 8,829.02 | **Test R²:** 0.6935  

### ** Paris (Polynomial Regression + Ridge)**
- **Train MSE:** 9,161.74 | **Train R²:** 0.5973  
- **Test MSE:** 10,813.25 | **Test R²:** 0.5041  

### ** Interpretation of Results**
- **Barcelona and London achieved the best R² scores.**  
- **Polynomial Ridge Regression performed well in London but showed lower-than-expected performance in Paris.**  
- **Berlin and Paris models had lower R² scores compared to other cities.**  

---
![Image](https://github.com/user-attachments/assets/a8733871-cae0-4f90-979a-0da5b7eeaa2d)
![Image](https://github.com/user-attachments/assets/f9164efc-9049-464e-8b16-3ca8d9c766bb)
![Image](https://github.com/user-attachments/assets/01b35aec-0a19-4548-b888-b97e8496f9e4)
![Image](https://github.com/user-attachments/assets/16ec8e1b-80ba-468a-bbe0-35744b63d8bb)


