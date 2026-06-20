# This is SMLR Section B & C Referred from May 2025, Feb 2025, Nov 2024, Mar 2024 Papers.
# Date : 09/04/2026, 1:16 AM

# Default Import in .ipynb Jupyter Notebook given as question paper in exam system
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import scipy.stats as stats
from statsmodels.stats.api import het_goldfeldquandt

from sklearn.model_selection import train_test_split
#import functions to perform feature selection
from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from sklearn.feature_selection import RFE

# import function to perform linear regression
from sklearn.linear_model import LinearRegression
# import function for elastic net regression
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Ridge

# import functions to perform cross validation

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.linear_model import SGDRegressor
from statsmodels.stats.diagnostic import linear_rainbow


# =============================================================================
# Section B
# (40 Marks) (About Data, EDA, Data preprocessing)
# =============================================================================

# About Section B
#
# Dataset Used :
# 1. Laptop Price prediction [May 2025]
# 2. Fish Weight Prediction [Feb 2025, Mar 2024]
# 3. Possum's total length [Nov 2024]
# 4. Housing price dataset of Bengaluru city [Aug 2023]
# 5. NYC listing activity [Model paper]
# All Dataset is mostly unique from prev papers
# Only 1 Dataset for both Section B and C
#
# IMP Questions : (40 Marks)
#
# About Data : (Max 9 Marks)
# 1. IMP : Load dataset (Every papers - 1 Mark)
# 2. IMP : The dimensions of the dataset [no of rows and columns] (Every papers - 1 Mark)
# 3. IMP : Data types of all the features (Every Papers - 1 Mark)
# 4. IMP : Identify the feature need of type casting and perform it (Every Paper - 1 Mark)
# 5. IMP : Statistical summary of all the numeric and categorical features and drop unnecessary features (Every Paper - 2 Marks)
# 6. IMP : How many unique categories are available and number of instances in each of the categorical features (Every Paper - 3 Marks)
#
# EDA : (Max 9 marks)
# 7. IMP : Explore the associations between the numerical predictors and the target feature using visualizations and observations. (All Papers - 4 Marks)
# 8. IMP : Examine how the categorical features are associated with the target variable. Use visualizations and interpretations. (All Papers - 3 Marks)
# 9. IMP : Visualize the relationship between Column-X and Column-Y, use scatterplot (All Papers - 1 Marks)
# 10. IMP : Skewness of numerical features (All Papers - 1 Marks)
#    *. Show outliers distribution of variable Column-Z by drawing Boxplot. (Aug 2023 - 3 Marks)
#    *. Check/Visualize the relationships between categorical features and the target feature using violin plot. State the inferences (Nov 2024 - 2 Marks)
#
# Data Preprocessing : (Max 25 Marks)
# 11. IMP : Check for the presence of missing values across features and represent them visually also treat it. (All Papers - 5 Marks)
# 12. IMP : Examine the numerical features for any outliers and provide visual evidence and also treat it with dropping (Use IQR). (All Papers - 5 Marks)
# 13. IMP : Perform label(or n-1 dummy) encoding to convert categorical features into numerical, followed by StandardScaler transformation on the numerical data. (All Papers - 5 Marks)
# 14. IMP : Split the pre-processed data frame into 2 parts y (output), x (input) features. (All Papers - 1 Marks)
# 15. IMP : Plot output feature and print skewness. Describe your observations. (All Papers- 4 Marks)
# 16. IMP : Check and reduce multicollinearity using VIF. (All Papers - 5 Marks)
#    *. Replace missing value in Specific Column with specified value (Aug 2023 - 5 Marks)


# =============================================================================
# Syntax
# =============================================================================

# 1. Read/load the dataset. (1 Marks) (Asked in Every Paper)

file_path = "path to your file"
df = pd.read_csv(file_path) # use pd.read_excel(file_path) if file_path ends with ".xls" or "xlsx" instead if ".csv"
df.head() # Displays first 5 rows. pass n to display first n rows : df.head(n)


