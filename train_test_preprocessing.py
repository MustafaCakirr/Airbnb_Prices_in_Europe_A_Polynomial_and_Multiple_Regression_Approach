from numpy.random import rand
from sklearn.model_selection import train_test_split
from data_preprocessing import * 
from sklearn.preprocessing import StandardScaler

# Train-Test Split
ax_train,ax_test,ay_train,ay_test = train_test_split(x_amsterdam_data,y_amsterdam_data,test_size=0.3,random_state=2)
barx_train,barx_test,bary_train,bary_test = train_test_split(x_barcelona_data,y_barcelona_data,test_size=0.3,random_state=2)
berx_train,berx_test,bery_train,bery_test = train_test_split(x_berlin_data,y_berlin_data,test_size=0.3,random_state=2)
lx_train,lx_test,ly_train,ly_test = train_test_split(x_london_data,y_london_data,test_size=0.3,random_state=2)
px_train,px_test,py_train,py_test = train_test_split(x_paris_data,y_paris_data,test_size=0.3,random_state=2)

ax_test = ax_test.reindex(columns=ax_train.columns, fill_value=0)
barx_test = barx_test.reindex(columns=barx_train.columns, fill_value=0)
berx_test = berx_test.reindex(columns=berx_train.columns, fill_value=0)
lx_test = lx_test.reindex(columns=lx_train.columns, fill_value=0)
px_test = px_test.reindex(columns=px_train.columns, fill_value=0)

# Train ve Test Lists
x_train_unscale_list = [ax_train, barx_train, berx_train, lx_train, px_train]
x_test_unscale_list = [ax_test, barx_test, berx_test, lx_test, px_test]

# Empty list for Store
x_train_scaled_list = []
x_test_scaled_list = []

# Scaling
scaler = StandardScaler()

for i in range(len(x_train_unscale_list)):
    
    scaler.fit(x_train_unscale_list[i])  # Train data fit 
    x_train_scaled = scaler.transform(x_train_unscale_list[i])  # Train data transform
    x_test_scaled = scaler.transform(x_test_unscale_list[i])  

    # Add scaled data to empty lists
    x_train_scaled_list.append(x_train_scaled)
    x_test_scaled_list.append(x_test_scaled)

# Reassign scaled datasets to their original variables
ax_train_scaled, barx_train_scaled, berx_train_scaled, lx_train_scaled, px_train_scaled = x_train_scaled_list
ax_test_scaled, barx_test_scaled, berx_test_scaled, lx_test_scaled, px_test_scaled = x_test_scaled_list
