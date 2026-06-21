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


# Read/load the dataset
file_path = "fish.csv"
df = pd.read_csv(file_path) # use pd.read_excel(file_path) if file_path ends with ".xls" or "xlsx" instead if ".csv"
df.head() # Displays first 5 rows. pass n to display first n rows : df.head(n)


#The dimensions of the dataset 
rows, columns = df.shape
print("Number of rows :", rows)
print("Number of columns :", columns)
target_col = 'Weight'


# Data types of all the features
print(df.dtypes)

# Missing Values
print("Missing values per feature:")
print(df.isnull().sum())


# Incorrect Datatypes

# Type cast those as needed (Float to Int, String to DateTime)
# Syntax : df["column_name"] = df["columns_name"].astype(datetype);
# datatype are `str`, `int`, `float`, `category`
# df['timestamp'] = pd.to_datetime(df['timestamp']) for datetime
#df['columnx'] = df['columnx'].fillna(0).astype(int) # fillna optional if value is missing or NaN/Na

#df.replace(['?', 'N/A', '-', 'unknown', ' '], np.nan, inplace=True)                 # Requied to Replace invalid values
# df['thalachh'] = df['thalachh'].astype('object')   # placeholder line                    # Convert datatype to category/object
#df['thalachh'] = pd.to_numeric(df['thalachh'])
#df.describe()

# Coerce object columns that are actually numeric (handles columns like
# thalachh where invalid '?' values made pandas read as string).
# Use try/except for pandas 2.x/3.x compatibility (errors='ignore' was removed).
# for col in df.select_dtypes(include=['object']).columns:
  #  try:
   #     df[col] = pd.to_numeric(df[col])
    #except (ValueError, TypeError):
     #   pass   # leave genuinely categorical columns untouched

# convert numeric-coded categoricals to 'object' so they are treated as categories
# (Session-3: 'Year';  IPL: 'AGE', 'CAPTAINCY EXP')
# df['Year'] = df['Year'].astype(object)
# df['AGE']  = df['AGE'].astype(object)

# parse dates properly (so you can extract day/month/year later)
# df['date'] = pd.to_datetime(df['date'], errors='coerce')

# clean a numeric column stored as text with symbols ("$1,200" -> 1200.0)
# df['price'] = (df['price'].replace('[\$,]', '', regex=True).astype(float))
# The car-price brand-typo fix (pattern you can reuse for any messy category column)
# cars['CompanyName'] = cars['CompanyName'].str.lower()
# fix = {'maxda':'mazda', 'porcshce':'porsche', 'toyouta':'toyota','vokswagen':'volkswagen', 'vw':'volkswagen'}
# cars['CompanyName'] = cars['CompanyName'].replace(fix)


# Duplicates, inconsistent values, typos, mixed units, invalid entries
'''| **Duplicate rows** | `df.duplicated().sum()` | `df.drop_duplicates()` |
| **Inconsistent text** ("Male"/"male"/"M") | `df[c].value_counts()` | `.str.lower().str.strip()`, then map |. # cars['CompanyName'] = cars['CompanyName'].str.lower()
| **Typos in categories** (`toyouta`→`toyota`) | `df[c].unique()` | `df[c].replace('toyouta','toyota')` |
| **Mixed units** (kg vs g) | range/`describe()` looks bimodal | divide/convert offending rows |
| **Invalid entries** (age = −5, price = 0) | `df[df[c] < 0]` | set to NaN then impute, or drop |
| **Whitespace / case in headers** | `df.columns` | `df.columns = df.columns.str.strip()` |
| **Constant / zero-variance column** | `df.std()==0` or `nunique()==1` | drop it (adds nothing) |. '''

# count + percentage of missing values, worst first
def missing_report(df):
    total = df.isnull().sum().sort_values(ascending=False)
    pct = (df.isnull().mean() * 100).sort_values(ascending=False)
    return pd.concat([total, pct], axis=1, keys=['Total', 'Percent_%']).round(2)


# Statistical summary of all the numeric and categorical features
cat_cols = df.select_dtypes(include='object').columns

for col in cat_cols:
    print(f"\n{col}")
    print(df[col].unique())


# Summary for numeric columns only
print("Numeric Summary:")
print(df.describe())


# Summary for categorical columns only
print("Categorical Summary:")
print(df.describe(include=['object']))


# Combined summary
print(df.describe(include='all'))


'''Column: [COLUMN_NAME]
1. The column contains [COUNT] non-null observations with values ranging from [MIN] to [MAX].
   → If Count = Total Rows: "No missing values are present."
   → If Count < Total Rows: "Missing values are present and may require treatment."
2. The average value is [MEAN], while the median is [MEDIAN].
   → If Mean ≈ Median: "The data appears to be symmetrically distributed."
   → If Mean > Median: "The data appears positively skewed (right-skewed)."
   → If Mean < Median: "The data appears negatively skewed (left-skewed)."
3. The standard deviation is [STD].
   → If Std < 10% of Mean: "Low variability; values are concentrated around the mean."
   → If Std is 10%-30% of Mean: "Moderate variability in the data."
   → If Std > 30% of Mean: "High variability; values are widely dispersed."
4. 25% of the observations are below [Q1] and 75% are below [Q3].
   → If Q3-Q1 is small: "The middle 50% of observations are tightly clustered."
   → If Q3-Q1 is large: "The middle 50% of observations show significant variation."
5. The data ranges from [MIN] to [MAX].
   → If Range (Max-Min) is small: "The data has low spread."
   → If Range (Max-Min) is large: "The data has high spread and variability."
6. Potential outlier analysis:
   → If Max >> Q3: "Potential upper outliers may be present."
   → If Min << Q1: "Potential lower outliers may be present."
   → If Max and Min are reasonably close to quartiles: "No significant outliers are evident."
7. Overall Summary:
   → Replace with one of the following:
   * "The column is well distributed with no significant anomalies."
   * "The column shows moderate variability with a few extreme values."
   * "The column exhibits high dispersion and may contain outliers."
   * "The column contains missing values that require preprocessing."  '''