# 2. The dimensions of the dataset (1 Marks) (Asked in Every Paper)

rows, columns = df.shape
print("Number of rows :", rows)
print("Number of columns :", columns)


# 3. Data types of all the features (1 Marks) (Asked in Every Paper)

print(df.dtypes)


# 4. Identify the feature need of type casting and perform it (1 Marks) (Asked in Every Paper)

# Identify the feature need of type casting

# Type cast those as needed (Float to Int, String to DateTime)
# Syntax : df["column_name"] = df["columns_name"].astype(datetype);
# datatype are `str`, `int`, `float`, `category`

# df['timestamp'] = pd.to_datetime(df['timestamp']) for datetime


df['columnx'] = df['columnx'].fillna(0).astype(int) # fillna optional if value is missing or NaN/Na


# 5. Statistical summary of all the numeric and categorical features and drop unnecessary features (2 Marks) (Asked in Every Paper)

# Summary for numeric columns only
print("Numeric Summary:")
print(df.describe())

# Summary for categorical columns only
print("Categorical Summary:")
print(df.describe(include=['object']))

# Combined summary
print(df.describe(include='all'))

# Identify unnecessary features such as ID, etc and drop them with axis=1
df.drop(["ID"], axis = 1)


# 6. How many unique categories are available and number of instances in each of the categorical features (3 Marks) (Asked in Every Paper)

# Select only categorical columns
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
print(f"Categorical Features: {list(categorical_cols)}")

for col in categorical_cols:
    print(f"\n--- Analysis of Feature: '{col}' ---")

    # Get the number of unique categories
    unique_count = df[col].nunique()
    print(f"Number of Unique Categories: {unique_count}")

    # Get the number of instances (frequency) for each category
    print("Instance counts per category:")
    print(df[col].value_counts())


# 7. Explore the associations between the numerical predictors and the target feature using visualizations and observations. (4 Marks) (Asked in Every Papers)

# Identify Target Feature : (Given in Question, Which is the column is to be predicted)

# Correlation Heatmap on Numerical Columns vs target Column

# Select only the numerical columns
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Compute correlation
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='RdYlGn', fmt='.2f')
plt.title('Numerical Features Correlation with Price')
plt.show()

# Independent Plots

plt.figure(figsize=(12, 5))

# column-x vs target
plt.subplot(1, 2, 1)
sns.scatterplot(x=df['column-x'], y=df['target'])
plt.title('column-x vs target')

# column-y vs target
plt.subplot(1, 2, 2)
sns.scatterplot(x=df['column-y'], y=df['target'])
plt.title('column-y vs target')

plt.show()

# Write Observations


# 8. Examine how the categorical features are associated with the target variable. Use visualizations and interpretations. (3 Marks) (Asked in Every Papers)

# Identify Target Feature : (Given in Question)


# List of categorical columns to check
cat_df = df.select_dtypes(include=['object', 'category'])
cat_cols = cat_cols = cat_df.columns.tolist()

plt.figure(figsize=(15, 20))

for i, col in enumerate(cat_cols):
    plt.subplot(4, 2, i+1)
    # Using barplot to see the mean target for each category
    sns.barplot(x=df[col], y=df['target'])
    plt.xticks(rotation='vertical')
    plt.title(f'Average target by {col}')

plt.tight_layout()
plt.show()

# Write Observations


# 9. Visualize the relationship between Column-X and Column-Y, use scatterplot (1 Marks) (Asked in Every Papers)

plt.figure(figsize=(6,4))

sns.scatterplot(x=df['column-X'], y=df['column-Y'])
plt.title('column-X vs column-Y')
plt.show()

#c.Check/Visualize the  relationships between categorical features and the target feature using violinplot. State the inferences (2 marks)
cat_cols = ['site','Pop','sex']

plt.figure(figsize=(15,5))

for i,col in enumerate(cat_cols):
    plt.subplot(1,3,i+1)

    sns.violinplot(
        x=df[col],
        y=df['totlngth']
    )

plt.tight_layout()
plt.show()


