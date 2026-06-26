# import 'Pandas' 
import pandas as pd 

# import 'Numpy' 
import numpy as np

# import subpackage of Matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# import 'Seaborn' 
import seaborn as sns

# to suppress warnings 
from warnings import filterwarnings
filterwarnings('ignore')

# display all columns of the dataframe
pd.options.display.max_columns = None

# display all rows of the dataframe
pd.options.display.max_rows = None

# import train-test split 
from sklearn.model_selection import train_test_split

# import StandardScaler to perform scaling
from sklearn.preprocessing import StandardScaler, MinMaxScaler, TargetEncoder
from sklearn.feature_selection import RFE
from statsmodels.stats.outliers_influence import variance_inflation_factor



# import various functions from sklearn 
from sklearn.metrics import classification_report
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import StackingClassifier
from sklearn.tree import DecisionTreeClassifier

# import the XGBoost function for classification
from xgboost import XGBClassifier

# import the functions for visualizing the decision tree
from sklearn import tree
import pydotplus
from IPython.display import Image 

# pip install pydotplus
# !conda install -c conda-forge python-graphviz -y

df_bank = pd.read_csv("bank_churn.csv")

# display the first five rows of the data
df_bank.head()

# The data definition is as follows:
# 
# CreditScore: Credit score of the customer
# 
# Geography: Resident country of the customer
# 
# Gender: Gender of the customer
# 
# Age: Age of the customer
# 
# NumOfYrsWithBank: Years for which the customer has been with the bank
# 
# Balance: Bank balance of the customer in Euro
# 
# NumOfProducts: Number of bank facilities for which customer has opted
# 
# HasCrCard: Whether the customer has credit card or not (1 = Yes, 0 = No)
# 
# Closed_Acc: Whether the customer has closed the bank account or not (1 = Yes, 0 = No) (target/dependent variable)

df_num = df_bank.select_dtypes(include=np.number).drop(["Closed_Acc"],axis=1)

# scale all the numeric independent variables
X_scaler = StandardScaler()

num_scaled = X_scaler.fit_transform(df_num)

# create a dataframe of scaled numerical variables and pass the required column names to the parameter 'columns'
df_num_scaled = pd.DataFrame(num_scaled, columns = df_num.columns)

df_cat = df_bank.select_dtypes(include="object")

dummy_variables = pd.get_dummies(df_cat, drop_first=True)

X = pd.concat([df_num_scaled, dummy_variables],axis=1)

# add a constant column to the dataframe
# while using the 'Logit' method in the Statsmodels library, the method do not consider the intercept by default
X = sm.add_constant(X)

# consider the dependent variable
y = df_bank["Closed_Acc"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1, test_size = 0.2)

logreg_full = sm.Logit(y_train, X_train).fit()

# take the exponential of the coefficient of a variable to calculate the odds
# 'params' returns the coefficients of all the independent variables
df_odds = pd.DataFrame(np.exp(logreg_full.params), columns= ['Odds']) 

# print the dataframe
df_odds

# #### 3. Calculate the Specificity and Sensitivity from the confusion matrix of the full model (consider the probability threshold as 0.25)

y_pred_prob = logreg_full.predict(X_test)

# consider the cut-off probability as 0.25
# convert probabilities to 0 and 1 using 'if_else'
y_pred = [ 0 if x < 0.25 else 1 for x in y_pred_prob]

# create a confusion matrix
# pass the actual and predicted target values to the confusion_matrix()
cm = confusion_matrix(y_test, y_pred)

# identify each grid in confusion matrix in terms of correct and wrong predictions 
# True Negatives are denoted by 'TN'
TN = cm[0,0]

# True Positives are denoted by 'TP'
TP = cm[1,1]

# False Positives are denoted by 'FP'
FP = cm[0,1]

# False Negatives are denoted by 'FN'
FN = cm[1,0]

sensitivity = TP / (TP+FN)

# print the value
print(sensitivity)

specificity = TN / (TN+FP)

# print the value
print(specificity)

# #### 4. Build a logistic model on the 6 features obtained by RFE and plot the ROC curve

X_train_rfe = X_train.iloc[:,1:]
X_test_rfe = X_test.iloc[:,1:]

# initiate logistic regression model 
logreg = LogisticRegression()

# if we do not pass the number of features, RFE considers half of the features
rfe_model = RFE(estimator = logreg, n_features_to_select = 6)

# fit the RFE model on the train dataset using fit()
rfe_model = rfe_model.fit(X_train_rfe, y_train)

