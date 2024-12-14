#Project Name

PropMartix_Real_Estate_Market_Analysis

##Team Members
Abijay (Ku2407u084)
Jainil  (Ku2407u084)
Melbourne Housing Data Analysis

This project performs data analysis and prediction on the Melbourne Housing Synthetic dataset. The project includes data preprocessing, model training, evaluation, and visualization of insights.

Project Overview

The analysis is divided into the following parts:

Importing Libraries and Loading Data

Data Preprocessing

Splitting the Data into Training and Test Sets

Model Training and Evaluation

Visualization

Part 1: Importing Libraries and Loading Data

Libraries used:

numpy, pandas for data manipulation and computation.

matplotlib.pyplot for data visualization.

sklearn.model_selection for splitting data into training and test sets.

sklearn.linear_model for training a linear regression model.

sklearn.metrics for model evaluation.

Dataset: Melbourne_Housing_Synthetic.csv is loaded using pandas.

Part 2: Data Preprocessing

Handling Missing Values:

Rows with missing Price values are dropped.

Other missing values are filled with the median of respective columns.

Encoding Categorical Variables:

One-hot encoding is applied to the categorical columns Type, Method, and Regionname.

Feature Selection:

Selected features include numerical columns (Rooms, Bathroom, Car, Landsize, BuildingArea, YearBuilt, Distance, Lattitude, Longtitude) and encoded categorical variables.

Part 3: Splitting the Data into Training and Test Sets

Data is split into training and test sets using an 80-20 split ratio.

random_state=42 ensures reproducibility.

Part 4: Model Training and Evaluation

Model: A linear regression model is trained using the training dataset.

Evaluation Metrics:

Mean Absolute Error (MAE): Measures the average absolute error between predictions and actual values.

Mean Squared Error (MSE): Captures the average squared error.

Root Mean Squared Error (RMSE): Square root of MSE, providing an error measure in the same unit as the target variable.

Part 5: Visualization - Pie Chart (Property Types Distribution)

Distribution of property types is visualized as a pie chart.

Data for the chart is derived from the Type column of the raw dataset.

Part 6: Visualization - Histogram (Price Distribution)

A histogram visualizes the distribution of property prices.

Bins = 30, and color is set to skyblue with black edges.

Part 7: Visualization - Heatmap (Correlation Matrix)

Correlation between numerical features is visualized using a heatmap.

numpy and matplotlib are used for generating the heatmap.

Color scheme: coolwarm.

Part 8: Visualization - Line Graph (Price Trends Over Time)

A line graph shows average property price trends over time (monthly).

If a Date column exists:

It is converted to datetime type.

Prices are grouped by monthly periods.

Requirements

Python 3.x

Required Libraries: numpy, pandas, matplotlib, scikit-learn

How to Run the Code

Ensure Melbourne_Housing_Synthetic.csv is in the working directory.

Install required libraries using:

pip install numpy pandas matplotlib scikit-learn

Execute the script in a Python environment (e.g., Jupyter Notebook or any IDE).

Results

Model Evaluation:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

Visualizations:

Pie Chart: Property type distribution.

Histogram: Price distribution.

Heatmap: Feature correlation.

Line Graph: Average property price trends (if applicable).

Notes

Ensure all required columns (e.g., Price, Type, etc.) exist in the dataset.

If the Date column is missing, the price trend graph will not be generated.


