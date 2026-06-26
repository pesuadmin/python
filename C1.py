import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Read dataset
df = pd.read_csv("Hotel Reservations.csv")
print("Shape of Dataset :", df.shape) ; df.head() 
num_cols = df.select_dtypes(include=np.number).columns ; print("\nNumber of Numerical Variables :", len(num_cols)) ; print(num_cols)
cat_cols = df.select_dtypes(include=['object']).columns ;  print("\nNumber of Categorical Variables :", len(cat_cols)) ; print(cat_cols)
print("\nDescriptive Statistics for Numerical Variables") # Descriptive statistics for numerical variables
print(df[num_cols].describe()) ; print("\nDescriptive Statistics for Categorical Variables") # Descriptive statistics for categorical variables
print(df[cat_cols].describe()) ; target_col = 'booking_status'   #  target column
# Inference
''' The dataset contains both numerical and categorical variables. ; Numerical features show variation in mean, standard deviation, minimum, and maximum values. ; Some numerical variables may contain outliers due to large differences between quartiles and maximum values. ; Certain variables may be positively or negatively skewed. ; Missing values may be present in some columns. ; Categorical variables contain multiple unique categories with varying frequencies ; Some categories may dominate the dataset, indicating imbalance. ; Features with very low variance may contribute less to prediction. ; Large standard deviation indicates high variability in the data. ; Difference between mean and median may indicate skewness. ; Presence of duplicate or unnecessary columns may require feature removal. ; Some variables may require scaling before model building. ; Categorical columns will require encoding for machine learning algorithms. ; Dataset appears suitable for classification analysis after preprocessing. ; Further steps like missing value treatment, outlier detection, and correlation analysis are required before model training. '''

##############
cat_cols = df.select_dtypes(include=['object']).columns # Categorical columns
for col in cat_cols:                     # Summary of categorical variables           
    print("\nColumn Name :", col)
    # Number of unique categories
    print("Number of Unique Categories :", df[col].nunique())
    # Proportion of observations
    print(df[col].value_counts(normalize=True) * 100) # el


##############
# df.replace(['?', 'N/A', '-', 'unknown', ' '], np.nan, inplace=True)                 # Requied to Replace invalid values
# df['thalachh'] = df['thalachh'].astype('float64')   # placeholder line                    # Convert datatype to category/object
#df['thalachh'] = pd.to_numeric(df['thalachh'])
# df['City'] = df['City'].str.strip()
# df['City'] = df['City'].str.lower()
# df['col_name'] = df['col_name'].astype('object')   # placeholder line                    # Convert datatype to category/object
# df['Salary'] = pd.to_numeric(df['Salary']). # df['Date'] = pd.to_datetime(df['Date'])  # convert datatype
# df.rename(columns={'old_name':'new_name'},inplace=True)
df.describe()

for col in df.select_dtypes(include=['object']).columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except (ValueError, TypeError):
        pass   #el

# Inference :
'''Some categorical variables may contain highly dominant categories. ; Few categories may have very low frequency indicating class imbalance. ; Certain columns may contain rare or inconsistent categories. ; These variables may require encoding before model building.'''

df.describe()



##############


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
# Incorrect Datatypes

# Type cast those as needed (Float to Int, String to DateTime)
# Syntax : df["column_name"] = df["columns_name"].astype(datetype);
# datatype are `str`, `int`, `float`, `category`
# df['timestamp'] = pd.to_datetime(df['timestamp']) for datetime
#df['columnx'] = df['columnx'].fillna(0).astype(int) # fillna optional if value is missing or NaN/Na

# df['Age'] = 2025 - df['Birth_Year']
# df['BMI_Category'] = np.where(df['BMI'] > 25,'Overweight','Normal')
# df['column_name'] = df['column_name'].str.replace(r'[^A-Za-z0-9 .]','',regex=True). # Retains only alphanumberic and decimal
#df['Salary'] = df['Salary'].str.replace(r'[^0-9.]','',    regex=True). # Only numeric for decimal places
# X = X.replace([np.inf, -np.inf], 0)
# df = df.replace(['@', '#'], '-', regex=True)
# df = df.replace(np.nan, 0)



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

##############
# Missing values
print(df.isnull().sum())

# Missing value plot
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Outlier detection using boxplots
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show() #el

# Target variable balance
print(df[target_col].value_counts())
# Countplot for target variable
sns.countplot(x=df[target_col])
plt.title("Target Variable Distribution")
plt.show()

# df['Target'].value_counts(normalize=True)*100.   - Check class imbalance
# Inference 
''' Missing values are present in some columns. ; Boxplots indicate presence/absence of outliers in numerical features. ; Extreme values may affect model performance. ; Target variable distribution shows whether the classes are balanced or imbalanced. ; Imbalanced target classes may require resampling techniques like SMOTE or undersampling. '''

