import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Sample data
data = {
    'area': [1000, 1500, 2000, 2500, 3000],
    'bedrooms': [2, 3, 3, 4, 4],
    'bathrooms': [1, 2, 2, 3, 3],
    'price': [100000, 150000, 200000, 250000, 300000]
}
df = pd.DataFrame(data)

# Features and target
X = df[['area', 'bedrooms', 'bathrooms']]
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