# 10. Skewness of numerical features (1 Marks)(Asked in Every Papers)

# Calculate skewness for all numerical columns
skewness = df.skew(numeric_only=True)
print(skewness)

#print(df.select_dtypes(include=['int64','float64']).skew())


# 11. Check for the presence of missing values across features and represent them visually also treat it. (5 Marks) (Asked in Every Paper)

print("Missing values per feature:")
print(df.isnull().sum())

# Visual representation of missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

# Treatment of missing values

# For Numerical columns: Fill with median
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# For Categorical columns: Fill with mode
cat_cols_missing = df.select_dtypes(include=['object', 'category']).columns
for col in cat_cols_missing:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after treatment:")
print(df.isnull().sum())


# 12. Examine the numerical features for any outliers and provide visual evidence and also treat it with dropping (Use IQR). (5 Marks) (Asked in Every Papers)

# Visual evidence of outliers using Boxplots
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

plt.figure(figsize=(15, 10))
for i, col in enumerate(numeric_cols):
    plt.subplot(3, 3, i + 1)
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot of {col}')

plt.tight_layout()
plt.show()

# Treat outliers using IQR (Dropping)
print(f"Shape before removing outliers: {df.shape}")

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filtering the outliers
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

print(f"Shape after removing outliers: {df.shape}")


# 13. Perform label (or n-1 dummy) encoding to convert categorical features into numerical, followed by StandardScaler transformation on the numerical data. (5 Marks) (Asked in Every Papers)

# Perform label encoding for categorical features
le = LabelEncoder()
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object', 'category']).columns

for col in cat_cols:
    df[col] = le.fit_transform(df[col])

df.head()

"""
# Perform n-1 dummy encoding
df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

print("Dataframe after n-1 dummy encoding:")
df.head()
"""

# Perform StandardScaler transformation on the numerical data
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("Data after Label Encoding and Standard Scaling:")
print(df.head())


# 14. Split the pre-processed data frame into 2 parts y (output), x (input) features. (1 Marks) (Asked in Every Papers)

# Split the data into features (X) and target (y)
X = df.drop('target', axis=1)
y = df['target']

print("Input Features (X) Shape:", X.shape)
print("Output Feature (y) Shape:", y.shape)


# 15. Plot output feature and print skewness. Describe your observations. (4 Marks) (Asked in Every Papers)

# Plotting the output feature distribution
plt.figure(figsize=(8, 6))
sns.histplot(y, kde=True, color='blue')
plt.title('Distribution of target (Output Feature)')
plt.show()

# Print skewness
print(f"Skewness of the output feature: {y.skew()}")

# Observations:
# 1. The plot shows the distribution of the target variable after scaling.
# 2. A skewness value close to 0 indicates a near-normal distribution.
# 3. If skewness is positive, the tail is on the right; if negative, it's on the left.


# 16. Check and reduce multicollinearity using VIF. (5 Marks) (Asked in Every Paper)

def calculate_vif(X_df):
    vif_data = pd.DataFrame()
    vif_data["Feature"] = X_df.columns
    vif_data["VIF"] = [variance_inflation_factor(X_df.values, i) for i in range(len(X_df.columns))]
    return vif_data.sort_values(by="VIF", ascending=False)

# Calculate initial VIF
print("Initial VIF values:")
vif_df = calculate_vif(X)
print(vif_df)

# Drop features with high VIF (e.g., VIF > 5 or 10) one by one and re-calculate
# For example, if 'column-A' or 'column-b' has very high VIF and is redundant:
X = X.drop(columns=['column-A', "column-b", "column-c"])

# Recalculate VIF after potential dropping
print("\nVIF values after reducing multicollinearity:")
print(calculate_vif(X))

# End of Syntax


# =============================================================================
# Section C
# (40 Marks) (Modelling, Model Comparison and Hyper parameter Tuning)
# =============================================================================