df[target_col].value_counts(normalize=True)*100.   # - Check class imbalance.    - 60/40 - moderate imbalance.  - 80/20 and above severely imbalanced
# ── Target Variable Balance ──
counts = df[target_col].value_counts()
pct = df[target_col].value_counts(normalize=True) * 100

print("Target Variable Distribution:")
print(pd.DataFrame({'Count': counts, 'Percentage (%)': pct.round(2)}))

fig, axes = plt.subplots(1, 2, figsize=(15, 8))

sns.countplot(x=df[target_col], ax=axes[0], palette=['steelblue', 'orange'])
axes[0].set_title("Target Variable Count (Loan)")
axes[0].set_xlabel("Loan (0=No Default, 1=Default)")
for p in axes[0].patches:
    axes[0].annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width()/2, p.get_height()),ha='center', va='bottom', fontsize=11) #el

axes[1].pie(counts, labels=['No Default (0)', 'Default (1)'],autopct='%1.1f%%', colors=['steelblue', 'orange'], startangle=90)
axes[1].set_title("Target Variable Proportion")

plt.tight_layout()
plt.show()


''' 60 / 40.  - The target variable has a moderately balanced class distribution, with approximately 60% positive and 40% negative instances. Since the class imbalance is not severe, the model is not expected to be heavily biased toward the majority class. However, the F1 score remains an appropriate evaluation metric because it considers both Precision and Recall, providing a more comprehensive assessment of classification performance than accuracy alone.'''
'''80/20 - The target variable exhibits a significant class imbalance, with approximately 80% of observations belonging to one class and only 20% to the other. In such cases, accuracy alone may provide an overly optimistic view of model performance because a model could achieve high accuracy by predominantly predicting the majority class. Therefore, evaluation metrics such as Precision, Recall, F1 Score, and ROC-AUC should be used to assess the model's ability to correctly identify the minority class. '''
''' 90/10 -  The dataset is highly imbalanced, with the minority class representing only 10% of the observations. This imbalance increases the risk of the model being biased toward the majority class. Consequently, greater emphasis should be placed on Recall and F1 Score for the minority class rather than overall accuracy. Techniques such as class weighting, oversampling (e.g., SMOTE), undersampling, or threshold tuning should be considered to improve minority class detection.'''

## Balanced dataset (50:50) -->  Accuracy, F1 Score, ROC-AUC  ## Moderately imbalanced (60:40, 70:30) --> F1 Score, ROC-AUC   ##  Highly imbalanced (80:20+) --> F1 Score, ROC-AUC, Precision-Recall AUC |##  False Negatives are most costly (Disease Screening / Fraud Detection) -->  Recall  ## | False Positives are most costly (Spam Detection) -->  Precision    ## | Need overall ranking across thresholds -->  ROC-AUC  ## | Rare positive class  -->  Precision-Recall AUC + F1 Score         |



##############
# Encoding categorical attributes
#   - LabelEncoder (default below) — works for any classification dataset
#   - OrdinalEncoder — uncomment if dataset has an ordinal column (e.g. Low/Med/High)
#   - get_dummies — uncomment if you specifically want one-hot encoding

from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OrdinalEncoder   # uncomment if needed

# Identify categorical columns (excluding ID column if present)
cat_cols = df.select_dtypes(include=['object','category']).columns
cat_cols = [c for c in cat_cols if c != 'Booking_ID']   # ← exam-required exclusion (update ID name per dataset)

# ─── Ordinal Encoding (only if your dataset has a ranked column) ───
# oe = OrdinalEncoder(categories=[['Low', 'Medium', 'High']])
# df[['priority']] = oe.fit_transform(df[['priority']])

# ─── One-Hot Encoding (alternative — uncomment if preferred over LabelEncoder) ───
# df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

# ─── Label Encoding (default, safest choice) ───
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col].astype(str)) #el

# df['Education'] = df['Education'].replace({'High School': 1,'Graduate': 2,'Post Graduate': 3}) # Manual encoding 
# df['Gender'] = df['Gender'].map({'Male': 1,'Female': 0})    

# Display encoded dataset
df.head()

!pip install category_encoders
import category_encoders as ce

# Separate features and target
X = df.drop('Target', axis=1)
y = df['Target']

# Initialize encoder
encoder = ce.TargetEncoder(cols=['Category'])

# Fit and transform
X['Category_TE'] = encoder.fit_transform(X['Category'], y)

# Drop original column (optional)
X.drop('Category', axis=1, inplace=True)
# df['Target_log'] = np.log(df['Target']). # log1p.   - Required for log transformation - highly right -skewed data

