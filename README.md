# customer-churn-analysis
Customer churn analysis using Python

# 📊 Customer Churn Analysis

## 🔹 Project Overview
This project analyzes telecom customer data to identify patterns and factors leading to customer churn.

Customer churn is a critical problem for businesses, and this analysis helps in understanding why customers leave.


## 🔹 Tech Stack
- Python
- Pandas
- Matplotlib
- Seaborn


## 🔹 Dataset
- Contains ~7000 customer records
- Features include:
  - Tenure
  - Contract type
  - Monthly charges
  - Payment method
  - Churn status


## 🔹 Key Steps Performed
- Data loading and cleaning
- Handling missing values
- Exploratory Data Analysis (EDA)
- Feature-wise churn analysis
- Data visualization


## 🔹 Visualizations
The project includes:
- Churn distribution (Count Plot)
- Contract type vs Churn
- Tenure distribution (Histogram)
- Monthly charges vs Churn (Box Plot)


## 🔹 Key Insights
- Customers with **monthly contracts** show higher churn
- Customers with **low tenure** are more likely to leave
- Higher monthly charges slightly increase churn probability


## 🔹 Business Impact
This analysis can help companies:
- Identify high-risk customers
- Improve retention strategies
- Design better long-term plans


## 🔹 How to Run
```bash
pip install pandas matplotlib seaborn
python churn_analysis.py