# --- The two car-price feature-engineering moves (high-yield, reusable) ---

# 1) RATIO / combination feature: blend two mileage columns into one economy index
# cars['fueleconomy'] = 0.55 * cars['citympg'] + 0.45 * cars['highwaympg']

# 2) BINNING a high-cardinality category by its mean target into ordered bands
# table  = cars.groupby('CompanyName')['price'].mean()
# tmp    = cars.merge(table.rename('avg_price'), on='CompanyName')
# bins   = [0, 10000, 20000, 40000]
# labels = ['Budget', 'Medium', 'Highend']
# cars['carsrange'] = pd.cut(tmp['avg_price'], bins=bins, right=False, labels=labels)

# Generic reusable patterns:
# Interaction:   df['x1_x2'] = df['x1'] * df['x2']
# Ratio:         df['per_capita'] = df['total'] / df['count']
# Binning:       df['age_band'] = pd.cut(df['age'], bins=[0,18,35,60,120],
#                                        labels=['child','young','adult','senior'])
# Date expand:   df['month'] = df['date'].dt.month ; df['dow'] = df['date'].dt.dayofweek
# Aggregation:   df['cust_avg'] = df.groupby('cust_id')['amount'].transform('mean')


# Indentify unnecessary features such as ID, etc and drop them with axis=1
df.drop(["Category"], axis = 1, inplace = True)


# Unique categories are available and number of instances in each of the categorical features
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


# associations between the numerical predictors and the target feature 
# Indentify Target Feature : (Given in Question, Which is the column is to be predicted)

# Correlation Heatmap on Numerical Columns vs target Column

# Select only the numerical columns
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Compute correlation
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='RdYlGn', fmt='.2f')
plt.title('Numerical Features Correlation with Price')
plt.show()

'''   Heatmap Inference:
1. The correlation between [COLUMN_1] and [COLUMN_2] is [CORRELATION_VALUE].
   → If r = +1: "Perfect positive correlation."
   → If r = -1: "Perfect negative correlation."
   → If r ≈ 0: "No linear relationship exists."
2. Strength of Correlation:
   → If |r| > 0.8: "Very strong correlation."
   → If 0.6 ≤ |r| ≤ 0.8: "Strong correlation."
   → If 0.4 ≤ |r| < 0.6: "Moderate correlation."
   → If 0.2 ≤ |r| < 0.4: "Weak correlation."
   → If |r| < 0.2: "Very weak or negligible correlation."
3. Direction of Correlation:
   → If r > 0: "As one variable increases, the other tends to increase."
   → If r < 0: "As one variable increases, the other tends to decrease."
4. Correlation with Target Variable [TARGET]:
   → If |r| > 0.7: "This feature is a strong predictor of the target."
   → If 0.4 ≤ |r| ≤ 0.7: "This feature has moderate predictive power."
   → If |r| < 0.4: "This feature has limited predictive influence."
5. Multicollinearity Check:
   → If correlation between two independent variables > 0.8:
   "Potential multicollinearity exists; consider removing one of the features or calculating VIF."
   → If all correlations < 0.8:
   "No significant multicollinearity is observed."
6. Feature Selection Insight:
   → If feature has high correlation with target and low correlation with other predictors:
   "This feature is a good candidate for model building."
   → If feature has low correlation with target:
   "This feature may contribute less to prediction."
7. Overall Summary:
   → Replace with one of the following:
   * "Most features show weak correlations, indicating low multicollinearity."
   * "Several features exhibit strong correlations with the target and can be considered important predictors."
   * "High correlations among predictors indicate possible multicollinearity issues."
   * "The heatmap suggests a balanced set of predictors with minimal redundancy."   '''


# Independent Plots

plt.figure(figsize=(12, 5))
cols = df.select_dtypes(include='number').columns
# cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in cols:
    
    if col != target_col:   # Skip target column itself
        plt.figure(figsize=(6,4))
        plt.scatter(df[col], df[target_col])
        plt.title(f'{col} vs {target_col}')
        plt.xlabel(col)
        plt.ylabel(target_col)
        plt.show()



# Write Observations
# Scatter Plot Inference:

