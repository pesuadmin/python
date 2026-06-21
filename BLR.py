  

import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder

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
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error


# # Part B ( 40 marks)

# ### 2. Basic Pandas DataFrame Operations (8 marks)
# #### Perform the following operation using pandas library   
#      1. Read/load the dataset as a pandas Dataframe.(1 mark)
#      2. Print/show the dimensions of Dataframe i.e. no of rows and columns.(1 mark)
#      3. Print/show the data types of all the features/columns. (1 mark)
#      4. Print/show statistical summary of all the numeric features. (1 mark)
#      5. Print/show statistical summary for all the categorical variable.(2 marks)
#      6. Find out Feature wise Missing value counts.(2 marks)

# 2.1. Read/load the dataset as a pandas Dataframe
file_path = "Bengaluru_House_Data.csv"
df = pd.read_csv(file_path) # use pd.read_excel(file_path) if file_path ends with ".xls" or "xlsx" instead if ".csv"
df.head() # Displays first 5 rows. pass n to display first n rows : df.head(n)


# 2.2. Print/show the dimensions of Dataframe i.e. no of rows and columns.
rows, columns = df.shape
print("Number of rows :", rows)
print("Number of columns :", columns)


#2.3.Print/show the data types of the features/columns.
print(df.dtypes)


# 2.4. Print/show statistical summary of all the numeric  features
# Summary for numeric columns only
print("Numeric Summary:")
print(df.describe())


# 2.5 Print/show statistical summary for all the categorical variable
# hint (include = "object")
# Summary for categorical columns only
print("Categorical Summary:")
print(df.describe(include=['object']))


print(df.describe(include='all'))


# 2.6. Print/show  feature wise missing value counts
print(df.isnull().sum())


# ### 3.  Perform Below  Exploratory Data Analysis(EDA) Tasks.
#     1. Show/Visualize the relationship between features 'bath' and 'price' using scattered plot. (1 marks)
#     2. Show/Visualize the relationship between features 'balcony'and 'price' using scattered plot. (1 mark)
#     3. show/Visualize the relationship between features 'bath','balcony' and 'price' using 3D Scatterplot. (2 marks)
#     4. Show outliers distribution of variable 'bath' by drawing  Boxplot. (3marks)
#

#3.1. Visualize the relationship between 'bath'and 'price' using scattered plot
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,4))
sns.scatterplot(x=df['bath'], y=df['price'])
plt.title("bath vs price")
plt.show()


#3.2. Visualize the relationship between 'balcony'and 'price' using scattered plot
plt.figure(figsize=(6,4))
sns.scatterplot(x=df['balcony'], y=df['price'])
plt.title("balcony vs price")
plt.show()


#3.3. Visualize the relationship between 'bath','balcony' and 'price' using 3D Scatterplot
# hint :fig = plt.figure(figsize=(8, 8))
# hint : ax = plt.axes(projection='3d')

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    df['bath'],
    df['balcony'],
    df['price']
)

ax.set_xlabel('bath')
ax.set_ylabel('balcony')
ax.set_zlabel('price')

plt.show()


#3.4Show outliers distribution of variable 'bath' by drawing  Boxplot.
plt.figure(figsize=(6,4))
sns.boxplot(y=df['bath'])
plt.title("Boxplot of bath")
plt.show()


# ### 4. Pre-process the Dataframe as  Mentioned Below. (25 marks)
#
#     1. Replace missing values of the feature 'balcony'  with numerical value 0 and convert its feature type to int.(2 marks)
#     2. Replace missing values of the feature 'bath' missing values with numerical 1 and convert feature type to int.(2 marks)
#     3. Replace missing values of the feature 'location'  with a constant "missing".(2 marks)
#     4. Replace missing values of the feature 'society'  with a constant "missing".(2 marks)
#     5. Convert the feature 'size' to int by removing albhabetic content and keep only numeric content. In case of  missing/null content replace by constant numeric value- 2. (3 marks)
#     6. Convert the feature 'total_sqft' to numerical using 'to_numeric' method.Also, replace all its missing entries by mean.(3 marks)
#     7. Eliminate all the outlies records/rows from Dtaframe with respect to feature'bath' (2 marks)
#     8. convert 3 categorical features i.e. 'availability', 'location' and 'society' into numerical using label encoding. ( 6 marks)
#     9.  Perfrom one hot encdoding on feature 'area_type' , also ensure output columns are of type int  (3 marks)

# 4.1 Replace missing values of the feature 'balcony' with numerical value 0 and convert its feature type to int.
# hint: use fillna( ).astype( )
df['balcony'] = df['balcony'].fillna(0)

df['balcony'] = df['balcony'].astype(int)


# 4.2 Replace missing values of the feature 'bath' missing values with numerical 1 and convert feature type to int
## hint: use fillna( ).astype( )
df['bath'] = df['bath'].fillna(1)

df['bath'] = df['bath'].astype(int)


# 4.3 Replace missing values of the feature 'location'  with a constant "missing".
### hint: use fillna( )
df['location'] = df['location'].fillna("missing")