# create a series containing feature and its corresponding rank obtained from RFE
# 'ranking_' returns the rank of each variable after applying RFE
feat_index = pd.Series(data = rfe_model.ranking_, index = X_train_rfe.columns)

# select the features with rank = 1, 'index' returns the indices of a series (i.e. features with rank=1) 
signi_feat_rfe = feat_index[feat_index==1].index

# print the significant features obtained from RFE
print(signi_feat_rfe)

logreg_rfe = sm.Logit(y_train, X_train[['const', 'CreditScore', 'Age', 'Balance', 'NumOfProducts', 'Geography_Germany',
                                        'Gender_Male']]).fit()

# print the summary of the model
print(logreg_rfe.summary())

# Do predictions on test
y_pred_prob_rfe = logreg_rfe.predict(X_test[['const', 'CreditScore', 'Age', 'Balance', 'NumOfProducts', 'Geography_Germany',
                                             'Gender_Male']])

# plot ROC curve

fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob_rfe)

# plot the ROC curve
plt.plot(fpr, tpr)

# set limits for x and y axes
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])

# plot the straight line showing worst prediction for the model
plt.plot([0, 1], [0, 1],'r--')

# add plot and axes labels
# set text size using 'fontsize'
plt.title('ROC curve for Customer Churn Prediction Classifier (RFE Model)', fontsize = 15)
plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)

# plot the grid
plt.grid(True)

# ### Navie Baye's & KNN 

df_nba = pd.read_csv('nba_data.csv')
print(df_nba.shape)
# display the first five rows of the data
df_nba.head()

print(df_nba.duplicated().value_counts())

df_nba = df_nba.drop_duplicates()

# recheck the duplicates
df_nba.duplicated().value_counts()

df_nba = df_nba.drop('NAME', axis = 1)

df_feature = df_nba.drop('CAREER_5YRS', axis=1)

df_target = df_nba['CAREER_5YRS']

df_feature.boxplot()

plt.title('Distribution of all Independent Variables', fontsize = 15)

plt.xticks(rotation = 'vertical', fontsize = 15)

# display the plot
plt.show()

# outlier Removal using IQR method

Q1 = df_feature.quantile(0.25)

Q3 = df_feature.quantile(0.75)

IQR = Q3 - Q1

df_nba = df_nba[~((df_nba < (Q1 - 1.5 * IQR)) | (df_nba > (Q3 + 1.5 * IQR))).any(axis=1)]

# reset the index of the dataframe without outliers
df_nba = df_nba.reset_index(drop = True)

# check the shape of the data
df_nba.shape

# ### 4. Build a naive bayes model on 70% of the original data and plot the ROC curve along with the AUC score
# 
# As, for the naive bayes algorithm, feature scaling is not required. We use the original dataset to build the model.
# 
# The columns in the original dataset are of integer type; thus, we can use a multinomial naive bayes classifier given by the MultinomialNB().

df_feature = df_nba.drop('CAREER_5YRS', axis=1)

df_target = df_nba['CAREER_5YRS']

X_scaler = MinMaxScaler()

num_scaled = X_scaler.fit_transform(df_feature)

df_feature_scaled = pd.DataFrame(num_scaled, columns = df_feature.columns)

# check the range of each variable
print('Range: \n', df_feature_scaled.max() - df_feature_scaled.min())

X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(df_feature_scaled, df_target, 
                                                                                random_state = 1, test_size = 0.3)

mnb = MultinomialNB()

# fit the model using fit() on train data
mnb_model = mnb.fit(X_train, y_train)

y_pred_prob = mnb_model.predict_proba(X_test)[:,1]

fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# plot the ROC curve
plt.plot(fpr, tpr)

# set limits for x and y axes
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])

# plot the straight line showing worst prediction for the model
plt.plot([0, 1], [0, 1],'r--')


plt.title('ROC Curve Naive Bayes Classifier', fontsize = 15)
plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)

# add the AUC score to the plot
# 'x' and 'y' gives position of the text
# 's' is the text 
# use round() to round-off the AUC score upto 4 digits
plt.text(x = 0.02, y = 0.9, s = ('AUC Score:',round(roc_auc_score(y_test, y_pred_prob),4)))

# plot the grid
plt.grid(True)

