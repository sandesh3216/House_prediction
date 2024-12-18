import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle


file_path = r'C:\Users\sande\OneDrive\Desktop\housing_prices_pred\Dataset\AmesHousing.csv'
housing_data = pd.read_csv(file_path)

features = [
    "Lot Area", "Overall Qual", "Year Built", 
    "Gr Liv Area", "Garage Area", "Total Bsmt SF"
]
target = "SalePrice"

data = housing_data[features + [target]].dropna()


X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
r2 = model.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)
rmse = mse**0.5

print(f"R² Score: {r2}")
print(f"Root Mean Squared Error: {rmse}")

model_filename = 'linear_regression_model.pkl'
with open(model_filename, 'wb') as f:
    pickle.dump(model, f)

print(f"{model_filename}")