# 4.4 Replace missing values of the feature 'society'  with a constant "missing".
df['society'] = df['society'].fillna("missing")


# 4.5 Convert the feature 'size' to int by  and keep only numeric content.
#In case of  missing/null content replace by constant numeric value- 2.
# e.g. '2 BHK' to 2
# hint  : use str.replace(' BHK', '').str.replace(' Bedroom', '').str.replace(' RK', '')
df['size'] = (
    df['size']
    .str.extract('(\d+)')
)

df['size'] = df['size'].fillna(2)

df['size'] = df['size'].astype(int)


#4.6  Convert the feature 'total_sqft' to numerical using 'to_numeric' method .
#Also, replace all its missing entries by mean
# hint : use method pd.to_numeric( df["total_sqft"],errors="coerce")
# and fillna( df["total_sqft"].mean())

df['total_sqft'] = pd.to_numeric(
    df['total_sqft'],
    errors='coerce'
)

df['total_sqft'].fillna(
    df['total_sqft'].mean(),
    inplace=True
)


# 4.7 Eliminate all the outlies records/rows from Dataframe with respect to feature'bath'

# # calculate the first quartile
# Q1 = df[' '].quantile(0.25)# calculate the first quartile
# # calculate the third quartile
# Q3 =df[' '].quantile(0.75)
# # The Interquartile Range (IQR) is defined as the difference between the third and first quartile
# # calculate IQR for each numeric variable
# IQR = Q3 - Q1
# # Define the upper and lower bounds for outliers
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# Eliminate all the outlies records/rows from Dataframe
#df = df[(df[' ']>lower_bound ) & (df[' '] < upper_bound)]

Q1 = df['bath'].quantile(0.25)
Q3 = df['bath'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

df = df[
    (df['bath'] >= lower) &
    (df['bath'] <= upper)
]


#4.8. convert 3 categorical featurs i.e. 'availability', 'location' and 'society' into numerical using label encoding.
#  hint: LabelEncoder().fit_transform()

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

for col in [
    'availability',
    'location',
    'society'
]:
    df[col] = le.fit_transform(df[col])


# 4.9  Perfrom one hot encdoding on feature 'area_type' , also ensure output columns are of type int
# hint pd.get_dummies(df, columns=['area_type'], prefix='', prefix_sep='',dtype= int)

df = pd.get_dummies(
    df,
    columns=['area_type'],
    drop_first=True,
    dtype=int
)

df.head()


print(df.shape)
print(df.head())


# # Part C (40 Marks)

# ### 5.  Perfrom Below Modeling Tasks (15 marks)
#     1. Split the processed dataframe into 2 parts train and test with ratio as 70:30. Ensure feture 'price' as target(y). (3 marks)
#     2. Use OLS statsmodels package to build the Linear Regression model on the train set.Also,generate the summary report.  (6 marks)
#     3. Using sklearn's linear regression model train model on the train set and Interpret the coefficients. (6 marks)
#

# 5.1. Split the processed dataframe into 2 parts train and test with ratio as 70:30.
#Ensure feture 'price' as target(y).
# y = df['price']
# X = df.drop('price', axis=1)

from sklearn.model_selection import train_test_split

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

print(X_train.shape, X_test.shape)


# 5.2. Use OLS statsmodels package to build the Linear Regression model on the train set.
#Also,generate the summary report.


import statsmodels.api as sm

X_train_sm = sm.add_constant(X_train)

ols_model = sm.OLS(
    y_train,
    X_train_sm
).fit()

print(ols_model.summary())
#generate the summary report.


# 5.3 Using sklearn's linear regression model train model on the train set and
#Interpret the coefficients.
#lr= LinearRegression()
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(
    X_train,
    y_train
)

print("Intercept:")
print(lr.intercept_)

coef_df = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': lr.coef_
})

print(coef_df)


# ### 6. Model Comparisons and Hyperparameter tuning  (25 Marks)
#
# 1. Train below models and obtain  values using 5 fold cross validation on train data and 'rmse' metric. Find the metric scorein test set and suggest the best model. ( 15 marks)
#         - Ridge(alpha = 1, max_iter = 500)  (5 marks)
#         - Lasso(alpha = 0.01, max_iter = 500) (5 marks)
#         - ElasticNet(alpha = 0.1, l1_ratio = 0.01, max_iter = 500) (5 marks)
#
# 2.  Using Random serach on Lasso model find the best value of alpha and correxponding rmse value on test set. ( 10 marks)
#

from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_percentage_error,
    r2_score
)

pred_lr = lr.predict(X_test)

rmse = mean_squared_error(
    y_test,
    pred_lr,
    squared=False
)

mape = mean_absolute_percentage_error(
    y_test,
    pred_lr
)

r2 = r2_score(
    y_test,
    pred_lr
)

print("RMSE :", rmse)
print("MAPE :", mape)
print("R2 :", r2)


from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
import numpy as np

