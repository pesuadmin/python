## Find the Best Threshold Using Youden's Index
from sklearn.metrics import roc_curve
import numpy as np
# Predicted probabilities
y_prob = model.predict_proba(X_test)[:, 1]
# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
# Youden Index
youden_index = tpr - fpr
# Best Threshold
best_index = np.argmax(youden_index)
best_threshold = thresholds[best_index]
print("Best Threshold :", round(best_threshold, 4))
print("Youden Index   :", round(youden_index[best_index], 4))
print("Sensitivity    :", round(tpr[best_index], 4))
print("Specificity    :", round(1 - fpr[best_index], 4))

## Evaluate the Model at the Best Threshold
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,cohen_kappa_score,confusion_matrix,classification_report)
# Predictions using best threshold
y_pred = (y_prob >= best_threshold).astype(int)
print("="*60)
print(f"Optimal Threshold (Youden Index): {best_threshold:.4f}")
print("="*60)
print("Accuracy      :", round(accuracy_score(y_test, y_pred),4))
print("Precision     :", round(precision_score(y_test, y_pred),4))
print("Recall        :", round(recall_score(y_test, y_pred),4))
print("F1 Score      :", round(f1_score(y_test, y_pred),4))
print("ROC-AUC       :", round(roc_auc_score(y_test, y_prob),4))
print("Cohen's Kappa :", round(cohen_kappa_score(y_test, y_pred),4))
print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Plot Youden Index
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
plt.plot(thresholds, youden_index, color='blue')
plt.scatter(best_threshold,youden_index[best_index],color='red',s=100,label=f'Best Threshold = {best_threshold:.3f}')
plt.xlabel("Threshold")
plt.ylabel("Youden Index")
plt.title("Youden Index vs Threshold")
plt.grid(alpha=0.3)
plt.legend()
plt.show()

# Change the line based on the Algo
y_prob = lr_model.predict_proba(X_test_sc)[:,1]
y_prob = knn_model.predict_proba(X_test_sc)[:,1]
y_prob = dt_model.predict_proba(X_test)[:,1]
y_prob = rf_model.predict_proba(X_test)[:,1]
y_prob = gb_model.predict_proba(X_test)[:,1]


## All Plots
import matplotlib.pyplot as plt
import seaborn as sns


x_col = 'Age'             # Numeric / Categorical / Date column
y_col = 'Salary'          # Numeric column (for Bar/Line/Violin)
hue_col = 'Target'        # Optional grouping column
title = "My Plot"
plt.figure(figsize=(8,5))

# sns.histplot(data=df,x=x_col,bins=30,kde=False,color='steelblue')
# sns.histplot(data=df, x=x_col, bins=30,kde=True,color='steelblue' )
# sns.kdeplot( data=df, x=x_col, fill=True,color='steelblue')
# sns.violinplot(data=df, x=hue_col, y=y_col,hue=hue_col,palette='Set2',legend=False)
# sns.countplot( data=df, x=x_col, hue=x_col,palette='Set2',legend=False)
# sns.barplot(data=df, x=x_col,y=y_col,hue=x_col,estimator='mean',palette='viridis',legend=False)
# sns.lineplot( data=df, x=x_col, y=y_col,marker='o',linewidth=2)
plt.title(title) ; plt.xlabel(x_col) ; plt.ylabel(y_col) ; plt.xticks(rotation=45) ; plt.grid(alpha=0.3) ; plt.tight_layout() ;plt.show()

# ROC Curve for Multiple Algo
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

# Logistic Regression
lr_prob = tuned['LR (tuned)'].predict_proba(X_test_sc)[:,1]
fpr, tpr, _ = roc_curve(y_test, lr_prob)
plt.plot(fpr, tpr,
         label=f'Logistic Regression (AUC={roc_auc_score(y_test, lr_prob):.3f})')

# Decision Tree
dt_prob = tuned['DT (tuned)'].predict_proba(X_test)[:,1]
fpr, tpr, _ = roc_curve(y_test, dt_prob)
plt.plot(fpr, tpr,
         label=f'Decision Tree (AUC={roc_auc_score(y_test, dt_prob):.3f})')

# Random Forest
rf_prob = tuned['RF (tuned)'].predict_proba(X_test)[:,1]
fpr, tpr, _ = roc_curve(y_test, rf_prob)
plt.plot(fpr, tpr,
         label=f'Random Forest (AUC={roc_auc_score(y_test, rf_prob):.3f})')