# Inference

''' Categorical variables were converted into numerical format successfully. ; Encoded data can now be used for machine learning models. ; Label encoding assigns unique numerical values to each category. ; Dataset is ready for further preprocessing and model building. '''



df.describe()

##############. Fix Data Defects  # Outliers  # Unnessary features
# Numerical columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
# Categorical columns
cat_cols = df.select_dtypes(include=['object']).columns
df.duplicated().sum()  # Find Duplicate
df.drop_duplicates(inplace=True)  # Remove Duplicate

# df['BloodPressure'] = df['BloodPressure'].replace(0, np.nan)
# df['age'] = df['age'].fillna(df['age'].mean())
# df.groupby(['Gender','Age_Group'])['BMI'].transform('median'))


#df['column_name'] = df['column_name'].fillna(df.groupby(['group_col1','group_col2'])['column_name'].transform('mean')      # or median)
#df['Occupation'] = df['Occupation'].fillna(df.groupby('City')['Occupation'].transform(lambda x: x.mode()[0]))
# num_cols = ['age', 'bmi']
for col in num_cols:
    df[col] = df[col].fillna(df[col].median()) #el

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0]) #el

# Check missing values
print(df.isnull().sum())

# Inference
''' Missing values were successfully handled using central tendency measures. ; Median was used for numerical variables to reduce outlier influence. ; Mode was used for categorical variables since it represents the most frequent category. ; Dataset is now free from missing values and ready for further analysis. '''

##############

# Numerical columns
num_cols = [col for col in df.select_dtypes(include='number').columns if df[col].nunique() > 4]


# Detecting outliers using IQR method
for col in num_cols:
    
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    print(f"{col} : {len(outliers)} outliers")

    # Boxplot
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show() #el

    # Inference 
''' Outliers are present in some numerical variables. ; Boxplots help visualize extreme observations. ; If the number of outliers is very small, treatment may not be necessary. ; If outliers are large in number and affect model performance, capping or removal can be considered. ; Tree-based models are generally less sensitive to outliers.  '''

df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

for col in num_cols:
# Boxplot
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show() #el


##############
# IMPORTANT: Exclude the target column to avoid corrupting binary labels

from scipy.stats import zscore

# Get numeric columns BUT exclude the target column
target_col = target_col  # ← update this per dataset (e.g. 'stroke', 'Exited', 'Loan', 'Survive', 'Attrition')
num = [c for c in df.select_dtypes(include=np.number).columns if c != target_col]
# cols_to_clip = ['Age', 'Annual_Income', 'Balance']
# for c in cols_to_clip:

for c in num:
    # Calculate Z-score
    z = np.abs(zscore(df[c]))
    
    # Count outliers
    outliers = (z > 3).sum()
    print(f"{c}: {outliers} outliers")
    
    # Calculate clipping limits (mean ± 3*std)
    upper = df[c].mean() + 3 * df[c].std()
    lower = df[c].mean() - 3 * df[c].std()
    
    # Clip outliers
    df[c] = np.clip(df[c], lower, upper) #el

print("\nOutliers clipped successfully (target column preserved)")


##############

# Check unique values in each column
print(df.nunique())

# Drop unnecessary columns
df.drop(['Booking_ID'], axis=1, inplace=True)
# df.drop(['ID','Name'], axis=1, inplace=True) # Drop multiple columns

# Display dataset
df.head()

# Inference
'''  The column was removed because it did not provide meaningful predictive information and could negatively impact model performance. Removing irrelevant features helps reduce dimensionality, improve model efficiency, and simplify analysis. ;Feature reduction may reduce overfitting and computational complexity. ; The CustomerID column was removed as it serves only as a unique identifier and does not contribute to the prediction of the target variable. Retaining such columns may add unnecessary noise to the model.  '''

############## Correlation
# Numerical columns
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Keep only columns having more than one unique value
corr_df = numeric_df.loc[:, numeric_df.nunique() > 1]

# Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(corr_df.corr(), annot=True, cmap='RdYlGn', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()# Numerical columns
numeric_df = df.select_dtypes(include=['int64', 'float64'])

df.describe()

##############. Correlation

# Correlation matrix
corr = df.corr(numeric_only=True)
corr




# Inference

'''  Correlation values close to +1 indicate strong positive relationship.  ;  Correlation values close to -1 indicate strong negative relationship. ; Correlation values close to 0 indicate weak or no relationship. ; Positive correlation means both variables increase/decrease together.  ; Negative correlation means one variable increases while the other decreases. ; Correlation Strength Reference ; 0.0 to 0.3 → Weak correlation ; 0.3 to 0.7 → Moderate correlation ; 0.7 to 1.0 → Strong correlation. ; +ve value → Same direction relationship ; -ve value → Opposite direction relationship '''