'''1. Relationship between [X_VARIABLE] and [Y_VARIABLE]:
   → If points move upward from left to right:
   "A positive relationship exists between the variables."
   → If points move downward from left to right:
   "A negative relationship exists between the variables."
   → If points are randomly scattered:
   "No clear relationship exists between the variables."
2. Strength of Relationship:
   → If points are tightly clustered around a line:
   "A strong relationship exists between the variables."
   → If points are moderately scattered:
   "A moderate relationship exists between the variables."
   → If points are widely dispersed:
   "A weak relationship exists between the variables."
3. Trend Analysis:
   → If points follow an increasing pattern:
   "As [X_VARIABLE] increases, [Y_VARIABLE] tends to increase."
   → If points follow a decreasing pattern:
   "As [X_VARIABLE] increases, [Y_VARIABLE] tends to decrease."
   → If no visible pattern exists:
   "No significant trend is observed."
4. Linearity Check:
   → If points approximately form a straight line:
   "The relationship appears linear."
   → If points form a curve:
   "The relationship appears non-linear and may require transformation or advanced models."
5. Outlier Detection:
   → If one or more points are far away from the main cluster:
   "Potential outliers are present and should be investigated."
   → If all points are close to the main cluster:
   "No significant outliers are observed."
6. Clustering Pattern:
   → If distinct groups of points are visible:
   "The data exhibits clustering, suggesting possible segments or categories."
   → If points are uniformly distributed:
   "No distinct clusters are observed."
7. Variability Analysis:
   → If spread increases as X increases:
   "Heteroscedasticity may be present (variance changes across values)."
   → If spread remains constant:
   "The variance appears relatively constant."
8. Overall Summary:
   → Replace with one of the following:
   * "The scatter plot indicates a strong positive relationship between the variables."
   * "The scatter plot indicates a strong negative relationship between the variables."
   * "The scatter plot shows a weak relationship with considerable variability."
   * "The scatter plot reveals no significant relationship between the variables."
   * "The scatter plot suggests a non-linear relationship that may require further analysis."'''





# Categorical features are associated with the target variable. - Bar
# Indentify Target Feature : (Given in Question)

# List of categorical columns to check
cat_df = df.select_dtypes(include=['object', 'category'])
cat_cols = cat_cols = cat_df.columns.tolist()

plt.figure(figsize=(15, 20))
for i, col in enumerate(cat_cols):
    plt.subplot(4, 2, i+1)
    # Using barplot to see the mean target for each category
    sns.barplot(x=df[col], y=df[target_col])
    plt.xticks(rotation='vertical')
    plt.title(f'Average target by {col}')
    plt.tight_layout()
    plt.show()

# Write Observations
'''Overall Summary:
→ Replace with one of the following:
"The bar plot indicates that [CATEGORY] is the most prominent category."
"The bar plot shows a balanced distribution across categories."
"The bar plot reveals significant variation among categories."
"The bar plot highlights clear differences in category performance."
"The bar plot suggests that a few categories dominate the dataset."'''


# Create a countplot for passenger classes
import seaborn as sns
import matplotlib.pyplot as plt

cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(x=col, data=df)
    plt.title(f'Count Plot of {col}')
    plt.xticks(rotation=45)
    plt.show()

'''Overall Summary:
→ Replace with one of the following:
"The count plot indicates a balanced distribution across categories."
"The count plot reveals a dominant category with significantly higher frequency."
"The count plot highlights class imbalance within the dataset."
"The count plot shows that certain categories are underrepresented."
"The count plot suggests a relatively uniform distribution of observations."   '''


# Pair plot
import seaborn as sns
import matplotlib.pyplot as plt

num_cols = df.select_dtypes(include='number')
sns.pairplot(num_cols)
plt.suptitle("Pair Plot", y=1.02)
plt.show()


'''Overall Summary:
→ Replace with one of the following:
"The pair plot reveals strong relationships among several variables."
"The pair plot indicates weak relationships and minimal multicollinearity."
"The pair plot highlights distinct clusters and potential class separation."
"The pair plot reveals the presence of outliers and skewed distributions."
"The pair plot suggests that some variables may be highly correlated and require further analysis."  '''


# Scatter plot - individual
plt.figure(figsize=(6,4))
sns.scatterplot(x=df['column-X'], y=df['column-Y'])
plt.title('column-X vs column-Y')
plt.show()


# Scatterplot 3-D
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['bath'],df['balcony'],df['price'])
ax.set_xlabel('bath')
ax.set_ylabel('balcony')
ax.set_zlabel('price')
plt.show()


#c.Check/Visualize the  relationships between categorical features and the target feature using violinplot. State the inferences (2 marks)
# cat_cols = ['site','Pop','gender']
# at_cols = ['Species']

import seaborn as sns
import matplotlib.pyplot as plt
target = target_col   # Numerical column
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    plt.figure(figsize=(20,18))
    sns.violinplot(x=col, y=target, data=df)
    plt.title(f'{target} vs {col}')
    plt.xticks(rotation=45)
    plt.show()


    '''    Replace with one of the following:
"The violin plot indicates a symmetric distribution with moderate variability."
"The violin plot reveals positive skewness and a concentration of observations around specific values."
"The violin plot highlights multiple peaks, suggesting distinct subgroups within the data."
"The violin plot shows significant variability and possible extreme values."
"The violin plot suggests similar distributions across categories."'''


# Calculate skewness for all numerical columns
skewness = df.skew(numeric_only=True)
print(skewness)

#print(df.select_dtypes(include=['int64','float64']).skew())


'''Skewness Analysis for [COLUMN_NAME]:
The skewness value of the column is [SKEW_VALUE].
→ If Skewness ≈ 0 (between -0.5 and +0.5):
"The distribution is approximately symmetric with little or no skewness."
→ If Skewness > 0:
"The distribution is positively skewed (right-skewed), indicating the presence of relatively higher values pulling the distribution toward the right."
→ If Skewness < 0:
"The distribution is negatively skewed (left-skewed), indicating the presence of relatively lower values pulling the distribution toward the left."
→ If 0.5 ≤ |Skewness| < 1:
"The distribution exhibits moderate skewness."
→ If |Skewness| ≥ 1:
"The distribution exhibits high skewness."
Overall Summary:
"The variable follows a [SYMMETRIC / MODERATELY SKEWED / HIGHLY SKEWED] distribution with [POSITIVE / NEGATIVE / NO] skewness."'''