# Gradient Boosting
gb_prob = tuned['GB (tuned)'].predict_proba(X_test)[:,1]
fpr, tpr, _ = roc_curve(y_test, gb_prob)
plt.plot(fpr, tpr,
         label=f'Gradient Boosting (AUC={roc_auc_score(y_test, gb_prob):.3f})')

# KNN
knn_prob = tuned['KNN (tuned)'].predict_proba(X_test_sc)[:,1]
fpr, tpr, _ = roc_curve(y_test, knn_prob)
plt.plot(fpr, tpr,
         label=f'KNN (AUC={roc_auc_score(y_test, knn_prob):.3f})')

plt.plot([0,1], [0,1], 'k--', label='Random Classifier')

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Compare Multiple Models on One Precision-Recall Curve
from sklearn.metrics import (
    precision_recall_curve,
    average_precision_score
)

import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

# Logistic Regression
lr_prob = tuned['LR (tuned)'].predict_proba(X_test_sc)[:,1]
precision, recall, _ = precision_recall_curve(y_test, lr_prob)
plt.plot(recall, precision,
         label=f'Logistic Regression (AP={average_precision_score(y_test, lr_prob):.3f})')

# Decision Tree
dt_prob = tuned['DT (tuned)'].predict_proba(X_test)[:,1]
precision, recall, _ = precision_recall_curve(y_test, dt_prob)
plt.plot(recall, precision,
         label=f'Decision Tree (AP={average_precision_score(y_test, dt_prob):.3f})')

# Random Forest
rf_prob = tuned['RF (tuned)'].predict_proba(X_test)[:,1]
precision, recall, _ = precision_recall_curve(y_test, rf_prob)
plt.plot(recall, precision,
         label=f'Random Forest (AP={average_precision_score(y_test, rf_prob):.3f})')

# Gradient Boosting
gb_prob = tuned['GB (tuned)'].predict_proba(X_test)[:,1]
precision, recall, _ = precision_recall_curve(y_test, gb_prob)
plt.plot(recall, precision,
         label=f'Gradient Boosting (AP={average_precision_score(y_test, gb_prob):.3f})')

# KNN
knn_prob = tuned['KNN (tuned)'].predict_proba(X_test_sc)[:,1]
precision, recall, _ = precision_recall_curve(y_test, knn_prob)
plt.plot(recall, precision,
         label=f'KNN (AP={average_precision_score(y_test, knn_prob):.3f})')

plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve Comparison")
plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()


#  KNN Imputation
from sklearn.impute import KNNImputer

# Looks at the K nearest rows (Euclidean) and averages their values for the missing cell.
# Use when: features are numeric & correlated with each other (so neighbors are informative).
knn_imp = KNNImputer(n_neighbors=5)
df[num_cols] = knn_imp.fit_transform(df[num_cols])

#  Iterative (MICE) imputation
from sklearn.experimental import enable_iterative_imputer    # required import
from sklearn.impute        import IterativeImputer

# Models each column with missing values as a function of the other columns.
# Iterates until stable. Most accurate but slowest.
mice = IterativeImputer(max_iter=10, random_state=42)
df[num_cols] = mice.fit_transform(df[num_cols])

# Forward / Backward fill (time-series only)
# Use ONLY when rows are ordered by time. Carries the previous valid value forward.
df = df.sort_values("date")
df = df.fillna(method="ffill")            # forward fill
df = df.fillna(method="bfill")            # backward fill (rare; use only if first row has NaN)



# OUTLIER Detection:

# ======================================================
# UNIVERSAL OUTLIER DETECTION & HANDLING TEMPLATE
# ======================================================

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler

# ------------------------------------------------------
# Select Column
# ------------------------------------------------------

column = 'Income'      # Change column name

# ======================================================
# STEP 1 : DETECT OUTLIERS (Uncomment ONE)
# ======================================================

# -------- IQR --------
outliers = flag_outliers_iqr(df, column, k=1.5)

# -------- Z-Score --------
# outliers = flag_outliers_z(df, column, threshold=3)

# -------- Percentile --------
# outliers = flag_outliers_pct(df, column, lower=0.01, upper=0.99)

# ======================================================
# STEP 2 : SUMMARY
# ======================================================

print("="*60)
print(f"Column : {column}")
print("="*60)

print("Total Records :", len(df))
print("Outliers      :", outliers.sum())
print("Percentage    :", round(outliers.mean()*100,2), "%")

# Display Outliers
print("\nOutlier Records")
print(df[outliers])

# ======================================================
# STEP 3 : HANDLE OUTLIERS
# (Uncomment ONE)
# ======================================================

# ------------------------------------------------------
# A. REMOVE OUTLIERS
# ------------------------------------------------------

