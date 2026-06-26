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