# ── Pairplot (top correlated features with target) ──
import seaborn as sns
import matplotlib.pyplot as plt

# Correlation matrix
corr = df.corr(numeric_only=True)

# Target column
#target_col = "Loan"          # Change as required

# Top correlated features (excluding target itself)
top_feats = (corr[target_col].drop(target_col).abs().sort_values(ascending=False).head(5).index.tolist())

print("Top 5 Features:", top_feats)

# Pairplot
sns.pairplot(df[top_feats + [target_col]],hue=target_col,diag_kind="kde",plot_kws={"alpha":0.5}
)
plt.suptitle(f"Pairplot - Top Features vs {target_col}", y=1.02)
plt.show()


#########. VIF
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Multicollinearity using VIF
import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Specify target column
#target_col = 'Loan_Status'   # Change as per your dataset

# Create feature matrix
X = df.drop(columns=[target_col])

# Keep only numeric columns
X = X.select_dtypes(include=np.number)

# Function to calculate VIF
def calculate_vif(X_df):
    vif = pd.DataFrame()
    vif["Feature"] = X_df.columns
    vif["VIF"] = [variance_inflation_factor(X_df.values, i)
        for i in range(X_df.shape[1])] #el
    return vif.sort_values("VIF", ascending=False)

# Calculate VIF
vif_df = calculate_vif(X)

print(vif_df)

##############. Split Data Set 
from sklearn.model_selection import train_test_split

X = df.drop(columns=[target_col])
y = df[target_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)

print(f"Total samples   : {len(df)}")
print(f"Training samples: {len(X_train)}  ({len(X_train)/len(df)*100:.1f}%)")
print(f"Testing samples : {len(X_test)}   ({len(X_test)/len(df)*100:.1f}%)")
print(f"\nTarget distribution — Train:")
print(y_train.value_counts(normalize=True).round(3))
print(f"\nTarget distribution — Test:")
print(y_test.value_counts(normalize=True).round(3))


#Inference
'''   Dataset was divided into training and testing sets in 70:30 ratio. ; Training data is used for model learning and testing data is used for evaluation. ; Random state ensures reproducibility of results. ;  '''

##############
# Feature scaling   - REQUIRED FOR LINEAR REGRESSSION, LOGISTIC REGRESSION, KNN-Means, SVM
from sklearn.preprocessing import StandardScaler  # from sklearn.preprocessing import MinMaxScaler
scaler = StandardScaler()  # scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)   # transform only, no fit

##############. Fit Logistic Regression Model 

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,cohen_kappa_score,classification_report,confusion_matrix,ConfusionMatrixDisplay,roc_curve)
import matplotlib.pyplot as plt

scaler = StandardScaler() # Feature Scaling
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)


lr = LogisticRegression(class_weight='balanced',max_iter=1000,random_state=42) # Train Logistic Regression
lr.fit(X_train_sc, y_train)
y_pred = lr.predict(X_test_sc) # Predictions
y_prob = lr.predict_proba(X_test_sc)[:,1]


# Model Evaluation
print("Accuracy      :", round(accuracy_score(y_test, y_pred),4))
print("Precision     :", round(precision_score(y_test, y_pred),4))
print("Recall        :", round(recall_score(y_test, y_pred),4))
print("F1 Score      :", round(f1_score(y_test, y_pred),4))
print("ROC AUC Score :", round(roc_auc_score(y_test, y_prob),4))
print("Cohen's Kappa :", round(cohen_kappa_score(y_test, y_pred),4))


# Classification Report
print("\nClassification Report\n")
print(classification_report(y_test, y_pred))


# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues", values_format='d')
plt.title("Confusion Matrix - Logistic Regression")
plt.show()


# ROC Curve

fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.figure(figsize=(7,5))
plt.plot(fpr,tpr,linewidth=2,label=f"AUC = {roc_auc_score(y_test,y_prob):.4f}")
plt.plot([0,1],[0,1],linestyle="--",color="red",label="Random Classifier")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Logistic Regression")
plt.legend(loc="lower right")
plt.grid(True)
plt.show()

  

  # Inference
    '''  Logistic Regression model was trained successfully. ; Different threshold values affect model predictions and F1 score. ; Lower threshold increases positive predictions and recall. ; Higher threshold increases precision but may reduce recall. ; Best threshold is usually the one with highest F1 score. ; F1 Score Reference ; Close to 1 → Better model performance ; Close to 0 → Poor model performance ; 
F1 Score	Interpretation ; < 0.50	Poor ; 0.50 – 0.70	Average ; 0.70 – 0.85	Good. ;  > 0.85	Excellent ; Threshold Reference. ;  0.3 → More sensitive model (higher recall). ; 0.5 → Default balanced threshold ; 0.7 → More strict model (higher precision) '''