# Missing Values and treatment
print("Missing values per feature:")
print(df.isnull().sum())


# Visual representation of missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()


# Treatment of missing values
# df['Age'] = df.groupby('Gender')['Age'].transform('Age')

# df['balcony'] = df['balcony'].fillna(0)
# df['balcony'] = df['balcony'].astype(int)
# df['bath'] = df['bath'].fillna(1)
# df['bath'] = df['bath'].astype(int)
# df['location'] = df['location'].fillna("missing")

# e.g. '2 BHK' to 2
# hint  : use str.replace(' BHK', '').str.replace(' Bedroom', '').str.replace(' RK', '')
# df['size'] = (df['size'].str.extract('(\d+)'))
# df['size'] = df['size'].fillna(2)
# df['size'] = df['size'].astype(int)

df['total_sqft'] = pd.to_numeric(df['total_sqft'],errors='coerce')

df['total_sqft'].fillna(df['total_sqft'].mean(),inplace=True)


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


# Visual evidence of outliers using Boxplots
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

plt.figure(figsize=(15, 10))
for i, col in enumerate(numeric_cols):
    plt.subplot(3, 3, i + 1)
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot of {col}')

plt.tight_layout()
plt.show()


'''Box Plot Inference:
1. Median Analysis:
   → If median line is approximately at the center of the box:
   "The data appears to be symmetrically distributed."
   → If median is closer to Q1:
   "The data appears positively skewed (right-skewed)."
   → If median is closer to Q3:
   "The data appears negatively skewed (left-skewed).
9. Overall Summary:
   → Replace with one of the following:
   * "The box plot indicates a symmetric distribution with minimal outliers."
   * "The box plot reveals positive skewness and the presence of upper-end outliers."
   * "The box plot reveals negative skewness and the presence of lower-end outliers."
   * "The box plot shows high variability with several extreme observations."
   * "The box plot indicates a relatively consistent distribution with low variability."'''


# Treat outliers using IQR (Dropping)
print(f"Shape before removing outliers: {df.shape}")

# Q1 = df['bath'].quantile(0.25)
# Q3 = df['bath'].quantile(0.75)

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filtering the outliers
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

print(f"Shape after removing outliers: {df.shape}")


# Clip outliers using Z-score
# IMPORTANT: Exclude the target column to avoid corrupting binary labels
#     (this is critical for severely imbalanced datasets like stroke 95/5)

from scipy.stats import zscore
import numpy as np

# Get numeric columns BUT exclude the target column


# Outlier detection using boxplots

num_cols = [col for col in df.select_dtypes(include=np.number).columns
            if df[col].nunique() > 10 and col != target_col]


for c in num_cols:
    # Calculate Z-score
    z = np.abs(zscore(df[c]))
    
    # Count outliers
    outliers = (z > 3).sum()
    print(f"{c}: {outliers} outliers")
    
    # Calculate clipping limits (mean ± 3*std)
    upper = df[c].mean() + 3 * df[c].std()
    lower = df[c].mean() - 3 * df[c].std()
    
    # Clip outliers
    df[c] = np.clip(df[c], lower, upper)

print("\nOutliers clipped successfully (target column preserved)")


# Perform label encoding for categorical features
le = LabelEncoder()

# df['Education'] = le.fit_transform(df['Education'])  --> For encoding specific 

# cols = ['Gender', 'Education']
# for col in cols:
#    df[col] = le.fit_transform(df[col]).  --> for specific columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object', 'category']).columns

for col in cat_cols:
    df[col] = le.fit_transform(df[col])

df.head()



# Perform n-1 dummy encoding
df = pd.get_dummies(df, columns=cat_cols, drop_first=True,dtype=int)
cols = ['Gender', 'Education']

# df = pd.get_dummies(df, columns=['City'], drop_first=True, dtype=int).   --> For specific column

print("Dataframe after n-1 dummy encoding:")
df.head()


# Perform StandardScaler transformation on the numerical data
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("Data after Label Encoding and Standard Scaling:")
print(df.head())


# Split the data into features (X) and target (y)
X = df.drop(target_col, axis=1)
y = df[target_col]

print("Input Features (X) Shape:", X.shape)
print("Output Feature (y) Shape:", y.shape)


# Plotting the output feature distribution - skewness
plt.figure(figsize=(8, 6))
sns.histplot(y, kde=True, color='blue')
plt.title('Distribution of target (Output Feature)')
plt.show()
'''"The histogram indicates an approximately normal distribution with moderate variability."
"The histogram reveals a positively skewed distribution with a few high-value observations."
"The histogram reveals a negatively skewed distribution with a few low-value observations."
"The histogram indicates a multimodal distribution, suggesting multiple underlying groups."
"The histogram shows a wide spread with potential outliers."  '''


# Print skewness
print(f"Skewness of the output feature: {y.skew()}")

# Observations:
# 1. The plot shows the distribution of the target variable after scaling.
# 2. A skewness value close to 0 indicates a near-normal distribution.
# 3. If skewness is positive, the tail is on the right; if negative, it's on the left.


# Multicollinearity using VIF
def calculate_vif(X_df):
    vif_data = pd.DataFrame()
    vif_data["Feature"] = X_df.columns
    vif_data["VIF"] = [variance_inflation_factor(X_df.values, i) for i in range(len(X_df.columns))]
    return vif_data.sort_values(by="VIF", ascending=False)