# 4. Is scaling required for the KNN algorithm? If yes, scale the data such that the range of each variable will be equal to 1
# 
# As KNN is the distance-based algorithm, it uses different distance metrics to identify the nearest points for the given data point. If we apply KNN on the unscaled data, the variable with higher values (in our case, the variable GP) will dominate the other variables. Thus, we scale the independent variables before applying the KNN algorithm.

# #### 5. Build a 7-NN model on 70% of the data using the 'Chebyshev' distance and find its accuracy

X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(df_feature_scaled, df_target, 
                                                                                random_state = 1, test_size = 0.3)

knn = KNeighborsClassifier(n_neighbors = 7, metric = 'chebyshev')

# fit the model using fit() on train data
knn_model = knn.fit(X_train_scaled, y_train_scaled)

y_pred = knn_model.predict(X_test_scaled)

# calculate the accuracy
print('Accuracy:', accuracy_score(y_test_scaled, y_pred))

# 6. Find the best value of 'K' for the KNN model from the given list of values (use 5-fold cross validation)
# Use the given list:
# 
# K = [3, 5, 7, 9, 11, 13]
# 
# Consider the train and test set in Q5.

K = [3, 5, 7, 9, 11, 13]


tuned_paramaters = [{'n_neighbors': K}]
 
# default metric is minkowski, and with p=2 it is equivalent to the euclidean metric
knn = KNeighborsClassifier()

knn_grid = GridSearchCV(estimator = knn, param_grid = tuned_paramaters, cv = 5)

# use fit() to fit the model on the train set
knn_grid_model = knn_grid.fit(X_train_scaled, y_train_scaled)

# get the best parameters
print('Best value of K: ', knn_grid_model.best_params_, '\n')

# 7. Which distance metric among 'manhattan', 'euclidean' and 'chebyshev' is suitable for the given dataset? (consider K = 19)

tuned_paramaters = {'metric': ['euclidean', 'manhattan', 'Chebyshev']}

knn = KNeighborsClassifier(n_neighbors = 19)

knn_grid = GridSearchCV(estimator = knn, param_grid = tuned_paramaters, cv = 5)

# fit the model on train data using fit()
knn_grid.fit(X_train_scaled, y_train_scaled)

# get the best parameters
print('Best parameters for KNN Classifier: ', knn_grid.best_params_, '\n')

# 8. Find the euclidean distance between the first observation of the dataframe 'X_test_scaled' and its five neighboring points in the train set (use for loop)

test_pt = X_test_scaled.iloc[0,:]

d = []

# use for loop to consider each data point in the train set
for i in X_train_scaled.index:
    sum = 0
    
    # use for loop to access each element in a observation
    for j in range(len(X_test_scaled.iloc[0,:])):
        
        # calculate the squared euclidean distance
        sum = sum + (X_test_scaled.iloc[0,:][j] - X_train_scaled.loc[i][j])**2
    
    # take the square root of 'sum' to get the euclidean distance 
    distance = sum ** (1/2)
    
    # append the result to the list 'd'
    d.append(distance)    

d.sort()

# print first five distance values
print(d[0:5])

# 9. Use the parameters obtained in Q7 to build the KNN model, and find the number of false predictions using the test set

knn_classification = KNeighborsClassifier(n_neighbors = 19, metric = 'euclidean')

# fit the model using fit() on train data
knn_model = knn_classification.fit(X_train_scaled, y_train_scaled)

y_pred = knn_model.predict(X_test_scaled)

cm = confusion_matrix(y_test_scaled, y_pred)

conf_matrix = pd.DataFrame(data = cm, columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])

sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = ListedColormap(['lightgreen']), cbar = False, 
            linewidths = 0.1, annot_kws = {'size':25})

plt.xticks(fontsize = 20)

plt.yticks(fontsize = 20)

# display the plot
plt.show()

# **Interpretation:** The off-diagonal entries in the confusion matrix returns the count of false predictions made by the model on the test set. Here, 103 observations out of 317 are wrongly predicted.

# ### ------------------ DECISION TREE -------------------- ###

df_seed = pd.read_csv('seedtype_data.csv')
df_seed.shape

# 1. Is there any record where no data have been reported? If yes, do the needful

na_data = df_seed.isna() 
print(na_data)

# seperate the indicating values for each record 
# all() returns only if all elements are True over the given axis 
df_null = na_data.all(axis='columns') == True  # mask

# obtain a list of all records where indicating value is true 
df_null.index[df_null].tolist()

# 'how = all' drops the row which has all the null entries, the whole row is null 
df_seed = df_seed.dropna(axis = 0, how = 'all')