# About Section C
#
# IMP Questions : (40 Marks)
#
# Modelling : (Max 21 Marks)
# 1. IMP : Use OLS statsmodels package to build the Linear Regression model (Without multicollinearity feature) on the train set to ensure feature Column-Y as target(y).
#    Generate the summary report. (All Papers - 8 Marks)
# 2. IMP : Check assumptions of linear regression. Write your inferences. (All Papers - 7 Marks)
# 3. IMP : Predict the values using test set, Compute measures of RMSE,MAPE,R-square for test set. (All Papers - 5 Marks)
# 4. IMP : Split the pre-processed data frame into 2 parts train and test with ratio as 80:20. Ensure feature Column-Y as target(y).(All Papers - 1 Marks)
#
# Model Comparison and Hyperparameter Tuning : (20 Marks)
# 5. IMP : Train a Linear Regression model using sklearn on the training data and calculate the bias error (1 - mean R²) and
#          variance error (standard deviation of R²) by performing 5-fold cross-validation (All Papers - 5 Marks)
# 6. IMP : Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric.
#    a. Find the metric score in the test set and suggest the best model. (All Papers - 10 marks)
#    or
#    b. ElasticNet(alpha=0.1,l1_ratio=0.5)  (5 marks) and Lasso(alpha = 0.01, max_iter = 500) (5 marks)
# 7. IMP : Using Grid (or random) search on the ridge (or lasso) model, find the best value of alpha and corresponding rmse value on the test set (All Papers - 5 Marks)

#a. Perform backward elimination for selecting the "best" features, 
# you can use SequentialFeatureSelector (SFS) from mlxtend.( 3 marks)
from sklearn.linear_model import LinearRegression
from mlxtend.feature_selection import SequentialFeatureSelector
lr = LinearRegression()

sfs = SequentialFeatureSelector(
    lr,
    k_features='best',
    forward=False,
    scoring='r2',
    cv=5
)

sfs.fit(X_train,y_train)
print(sfs.k_feature_names_)


# =============================================================================
# Syntax
# =============================================================================

# 1. Use OLS statsmodels package to build the Linear Regression model (Without multicollinearity feature) on the train set to ensure feature Column-Y as target(y). Generate the summary report. (All Papers - 8 Marks)

# Split the data into train and test sets (80:20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_ols = sm.add_constant(X_train) # Add a constant to the features for OLS intercept
ols_model = sm.OLS(y_train, X_train_ols).fit()

# Generate the summary report
print(ols_model.summary())


# 2. Check assumptions of linear regression. Write your inferences. (All Papers - 7 Marks)

# 1. Linearity Test (Rainbow Test)
stat, p_value = linear_rainbow(ols_model)
print(f"Linearity Rainbow test p-value: {p_value:.4f}")

# 2. Homoscedasticity (Residual Plot & Goldfeld-Quandt)
residuals = ols_model.resid
y_pred = ols_model.predict(X_train_ols)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Residuals vs Predicted (Homoscedasticity)')

# Goldfeld-Quandt test
gq_test = het_goldfeldquandt(y_train, X_train_ols)
print(f"Goldfeld-Quandt test p-value: {gq_test[1]:.4f}")

# 3. Normality of Residuals (Q-Q Plot)
plt.subplot(1, 2, 2)
stats.probplot(residuals, plot=plt)
plt.title('Q-Q Plot')
plt.show()

# 4. Independence (Durbin-Watson)
from statsmodels.stats.stattools import durbin_watson
dw = durbin_watson(residuals)
print(f"Durbin-Watson score: {dw:.4f}")

# Inferences:
# 1. Linearity: If Rainbow p-value > 0.05, the relationship is linear.
# 2. Homoscedasticity: If GQ p-value > 0.05, constant variance is assumed. The scatter plot should show no distinct pattern.
# 3. Normality: If residuals follow the red line in the Q-Q plot, they are normally distributed.
# 4. Independence: A Durbin-Watson score around 2 indicates no autocorrelation.


# 3. Predict the values using test set, Compute measures of RMSE,MAPE,R-square for test set. (All Papers - 5 Marks)