''' The Logistic Regression model achieved a ROC-AUC score of 0.8868, indicating good to excellent discriminatory ability. This means the model can effectively distinguish between positive and negative classes across different classification thresholds. '''

# Threshold Comparison
thresholds = [0.3, 0.5, 0.7]
for t in thresholds:
    y_pred = (y_prob >= t).astype(int)
    print("="*60)
    print(f"Threshold : {t}")
    print("="*60)
    print("Accuracy      :", round(accuracy_score(y_test, y_pred),4))
    print("Precision     :", round(precision_score(y_test, y_pred),4))
    print("Recall        :", round(recall_score(y_test, y_pred),4))
    print("F1 Score      :", round(f1_score(y_test, y_pred),4))
    print("Cohen's Kappa :", round(cohen_kappa_score(y_test, y_pred),4))
    print("\nClassification Report")
    print(classification_report(y_test, y_pred)) #el

'''.The model demonstrates the expected trade-off between Precision and Recall as the classification threshold changes. Increasing the threshold from 0.3 to 0.7 improves Precision but reduces Recall, leading to a decline in the F1 Score.

Although threshold 0.5 achieves the highest Accuracy (80.43%) and Cohen's Kappa (0.5773), threshold 0.3 provides the highest F1 Score (85.97%) because it offers the best balance between Precision and Recall. Since the F1 Score is particularly suitable for evaluating models on moderately imbalanced datasets, threshold 0.3 is the preferred threshold for this classification problem. '''

from sklearn.metrics import f1_score
import numpy as np
import matplotlib.pyplot as plt

thresholds = np.arange(0.1, 1.0, 0.05)
f1_scores = []
for t in thresholds:
    y_pred = (y_prob >= t).astype(int)
    f1_scores.append(f1_score(y_test, y_pred)) #el
plt.figure(figsize=(8,5))
plt.plot(thresholds,f1_scores,marker='o',linewidth=2)
best_idx = np.argmax(f1_scores)
plt.scatter(thresholds[best_idx],f1_scores[best_idx],color='red',s=100,label=f"Best Threshold = {thresholds[best_idx]:.2f}")
plt.xlabel("Threshold")
plt.ylabel("F1 Score")
plt.title("F1 Score vs Threshold")
plt.grid(True)
plt.legend()
plt.show()
print("Best Threshold :", round(thresholds[best_idx],2))
print("Maximum F1 Score :", round(f1_scores[best_idx],4))

##############. Compare the performance of logistic regression, Decision Tree, Random Forest models on the given dataset

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, cohen_kappa_score

# ── Default Models ──
models = {'Logistic Regression': LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42),'Decision Tree': DecisionTreeClassifier(random_state=42),'Random Forest':RandomForestClassifier(random_state=42, n_jobs=-1),'Gradient Boosting':   GradientBoostingClassifier(random_state=42)}
print("=" * 75)
print(f"{'Model':<28} {'Accuracy':>9} {'F1':>8} {'ROC-AUC':>9} {'Kappa':>8}")
print("=" * 75)
default_results = {}
for name, model in models.items():
    Xtr = X_train_sc if 'Logistic' in name else X_train
    Xte = X_test_sc  if 'Logistic' in name else X_test
    model.fit(Xtr, y_train)
    y_pred = model.predict(Xte)
    y_prob = model.predict_proba(Xte)[:, 1]
    acc  = accuracy_score(y_test, y_pred)
    f1   = f1_score(y_test, y_pred)
    roc  = roc_auc_score(y_test, y_prob)
    kap  = cohen_kappa_score(y_test, y_pred)
    default_results[name] = {'Accuracy': acc, 'F1': f1, 'ROC-AUC': roc, 'Kappa': kap}
    print(f"{name:<28} {acc:>9.4f} {f1:>8.4f} {roc:>9.4f} {kap:>8.4f}") #el
   
    # Inference

    ''' Models were compared using Accuracy and F1 Score. ;  Higher Accuracy and F1 Score indicate better model performance. ;  Decision Tree may overfit the data. ; Random Forest generally performs better due to ensemble learning. ;  Logistic Regression works well for simple linear relationships. ;  Performance Reference ; Accuracy / F1	Interpretation. ;  < 0.60	Poor. ; 0.60 – 0.75	Average ; 0.75 – 0.90	Good ; > 0.90	Excellent'''