# check the dimensions of the data after removing the empty rows
df_seed.shape

df_seed.isnull().sum()

# #### 2. Use the visualization technique to identify the variables with missing data

sns.heatmap(df_seed.isnull(), cbar = False)

# display the plot
plt.show()

# **Interpretation:** The above plot shows the variable `Kernel_len` contains missing data. The black color shows the non-null data and the cream color represents the missing data.

df_seed['Kernel_len'].describe()

# As we can see that there is no significant difference between the mean and median of the kernel length. We replace the missing values with the mean of the variable.

df_seed['Kernel_len'] = df_seed['Kernel_len'].fillna(df_seed['Kernel_len'].mean())

df_feature = df_seed.drop('Type', axis=1)

# store the target variable 'Type' in a dataframe 'df_target'
df_target = df_seed["Type"]

df_feature.boxplot()

# set plot label
# set text size using 'fontsize'
plt.title('Distribution of all Independent Variables', fontsize = 15)

# xticks() returns the x-axis ticks
# 'rotation = vertical' rotates the x-axis labels vertically
# set text size using 'fontsize'
plt.xticks(rotation = 'vertical', fontsize = 15)

# display the plot
plt.show()

X_train, X_test, y_train, y_test = train_test_split(df_feature, df_target, random_state = 1, test_size = 0.3)

print('X_train', X_train.shape)
print('y_train', y_train.shape)


print('X_test', X_test.shape)
print('y_test', y_test.shape)

# #### Build a decision tree model on the train set using 'gini' criterion.

decision_tree_classification = DecisionTreeClassifier(criterion = 'gini', random_state = 1)

# fit the model using fit() on train data
decision_tree = decision_tree_classification.fit(X_train, y_train)

#### Let us plot the confusion matrix. The sum of the diagonal elements in the matrix corresponds to the 
#### total correct predictions.

y_pred = decision_tree.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])


sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = 'Blues', cbar = False, annot_kws = {'size':25})

# set the font size of x-axis ticks using 'fontsize'
plt.xticks(fontsize = 20)

# set the font size of y-axis ticks using 'fontsize'
plt.yticks(fontsize = 20)

# display the plot
plt.show()

# #### Plot a decision tree for the model in the previous question and identify the seed type of the first observation in the test set

labels = X_train.columns

# export a decision tree in DOT format
# pass the 'decision_tree' to export it to Graphviz
# pass the column names to 'feature_names'
# pass the required class labels to 'class_names'
dot_data = tree.export_graphviz(decision_tree, feature_names = labels, class_names = ["Kama","Rosa"])  

# plot the decision tree using DOT format in 'dot_data'
graph = pydotplus.graph_from_dot_data(dot_data)  

# display the decision tree
Image(graph.create_png())

# #### Select the optimal number for decision trees from the given list of values to build a random forest using entropy criterion
# 
# **Use the given list:**
# 
# no_of_trees = [6, 8, 10, 12, 14, 16]
# 
# Consider the train and test set in Q1

no_of_trees = [6, 8, 10, 12, 14, 16]

# create a dictionary with hyperparameter and its values
# pass a list of values to 'n_estimators' to build the different number of trees in the random forest
tuned_paramaters = [{'n_estimators': no_of_trees}]
 
random_forest_classification = RandomForestClassifier(criterion = 'entropy', random_state = 1)

# use GridSearchCV() to find the optimal value of the hyperparameters
rf_grid = GridSearchCV(estimator = random_forest_classification, 
                       param_grid = tuned_paramaters, 
                       cv = 5)

# use fit() to fit the model on the train set
rf_model = rf_grid.fit(X_train, y_train)

# get the best parameters
print('Best parameter for random forest classifier: ', rf_model.best_params_, '\n')

# #### Identify the most important variable in the random forest build with the optimal number of trees obtained in above question
# 
# Consider the train and test set in Q1.
# 
# First build the random forest with the `entropy` criterion and optimal number of trees (i.e. 8)

rf_grid_model = RandomForestClassifier(criterion = 'entropy', n_estimators = rf_model.best_params_.get('n_estimators'),
                                       random_state = 1)

# use fit() to fit the model on the train set
rf_grid_model = rf_grid_model.fit(X_train, y_train)

important_features = pd.DataFrame({'Features': X_train.columns, 
                                   'Importance': rf_grid_model.feature_importances_})

# print the dataframe
important_features