# Calculate initial VIF
print("Initial VIF values:")
vif_df = calculate_vif(X)
print(vif_df)

'''→ If 5 ≤ VIF < 10:
"Moderate multicollinearity exists. The feature should be reviewed further."
→ If VIF ≥ 10:
"High multicollinearity exists. Consider removing, combining, or transforming the feature."
Model-Level Summary:
→ If all VIF values < 5:
"No significant multicollinearity is observed among the independent variables."'''


X = X.drop(columns=["D_length"])
# Recalculate VIF after potential dropping
print("\nVIF values after reducing multicollinearity:")
print(calculate_vif(X))


X = X.drop(columns=["C_length"])

# Recalculate VIF after potential dropping
print("\nVIF values after reducing multicollinearity:")
print(calculate_vif(X))


# # Section C
#
#

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#a. Perform backward elimination for selecting the "best" features, 
# you can use SequentialFeatureSelector (SFS) from mlxtend.( 3 marks)
from sklearn.linear_model import LinearRegression
from mlxtend.feature_selection import SequentialFeatureSelector
lr = LinearRegression()
sfs = SequentialFeatureSelector(lr,k_features='best',forward=False,scoring='r2',cv=5)
sfs.fit(X_train,y_train)
print(sfs.k_feature_names_)


# Split the data into train and test sets (80:20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_ols = sm.add_constant(X_train) # Add a constant to the features for OLS intercept
ols_model = sm.OLS(y_train, X_train_ols).fit()





# Generate the summary report
print(ols_model.summary())

'''OLS Summary Report Inference
1. R-Squared
R² = [VALUE]
→ If R² > 0.90
   "The model explains more than 90% of the variation in the target variable, indicating an excellent fit."
→ If 0.70 ≤ R² ≤ 0.90
   "The model explains a substantial proportion of variability and demonstrates a good fit."
→ If 0.50 ≤ R² < 0.70
   "The model has moderate explanatory power."
→ If R² < 0.50
   "The model has limited explanatory power and may require additional predictors."
2. Adjusted R-Squared
Adj R² = [VALUE]
→ If R² ≈ Adjusted R²
   "Most predictors contribute meaningfully to the model."
→ If R² >> Adjusted R²
   "Some predictors may not be contributing significantly and should be reviewed."
3. F-Statistic & Prob(F-statistic)
Prob(F-statistic) = [VALUE]
→ If p-value < 0.05
   "The overall regression model is statistically significant."
→ If p-value > 0.05
   "The model is not statistically significant."
4. Individual Predictor Significance
P>|t| = [VALUE]
→ If p-value < 0.05
   "The predictor is statistically significant and contributes to the model."
→ If p-value > 0.05
   "The predictor is not statistically significant and may be considered for removal."
5. Coefficient Interpretation
coef = [VALUE]
→ If coefficient > 0
   "The predictor has a positive relationship with the target variable."
→ If coefficient < 0
   "The predictor has a negative relationship with the target variable."
6. Durbin-Watson Statistic
DW = [VALUE]
→ Around 2
   "No significant autocorrelation exists."
→ Less than 1.5
   "Positive autocorrelation may be present."
→ Greater than 2.5
   "Negative autocorrelation may be present."
7. Condition Number
Cond. No = [VALUE]
→ Less than 30
   "No serious multicollinearity concerns."
→ Greater than 30
   "Potential multicollinearity may exist."
→ Greater than 100
   "Strong multicollinearity may exist."
8. Confidence Interval
[0.025 , 0.975]
→ If interval does not contain 0
   "The predictor is statistically significant."
→ If interval contains 0
   "The predictor may not be statistically significant."
9. Fastest Exam Version
"The model achieved an R² of [R2] and an Adjusted R² of [ADJ_R2], indicating that [R2]% of the variability in the target variable is explained by the independent variables. The Prob(F-statistic) value of [P_VALUE] indicates that the overall model is [STATISTICALLY SIGNIFICANT / NOT SIGNIFICANT]. Predictors with p-values less than 0.05 are considered significant contributors to the model. The Durbin-Watson statistic of [DW] suggests [NO/POSITIVE/NEGATIVE] autocorrelation. The Condition Number of [COND_NO] indicates [LOW/MODERATE/HIGH] multicollinearity."
10. Quick Replacement Table
R² > 0.90
→ Excellent Model Fit
0.70 ≤ R² ≤ 0.90
→ Good Model Fit
0.50 ≤ R² < 0.70
→ Moderate Model Fit
R² < 0.50
→ Weak Model Fit
p-value < 0.05
→ Statistically Significant
p-value > 0.05
→ Not Statistically Significant
Coefficient > 0
→ Positive Relationship
Coefficient < 0
→ Negative Relationship
DW ≈ 2
→ No Autocorrelation
DW < 1.5
→ Positive Autocorrelation
DW > 2.5
→ Negative Autocorrelation
Condition No < 30
→ No Multicollinearity
Condition No > 30
→ Potential Multicollinearity
Condition No > 100
→ Severe Multicollinearity
11. One-Liner for M.Tech Exams
"The OLS summary indicates that the model explains [R²]% of the variability in the target variable. The overall model is [significant/not significant] based on the F-statistic p-value. Significant predictors have p-values less than 0.05, while the Durbin-Watson statistic and Condition Number are used to assess autocorrelation and multicollinearity respectively."'''





# Assumptions of Linear Regresssion
# 1. Linearity Test (Rainbow Test)
stat, p_value = linear_rainbow(ols_model)
print(f"Linearity Rainbow test p-value: {p_value:.4f}")

