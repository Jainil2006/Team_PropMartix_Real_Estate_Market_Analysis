# Project Name

PropMartix_Real_Estate_Market_Analysis

## Team Members
1. Abijay (Ku2407u005)
2. Jainil (Ku2407u084)
3. Nigam  (Ku2407u0148)
4. Tushar (Ku2408u223)
5. Bhavya (Ku2407u034)


## Overview
This project analyzes Melbourne housing data to predict property prices and visualize key patterns. The workflow includes data preprocessing, model training, evaluation, and visualization of insights using Python.

## Table Of Content

1. Overview  
2. Project Steps
   1. Importing Libraries and Loading Data
   2. Data Preprocessing
   3. Splitting the Data
   4. Model Training and Evaluation
   5. Visualization
     a. Pie Chart: Property Types Distribution
     b. Histogram: Price Distribution
     c. Heatmap: Correlation Matrix
     d. Line Graph: Price Trends Over Time
3. Prerequisites 
   - Libraries  
   - Dataset
4. Usage  
5. Output
   - Evaluation Metrics
   - Visualizations
6. Notes
7. License
   
## Required Libaries 

- NumPy 
- Pandas 
- Matplotlib  
- Scikit-learn

## How to use


1. Install Required Libraries:  
   Make sure all required Python libraries are installed in your environment.

2. Prepare the Dataset:  
   Place the dataset file (`Melbourne_Housing_Synthetic.csv`) in the same directory as the script.

3. Run the Script:  
   Execute the script using your Python environment.

4. View Results:  
   - Evaluation metrics such as MAE, MSE, and RMSE will be displayed in the output.  
   - Visualizations (e.g., pie charts, histograms, heatmaps) will be displayed in pop-up windows for analysis. 

5. Adjust if Needed :  
   If the dataset format changes, update feature selection or preprocessing steps accordingly.
## CSV Requirements
1. The dataset file should be named Melbourne_Housing_Synthetic.csv.
2. Required columns:
  - Price (Target variable)
  - Rooms, Bathroom, Car, Landsize, BuildingArea, YearBuilt, Distance, Lattitude, Longtitude (Numeric features)
  - Type, Method, Regionname (Categorical features)
  - Optional: Date for time-based price trends
## Data Processing
1. Handle Missing Values:
  - Rows with missing Price are dropped.
  - Other missing values are filled with the column median.
2. Encode Categorical Data:
  - Apply one-hot encoding to the Type, Method, and Regionname columns.
3. Feature Selection:
  - Use numeric features and encoded categorical features for training.
4. Split Data:
  - Divide the data into 80% training and 20% testing sets.
## Visualizations
1. Pie Chart: Distribution of property types (e.g., house, apartment).
2. Histogram: Frequency of property prices across ranges.
3. Heatmap: Correlation matrix of numeric features to identify relationships.
4. Line Graph: Average property prices over time (if Date column exists).
## Output Examples
1. Evaluation Metrics:
  - Mean Absolute Error (MAE): Shows the average error in price prediction.
  - Mean Squared Error (MSE): Indicates average squared error.
  - Root Mean Squared Error (RMSE): Represents the standard deviation of the errors.
### Visualizations:
1. Pie chart showing property types like House: 60%, Apartment: 30%, Unit: 10%.
2. Histogram showing price distribution, e.g., peak frequency around $500,000–$700,000.
## Error Handling
1. Missing Columns:
  - If essential columns like Price are missing, the script will notify and exit.
  - Optional columns like Date will prompt a message if unavailable but won’t stop execution.
2. Invalid Values:
-  Non-numeric values in numeric columns will trigger an error message.
3. Empty Dataset:
  - The script will check if the dataset has rows after preprocessing. If not, it will stop execution with an appropriate message.
## Future Enhancements
1. Support for Additional Models:
  - Include advanced models like Random Forest or Gradient Boosting for better predictions.
2. Interactive Visualizations:
  - Use libraries like Plotly for dynamic and interactive charts.
3 .Improved Data Cleaning:
  - Automate handling of outliers and unusual values.
4. Feature Engineering:
  - Add new features like Price per Square Meter or Age of Property.
5. Deployment:
  - Package the model into a web application using Flask or Streamlit for end-user interaction.
## Author
- Developed by Team Prop Martix.
- Thank You.