# 1. Predict values using test set
X_test_ols = sm.add_constant(X_test)
y_pred_test = ols_model.predict(X_test_ols)


# 2. Compute Metrics
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
mape_test = mean_absolute_percentage_error(y_test, y_pred_test)
r2_test = r2_score(y_test, y_pred_test)

print(f"Test RMSE: {rmse_test:.4f}")
print(f"Test MAPE: {mape_test:.4f}")
print(f"Test R-square: {r2_test:.4f}")


# 4. Split the pre-processed data frame into 2 parts train and test with ratio as 80:20. Ensure feature Column-Y as target(y).(All Papers - 1 Marks)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train.shape, X_test.shape


# 5. Train a Linear Regression model using sklearn on the training data and calculate the bias error (1 - mean R²) and variance error (standard deviation of R²) by performing 5-fold cross-validation (All Papers - 5 Marks)

model = LinearRegression()
scores = cross_val_score(model, X_train, y_train, cv=5, scoring="r2")
mean_r2 = np.mean(scores)
std_r2 = np.std(scores)

bias_error = 1 - mean_r2
variance_error = std_r2


print(f"Cross-Validation R2 scores: {scores}")
print(f"Mean R2: {mean_r2:.4f}")
print(f"Bias Error (1 - mean R2): {bias_error:.4f}")
print(f"Variance Error (std dev of R2): {variance_error:.4f}")


# 6. Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric.
# a. Find the metric score in the test set and suggest the best model. (All Papers - 10 marks)
# or
# b. ElasticNet(alpha=0.1,l1_ratio=0.5) (5 marks) and Lasso(alpha = 0.01, max_iter = 500) (5 marks)

enet = ElasticNet(alpha=0.1, l1_ratio=0.5)
lasso = Lasso(alpha=0.01, max_iter=500)

enet_cv = cross_val_score(enet, X_train, y_train, cv=5, scoring='neg_root_mean_squared_error')
lasso_cv = cross_val_score(lasso, X_train, y_train, cv=5, scoring='neg_root_mean_squared_error')

print(f"ElasticNet CV RMSE: {-enet_cv.mean():.4f}")
print(f"Lasso CV RMSE: {-lasso_cv.mean():.4f}")

enet.fit(X_train, y_train)
lasso.fit(X_train, y_train)

enet_test_rmse = np.sqrt(mean_squared_error(y_test, enet.predict(X_test)))
lasso_test_rmse = np.sqrt(mean_squared_error(y_test, lasso.predict(X_test)))

print(f"\nTest RMSE (ElasticNet): {enet_test_rmse:.4f}")
print(f"Test RMSE (Lasso): {lasso_test_rmse:.4f}")

best_model = 'ElasticNet' if enet_test_rmse < lasso_test_rmse else 'Lasso'
print(f"\nSuggested Best Model: {best_model}")


# 7. Using Grid (or random) search on the ridge (or lasso) model, find the best value of alpha and corresponding rmse value on the test set (All Papers - 5 Marks)

param_grid = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100]}

ridge = Ridge() # lasso = Lasso(max_iter=10000)

grid_search = GridSearchCV(estimator=ridge, param_grid=param_grid, cv=5, scoring='neg_root_mean_squared_error')
grid_search.fit(X_train, y_train)

"""
Random Search :
param_dist = {'alpha': np.logspace(-4, 2, 20)}

random_search = RandomizedSearchCV(estimator=lasso_model, param_distributions=param_dist, n_iter=10, cv=5, scoring='neg_root_mean_squared_error', random_state=42)
random_search.fit(X_train, y_train)
"""

best_alpha = grid_search.best_params_['alpha']
best_cv_rmse = -grid_search.best_score_

best_model = grid_search.best_estimator_
y_pred_ridge = best_model.predict(X_test)
test_rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred_ridge))

print(f"Best alpha value: {best_alpha}")
print(f"Best CV RMSE: {best_cv_rmse:.4f}")
print(f"Test RMSE with best alpha: {test_rmse_ridge:.4f}")

# End of Paper Solutions