# #### Which is the best criterion to build a decision tree for the given dataset?
# 
# Consider the train and test set in Q1.
# 
# Let us use the GridSearchCV method to find the best criterion among the criteria `gini` and `entropy`.

tuned_paramaters = [{'criterion': ['gini', 'entropy']}]
 
decision_tree_classification = DecisionTreeClassifier(random_state = 1)

tree_grid = GridSearchCV(estimator = decision_tree_classification, param_grid = tuned_paramaters, cv = 5)

# fit the model on X_train and y_train using fit()
dt_grid = tree_grid.fit(X_train, y_train)

# get the best parameters
print('Best parameter for decision tree classifier: ', dt_grid.best_params_, '\n')

# #### Build a random forest containing ten trees and compute the precision and sensitivity of the model from the confusion matrix

# Practice

# #### 7. Find the optimal depth of the decision tree from the given list of values
# 
# Use the given list:
# 
# depth_values = [3, 5, 7, 9]
# 
# Consider the train and test set in Q1.
# 
# #### Practice

#### 8. Build and plot a decision tree with maximum 5 terminal nodes (use the entropy criterion)

#### 9. Build a random forest with entropy criterion such that each leaf node will contain at least three samples. Also calculate the f-1 score and accuracy of the model

#### 10. Plot a decision tree with the optimal criterion such that it will contain no more than 4 terminal nodes and each terminal node will contain at least 5 observations

# Practice code

# Practice code

# Practice code

# #### -------------- Ensemble Methods --------------------------- ####

# #### 1.Build a gradient boosting model on a training dataset.

gboost_model = GradientBoostingClassifier(n_estimators = 250, max_depth = 2, random_state = 1)

# fit the model using fit() on train data
gboost_model.fit(X_train, y_train)

y_pred = gboost_model.predict(X_test)

# create a confusion matrix
# pass the actual and predicted target values to the confusion_matrix()
cm = confusion_matrix(y_test, y_pred)

# identify each grid in the confusion matrix in terms of correct and wrong predictions 
# True Negatives are denoted by 'TN'
TN = cm[0,0]

# True Positives are denoted by 'TP'
TP = cm[1,1]

# False Positives are denoted by 'FP'
FP = cm[0,1]

# False Negatives are denoted by 'FN'
FN = cm[1,0]

#  #### 2.Create 80 stumps using AdaBoost and plot the ROC curve along with the AUC score

ada_model = AdaBoostClassifier(n_estimators = 80, random_state = 1)

# fit the model using fit() on train data
ada_model.fit(X_train, y_train)

#### Plot the ROC curve along with the AUC score.

y_pred_prob = ada_model.predict_proba(X_test)[:, 1]

# the roc_curve() returns the values for false positive rate, true positive rate and threshold
# pass the actual target values and predicted probabilities to the function
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# plot the ROC curve
plt.plot(fpr, tpr)

# set limits for x and y axes
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])

# plot the straight line showing worst prediction for the model
plt.plot([0, 1], [0, 1],'r--')

# add plot and axes labels
# set text size using 'fontsize'
plt.title('ROC curve for AdaBoost Classifier', fontsize = 15)
plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)

# add the AUC score to the plot
# 'x' and 'y' gives position of the text
# 's' is the text 
# use round() to round-off the AUC score upto 4 digits
plt.text(x = 0.07, y = 0.85, s = ('AUC Score:', round(roc_auc_score(y_test, y_pred_prob),4)))
                               
# plot the grid
plt.grid(True)

# #### 3.Select the optimal maximum depth from the given values for 180 base learners to build the gradient boosting classifier (consider 3-fold cross validation)
# 
# **Use the given list:**
# 
# depth = [2, 3, 4, 5, 6, 7, 8]
# 
# Consider the train and test set in Q5.

# given list of values for maximum depth
depth = [2, 3, 4, 5, 6, 7, 8]

# create a dictionary with hyperparameter and its values
# max_depth: pass the list 'depth' as the maximum tree depth for base learners
tuning_parameters = {'max_depth': depth}

# instantiate the 'GradientBoostingClassifier' 
# pass the 'random_state' to obtain the same results for each time you run the code
gb_model = GradientBoostingClassifier(n_estimators = 180, random_state = 1)

gb_grid = GridSearchCV(estimator = gb_model, param_grid = tuning_parameters, cv = 3)

# fit the model on X_train and y_train using fit()
gb_grid.fit(X_train, y_train)

# get the best parameters
print('Best maximum depth for gradient boost classifier:', gb_grid.best_params_, '\n')

