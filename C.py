
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
# Best CV RMSE
best_cv_rmse = np.sqrt(-grid.best_score_)

# Test RMSE
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




