'''Linearity Rainbow Test
Rainbow Test p-value = [P_VALUE]
→ If p-value > 0.05
Fail to reject the null hypothesis. The relationship between the independent variables and the target variable appears to be linear. Therefore, the linearity assumption of Linear Regression is satisfied.
→ If p-value ≤ 0.05
Reject the null hypothesis. The relationship between the independent variables and the target variable may not be linear. Therefore, the linearity assumption of Linear Regression is violated and further transformation or non-linear modeling techniques may be required.'''


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

'''Homoscedasticity Analysis
1. Residual Plot Analysis
→ If residuals are randomly scattered around the zero line with roughly constant spread:
"The residuals are randomly distributed around zero with a constant variance. Therefore, the homoscedasticity assumption is satisfied."
→ If residuals show a funnel shape (increasing or decreasing spread):
"The residuals exhibit changing variance across fitted values, indicating heteroscedasticity. Therefore, the homoscedasticity assumption is violated."
→ If residuals display a systematic pattern or curve:
"The residuals exhibit a non-random pattern, suggesting model misspecification or violation of regression assumptions."
2. Goldfeld-Quandt Test
Goldfeld-Quandt Test p-value = [P_VALUE]
→ If p-value > 0.05
"Fail to reject the null hypothesis. The residual variance appears constant across observations. Therefore, the homoscedasticity assumption is satisfied."
→ If p-value ≤ 0.05
"Reject the null hypothesis. The residual variance is not constant across observations. Therefore, heteroscedasticity is present and the homoscedasticity assumption is violated."
3. Overall Conclusion
→ If Residual Plot Random + p-value > 0.05
"Both the residual plot and Goldfeld-Quandt test indicate constant variance in residuals. Hence, the homoscedasticity assumption is satisfied."
→ If Residual Plot Funnel + p-value ≤ 0.05
"Both the residual plot and Goldfeld-Quandt test indicate heteroscedasticity. Hence, the homoscedasticity assumption is violated."
→ If Plot and Test disagree
"The graphical and statistical assessments provide mixed results. Additional heteroscedasticity tests such as Breusch-Pagan or White Test may be performed for confirmation."'''


# 3. Normality of Residuals (Q-Q Plot)
plt.subplot(1, 2, 2)
stats.probplot(residuals, plot=plt)
plt.title('Q-Q Plot')
plt.show()


'''Normality of Residuals Analysis (Q-Q Plot)
1. Q-Q Plot Analysis
→ If most points lie closely along the diagonal reference line:
"The residuals closely follow the reference line, indicating that the residuals are approximately normally distributed. Therefore, the normality assumption is satisfied."
→ If points show slight deviation at the ends (tails) but follow the line overall:
"The residuals are approximately normally distributed with minor deviations at the tails. The normality assumption is reasonably satisfied."
→ If points significantly deviate from the diagonal line:
"The residuals do not follow the reference line and exhibit substantial deviations. Therefore, the normality assumption is violated."
→ If points form an S-shaped pattern:
"The residuals exhibit skewness and may not be normally distributed."
→ If points curve away from the line at both ends:
"The residuals may contain heavy tails or outliers, indicating deviation from normality."
2. Outlier Assessment
→ If a few points are far away from the reference line:
"Potential outliers or extreme observations may be present."
→ If all points remain close to the line:
"No significant outliers are evident."
3. Overall Conclusion
→ If points closely follow the line:
"The Q-Q plot indicates that residuals are approximately normally distributed. Hence, the normality assumption is satisfied."
→ If moderate deviations occur:
"The Q-Q plot suggests minor departures from normality; however, the assumption is reasonably satisfied."
→ If large deviations occur:
"The Q-Q plot indicates that residuals are not normally distributed. Therefore, the normality assumption is violated."'''


# 4. Independence (Durbin-Watson)
from statsmodels.stats.stattools import durbin_watson
dw = durbin_watson(residuals)
print(f"Durbin-Watson score: {dw:.4f}")

'''Independence of Residuals Analysis (Durbin-Watson Test)
Durbin-Watson Statistic = [DW_VALUE]
→ If DW ≈ 2 (between 1.5 and 2.5)
"The Durbin-Watson statistic is close to 2, indicating that residuals are independent and no significant autocorrelation is present. Therefore, the independence assumption is satisfied."
→ If DW < 1.5
"The Durbin-Watson statistic is substantially less than 2, indicating positive autocorrelation among residuals. Therefore, the independence assumption is violated."
→ If DW > 2.5
"The Durbin-Watson statistic is substantially greater than 2, indicating negative autocorrelation among residuals. Therefore, the independence assumption is violated."
Overall Conclusion:
→ If 1.5 ≤ DW ≤ 2.5
"The residuals are independent and the regression model satisfies the independence assumption."
→ If DW < 1.5
"The residuals exhibit positive autocorrelation, suggesting that the independence assumption is violated."
→ If DW > 2.5
"The residuals exhibit negative autocorrelation, suggesting that the independence assumption is violated."'''


# Inferences:
# 1. Linearity: If Rainbow p-value > 0.05, the relationship is linear.
# 2. Homoscedasticity: If GQ p-value > 0.05, constant variance is assumed. The scatter plot should show no distinct pattern.
# 3. Normality: If residuals follow the red line in the Q-Q plot, they are normally distributed.
# 4. Independence: A Durbin-Watson score around 2 indicates no autocorrelation.


