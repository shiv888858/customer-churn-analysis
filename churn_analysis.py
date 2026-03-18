import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("churn.csv")

# Show first rows
print(data.head())

# Check missing values
print("\nMissing values:\n", data.isnull().sum())

# Fix TotalCharges column
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')

# Drop null values
data = data.dropna()

# Churn count
print("\nChurn count:\n", data['Churn'].value_counts())

# Graph 1
sns.countplot(x='Churn', data=data)
plt.title("Churn Distribution")
plt.show()

# Graph 2
sns.countplot(x='Contract', hue='Churn', data=data)
plt.title("Churn by Contract")
plt.xticks(rotation=30)
plt.show()

# Graph 3
sns.histplot(data=data, x='tenure', hue='Churn', bins=30)
plt.title("Tenure vs Churn")
plt.show()

# Graph 4
sns.boxplot(x='Churn', y='MonthlyCharges', data=data)
plt.title("Monthly Charges vs Churn")
plt.show()

print("\nInsight: Monthly contract + low tenure customers churn more.")