ridge = Ridge(
    alpha=1,
    max_iter=500
)

cv_rmse = np.sqrt(
    -cross_val_score(
        ridge,
        X_train,
        y_train,
        cv=5,
        scoring='neg_mean_squared_error'
    )
)

print("Ridge CV RMSE:", cv_rmse.mean())

ridge.fit(X_train, y_train)

pred_ridge = ridge.predict(X_test)

rmse_ridge = mean_squared_error(
    y_test,
    pred_ridge,
    squared=False
)

print("Test RMSE:", rmse_ridge)


# #### 6.1  Train below models and obtain  values using 5 fold cross validation on train data and 'rmse' metric. Find the metric scorein test set and suggest the best model.
#         - Ridge(alpha = 1, max_iter = 500)
#         - Lasso(alpha = 0.01, max_iter = 500)
#         - ElasticNet(alpha = 0.1, l1_ratio = 0.01, max_iter = 500)

# Train & evaluate Ridge
ridge = Ridge(alpha = 1, max_iter = 500)

# fit the model on train set
#  fetch cross validation score
# hint use cross_val_score() and scoring as 'neg_root_mean_squared_error'
# fetch rmse on test set
#hint :mean_squared_error(y_test, y_pred)
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
import numpy as np

ridge = Ridge(
    alpha=1,
    max_iter=500
)

cv_rmse = np.sqrt(
    -cross_val_score(
        ridge,
        X_train,
        y_train,
        cv=5,
        scoring='neg_mean_squared_error'
    )
)

print("Ridge CV RMSE:", cv_rmse.mean())

ridge.fit(X_train, y_train)

pred_ridge = ridge.predict(X_test)

rmse_ridge = mean_squared_error(
    y_test,
    pred_ridge,
    squared=False
)

print("Test RMSE:", rmse_ridge)


# Train & evaluate Lasso
# fit the model on train set
#  fetch cross validation score
# hint use cross_val_score() and scoring as 'neg_root_mean_squared_error'
# fetch rmse on test set
#hint :mean_squared_error(y_test, y_pred)
from sklearn.linear_model import Lasso

lasso = Lasso(
    alpha=0.01,
    max_iter=500
)

cv_rmse = np.sqrt(
    -cross_val_score(
        lasso,
        X_train,
        y_train,
        cv=5,
        scoring='neg_mean_squared_error'
    )
)

print("Lasso CV RMSE:", cv_rmse.mean())

lasso.fit(X_train, y_train)

pred_lasso = lasso.predict(X_test)

rmse_lasso = mean_squared_error(
    y_test,
    pred_lasso,
    squared=False
)

print("Test RMSE:", rmse_lasso)


## Train & evaluate ElasticNet
# enet = ElasticNet(alpha = 0.1, l1_ratio = 0.01, max_iter = 500)

# fit the model on train set


#  fetch cross validation score
# hint use cross_val_score() and scoring as 'neg_root_mean_squared_error'



# fetch rmse on test set
#hint :mean_squared_error(y_test, y_pred)

from sklearn.linear_model import ElasticNet

elastic = ElasticNet(
    alpha=0.1,
    l1_ratio=0.01,
    max_iter=500
)

cv_rmse = np.sqrt(
    -cross_val_score(
        elastic,
        X_train,
        y_train,
        cv=5,
        scoring='neg_mean_squared_error'
    )
)

print("ElasticNet CV RMSE:", cv_rmse.mean())

elastic.fit(X_train, y_train)

pred_elastic = elastic.predict(X_test)

rmse_elastic = mean_squared_error(
    y_test,
    pred_elastic,
    squared=False
)

print("Test RMSE:", rmse_elastic)


comparison = pd.DataFrame({
    'Model': [
        'Ridge',
        'Lasso',
        'ElasticNet'
    ],
    'Test RMSE': [
        rmse_ridge,
        rmse_lasso,
        rmse_elastic
    ]
})

print(comparison)


print(
    comparison.sort_values(
        'Test RMSE'
    )
)


# #### 6.2 Using Random serach CV on Lasso model find the best value of alpha and corresponding rmse value on test set.
#
#


# Random serach on Lasso
# import function to perform RandomizedSearchCV

# hint use : tuned_paramaters = [{'alpha':[0.0001, 0.001, 0.01, 0.1, 1, 5, 10, 20, 40, 60], }]

# initiate the elastic net regression model
lasso = Lasso()



# hint use RandomizedSearchCV ()


# fit the Randomise serch CV model on X_train and y_train using fit()


# get the best parameters


# and print  corresponding rmse value on test set.
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform

param_dist = {
    'alpha': uniform(
        0.0001,
        1
    )
}

random_search = RandomizedSearchCV(
    estimator=Lasso(max_iter=500),
    param_distributions=param_dist,
    n_iter=20,
    cv=5,
    scoring='neg_root_mean_squared_error',
    random_state=42
)

random_search.fit(
    X_train,
    y_train
)

print(
    "Best Alpha:",
    random_search.best_params_
)





