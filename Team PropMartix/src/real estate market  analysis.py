 #Part 1: Importing Libraries and Loading Data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load dataset
data = pd.read_csv('Melbourne_Housing_Synthetic.csv')
# Part 2: Data Preprocessing

# Drop rows with missing price and fill other missing values with median
data = data.dropna(subset=["Price"])
data.fillna(data.median(numeric_only=True), inplace=True)

# Encode categorical variables using one-hot encoding for selected columns
categorical_cols = ["Type", "Method", "Regionname"]
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Select features for analysis and prediction
features = [
    "Rooms", "Bathroom", "Car", "Landsize", "BuildingArea", "YearBuilt",
    "Distance", "Lattitude", "Longtitude"
] + [col for col in data.columns if col.startswith(tuple(categorical_cols))]
X = data[features]
y = data["Price"]
# Part 3: Splitting the Data into Training and Test Sets

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Part 4: Model Training and Evaluation

# Model training and prediction
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Display evaluation results
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")
# Part 5: Visualization - Pie Chart (Property Types Distribution)

# Reload raw data to access the original 'Type' column
raw_data = pd.read_csv('Melbourne_Housing_Synthetic.csv')
type_counts = raw_data["Type"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Property Types")
plt.show()
# Part 6: Visualization - Histogram (Price Distribution)

plt.figure(figsize=(8, 6))
plt.hist(data["Price"], bins=30, color='skyblue', edgecolor='black')
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
# Part 7: Visualization - Heatmap (Correlation Matrix)

# Only include numeric columns for correlation
numeric_data = data.select_dtypes(include=[np.number])
correlation_matrix = numeric_data.corr()

plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap="coolwarm", aspect="auto")
plt.colorbar(label="Correlation Coefficient")
plt.xticks(ticks=np.arange(len(correlation_matrix.columns)), labels=correlation_matrix.columns, rotation=90)
plt.yticks(ticks=np.arange(len(correlation_matrix.columns)), labels=correlation_matrix.columns)
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.show()
# Part 8: Visualization - Line Graph (Price Trends Over Time)

# Assuming 'Date' column exists and is converted to datetime (if applicable)
if "Date" in data.columns:
    data["Date"] = pd.to_datetime(data["Date"])
    price_trend = data.groupby(data["Date"].dt.to_period("M"))["Price"].mean()

    plt.figure(figsize=(10, 6))
    plt.plot(price_trend.index.astype(str), price_trend.values, marker='o', linestyle='-', color='blue')
    plt.title("Average Property Prices Over Time")
    plt.xlabel("Time (Monthly)")
    plt.ylabel("Average Price")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
else:
    print("Date column not found for plotting price trends.")