# Compute measures of RMSE,MAPE,R-square for test set
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

'''Model Performance Evaluation
1. RMSE (Root Mean Squared Error)
Test RMSE = [RMSE_VALUE]
→ Lower RMSE
   "The model predictions are closer to the actual values, indicating better predictive accuracy."
→ Higher RMSE
   "The model predictions deviate significantly from the actual values, indicating lower predictive accuracy."
→ RMSE ≈ 0
   "The model demonstrates excellent predictive performance with minimal prediction error."
2. MAPE (Mean Absolute Percentage Error)
Test MAPE = [MAPE_VALUE]
→ If MAPE < 10%
   "The model exhibits highly accurate forecasting performance."
→ If 10% ≤ MAPE < 20%
   "The model demonstrates good predictive accuracy."
→ If 20% ≤ MAPE < 50%
   "The model provides reasonable forecasting accuracy."
→ If MAPE ≥ 50%
   "The model exhibits poor forecasting performance and may require improvement."
3. R-Square (Coefficient of Determination)
Test R-Square = [R2_VALUE]
→ If R² > 0.90
   "The model explains more than 90% of the variability in the target variable, indicating an excellent fit."
→ If 0.70 ≤ R² ≤ 0.90
   "The model explains a substantial proportion of variability and demonstrates a good fit."
→ If 0.50 ≤ R² < 0.70
   "The model has moderate explanatory power."
→ If R² < 0.50
   "The model has limited explanatory power and may require additional features or model tuning."
4. Overall Model Performance
→ Low RMSE + Low MAPE + High R²
   "The model demonstrates strong predictive performance and generalizes well to unseen data."
→ High RMSE + High MAPE + Low R²
   "The model exhibits poor predictive performance and requires further improvement."
→ Moderate RMSE + Moderate MAPE + Moderate R²
   "The model provides acceptable predictive performance with scope for optimization."'''


# Split the pre-processed data frame into 2 parts train and test with ratio as 80:20.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train.shape, X_test.shape


# Train a Linear Regression model using sklearn on the training data and calculate the bias error (1 - mean R²) and variance error (standard deviation of R²) by performing 5-fold cross-validation
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

'''Bias-Variance Analysis
Mean Cross-Validation R² = [MEAN_R2]
Bias Error = [BIAS_ERROR]
Variance Error = [VARIANCE_ERROR]
1. Mean R² Analysis
→ If Mean R² > 0.90
"The model demonstrates excellent predictive performance and explains more than 90% of the variability in the target variable."
→ If 0.70 ≤ Mean R² ≤ 0.90
"The model demonstrates good predictive performance."
→ If 0.50 ≤ Mean R² < 0.70
"The model demonstrates moderate predictive performance."
→ If Mean R² < 0.50
"The model demonstrates weak predictive performance and may require further improvement."
2. Bias Error Analysis
→ If Bias Error < 0.10
"The model exhibits low bias and captures the underlying data patterns effectively."
→ If 0.10 ≤ Bias Error < 0.30
"The model exhibits moderate bias."
→ If Bias Error ≥ 0.30
"The model exhibits high bias and may be underfitting the data."
3. Variance Error Analysis
→ If Variance Error < 0.05
"The model exhibits low variance and produces consistent performance across folds."
→ If 0.05 ≤ Variance Error < 0.10
"The model exhibits moderate variance."
→ If Variance Error ≥ 0.10
"The model exhibits high variance and may be sensitive to changes in training data."
4. Bias-Variance Interpretation
→ Low Bias + Low Variance
"The model is well-balanced and expected to generalize well to unseen data."
→ High Bias + Low Variance
"The model is underfitting the data."
→ Low Bias + High Variance
"The model may be overfitting the training data."
→ High Bias + High Variance
"The model suffers from both underfitting and instability and requires improvement."
5. Overall Conclusion
"The model achieved a mean cross-validation R² of [MEAN_R2], with a bias error of [BIAS_ERROR] and a variance error of [VARIANCE_ERROR]. This indicates [LOW/MODERATE/HIGH] bias and [LOW/MODERATE/HIGH] variance, suggesting that the model is [WELL BALANCED / UNDERFITTING / OVERFITTING]."'''


# Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric.
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.model_selection import cross_val_score

ridge = Ridge(alpha=0.1)
lasso = Lasso(alpha=0.01, max_iter=500)
enet = ElasticNet(alpha=0.1, l1_ratio=0.5)

ridge_cv = cross_val_score(ridge, X_train, y_train,cv=5,scoring='neg_root_mean_squared_error')
lasso_cv = cross_val_score(lasso, X_train, y_train,cv=5,scoring='neg_root_mean_squared_error')
enet_cv = cross_val_score(enet, X_train, y_train,cv=5,scoring='neg_root_mean_squared_error')

print(f"Ridge CV RMSE      : {-ridge_cv.mean():.4f}")
print(f"Lasso CV RMSE      : {-lasso_cv.mean():.4f}")
print(f"ElasticNet CV RMSE : {-enet_cv.mean():.4f}")