# df_clean = df.loc[~outliers].copy()

# ------------------------------------------------------
# B. KEEP ONLY OUTLIERS
# ------------------------------------------------------

# df_clean = df.loc[outliers].copy()

# ------------------------------------------------------
# C. FLAG OUTLIERS
# ------------------------------------------------------

# df[column + "_Outlier"] = outliers

# ------------------------------------------------------
# D. CAP OUTLIERS (Winsorization using IQR)
# ------------------------------------------------------

# def cap_iqr(df, col, k=1.5):
#     lo, hi = iqr_bounds(df[col], k)
#     df[col] = df[col].clip(lower=lo, upper=hi)
#     return df

# df = cap_iqr(df, column)

# ------------------------------------------------------
# E. CAP USING PERCENTILES
# ------------------------------------------------------

# lo, hi = df[column].quantile([0.01,0.99])
# df[column] = df[column].clip(lo, hi)

# ------------------------------------------------------
# F. USE ROBUST SCALER
# ------------------------------------------------------

# num_cols = df.select_dtypes(include='number').columns
# df[num_cols] = RobustScaler().fit_transform(df[num_cols])

# ======================================================
# STEP 4 : VISUALIZE
# ======================================================

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    y=column,
    color='skyblue'
)

plt.title(f'Boxplot of {column}')

plt.tight_layout()
plt.show()


# ======================================================
# UNIVERSAL OUTLIER DETECTION & HANDLING TEMPLATE
# ======================================================

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler

# ------------------------------------------------------
# Select Column
# ------------------------------------------------------

column = 'Income'      # Change column name

# ======================================================
# STEP 1 : DETECT OUTLIERS (Uncomment ONE)
# ======================================================

# -------- IQR --------
outliers = flag_outliers_iqr(df, column, k=1.5)

# -------- Z-Score --------
# outliers = flag_outliers_z(df, column, threshold=3)

# -------- Percentile --------
# outliers = flag_outliers_pct(df, column, lower=0.01, upper=0.99)

# ======================================================
# STEP 2 : SUMMARY
# ======================================================

print("="*60)
print(f"Column : {column}")
print("="*60)

print("Total Records :", len(df))
print("Outliers      :", outliers.sum())
print("Percentage    :", round(outliers.mean()*100,2), "%")

# Display Outliers
print("\nOutlier Records")
print(df[outliers])

# ======================================================
# STEP 3 : HANDLE OUTLIERS
# (Uncomment ONE)
# ======================================================

# ------------------------------------------------------
# A. REMOVE OUTLIERS
# ------------------------------------------------------

# df_clean = df.loc[~outliers].copy()

# ------------------------------------------------------
# B. KEEP ONLY OUTLIERS
# ------------------------------------------------------

# df_clean = df.loc[outliers].copy()

# ------------------------------------------------------
# C. FLAG OUTLIERS
# ------------------------------------------------------

# df[column + "_Outlier"] = outliers

# ------------------------------------------------------
# D. CAP OUTLIERS (Winsorization using IQR)
# ------------------------------------------------------

# def cap_iqr(df, col, k=1.5):
#     lo, hi = iqr_bounds(df[col], k)
#     df[col] = df[col].clip(lower=lo, upper=hi)
#     return df

# df = cap_iqr(df, column)

# ------------------------------------------------------
# E. CAP USING PERCENTILES
# ------------------------------------------------------

# lo, hi = df[column].quantile([0.01,0.99])
# df[column] = df[column].clip(lo, hi)

# ------------------------------------------------------
# F. USE ROBUST SCALER
# ------------------------------------------------------

# num_cols = df.select_dtypes(include='number').columns
# df[num_cols] = RobustScaler().fit_transform(df[num_cols])

# ======================================================
# STEP 4 : VISUALIZE
# ======================================================

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    y=column,
    color='skyblue'
)

plt.title(f'Boxplot of {column}')

plt.tight_layout()
plt.show()


# Skewness
Skewness fix — log/sqrt/Box-Cox transform
from scipy.stats import boxcox

# Check skewness of all numeric columns
skew_summary = df[num_cols].skew().sort_values(ascending=False)
print(skew_summary)
# |skew| > 1 means heavily skewed

# Log transform (positive values only) — pulls right tail in
df["log_income"] = np.log1p(df["income"])  # log1p handles 0 safely (log(1+x))

# Square-root transform (positive values, gentler than log)
df["sqrt_views"] = np.sqrt(df["views"])

# Box-Cox (must be strictly positive)
df["boxcox_price"], lam = boxcox(df["price"] + 0.001)