# ── Tuned Models ──
tuned = {
    'LR (tuned)': LogisticRegression(C=0.1, max_iter=1000, class_weight='balanced', random_state=42),
    'DT (tuned)': DecisionTreeClassifier(max_depth=10, min_samples_split=20,
                                          class_weight='balanced', random_state=42),
    'RF (tuned)': RandomForestClassifier(n_estimators=200, max_depth=15,
                                          class_weight='balanced', min_samples_split=10,
                                          random_state=42, n_jobs=-1),
    'GB (tuned)': GradientBoostingClassifier(n_estimators=200, max_depth=4,
                                              learning_rate=0.05, random_state=42)
}

print("\n" + "=" * 75)
print(f"{'Model':<28} {'Accuracy':>9} {'F1':>8} {'ROC-AUC':>9} {'Kappa':>8}")
print("=" * 75)

tuned_results = {}
for name, model in tuned.items():
    Xtr = X_train_sc if 'LR' in name else X_train
    Xte = X_test_sc  if 'LR' in name else X_test
    model.fit(Xtr, y_train)
    y_pred = model.predict(Xte)
    y_prob = model.predict_proba(Xte)[:, 1]
    acc  = accuracy_score(y_test, y_pred)
    f1   = f1_score(y_test, y_pred)
    roc  = roc_auc_score(y_test, y_prob)
    kap  = cohen_kappa_score(y_test, y_pred)
    tuned_results[name] = {'Accuracy': acc, 'F1': f1, 'ROC-AUC': roc, 'Kappa': kap}
    print(f"{name:<28} {acc:>9.4f} {f1:>8.4f} {roc:>9.4f} {kap:>8.4f}")

##############
# Re-fit with optimizations
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(18, 5))

metrics_to_plot = ['F1', 'ROC-AUC']

for ax, metric in zip(axes, metrics_to_plot):

    default_vals = [default_results[m][metric] for m in['Logistic Regression','Decision Tree','Random Forest','Gradient Boosting']]
    tuned_vals = [tuned_results[m][metric] for m in['LR (tuned)','DT (tuned)','RF (tuned)','GB (tuned)']]
    x = np.arange(4)
    w = 0.35
    ax.bar(x - w/2,default_vals,w,label='Default',color='steelblue')
    ax.bar(x + w/2,tuned_vals, w,label='Tuned',color='tomato')
    ax.set_xticks(x)
    ax.set_xticklabels(['Logistic\nRegression','Decision\nTree','Random\nForest','Gradient\nBoosting'])
    ax.set_ylabel(metric)
    ax.set_title(f'{metric}: Default vs Tuned')
    ax.set_ylim(0,1)
    ax.grid(axis='y', alpha=0.3)
    ax.legend()

plt.suptitle("Model Comparison: Default vs Tuned Models", fontsize=14)
plt.tight_layout()
plt.show()

# ## Justification for Model Optimizations
# 
# ### Logistic Regression
# - **`C=0.1` (regularization strength):** A smaller `C` applies **stronger L2 regularization**, 
#   which shrinks coefficient magnitudes and reduces overfitting. This is preferred when features 
#   are correlated or when the default model shows signs of memorizing training data.
# - **`class_weight='balanced'`:** Automatically adjusts weights inversely proportional to class 
#   frequency, ensuring the minority class is not ignored during loss minimization. Essential when 
#   the target distribution is skewed (e.g., 70:30 or worse).
# - **`max_iter=1000`:** Ensures the optimization algorithm converges, especially on scaled data 
#   with many features. Prevents `ConvergenceWarning`.
# 
# ### Decision Tree
# - **`max_depth=10`:** Caps tree depth to prevent the tree from growing until every leaf is pure. 
#   A fully-grown tree memorizes training data and generalizes poorly. Depth of 8–12 is a 
#   safe starting range for most tabular datasets.
# - **`min_samples_split=20`:** Requires at least 20 samples in a node before splitting further. 
#   This prevents the tree from creating splits based on noise in small data subsets.
# - **`random_state=42`:** Ensures reproducibility of the same tree across runs.
# 
# ### Random Forest
# - **`n_estimators=200`:** Increases the number of trees in the ensemble. More trees provide 
#   more averaged predictions, which reduces variance. Returns diminish beyond ~200–500 trees, 
#   so this is a balanced choice between performance and training time.
# - **`max_depth=15`:** Controls per-tree complexity. Slightly deeper than the Decision Tree limit 
#   because RF's averaging already reduces overfitting risk, allowing each individual tree to 
#   learn more granular patterns.
# - **`min_samples_split=10`:** Prevents individual trees from over-splitting on noisy subsets.
# - **`n_jobs=-1`:** Uses all CPU cores to train trees in parallel, reducing wall-clock time.
# 
# ### Justification Summary (Mnemonic: "REGULARIZE → PRUNE → ENSEMBLE")
# - **LR → REGULARIZE:** Use `C` and `class_weight` to control coefficient magnitude and class balance.
# - **DT → PRUNE:** Use `max_depth` and `min_samples_split` to stop the tree before it memorizes.
# - **RF → ENSEMBLE:** Use `n_estimators` and per-tree depth limits to balance bias and variance.