'''Regularized Regression Model Comparison
ElasticNet CV RMSE = [ENET_RMSE]
Lasso CV RMSE = [LASSO_RMSE]
1. Model Accuracy Comparison
→ If ElasticNet RMSE < Lasso RMSE
"ElasticNet has a lower RMSE compared to Lasso, indicating better predictive performance and lower prediction error."
→ If Lasso RMSE < ElasticNet RMSE
"Lasso has a lower RMSE compared to ElasticNet, indicating better predictive performance and lower prediction error."
→ If both RMSE values are nearly equal
"Both models demonstrate comparable predictive performance."
2. Error Analysis
→ Lower RMSE
"The model predictions are closer to the actual values and therefore more accurate."
→ Higher RMSE
"The model predictions deviate more from the actual values, indicating comparatively lower accuracy."
3. Regularization Insight
→ ElasticNet performs better
"ElasticNet effectively balances L1 and L2 regularization, resulting in improved model generalization."
→ Lasso performs better
"Lasso's L1 regularization effectively performs feature selection and improves model performance."
→ Similar performance
"Both regularization techniques perform similarly and either model may be selected."
4. Model Selection
→ If ElasticNet RMSE < Lasso RMSE
"ElasticNet is the preferred model based on lower cross-validation RMSE."
→ If Lasso RMSE < ElasticNet RMSE
"Lasso is the preferred model based on lower cross-validation RMSE."
→ If Difference < 5%
"Both models perform similarly and model selection may be based on interpretability or feature selection requirements."'''


enet.fit(X_train, y_train)
lasso.fit(X_train, y_train)
ridge.fit(X_train, y_train)


enet_test_rmse = np.sqrt(mean_squared_error(y_test, enet.predict(X_test)))
lasso_test_rmse = np.sqrt(mean_squared_error(y_test, lasso.predict(X_test)))
ridge_test_rmse = np.sqrt(mean_squared_error(y_test, ridge.predict(X_test)))

print(f"\nTest RMSE (ElasticNet): {enet_test_rmse:.4f}")
print(f"Test RMSE (Lasso): {lasso_test_rmse:.4f}")
print(f"Test RMSE (Ridge): {ridge_test_rmse:.4f}")


test_rmse = {"Ridge": ridge_test_rmse, "Lasso": lasso_test_rmse,"ElasticNet": enet_test_rmse}
best_model = min(test_rmse, key=test_rmse.get)
print(f"Best Model on Test Data: {best_model}")
print(f"Lowest Test RMSE: {test_rmse[best_model]:.4f}")

'''Test Set Performance Comparison
ElasticNet Test RMSE = [ENET_TEST_RMSE]
Lasso Test RMSE = [LASSO_TEST_RMSE]
1. Model Accuracy Comparison
→ If ElasticNet Test RMSE < Lasso Test RMSE
"ElasticNet achieved a lower Test RMSE than Lasso, indicating superior predictive performance on unseen data."
→ If Lasso Test RMSE < ElasticNet Test RMSE
"Lasso achieved a lower Test RMSE than ElasticNet, indicating superior predictive performance on unseen data."
→ If both RMSE values are nearly equal
"Both models demonstrate similar predictive performance on the test dataset."
2. Prediction Error Analysis
→ Lower RMSE
"The model predictions are closer to the actual values and exhibit lower prediction error."
→ Higher RMSE
"The model predictions show greater deviation from the actual values."
3. Generalization Capability
→ Lower Test RMSE
"The model generalizes better to unseen data."
→ Higher Test RMSE
"The model exhibits comparatively weaker generalization performance."
4. Model Selection
→ If ElasticNet RMSE < Lasso RMSE
"ElasticNet is the preferred model based on lower test RMSE."
→ If Lasso RMSE < ElasticNet RMSE
"Lasso is the preferred model based on lower test RMSE."
→ If Difference < 5%
"Both models perform similarly and either model may be selected."'''


#Grid Search
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
import numpy as np

model = Ridge()          # Replace with Lasso() or ElasticNet()

param_grid = {'alpha':[0.001,0.01,0.1,1,10,100]}
# param_grid = {'alpha':[0.001,0.01,0.1,1,10,100],'l1_ratio':[0.2,0.4,0.6,0.8]}. - For Elastic Net

grid = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error')

grid.fit(X_train, y_train)
y_pred = grid.best_estimator_.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Best Parameters:", grid.best_params_)
print(f"Best CV RMSE: {best_cv_rmse:.4f}")
print("RMSE:", rmse)

'''Hyperparameter tuning was performed using GridSearchCV (or RandomizedSearchCV).
The best parameter(s) obtained were: <best_params_>. Using the optimal parameter values, the model achieved a Test RMSE of <RMSE>.
Since lower RMSE indicates better prediction accuracy, the tuned model provides improved performance and is selected as the final model.'''


#Random Search
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_squared_error
import numpy as np

models = {"Ridge": (Ridge(),{'alpha': np.logspace(-4, 2, 100)}),
          "Lasso": (Lasso(max_iter=10000),{'alpha': np.logspace(-4, 2, 100)}),
          "ElasticNet": (ElasticNet(max_iter=10000),{'alpha': np.logspace(-4, 2, 100),'l1_ratio': np.linspace(0.1, 0.9, 20) })}

for name, (model, params) in models.items():

    search = RandomizedSearchCV(model,param_distributions=params,n_iter=20,cv=5, scoring='neg_mean_squared_error',random_state=42)
    search.fit(X_train, y_train)
    y_pred = search.best_estimator_.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"\n{name}")
    print("Best Parameters:", search.best_params_)
    print("RMSE:", rmse)


    '''    RandomizedSearchCV identified the best parameter(s) as <best_params_>, resulting in a Test RMSE of <RMSE>. Since the RMSE is the lowest among the evaluated parameter combinations, the tuned model is selected as the final model.
    RandomizedSearchCV reduced computational cost while identifying near-optimal hyperparameters, resulting in improved model performance on the test dataset.'''




















