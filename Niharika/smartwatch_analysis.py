import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

data = pd.read_csv("D:\HR-Analytics-Project/dailyActivity_merged.csv")
print(data.head())
print(data.isnull().sum())
print(data.info())


# Changing datatype of ActivityDate
data["ActivityDate"] = pd.to_datetime(data["ActivityDate"], 
                                      format="mixed")
print(data.info())


# Adding all the active minutes to total minutes
data["TotalMinutes"] = data["VeryActiveMinutes"] + data["FairlyActiveMinutes"] + data["LightlyActiveMinutes"] + data["SedentaryMinutes"]
print(data["TotalMinutes"].sample(5))


# Calculate summary statistics
print(data.describe())


# Create histograms for key variables
plt.figure(figsize=(12, 6))
sns.histplot(data['TotalSteps'], kde=True, bins=20)
plt.title('Total Steps Histogram')
plt.xlabel('Total Steps')
plt.ylabel('Frequency')
plt.show()

# Create box plots
plt.figure(figsize=(12, 6))
sns.boxplot(data=data[['TotalSteps', 'Calories', 'TotalMinutes']])
plt.title('Box Plots for Key Variables')
plt.ylabel('Value')
plt.xticks()
plt.show()


# Convert the 'Date' column to a datetime object
data['ActivityDate'] = pd.to_datetime(data['ActivityDate'])

# Calculate daily averages
daily_avg = data.resample('D', on='ActivityDate').mean()

# Create time series plots
plt.figure(figsize=(14,6))
plt.plot(daily_avg.index, daily_avg['TotalSteps'], label='Total Steps', marker='o')
plt.xlabel('Date')
plt.ylabel('Average Total Steps')
plt.title('Daily Average Total Steps')
plt.legend()
plt.show()
# Calculate correlation matrix
correlation_matrix = data[['TotalSteps', 'Calories', 'TotalMinutes']].corr()

# Perform simple linear regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X = data['TotalMinutes'].values.reshape(-1, 1)
y = data['Calories']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Visualize regression results
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, model.predict(X_test), color='red', linewidth=3)
plt.title('Linear Regression: Calories Burned vs. Total Minutes')
plt.xlabel(' Total Minutes')
plt.ylabel('Calories Burned')
plt.show()





from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Fit polynomial regression models
degrees = [2, 3]  # You can try different degrees
for degree in degrees:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)

    # Visualize polynomial regression curves
    X_range = np.linspace(min(X_test), max(X_test), 100).reshape(-1, 1)
    y_pred = model.predict(X_range)

    plt.scatter(X_test, y_test, color='blue')
    plt.plot(X_range, y_pred, color='red', linewidth=3)
    plt.title(f'Polynomial Regression (Degree {degree}): Calories Burned vs. Total Minutes')
    plt.xlabel('Total Minutes')
    plt.ylabel('Calories Burned')
    plt.show()

    # Evaluate goodness of fit
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Degree {degree} - R-squared: {r2:.2f}, MSE: {mse:.2f}')


# Create a binary variable for activity classification
data['ActivityClass'] = (data['TotalSteps'] >= 10000).astype(int)

# Perform logistic regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

X = data[['TotalSteps', 'TotalMinutes']].values
y = data['ActivityClass']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')

# Visualize decision boundary and decision probabilities
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='coolwarm', marker='o')
plt.xlabel('Total Steps')
plt.ylabel('Total Minutes')
plt.title('Logistic Regression Decision Boundary')
plt.show()