# ### 4.Build the XGBoost model with a learning rate of 0.4 and gamma equal to 3. Calculate the accuracy by plotting the confusion matrix

xgb_model = XGBClassifier(learning_rate = 0.4, gamma = 3)

# fit the model using fit() on train data
xgb_model.fit(X_train, y_train)

y_pred = xgb_model.predict(X_test)

# create a confusion matrix
# pass the actual and predicted target values to the confusion_matrix()
cm = confusion_matrix(y_test, y_pred)

# label the confusion matrix  
# pass the matrix as 'data'
# pass the required column names to the parameter, 'columns'
# pass the required row names to the parameter, 'index'
conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])


# 'fmt = d' returns the integer value in each grid
# use 'ListedColormap' to assign the specified color to the grid
# 'cbar = False' will not return the color bar to the right side of the heatmap
# 'linewidths' assigns the width to the line that divides each grid
# 'annot_kws = {'size':25})' assigns the font size of the annotated text 
sns.heatmap(conf_matrix, annot = True, fmt = 'd', cbar = False, cmap = 'Greens')

# set the font size of x-axis ticks using 'fontsize'
plt.xticks(fontsize = 20)

# set the font size of y-axis ticks using 'fontsize'
plt.yticks(fontsize = 20)

# display the plot
plt.show()

# ### 5.Use the stacking technique on 70% of the data with the 9-NN and Naive Bayes model as base learners. Consider the Adaboost model as a final estimator. Also, compute the AUC score of the model
# 
# Since we are considering the KNN model as a base learner; it is necessary to scale the data before applying the stacking technique.

df_feature = df_seed.drop('Type', axis = 1)

# store the target variable 'Type' in a dataframe 'df_target'
df_target = df_seed['Type']

X_scaler = StandardScaler()

# consider the dataframe 'df_feature' to scale all the independent variables
num_scaled = X_scaler.fit_transform(df_feature)

# create a dataframe of scaled variables
# pass the required column names to the parameter 'columns'
df_feature_scaled = pd.DataFrame(num_scaled, columns = df_feature.columns)

X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(df_feature_scaled, df_target, 
                                                                                random_state = 1, test_size = 0.3)

# #### Build the stacking classifier using the KNN (with K = 9) and Naive Bayes model as base learners. Consider the Adaboost classifier as a final estimator. 

# consider the 9-NN and Naive Bayes algorithms as base learners
# pass the value of K to the parameter, 'n_neighbors'
base_learners = [('KNN_model', KNeighborsClassifier(n_neighbors = 9)),
                 ('NB_model', GaussianNB())]

# initialize stacking classifier 
# pass the base learners to the parameter, 'estimators'
# pass the AdaBoost model as the 'final_estimator'/ meta model
# pass the 'random_state' to obtain the same results for each time you run the code
stack_model_AdaBoost = StackingClassifier(estimators = base_learners, final_estimator = AdaBoostClassifier(random_state = 1))

# fit the model on train dataset
stack_model_AdaBoost.fit(X_train_scaled, y_train_scaled)

y_pred_prob = stack_model_AdaBoost.predict_proba(X_test_scaled)[:, 1]

# use 'roc_auc_score()' to calculate the AUC score 
print('AUC score for the model with AdaBoost as final estimator:', roc_auc_score(y_test_scaled, y_pred_prob))

# ### 6.Use the base learners in Q9 and build a stacking model with the XGBoost as final estimator. Compute the AUC score of the model and compare it with the result of Q9
# 
# #####  Build the stacking classifier using the KNN (with K = 9) and Naive bayes model as base learners. Consider the XGBoost classifier as final estimator. 

base_learners = [('KNN_model', KNeighborsClassifier(n_neighbors = 9)),
                 ('NB_model', GaussianNB())]

# initialize stacking classifier 
# pass the base learners to the parameter, 'estimators'
# pass the XGBoost model as the 'final_estimator'/ meta model
stack_model_XGBoost = StackingClassifier(estimators = base_learners, final_estimator = XGBClassifier())

# fit the model on train dataset
stack_model_XGBoost.fit(X_train_scaled, y_train_scaled)

y_pred_prob = stack_model_XGBoost.predict_proba(X_test_scaled)[:, 1]

# use 'roc_auc_score()' to calculate the AUC score 
print('AUC score for the model with XGBoost as final estimator:', roc_auc_score(y_test_scaled, y_pred_prob))