# ## Post-Tuning Observations
# 
# ### Comparison: Default vs Tuned
# 
# | Model | Default F1 | Tuned F1 | Change |
# |---|---|---|---|
# | Logistic Regression | [fill] | [fill] | [↑ / ↓ / ≈] |
# | Decision Tree       | [fill] | [fill] | [↑ / ↓ / ≈] |
# | Random Forest       | [fill] | [fill] | [↑ / ↓ / ≈] |
# 
# ### Inference
# 
# **Branch A — If tuning IMPROVED scores (most common case):**
# - Tuning produced measurable gains, confirming that default hyperparameters were not optimal 
#   for this dataset.
# - Logistic Regression benefited most from regularization, suggesting some multicollinearity 
#   or noise in the features.
# - Decision Tree showed reduced overfitting after depth-capping, narrowing the gap between 
#   train and test accuracy.
# - Random Forest remained the top performer, validating ensemble methods for this classification 
#   problem.
# 
# **Branch B — If tuning gave MARGINAL or NO improvement:**
# - The default hyperparameters were already well-suited to this dataset, indicating that the 
#   data is clean and the models generalize naturally without aggressive regularization.
# - Further improvements would likely require feature engineering, advanced encoding, or 
#   algorithms beyond the three tested (e.g., XGBoost, LightGBM).
# 
# **Branch C — If tuning DEGRADED scores:**
# - Over-regularization (LR) or excessive pruning (DT, RF) restricted the models below their 
#   natural capacity for this data.
# - Recommended next step: relax the constraints — increase `C`, raise `max_depth`, or use 
#   `GridSearchCV` to systematically search the hyperparameter space rather than guess.
# 
# ### Final Model Recommendation
# Based on the highest test F1 score, **[Random Forest / Logistic Regression / Decision Tree]** 
# is selected as the final model for this business problem. It balances predictive accuracy 
# with [interpretability / robustness to outliers / handling of mixed data types] — qualities 
# that align with the deployment requirements of this classification task.

# ### 3 (c) Summarize the solution to the business problem as follows (8 marks): 
# ● Feature Importance (4 marks): Identify and explain which features are most 
# influential in solving the problem and why. 
# 
# ● Evaluation Metrics Performance (2 marks)Provide an analysis of the model's 
# performance based on key evaluation metrics. 
# 
# ● Overall Results and Observations (2 marks): Summarize the overall findings, 
# including key insights and their implications for the business problem. 
# 

##############

# Feature importance using Random Forest # Evaluation Metrics PErformance #
# ── Feature Importance from Random Forest ──
rf_model = tuned.get('RF (tuned)', models['Random Forest'])

importance_df = pd.DataFrame({'Feature': X.columns,'Importance': rf_model.feature_importances_}).sort_values('Importance', ascending=False).reset_index(drop=True)

print("Feature Importance Ranking:")
print(importance_df.to_string(index=False))

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df, palette='viridis')
plt.title("Feature Importance — Random Forest (Top Features for Loan Default Prediction)")
plt.xlabel("Importance Score")
plt.tight_layout(); plt.show()


# Possible Inference
# 
# Features with higher importance values contribute more to prediction. ;  Highly important features have stronger influence on the target variable. ; Features with very low importance may be less useful and can be removed. ; Feature importance helps understand key business drivers and supports better decision making. ; 
# 
# 

##############
# Evaluation metrics
# ── Evaluation Metrics — Best Model (Random Forest Tuned) ──
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, cohen_kappa_score

y_pred_rf = rf_model.predict(X_test)
y_prob_rf  = rf_model.predict_proba(X_test)[:, 1]

#print("=" * 45)
print("  Evaluation Metrics — Random Forest (Tuned)")
print("-" * 50)
print(f"  Accuracy     : {accuracy_score(y_test, y_pred_rf):.4f}")
print(f"  Precision    : {precision_score(y_test, y_pred_rf):.4f}")
print(f"  Recall       : {recall_score(y_test, y_pred_rf):.4f}")
print(f"  F1 Score     : {f1_score(y_test, y_pred_rf):.4f}")
print(f"  ROC-AUC      : {roc_auc_score(y_test, y_prob_rf):.4f}")
print(f"  Cohen's Kappa: {cohen_kappa_score(y_test, y_pred_rf):.4f}")
#print("=" * 45)

# Possible Inference
# 
# Accuracy indicates overall correctness of the model.
# 
# Precision indicates how many predicted positives are actually correct.
# 
# Recall indicates how well the model identifies actual positive cases.
# 
# F1 Score provides balanced performance between Precision and Recall.
# 
# Metric Reference
# 
# Metric Value	Interpretation
# 
# < 0.60	Poor
# 
# 0.60 – 0.75	Average
# 
# 0.75 – 0.90	Good
# 
# > 0.90	Excellent
# 
# Higher metric values indicate better model performance.
# 
# F1 Score is preferred for imbalanced datasets.
# 

# Possible Inference
# The model was able to identify important patterns in the dataset successfully.
# 
# Feature analysis showed that a few variables contribute more strongly toward prediction.
# 
# Evaluation metrics indicate that the model achieved satisfactory performance.
# 
# The selected model can support better business decision-making and improve prediction accuracy.
# 
# Proper preprocessing and feature engineering helped improve overall model performance.
# 
# The findings can help optimize business strategies and reduce operational risks.
# 
# Generic Business Impact Statements
# 
# Helps improve customer targeting and decision-making.
# 
# Supports better resource planning and operational efficiency.
# 
# Enables data-driven business insights.
# 
# Helps identify key factors influencing the target outcome.
# 
# 

# ## 3(c) Business Problem Summary
# 
# ### Feature Importance (4 marks)
# 
# The Random Forest model ranks features by how much each one helps reduce 
# prediction error across all trees in the ensemble. The top features from the 
# importance table are the strongest drivers of the target variable.
# 
# **Top 3 features and why they matter:**
# 
# 1. **[Feature 1]** — has the highest importance score. This means the model 
#    uses this feature most often to split the data, indicating it has the 
#    strongest relationship with the target. In business terms, this is the 
#    single most useful piece of information for predicting the outcome.
# 
# 2. **[Feature 2]** — second most important. It captures a different aspect 
#    of the data that complements Feature 1, helping the model separate cases 
#    that Feature 1 alone cannot distinguish.
# 
# 3. **[Feature 3]** — third most important. Adds further refinement to 
#    predictions, especially for edge cases.
# 
# **Why these features dominate:**
# - They have a clear and measurable relationship with the target variable.
# - They show high variance across records, giving the model strong signal to 
#   split on.
# - They align with domain knowledge — these are the kinds of factors a 
#   business analyst would also examine when investigating this problem.
# 
# **Features with low importance** (bottom of the table) contribute little to 
# prediction and could be removed in a simpler model without major loss in 
# performance.
# 
# ---
# 
# ### Evaluation Metrics Performance (2 marks)
# 
# The final model was evaluated using four standard classification metrics:
# 
# | Metric    | Score   | What it tells us |
# |-----------|---------|-------------------|
# | Accuracy  | [fill]  | Overall correctness across both classes |
# | Precision | [fill]  | Of all predicted positives, how many were correct |
# | Recall    | [fill]  | Of all actual positives, how many were caught |
# | F1 Score  | [fill]  | Balanced measure combining precision and recall |
# 
# **Interpretation:**
# - The model achieves [strong / moderate / acceptable] performance overall.
# - High **precision** means few false alarms — when the model predicts 
#   positive, it is usually right.
# - High **recall** means few missed cases — the model catches most actual 
#   positives.
# - The **F1 score** confirms the model maintains a healthy balance between 
#   the two, which is especially important when the target classes are 
#   imbalanced.
# 
# ---
# 
# ### Overall Results and Observations (2 marks)
# 
# **Key findings:**
# - The classification problem was solved successfully using a structured 
#   pipeline: data cleaning → encoding → splitting → modeling → evaluation.
# - Among the three models tested (Logistic Regression, Decision Tree, 
#   Random Forest), **[Random Forest]** performed best, confirming that 
#   ensemble methods work well for this type of tabular data.
# - A small number of features drive most of the predictive power. This 
#   means the business can focus monitoring and decision-making on these 
#   few high-impact variables rather than tracking every available field.
# 
# **Business implications:**
# - The model can be deployed to support decision-making by flagging 
#   high-risk or high-value cases in advance.
# - Resources (staff time, marketing spend, inventory, operational effort) 
#   can be allocated more efficiently by focusing on the top predictive 
#   features identified.
# - The findings provide a data-driven foundation for refining business 
#   strategy — instead of acting on intuition, decisions can be backed by 
#   measurable evidence from the model.
# - Continued monitoring and periodic retraining will keep the model 
#   accurate as new data arrives and business conditions change.
# 
# **Conclusion:** The selected model meets the business requirement of 
# reliable classification and provides interpretable insights that connect 
# directly to operational decisions.
