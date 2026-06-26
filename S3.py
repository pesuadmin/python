'''

SESSION 6 SUPPLEMENT — Stacking, Voting & Model Comparison (Practicals)
Topic 01 — Hard Voting vs Soft Voting
Hard Voting (formal definition, formula)
Soft Voting (formal definition, formula)
Weighted Voting
Compare Hard Voting vs Soft Voting vs Stacking (point-wise)
Why Soft Voting performed WORSE than Hard Voting in the lab
Topic 02 — Stacking — Deep Dive
Two-level architecture (L0 and L1)
Steps of the Stacking Architecture
Why StackingClassifier uses cross-validation (data leakage prevention)
Why Stacking beats individual models
What the meta-model should be
Topic 03 — Lab Dataset and Results (Stack.csv)
Dataset details (3000 rows, 25 features)
Complete results table (all 4 individual models + 3 ensemble methods)
RepeatedStratifiedKFold explanation
Topic 04 — Numerical Examples (4 examples)
Easy: Hard Voting
Easy: Soft Voting
Moderate: Weighted Soft Voting (showing how weights flip prediction)
Exam-Level: Stacking — meta-feature matrix creation (100×4 derivation)
Topic 05 — Common Exam Mistakes (6 mistakes)
Topic 06 — Viva & Exam Questions (7 Q&As)
Topic 08 — Quick Revision Summary

# SMLC Session 5 — Model Evaluation, Overfitting, Ensemble Learning & Random Forest

# TOPIC 01 — Model Evaluation: Training Error vs Generalization Error
## Q: What is Model Evaluation and why does it matter?
- After building a model, you need to answer: "How good is it really?"
- Analogy: Like taking a test after studying. Your training error is your practice exam score (you already saw these questions). Your generalization error is your real exam score (new, unseen questions).
- A good model does well on both — not just the practice set.

## Q: What is Training Error?
- Training Error = misclassifications the model makes on the training data it was built on.
- Also called: Resubstitution Error or Apparent Error.
- This is always optimistic (too low) because the model has already "seen" this data.
- Very low training error does NOT mean a good model — it might just mean the model memorized everything.

## Q: What is Generalization Error?
- Generalization Error = misclassifications the model makes on new, unseen test data.
- This is the real measure of model quality.
- The goal of all model building: make generalization error as small as possible.
- A big gap between training error and generalization error = the model has overfit.

## Q: What is the Train–Test Error Gap and why does it matter?
- Gap = Training Accuracy − Test Accuracy.
- Small gap (e.g., 4%) → model generalizes well — good!
- Large gap (e.g., 28%) → model is overfitting — bad!
- Example from faculty notebook: Full DT gives 100% train, 72% test → gap = 28% → severe overfitting. Pruned DT gives 88% train, 84% test → gap = 4% → much better generalization.

# TOPIC 02 — Confusion Matrix (Revision + Context)
## Q: What is a Confusion Matrix?
- A 2×2 scorecard comparing what the model predicted vs what actually happened.
- Analogy: Fire alarm system. TP = fire + alarm rings (good!). FP = no fire + alarm rings (annoying false alarm). FN = fire + no alarm (dangerous!). TN = no fire + no alarm (peaceful).
Layout:
|  | Actual Positive (1) | Actual Negative (0) |
|---|---|---|
| Predicted Positive (1) | True Positive (TP)  | False Positive (FP)  Type I |
| Predicted Negative (0) | False Negative (FN)  Type II | True Negative (TN)  |
- Diagonal (TP + TN) = correct predictions.
- Off-diagonal (FP + FN) = errors.
Mnemonic: "Diagonal = Da-right answer!"

## Q: What are all the key metrics derived from the confusion matrix?
Accuracy:
- = (TP + TN) / (TP + TN + FP + FN)
- Total correct predictions out of all predictions.

Precision:
- = TP / (TP + FP)
- "Of all predicted positives, how many were actually correct?"
- High Precision = few false alarms. Prioritize when FP is costly.
- Example: Spam filter — don't wrongly delete important emails.

Recall (Sensitivity / TPR):
- = TP / (TP + FN)
- "Of all actual positives, how many did we successfully catch?"
- High Recall = few missed cases. Prioritize when FN is dangerous.
- Example: Cancer screening — don't miss a sick patient.

Specificity (TNR):
- = TN / (TN + FP)
- "Of all actual negatives, how many did we correctly reject?"

False Positive Rate (FPR):
- = FP / (FP + TN) = 1 − Specificity
- Rate of wrongly flagging a negative as positive.
- Used on the X-axis of the ROC curve.

F1-Score:
- = 2 × (Precision × Recall) / (Precision + Recall)
- Harmonic mean of Precision and Recall. Balances both.
- Use when you need both to be high and neither can be terrible.

Mnemonic for Precision vs Recall:
- Precision = TP / (TP + FP) → P for Predicted column. "How accurate are my positive predictions?"
- Recall = TP / (TP + FN) → R for Real/Actual row. "How many real positives did I find?"

## Q: What is the ROC Curve and AUC?
- ROC Curve = plots TPR (Recall) on the Y-axis vs FPR on the X-axis at every possible classification threshold.
- A random classifier (coin flip) gives a diagonal line → AUC = 0.5.
- A perfect classifier hugs the top-left corner → AUC = 1.0.
- AUC (Area Under the Curve) = a single number summarizing overall model quality. Higher = better.

# TOPIC 03 — Cross Entropy
## Q: What is Cross Entropy?
- Cross Entropy is the loss function used for classification problems.
- It measures the divergence (difference) between the predicted probability distribution and the actual (true) distribution.
- Lower Cross Entropy = better predictions.
- It severely punishes confident wrong predictions.
Formula:
- H = −Σ y_actual(i) × ln(y_predicted(i))
  - y_actual(i) = actual class probability (0 or 1 in one-hot encoding).
  - y_predicted(i) = the model's predicted probability for that class.
  - ln = natural logarithm.
  - The minus sign makes the result positive (since ln of values < 1 is negative).
  - Sum over all class categories.
Binary case simplified:
- H = −[ y × ln(p) + (1−y) × ln(1−p) ]
  - If actual = 1: only the first term survives: H = −ln(p). Lower p = higher loss.
  - If actual = 0: only the second term survives: H = −ln(1−p). Higher p = higher loss.
Key intuition:
- Predicted [0.2, 0.8], actual = class 1: H = −ln(0.8) = 0.223 (good, low loss).
- Predicted [0.1, 0.9], actual = class 1: H = −ln(0.9) = 0.105 (even better).
- Predicted [0.5, 0.5], actual = class 1: H = −ln(0.5) = 0.693 (model is uncertain, high loss).

# TOPIC 04 — Overfitting, Underfitting & Pruning
## Q: What is Overfitting?
- Overfitting occurs when the model memorizes training data instead of learning patterns.
- Signs: very low training error, very high test error (large gap between them).
- The model fits noise and random fluctuations in training data, not the true signal.
- Analogy: A student who memorizes the textbook word-for-word scores 100% on practice tests but fails when questions are rephrased. They "over-studied" the training material.
Symptoms in a Decision Tree:
- Singleton leaf nodes (1 sample per leaf).
- Very long decision chains (deep tree).
- 100% training accuracy → almost always means overfitting.

## Q: What is Underfitting?
- Underfitting occurs when the model is too simple to capture the patterns in data.
- Signs: high training error AND high test error.
- The model has not learned enough from the data.
- Analogy: A student who barely studied fails both practice and real exams.

---
## Q: Compare Overfitting vs Underfitting (point-wise)
- Training Error: Overfitting = very low (near 0); Underfitting = high.
- Test Error: Both have high test error (different reasons).
- Bias: Overfitting = low bias; Underfitting = high bias.
- Variance: Overfitting = high variance; Underfitting = low variance.
- Model complexity: Overfitting = too complex (too many branches/features); Underfitting = too simple.
- Fix: Overfitting → pruning, regularization, more data, ensemble methods; Underfitting → more features, less regularization, more complex model.
---
## Q: What is Pruning?
- Pruning = removing branches of a decision tree that provide little or no predictive power.
- It reduces model complexity and improves generalization.
- Analogy: Like trimming a Bonsai tree. An untrimmed tree grows wild and messy (overfits). Pruning keeps it healthy and well-shaped.
## Q: What is Pre-Pruning?
- Pre-Pruning = stopping the tree from growing too much in the first place.
- Done by setting hyperparameters before training.
- Analogy: You put a wire frame on the Bonsai while it is still growing — setting limits beforehand.
Key pre-pruning hyperparameters:
- max_depth: Maximum levels/depth the tree can have. Increasing this → simpler tree → less overfitting.
- min_samples_split: Minimum number of samples required to split a node. Higher value → fewer splits → simpler tree.
- min_samples_leaf: Minimum samples required in a leaf node. Higher value → bigger leaves → smoother predictions → less overfitting.
- max_leaf_nodes: Maximum number of leaf nodes allowed. Fewer leaves → simpler tree.
- max_features: Maximum features considered at each split. Fewer features → more randomness → less overfitting.
Mnemonic: "Max-Min-Max-Min-Max" → max_depth, min_samples_split, max_leaf_nodes, min_samples_leaf, max_features. Alternates between max and min! All limit tree complexity.

## Q: What is Post-Pruning?
- Post-Pruning = grow the tree fully first, then cut back unnecessary branches.
- Done after training is complete.
- Analogy: You let the Bonsai grow fully, then carefully clip unnecessary branches.
- Risk: Computationally expensive.
- In sklearn: use the `ccp_alpha` parameter (cost-complexity pruning).

## Q: Compare Pre-Pruning vs Post-Pruning (point-wise)
- When: Pre-Pruning = during tree growth; Post-Pruning = after fully grown.
- How: Pre-Pruning = set hyperparameters (max_depth etc.); Post-Pruning = remove branches that don't improve validation.
- Risk: Pre-Pruning may stop too early (may miss good splits); Post-Pruning is computationally expensive.
- Sklearn support: Pre-Pruning directly supported via hyperparameters; Post-Pruning uses `ccp_alpha` parameter.

# TOPIC 05 — Ensemble Learning
## Q: What is Ensemble Learning?
- Ensemble Learning = combining multiple weak models to make one strong model.
- Analogy: One cricket pundit might predict the winner incorrectly. But a panel of 10 experts voting together is much more accurate. Each expert has different knowledge. The group decision is stronger than any individual.
- Weak learner = a model that is only slightly better than random guessing.
- The combination of many weak learners creates a powerful classifier.
---
## Q: What are the three types of Ensemble Learning?
Bagging (Bootstrap Aggregation):
- Build multiple models independently in parallel, each on a different bootstrap sample.
- Aggregate predictions by majority vote (classification) or average (regression).
- All base models use the same algorithm (homogeneous).
- Reduces variance (not bias).
- Example: Random Forest.
- Data: Bootstrap sampling WITH replacement.
Boosting:
- Build models sequentially — each new model focuses on the errors of the previous one.
- All base models use the same algorithm (homogeneous).
- Reduces bias (not primarily variance).
- Can overfit if too many iterations are used.
- Examples: AdaBoost, XGBoost, GBM (Gradient Boosting Machines).
- Data: Re-weighted samples (difficult/wrongly classified samples get more weight).
Stacking:
- Build different types of base models (heterogeneous — different algorithms).
- Use the outputs of base models as inputs to a meta-model (also called a blender or second-level learner).
- The meta-model learns which base models to trust more.
- Examples: Voting Classifier.
- Data: Full data to base models; meta-model learns from base model predictions.
Mnemonic: BBS
- Bagging = Bootstrap + Build independently + Aggregate → Random Forest.
- Boosting = Build sequentially + Focus on errors → AdaBoost, XGBoost.
- Stacking = Stack different models + Meta-learner → Voting Classifier.

## Q: Compare Bagging vs Boosting vs Stacking (point-wise)
- Model type: Bagging = homogeneous (same algo); Boosting = homogeneous; Stacking = heterogeneous (different algos).
- Training: Bagging = parallel and independent; Boosting = sequential and dependent; Stacking = parallel base → sequential meta.
- Focus: Bagging = reduce variance; Boosting = reduce bias; Stacking = combine strengths of different models.
- Data sampling: Bagging = bootstrap with replacement; Boosting = re-weighted samples; Stacking = full data to base models.
- Aggregation: Bagging = majority vote / average; Boosting = weighted vote; Stacking = meta-model decides.
- Overfitting risk: Bagging = less prone; Boosting = can overfit with too many iterations; Stacking = depends on meta-model.
- Examples: Bagging → Random Forest; Boosting → AdaBoost, XGBoost; Stacking → Voting Classifier.

# TOPIC 06 — Bootstrap Sampling
## Q: What is Bootstrap Sampling?
- From your original dataset of N samples, pick N samples with replacement.
- "With replacement" means: you pick a sample, note it, put it back, then pick again.
- This creates a new dataset of the same size (N) as the original, but:
  - Some samples appear multiple times (duplicated).
  - Some samples are never picked at all.
- Analogy: Picking chocolates from a bag with replacement. You might pick some chocolates twice and never pick others.

## Q: What is the Out-of-Bag (OOB) probability? How is it derived?
- OOB samples = the original samples that were never selected in the bootstrap sample.
- These act as a free validation set for each tree — no extra data split needed!

Derivation:
- Probability a specific sample is NOT picked in one draw = 1 − 1/N.
- Probability it is NOT picked in ANY of the N draws = (1 − 1/N)^N.
- For large N: lim(1 − 1/N)^N as N → ∞ = 1/e ≈ 0.368.

Formula:
- P(OOB) = (1 − 1/N)^N ≈ 1/e ≈ 0.368

Key numbers:
- ~36.8% of data is OOB (left out of each bootstrap sample).
- ~63.2% of data is in each bootstrap sample (unique samples; some may be duplicated within).
- Mnemonic: "One-third Out of the Bag" — roughly 1/3 out, 2/3 in.

# TOPIC 07 — Random Forest
## Q: What is a Random Forest?
- An ensemble of many decision trees, each built on a different bootstrap sample of the data.
- Each tree also uses a random subset of features at each split — not all features.
- This randomness prevents all trees from looking the same and introduces diversity.
- Final prediction: majority vote (classification) or mean (regression).
- "Random" = each tree sees random data AND random features.
- "Forest" = many trees together.
- Analogy: Give each student a random subset of chapters. Each studies independently and gives their answer. The majority answer is usually correct.

## Q: How does Random Forest work step by step?
Step 1 — Bootstrap: Draw N bootstrap samples from the training data (with replacement). Each sample creates a different training set for one tree.
Step 2 — Random Feature Selection: At each node split in every tree, consider only a random subset of features (default = √p for classification, where p = total features).
Step 3 — Build each tree: Grow each tree independently to full depth (or with pruning constraints). Each tree trains only on its own bootstrap sample with its own random features.
Step 4 — Aggregate: For a new test sample, pass it through all trees.
- Classification: Each tree votes for a class → take the mode (majority vote).
- Regression: Each tree predicts a number → take the mean (average).
Mnemonic: BARF → Bootstrap, Aggregate, Random Features.
- Bootstrap the data.
- Build trees with Random Features.
- Aggregate by voting/averaging.

## Q: How does Random Forest reduce overfitting compared to a single Decision Tree?
- Bootstrap sampling: Each tree trains on a different subset, so no single tree memorizes all data.
- Random feature selection: Each split considers only √p features (not all features), introducing diversity among trees.
- Aggregation (voting): Individual errors from each tree tend to cancel out when many trees vote together.
- Combined effect: variance is reduced while bias stays low.
- A single decision tree has high variance — a small change in training data can create a very different tree. Many trees averaging together smooth this out.

## Q: Compare Decision Tree vs Random Forest (point-wise)
- Structure: DT = single tree; RF = ensemble of many trees.
- Overfitting: DT = very prone; RF = much less prone (diversity helps).
- Variance: DT = high; RF = low (averaging/voting reduces variance).
- Interpretability: DT = easy to visualize and explain; RF = black-box, hard to interpret.
- Speed: DT = fast to train; RF = slower (must build many trees).
- Accuracy: DT = lower (single perspective); RF = higher (many diverse perspectives).
- Features at each split: DT = all features; RF = random subset (default √p).
- Feature importance: DT = limited; RF = can compute Gini importance or permutation importance across all trees.

# TOPIC 08 — Feature Importance
## Q: What is Feature Importance?
- A score assigned to each feature based on its contribution to the predictions.
- Higher score = more important feature.
- Helps answer: "Which features matter most for this prediction?"
- In the faculty notebook (Graduate Admissions dataset): CGPA was the most important feature for admission prediction.

## Q: What are the two types of Feature Importance in Random Forests?
1. Gini Importance (Mean Decrease Impurity):
- Measures the average total decrease in Gini impurity across all trees, weighted by the proportion of samples reaching that node.
- Accessed in sklearn via: `model.feature_importances_`
- Fast to compute (already calculated during training).
- Weakness: biased toward high-cardinality features (features with many unique values tend to get higher importance scores even if they are not truly important).
2. Permutation Importance (Mean Decrease in Accuracy):
- Randomly shuffle one feature's values in the OOB data.
- Measure how much the model's accuracy drops.
- Big accuracy drop → the feature is very important (the model relies on it).
- Small accuracy drop → the feature is unimportant (shuffling it doesn't hurt much).
- More reliable than Gini importance.
- Weakness: slower to compute (must re-evaluate model for each feature).
## Q: Compare Gini Importance vs Permutation Importance (point-wise)
- Computes: Gini = mean decrease in impurity during training; Permutation = accuracy drop after shuffling feature values.
- When calculated: Gini = during training (free); Permutation = after training (extra computation needed).
- Bias: Gini is biased toward high-cardinality features; Permutation is not biased this way.
- Reliability: Permutation importance is more reliable and trustworthy.
- Speed: Gini is fast; Permutation is slow.
- Sklearn access: Gini = `model.feature_importances_`; Permutation = `sklearn.inspection.permutation_importance`.
---

# TOPIC 09 — Random Forest Hyperparameters
## Q: What are the key hyperparameters for Random Forest (sklearn)?
- n_estimators: Number of decision trees in the forest. Default = 100. More trees = better (up to a point), then marginal gains, but more computation.
- max_depth: Maximum depth of each tree. Default = None (unlimited). Limit to reduce overfitting.
- min_samples_split: Minimum samples needed to split a node. Default = 2.
- min_samples_leaf: Minimum samples required at a leaf node. Default = 1.
- max_leaf_nodes: Maximum number of terminal nodes per tree. Default = None.
- max_features: Maximum features at each split. Default = 'sqrt' for classification (uses √p features). Options: 'sqrt', 'log2', None, integer.
- max_samples: Number of bootstrap samples drawn. Default = same as dataset size (N).
- oob_score: Whether to use OOB samples for validation. Default = False. Set to True to get a free validation score.
---

# TOPIC 10 — Numerical Examples
## Example 01 — EASY: Compute All Metrics from Confusion Matrix
Problem: TP = 50, FP = 10, FN = 5, TN = 35. Total = 100.
Accuracy:
- = (50 + 35) / 100 = 85/100 = 0.85 (85%)
Precision:
- = 50 / (50 + 10) = 50/60 = 0.833 (83.3%)
Recall (Sensitivity):
- = 50 / (50 + 5) = 50/55 = 0.909 (90.9%)
F1-Score:
- = 2 × (0.833 × 0.909) / (0.833 + 0.909)
- = 2 × 0.757 / 1.742 = 0.869 (86.9%)
Specificity:
- = 35 / (35 + 10) = 35/45 = 0.778 (77.8%)
FPR:
- = 1 − Specificity = 1 − 0.778 = 0.222 (22.2%)
Interpretation: High recall (catches 90.9% of actual positives), good precision (83.3% correct positive calls), balanced F1 = 0.869.
---
## Example 02 — EASY: Cross Entropy Calculation
Problem: Actual class = 1 (one-hot: [0, 1]). Model predicts probabilities [0.2, 0.8].
Apply formula H = −Σ y_actual(i) × ln(y_predicted(i)):
- H = −[0 × ln(0.2) + 1 × ln(0.8)]
- H = −[0 + (−0.2231)]
- H = 0.223
What-if comparisons:
- If predicted [0.1, 0.9]: H = −ln(0.9) = 0.105 (lower = better, model is more confident and correct).
- If predicted [0.5, 0.5]: H = −ln(0.5) = 0.693 (higher = worse, model is uncertain).
Key rule: Cross entropy decreases as prediction probability approaches the correct answer.

## Example 03 — MODERATE: OOB Sample Probability
Problem: Dataset has 1000 samples. Bootstrap sample of size 1000 is drawn with replacement. What fraction is expected to be OOB?
Step 1: Probability a specific sample is NOT picked in one draw:
Step 2: Probability it is not picked in any of 1000 draws:
- = (0.999)^1000
Step 3: For large N, (1 − 1/N)^N → 1/e ≈ 0.368
Answer: About 36.8% (368 samples) are OOB. About 63.2% (632 unique samples) are in the bootstrap sample.

## Example 04 — EXAM-LEVEL: Random Forest Majority Voting
Problem: A 5-tree Random Forest predicts for a new sample: [Approved, Rejected, Approved, Approved, Rejected].
Step 1 — Count votes:
Step 2 — Take Mode:
- Mode = Approved (3 > 2).
Final Prediction: Approved (majority vote wins).
Regression version: If trees predicted [5.2, 4.8, 5.0, 5.5, 4.9], final prediction = (5.2+4.8+5.0+5.5+4.9)/5 = 5.08 (take mean, not mode).

---
## Example 05 — EXAM-LEVEL: Detecting Overfitting & Effect of Pruning
Problem: Full DT: Train Accuracy = 100%, Test Accuracy = 72%. Pruned DT (max_depth=5, min_samples_split=4): Train = 88%, Test = 84%.
Full tree analysis:
- Gap = 100% − 72% = 28% → Huge gap → severe overfitting.
- The tree memorized training data including noise.
Pruned tree analysis:
- Gap = 88% − 84% = 4% → Small gap → model generalizes well.
- Test accuracy jumped from 72% → 84% after pruning.
Conclusion:
- Pre-pruning (max_depth=5, min_samples_split=4) reduced overfitting and improved generalization.
- The slight drop in training accuracy (100% → 88%) is acceptable and desirable — it means the model learned patterns, not noise.
- A model that scores 100% on training and 84% on test is far better than one that scores 100% on training and 72% on test.

# TOPIC 11 — Common Exam Mistakes
## Mistake 1: Confusing Precision and Recall.
- Wrong: Swapping the denominators.
- Fix: Precision = TP/(TP+FP) — "P for Predicted column — how accurate are my positive predictions?" Recall = TP/(TP+FN) — "R for Real/Actual row — how many real positives did I find?"

## Mistake 2: Thinking 100% training accuracy is good.
- Correct: 100% training accuracy almost always means overfitting.
- Fix: Always check the gap between train and test accuracy. A big gap is the real problem.

## Mistake 3: Confusing FPR (rate) with FP (count).
- FPR is a rate = FP / (FP + TN).
- The ROC curve uses the rate (FPR), not the raw count (FP).
---
## Mistake 4: Saying "Random Forest uses all features at each split."
- Correct: Random Forest uses a random subset of features at each split.
- This is the key "randomness" that makes RF different from a simple ensemble of identical trees.
---
## Mistake 5: Mixing up Bagging and Boosting.
- Boosting = sequential + each model corrects the previous → reduces bias.
- Memory trick: "Bagging = Band of equals. Boosting = Building on mistakes."
---
## Mistake 6: Forgetting that bootstrap samples WITH REPLACEMENT.
- That is why some samples appear multiple times AND ~36.8% are left out (OOB).
- Without replacement → all samples used once → no OOB → not bootstrap.
---
## Mistake 7: Thinking more trees in RF always means better performance.
- After ~100–200 trees, additional trees give marginal accuracy improvement.
- But more trees = more computation time and memory.
---
## Mistake 8: Using only Gini importance for feature selection.
- A feature like "Student ID" could get high Gini importance even though it is useless.
- Fix: Cross-check with permutation importance for a more reliable view.
---
## Mistake 9: Using Cross Entropy for regression.
- For regression (predicting a continuous number), use MSE (Mean Squared Error) or MAE (Mean Absolute Error).
---
## Mistake 10: Setting hyperparameters by guessing.
- Correct: Use GridSearchCV to systematically try all combinations of hyperparameters with cross-validation, then pick the best combination.
---
# TOPIC 12 — Viva & Exam Questions
## Q1 (Easy): What is overfitting in a decision tree?
- Overfitting occurs when the tree uses all training data to create a perfect fit.
- Results in very low training error but high test error.
- Signs: singleton leaf nodes (1 sample per leaf), very long decision chains, 100% training accuracy.
- The tree memorizes noise instead of learning real patterns.

## Q2 (Easy): What is the difference between Bagging and Boosting?
- Bagging: Builds models independently in parallel on bootstrap samples. Aggregates by voting or averaging. Reduces variance. Example: Random Forest.
- Boosting: Builds models sequentially. Each new model focuses on errors of the previous one. Reduces bias. Example: AdaBoost, XGBoost.

## Q3 (Easy): Why is ~36.8% of data expected to be out-of-bag?
- In bootstrap sampling of N draws from N samples (with replacement), probability of NOT being picked in one draw = (1 − 1/N).
- Probability of not being picked in any of N draws = (1 − 1/N)^N.
- For large N, this converges to 1/e ≈ 0.368.
- So ~36.8% of samples are never selected in any given bootstrap sample.

## Q4 (Medium): How does Random Forest reduce overfitting compared to a single Decision Tree?
Three mechanisms work together:
- Bootstrap sampling: Each tree trains on a different subset, so no single tree memorizes all data.
- Random feature selection: Each split considers only √p features (not all), introducing diversity among trees.
- Aggregation: Individual tree errors cancel out through majority voting.
- Combined result: variance is reduced while bias stays low — the hallmark of a well-generalizing model.

## Q5 (Medium): When would you prioritize Recall over Precision?
- When missing a positive case (FN) is very costly.
- Examples: Cancer screening (missing a cancer patient is life-threatening), fraud detection (missing a fraudulent transaction is costly), earthquake warning systems.
- In these cases, you accept more false alarms (lower precision) rather than miss real positives.

## Q6 (Medium): Explain the ROC curve and AUC.
- ROC curve plots TPR (recall) on Y-axis vs FPR on X-axis at every possible classification threshold.
- A random classifier gives a diagonal line → AUC = 0.5.
- A perfect classifier hugs the top-left corner → AUC = 1.0.
- AUC = Area Under the Curve = single summary of model quality across all thresholds.
- Higher AUC = better the model is at discriminating between classes.


- A RF with n_estimators=1 and max_features=all features is trained on a bootstrap sample, not the full dataset.
- It sees ~63.2% of the data (with duplicates).
- A normal DT is trained on 100% of the data.
- So it is slightly different: the bootstrap sampling introduces randomness even without feature randomness.
- To make RF truly equivalent to a plain DT: remove both bagging (use full data) AND feature randomness (use all features).

## Q8 (Tricky Viva): Can a Random Forest overfit? If so, how?
- Yes, though it is much harder to overfit than a single decision tree.
- A RF can overfit when:
  - Individual trees are very deep with no pruning constraints.
  - Too few trees (variance not averaged out enough).
  - The dataset is very small.
- Remedies: set max_depth, increase n_estimators, use min_samples_leaf, reduce max_features further.

# TOPIC 13 — Real-Life Analogies
- Confusion Matrix: Fire alarm system. TP = fire + alarm rings (good). FP = no fire + alarm rings (annoying). FN = fire + no alarm (dangerous). TN = no fire + no alarm (peaceful). In healthcare, FN is worst. In spam, FP is worst.
- Overfitting: A student who memorizes the textbook word-for-word scores 100% on practice but fails when questions are rephrased. They over-studied the training material.
- Pruning: Like trimming a Bonsai tree. Pre-pruning = wire frame while growing. Post-pruning = clip after full growth.
- Ensemble Learning: An IPL expert panel. One pundit might predict wrong. A panel of 10 experts voting together is much more accurate.
- Random Forest: Group study with random topics. Give each student a random subset of chapters. Each studies independently. The majority answer is usually correct.
- Bootstrap Sampling: Picking chocolates from a bag with replacement. You pick one, put it back, pick again. Some chocolates get picked twice, some never — those are OOB.
---
# TOPIC 14 — Quick Revision Summary
## All Key Formulas
- Accuracy: (TP+TN) / Total
- Precision: TP / (TP+FP)
- Recall (Sensitivity/TPR): TP / (TP+FN)
- Specificity (TNR): TN / (TN+FP)
- FPR: FP / (FP+TN) = 1 − Specificity
- F1-Score: 2 × (P × R) / (P + R)
- Cross Entropy: −Σ y_actual(i) × ln(y_predicted(i))
- OOB Probability: (1 − 1/N)^N ≈ 1/e ≈ 0.368
## All Mnemonics
- Confusion Matrix diagonal: "Diagonal = Da-right answer!" TP (top-left), FP (top-right), FN (bottom-left), TN (bottom-right).
- Precision vs Recall: P → Predicted column (TP+FP); R → Real/Actual row (TP+FN).
- Ensemble BBS: Bagging = Bootstrap+Build independently; Boosting = Build sequentially; Stacking = Stack different models.
- OOB: "One-third Out of the Bag" — ~36.8% ≈ 1/3 out, ~63.2% ≈ 2/3 in.
- Random Forest: BARF → Bootstrap, Aggregate, Random Features.
- Pruning parameters: "Max-Min-Max-Min-Max" → max_depth, min_samples_split, max_leaf_nodes, min_samples_leaf, max_features.
- Overfit vs Underfit: "Over-study vs Under-study."

## Key Facts to Memorise

- Training Error = apparent error. Generalization Error = test error (the real one).
- Large (Train − Test) gap = overfitting.
- Confusion matrix diagonal = correct. Off-diagonal = errors.
- FPR = 1 − Specificity (NOT 1 − Recall!).
- Cross Entropy = loss function for classification only. Lower = better.
- Overfitting: low train error + high test error. Underfitting: high train + high test.
- Pruning reduces overfitting by limiting tree growth.
- Pre-Pruning = set hyperparameters before growing. Post-Pruning = cut after full growth.
- Ensemble = combining weak learners into a strong model.
- Bagging = parallel, same algo, reduces variance. Example: Random Forest.
- Boosting = sequential, same algo, reduces bias. Examples: AdaBoost, XGBoost.
- Stacking = different algos + meta-model. Example: Voting Classifier.
- Bootstrap = sampling WITH replacement. ~63.2% unique in sample, ~36.8% OOB.
- OOB ≈ 1/e ≈ 0.368. This is a formula to memorize.
- Random Forest = bagging + random feature selection at each split.
- RF default max_features for classification = √p (square root of total features).
- RF default n_estimators = 100.
- RF aggregates by majority vote (classification) or mean (regression).
- Feature importance: Gini importance via `model.feature_importances_`. Permutation importance = shuffle feature → measure accuracy drop.
- Gini importance is biased toward high-cardinality features. Permutation is more reliable.
- Faculty notebook: CGPA was the most important feature for Graduate Admissions prediction.
- More trees in RF = better up to ~100–200; then gains plateau.
- RF can overfit, but it is much harder than a single DT.

*SMLC Session 5 | PES University MTech | Model Evaluation, Overfitting, Ensemble Learning & Random Forest*
"""

# =============================================================================
# SESSION 6 — Boosting, XGBoost, Stacking & Voting
# =============================================================================
SESSION_6 = """
# SMLC Session 6 — Boosting, XGBoost, Stacking & Voting
## Detailed Study Notes | PES University MTech

# TOPIC 01 — What is Boosting?
## Q: What is Boosting in simple words?
- Imagine a relay race where each runner learns from the previous runner's mistakes.
- Runner 1 drops the baton at turns. Runner 2 practises turns extra hard. Runner 3 fixes what Runner 2 still got wrong.
- By the end, the team is amazing — even though each individual runner was average.
- That is Boosting: sequential learning from mistakes.

## Q: What is the formal definition of Boosting?
- Boosting is an Ensemble method where weak learners are built sequentially.
- Each new model focuses on correcting the errors of the previous model.
- Reduces both bias (systematic error) and variance.
- All base models are homogeneous — they use the same algorithm (same type of weak learner).
- The three main boosting algorithms are: AdaBoost → Gradient Boosting (GBM) → XGBoost.
- Each one improves on the previous.
- Mnemonic: AGX → AdaBoost → GBM → XGBoost. Each is better than the last!

# TOPIC 02 — AdaBoost (Adaptive Boosting)
## Q: What is AdaBoost in simple words?
- AdaBoost builds a forest of stumps (tiny trees with just 1 split).
- After each stump, it asks: "Which data points did I get wrong?"
- Those wrong ones get more weight (more attention) in the next round.
- Stumps that performed well get a bigger say in the final vote.
- Analogy: Like a tuition teacher who gives extra homework on topics you got wrong. After each test, harder practice problems focus on your weak areas.


- It makes a decision based on a single feature.
- It is the simplest possible tree — the weakest learner you can build.
- AdaBoost uses stumps as weak learners, not full trees.
- GBM and XGBoost use deeper trees (not stumps).

## Q: What is Total Error in AdaBoost?
- Total Error = the sum of weights of all misclassified samples in the current round.
- Initially, all samples have equal weight = 1/N (N = total samples).
- If a stump misclassifies heavy (high-weight) samples, its Total Error is large.
- If it misclassifies light (low-weight) samples, Total Error is small.
- Range: 0 (perfect stump) to 0.5 (random guessing for balanced data).

## Q: What is Amount of Say in AdaBoost?
- Amount of Say = the voting power given to a stump based on how well it performed.
- A stump with low error (performed well) gets a high Amount of Say.
- A stump with high error (performed badly) gets a low or negative Amount of Say.
Formula:
- Amount of Say = ½ × ln( (1 − ε) / ε )
  - ε = Total Error.
  - ln = natural logarithm.
  - ½ = scaling factor.
  - When ε is small (stump is good) → (1−ε)/ε is large → ln is large → Amount of Say is large.
  - When ε = 0.5 (random guessing) → ln(1) = 0 → Amount of Say = 0 (no voting power).
  - When ε approaches 0 → Amount of Say → +∞ (perfect stump gets maximum power).

## Q: What are the complete steps of the AdaBoost algorithm?
Mnemonic: SWAN → Stump → Weigh → Adjust → Normalize
Step 1: Assign equal weight to all samples: w = 1/N.
Step 2: Build a stump for each feature. Pick the stump with the lowest Gini Index as the best stump for this round.
Step 3: Calculate Total Error = sum of weights of misclassified samples.
Step 4: Calculate Amount of Say = ½ × ln((1 − ε) / ε).
Step 5: Update sample weights:
- Misclassified samples: w_new = w_old × e^(+Amount of Say) → weight increases (more attention next round).
- Correctly classified samples: w_new = w_old × e^(−Amount of Say) → weight decreases (less attention next round).
Step 6: Normalize all weights so they sum to 1.
Step 7: Create a new dataset by weighted random sampling. Misclassified samples now appear in larger intervals so they are more likely to be selected repeatedly.
Step 8: Repeat Steps 2–7 for the specified number of estimators (stumps).
Step 9: Final prediction = weighted vote using each stump's Amount of Say as the voting weight.

## Q: What are the weight update formulas for AdaBoost?
For WRONG (misclassified) samples:
- w_new = w_old × e^(+Amount of Say)
  - The positive exponent means weight increases.
  - e^(positive number) > 1 → multiplied by something > 1 → weight goes up.
For CORRECT (correctly classified) samples:
- w_new = w_old × e^(−Amount of Say)
  - The negative exponent means weight decreases.
  - e^(negative number) < 1 → multiplied by something < 1 → weight goes down.

Important: After updating, normalize all weights so they sum to 1. Otherwise the sampling distribution is invalid.

## Q: What happens when Total Error = 0.5 or 0 in AdaBoost?
- ε = 0.5: Amount of Say = ½ × ln(0.5/0.5) = ½ × ln(1) = 0. The stump is no better than random guessing → it gets zero voting weight → completely ignored.
- ε = 0: Amount of Say = ½ × ln(1/0) = ½ × ln(∞) = +∞. A perfect stump gets infinite voting power. In practice, boosting stops here since the model is already perfect.

# TOPIC 03 — Gradient Boosting (GBM)
## Q: What is Gradient Boosting in simple words?
- GBM starts with a simple prediction (like the average or log-odds), then builds a small tree to predict the residuals (errors of the current prediction).
- The next tree predicts the residuals of the residuals.
- Each tree takes a small step in the right direction, controlled by a learning rate.
- Analogy: Archery practice. First arrow lands far. Coach says "adjust 10% to the right." Second arrow is closer. Coach: "adjust 10% up." After many small corrections, you hit the bullseye. Each correction = learning_rate × residual.

## Q: What is a Residual?
- Residual = Actual value − Predicted value.
- It represents the error that the current model makes on each sample.
- GBM and XGBoost fit each new tree to the residuals of the previous prediction.
- The tree "learns to correct the mistake."

## Q: What is the Learning Rate (η)?
- Learning Rate (also written ε or η, pronounced "eta") = a shrinkage factor that scales each tree's contribution.
- It controls how much each new tree's prediction moves the overall model.
Effect:
- Small η (e.g., 0.01–0.1): each tree contributes little → need MORE trees → better generalization → less overfitting.
- Large η (e.g., 1.0): each tree contributes fully → need FEWER trees → risk of overfitting.
- It is a bias-variance tradeoff: smaller rate = less overfitting but more computation.
Defaults:
- GBM default learning rate = 0.1.
- XGBoost default learning rate = 0.3.

## Q: What are the complete steps of Gradient Boosting?
Mnemonic: PRATS → Predict → Residuals → Add Tree → Scale → Total (repeat)
Step 1: Start with an initial leaf = most common class (classification) or mean (regression). For binary classification, initial prediction = log(odds) of the positive class.
Step 2: Calculate residuals = Actual − Predicted probability for each sample.
Step 3: Build a tree (typically 8–32 leaves) to fit these residuals as target values.
Step 4: Calculate Output value for each leaf:
- Output = Σ residuals / Σ [prev_prob × (1 − prev_prob)]
  - Σ residuals = sum of all residuals in that leaf.
  - Σ [p × (1−p)] = sum of prev_prob × (1 − prev_prob) for all samples in that leaf (this is the Hessian of log-loss).
Step 5: Calculate new prediction:
- new log(odds) = prev log(odds) + learning_rate × Output
  - The learning rate scales down the tree's contribution.
Step 6: Convert log(odds) to probability:
- p = e^(log_odds) / (1 + e^(log_odds))
  - This is the sigmoid/logistic transformation.
Step 7: Compute new residuals. Repeat Steps 3–6 until max trees reached or residuals become tiny.

# TOPIC 04 — XGBoost (eXtreme Gradient Boosting)
## Q: What is XGBoost in simple words?
- XGBoost = "eXtreme Gradient Boosting."
- It is GBM with important additions: regularization (λ, γ) to prevent overfitting, a special Similarity Score to decide splits, and the ability to parallelize computations.
- Analogy: GBM is archery practice. XGBoost adds safety rules: γ (gamma) = "don't bother adjusting if the improvement is tiny" (pruning). λ (lambda) = "don't over-correct based on one weird arrow" (regularization). Result: learn faster AND more reliably.

## Q: What is the Similarity Score in XGBoost?
- Similarity Score measures how "pure" a group of residuals is at a node.
- Higher Similarity = the residuals in that node are more uniform (better split).
Formula:
- Similarity = (Σ residuals)² / (Σ [p_prev × (1 − p_prev)] + λ)
  - Σ residuals = sum of residuals of all samples in that node.
  - Σ [p × (1−p)] = sum of p_prev × (1−p_prev) for all samples (the Hessian of log-loss).
  - λ = L2 regularization parameter (default = 1).
  - Squaring the numerator makes it always positive and sensitive to the magnitude.
  - Adding λ to the denominator reduces Similarity → makes pruning easier.
---
## Q: What is Gain in XGBoost?
- Gain measures the improvement achieved by making a split.
- XGBoost picks the split (threshold) that maximizes Gain.
Formula:
- Gain = Similarity_left + Similarity_right − Similarity_parent
  - Similarity_left = Similarity Score of the left child node.
  - Similarity_right = Similarity Score of the right child node.
  - Similarity_parent = Similarity Score of the parent node before the split.
  - If Gain > 0, the split improves purity → consider keeping it.
  - If Gain ≤ 0, the split does not help.

- γ (gamma) = minimum loss reduction required for a split to be kept.
- It is a tree complexity / pruning parameter.
- Acts like a threshold that a split's Gain must exceed before the branch is kept.
Pruning rule:
- If (Gain − γ) < 0 → prune that branch (remove it).
- If (Gain − γ) ≥ 0 → keep the branch.
- Higher γ → stricter requirement → more branches pruned → simpler tree → less overfitting.
- Default γ = 0 (no pruning by default).
Mnemonic: "γ Guillotines" → gamma chops branches if the gain is too small.

## Q: What is lambda (λ) in XGBoost?
- λ (lambda) = L2 regularization on the leaf weights.
- It is added to the denominator of both the Similarity Score and the Output formula.
- Effect: reduces Similarity Scores → reduces Gain → makes pruning easier → reduces sensitivity to individual observations.
- Without λ (λ=0): Output = Σ residuals / Σ [p(1−p)].
- With λ=1: Output = Σ residuals / (Σ [p(1−p)] + 1) → output is smaller (more conservative).

Example (from exam):
- Left leaf residual = −0.5, p_prev = 0.5.
- λ=0: Output = −0.5 / (0.5×0.5) = −0.5/0.25 = −2.0.
- λ=1: Output = −0.5 / (0.25 + 1) = −0.5/1.25 = −0.4.
- Lambda shrank the output from −2.0 to −0.4 → more conservative, less overfitting.
Mnemonic: "λ Loosens" → lambda loosens/shrinks the output, making predictions more conservative.
---
## Q: What is Cover in XGBoost?
- Cover = the denominator of the Similarity Score without λ.
- Cover = Σ [p_prev × (1 − p_prev)] for all samples in a leaf.
- It represents the "minimum number of observations" that a leaf should have.
- XGBoost checks that each leaf's Cover ≥ min_child_weight (default = 1).
- If a leaf's Cover < min_child_weight, that leaf is removed.
- Purpose: prevents leaves with very few samples (which would be noise-fitting).

## Q: What are the complete steps of XGBoost?
Step 2: Calculate residuals = Observed − Predicted.
Step 3: Build a tree using Similarity Score to decide splits:
- Pick the threshold with maximum Gain.
Step 3.5: Continue splitting recursively.
Step 3.6: Cover check — for each leaf, ensure Cover ≥ min_child_weight. Remove leaves that fail this check.
Step 3.7: Gamma pruning — for each branch, if (Gain − γ) < 0 → prune that branch.
Step 3.8: Calculate Output for each remaining leaf:
- Output = Σ residuals / (Σ [p×(1−p)] + λ)
Step 4: Calculate new prediction:
- new log(odds) = prev log(odds) + η × Output

Step 5: Compute new residuals. Repeat until max trees reached or convergence.
---
## Q: What are the key XGBoost hyperparameters?
- n_estimators: Number of boosting rounds (trees). Default = 100.
- learning_rate (η): Shrinkage factor for each tree's output. Default = 0.3.
- max_depth: Maximum depth of each tree. Default = 6.
- gamma (γ): Minimum loss reduction for a split. Higher = more pruning. Default = 0.
- lambda (λ): L2 regularization on leaf weights. Default = 1.
- alpha: L1 regularization on leaf weights. Default = 0.
- min_child_weight: Minimum sum of instance weight (Cover) in a child node. Default = 1.
- subsample: Fraction of training samples used per tree (like bootstrap). Default = 1.
- colsample_bytree: Fraction of features used per tree. Default = 1.
- base_score: Initial prediction probability. Default = 0.5.

# TOPIC 05 — Stacking & Voting
## Q: What is Stacking?
- Stacking = build several different types of base models (heterogeneous — different algorithms).
- Feed their predictions as inputs/features to a final meta-model (also called second-level learner or blender).
- The meta-model learns the best way to combine the base models.
- Analogy: Three hospital specialists (cardiologist, radiologist, blood lab) each give their opinion. A senior doctor (meta-model) weighs all three and makes the final diagnosis — better than any specialist alone.
Stacking flow:
1. Train base models (e.g., Random Forest, KNN, Naive Bayes) on training data.
2. Use base model predictions as input features for the meta-model.
3. Meta-model learns which base models to trust for which types of inputs.
4. Final prediction comes from the meta-model.
Important: If any base learner requires feature scaling (like KNN), you must StandardScaler the data before feeding it to the StackingClassifier.
Faculty notebook result: Stacking (RF + KNN + NB → NB meta-model) gave 86% accuracy, AUC = 0.949 — the best of all models tested!

## Q: What is Voting?
- Voting = the simplest ensemble — multiple models vote on the answer.

Hard Voting (Majority Voting):
- Each model gets exactly 1 vote.
- The class with the most votes wins.
- Example: 3 models predict [Yes, Yes, No] → majority = Yes.
Soft Voting (Weighted Probability):
- Each model predicts a probability for each class.
- Probabilities are averaged (or weighted) across models.
- The class with the highest average probability wins.
- Soft voting is generally better because it uses more information (confidence levels).
Weighted Voting:
- Better models (more accurate) get more votes than worse ones.

## Q: Compare Stacking vs Voting (point-wise)
- Combination method: Voting = simple majority or weighted average; Stacking = another ML model (meta-learner).
- Base models: Both use heterogeneous (different) algorithms.
- Flexibility: Voting = simple and limited; Stacking = powerful and flexible.
- Can learn patterns? Voting = No (just counts votes); Stacking = Yes (meta-model can learn "Model A is better for class 0, Model B is better for class 1").
- Power: Stacking is more powerful than voting.
- Mnemonic: "Stack = Smart coordinator, Vote = Simple democracy."

# TOPIC 06 — Major Comparisons
## Q: Compare AdaBoost vs Gradient Boosting vs XGBoost (point-wise)
- Weak Learner: AdaBoost = stumps (depth=1); GBM = trees (depth 4–8); XGBoost = trees (depth up to 6 default).
- How it learns: AdaBoost = reweights misclassified samples; GBM = fits trees to residuals; XGBoost = fits trees to residuals with regularization.
- Loss optimization: AdaBoost = exponential loss; GBM = gradient descent on differentiable loss (1st order); XGBoost = 2nd order Taylor approximation (gradient + Hessian).
- Regularization: AdaBoost = none built-in; GBM = learning rate only; XGBoost = L1 (α), L2 (λ), γ pruning, learning rate.
- Speed: AdaBoost = moderate; GBM = slow; XGBoost = very fast (parallelized, sparse-aware).
- Overfitting control: AdaBoost = sensitive to noise; GBM = can overfit with deep trees; XGBoost = best control (λ, γ, Cover).
- Missing values: AdaBoost = cannot handle; GBM = cannot handle; XGBoost = built-in handling.
- Sklearn class: AdaBoost = `AdaBoostClassifier`; GBM = `GradientBoostingClassifier`; XGBoost = `XGBClassifier` (from xgboost library).

## Q: Compare Bagging vs Boosting (complete, point-wise)
- Training: Bagging = parallel and independent; Boosting = sequential and dependent.
- Sampling: Bagging = bootstrap with replacement; Boosting = weighted/residual-based.
- Focus: Bagging = reduce variance; Boosting = reduce bias (and variance).
- Weak learner: Bagging = full trees (often deep); Boosting = shallow trees or stumps.
- Combination: Bagging = equal-weight voting/averaging; Boosting = weighted sum (via learning rate).
- Overfitting: Bagging = rarely overfits; Boosting = can overfit without regularization.
- Example: Bagging → Random Forest; Boosting → AdaBoost, XGBoost.

## Q: Compare γ (gamma) vs λ (lambda) in XGBoost (point-wise)
- Full name: γ = min_split_loss / tree complexity parameter; λ = reg_lambda / L2 regularization.
- What it does: γ = prunes branches (post-hoc after split decision); λ = shrinks leaf outputs (during calculation).
- Effect: γ: if Gain < γ → remove branch; λ: reduces Similarity Score → smaller outputs.
- Higher value → : γ = more pruning → simpler tree; λ = more regularization → conservative predictions.
- Default: γ = 0 (no pruning); λ = 1 (always some regularization).
- Mnemonic: "γ Guillotines, λ Loosens."

# TOPIC 07 — Numerical Examples
## Example 01 — EASY: AdaBoost Amount of Say
Problem: A stump misclassifies 1 out of 14 samples (all weights equal at 1/14).
Total Error:
Amount of Say:
- = ½ × ln((1 − 0.0714) / 0.0714)
- = ½ × ln(12.99)
- = ½ × 2.565
- = 1.282
Interpretation: This stump is quite good (only 1 error out of 14). Amount of Say = 1.282 (large positive) → gets strong voting power.

## Example 02 — MODERATE: AdaBoost Weight Update
Problem: Amount of Say = 1.28, original weight = 1/14 = 0.0714.
(a) Misclassified sample:
- w_new = 0.0714 × e^(+1.28) = 0.0714 × 3.597 = 0.257
- Weight increased from 0.071 → 0.257 (3.6× higher!)
(b) Correctly classified sample:
- w_new = 0.0714 × e^(−1.28) = 0.0714 × 0.278 = 0.0198
- Weight decreased from 0.071 → 0.020 (3.6× lower)

Effect: The misclassified sample now has a much larger share of total weight → much higher chance of appearing in the next training set → next stump focuses on it.
---
## Example 03 — EXAM-LEVEL: XGBoost Similarity Score & Gain
Problem: Residuals: [−0.5, 0.5, 0.5, −0.5]. Previous probability for all = 0.5. λ = 0. Split at Hours < 14.5: Left = [−0.5, 0.5, 0.5]; Right = [−0.5].
Root Similarity Score:
- Σ residuals = (−0.5 + 0.5 + 0.5 − 0.5) = 0
- Σ [p(1−p)] = 4 × (0.5 × 0.5) = 1.0
- Similarity = 0² / (1.0 + 0) = 0
Left Child Similarity [−0.5, 0.5, 0.5]:
- Σ residuals = (−0.5 + 0.5 + 0.5) = 0.5
- Σ [p(1−p)] = 3 × 0.25 = 0.75
- Similarity = (0.5)² / 0.75 = 0.25/0.75 = 0.333
Right Child Similarity [−0.5]:
- Σ residuals = −0.5
- Σ [p(1−p)] = 1 × 0.25 = 0.25
- Similarity = (−0.5)² / 0.25 = 0.25/0.25 = 1.0
Gain:
- Gain = 0.333 + 1.0 − 0 = 1.333
Pruning check:
- If γ = 1: Gain − γ = 1.333 − 1 = +0.333 → keep branch (positive).
- If γ = 2: Gain − γ = 1.333 − 2 = −0.667 → prune branch (negative).

## Example 04 — EXAM-LEVEL: Effect of λ on XGBoost Output
Problem: Left leaf residual = −0.5, p_prev = 0.5. Calculate Output with (a) λ=0 and (b) λ=1.
Denominator base: p × (1−p) = 0.5 × 0.5 = 0.25
(a) λ = 0:
- Output = −0.5 / (0.25 + 0) = −0.5/0.25 = −2.0

(b) λ = 1:
- Output = −0.5 / (0.25 + 1) = −0.5/1.25 = −0.4
Impact: Lambda shrank the output from −2.0 to −0.4. Lambda reduces sensitivity to individual observations and makes the tree take smaller, more conservative steps. This is the regularization effect — the model is less likely to overfit.

# TOPIC 08 — Faculty Notebook Results (Graduate Admissions Dataset)
## Q: What were the results from the faculty notebook?
Dataset: Graduate Admissions (400 rows, 8 features, binary target: Admitted/Not Admitted).
- AdaBoost (40 stumps): Accuracy = 81%, AUC = 0.913.
- GBM (150 trees, depth 10): Accuracy = 79%, AUC = 0.895.
- XGBoost (depth 10, γ=1): Accuracy = 84%, AUC = 0.889.
- XGBoost + GridSearchCV: Accuracy = 84%, AUC = 0.915 (improved after tuning).
- Stacking (RF + KNN + NB → NB meta-model): Accuracy = 86%, AUC = 0.949 (BEST model!).
Most important feature (Gini Importance): CGPA was the most important predictor of admission.
Stacking was the winner — combining three diverse models with a meta-learner outperformed every single model.

# TOPIC 09 — Common Exam Mistakes
## Mistake 1: Confusing Bagging and Boosting.
- Bagging = parallel, independent models, reduces variance. Example: Random Forest.
- Boosting = sequential, dependent models (each corrects previous), reduces bias.
- They are totally different in training approach and what they fix.
## Mistake 2: Thinking AdaBoost uses full trees.
- Wrong: "AdaBoost builds full decision trees."
- Correct: AdaBoost uses stumps (depth=1) as weak learners, NOT full trees.
- GBM and XGBoost use deeper trees (typically depth 4–8).
## Mistake 3: Forgetting to normalize weights after updating in AdaBoost.
- Correct: After updating all weights, you MUST normalize so they sum to 1.
- Without normalization, the sampling distribution is invalid.
## Mistake 4: Mixing up γ (gamma) and λ (lambda) in XGBoost.
- γ = pruning (chops branches if Gain < γ). Default = 0.
- λ = L2 regularization (shrinks outputs). Default = 1.
- "γ Guillotines, λ Loosens."
## Mistake 5: Setting learning rate too high.
- Wrong: Using η = 1.0 (each tree contributes its full prediction).
- Correct: Use small values (0.01–0.3) with more trees.
- High learning rate = fast training but overfitting. Low learning rate = slower but better generalization.
## Mistake 6: Saying "XGBoost always beats GBM."
- XGBoost is usually better, but NOT always.
- On small datasets, GBM or even simpler models can be sufficient.
- XGBoost's advantage is most pronounced on large, complex datasets.
## Mistake 7: Ignoring Cover / min_child_weight in XGBoost.
- Cover ensures leaves have enough "support" (sufficient observations).
- Default = 1. If your dataset has very few samples, you may need to lower it.
- Leaves with insufficient Cover are removed — this is a safety mechanism.
## Mistake 8: Confusing Stacking with Voting.
- Stacking = a meta-model learns how to combine base models.
- In stacking, base model outputs become features for the meta-model.
- Stacking is more powerful because the meta-model can learn complex combination patterns.
## Mistake 9: Not scaling data before Stacking with KNN.
- If base learners include distance-based methods like KNN, you MUST use StandardScaler on the features first!
- KNN is sensitive to feature scale — without scaling, it gives meaningless distances.

# TOPIC 10 — Viva & Exam Questions
## Q1 (Easy): What is a "stump" in AdaBoost?
- A stump is a decision tree with only one split — 1 root node and 2 leaf nodes.
- It makes decisions based on a single feature.
- It is the simplest (weakest) possible learner.
- AdaBoost builds many stumps, each focusing on different mistakes.

## Q2 (Easy): How does Gradient Boosting minimize error?
- GBM uses gradient descent on the loss function.
- It starts with an initial prediction, computes residuals (errors), then builds a tree to predict those residuals.
- Each tree takes a small step (learning_rate × output) toward reducing the loss.
- Trees are added sequentially, each correcting what previous trees got wrong.

## Q3 (Easy): What is the role of learning rate in boosting?
- Learning rate (η) scales each tree's contribution.
- Small η (e.g., 0.1): each tree contributes only 10% → needs more trees → better generalization.
- Large η (e.g., 1.0): each tree contributes fully → fewer trees needed → risk of overfitting.
- It is a bias-variance tradeoff: smaller rate = less overfitting but more computation.

## Q4 (Medium): Explain the Similarity Score and Gain in XGBoost.
- Similarity Score = (Σ residuals)² / (Σ [p(1−p)] + λ). Measures how "pure" a group of residuals is.
- Gain = Similarity_left + Similarity_right − Similarity_parent. Measures improvement from a split.
- XGBoost picks the split with maximum Gain.
- If (Gain − γ) < 0, the branch is pruned.
## Q5 (Medium): How does λ (lambda) in XGBoost prevent overfitting?
- λ is added to the denominator of both Similarity Score and Output formula.
- Higher λ → lower Similarity → lower Gain → easier pruning (more branches removed).
- It also shrinks the Output value for each leaf, making the tree take more conservative steps.
- This reduces sensitivity to individual observations → prevents overfitting.

## Q6 (Medium): What is the difference between Stacking and Voting?
- Voting: simply combines predictions by majority (hard) or probability averaging (soft). No learning involved.
- Stacking: uses a meta-model that learns the best way to combine base model predictions.
- Meta-model is trained on outputs of base models → can learn "Model A is better for class 0, Model B for class 1."
- Stacking is more flexible and powerful. Proved in faculty notebook: Stacking gave best accuracy (86%) and AUC (0.949).

## Q7 (Tricky Viva): In AdaBoost, what happens when Total Error = 0.5 or 0?
- ε = 0.5: Amount of Say = ½ × ln(0.5/0.5) = ½ × ln(1) = 0. The stump is no better than random guessing → gets zero voting power → completely ignored.
- ε = 0: Amount of Say = ½ × ln(1/0) → +∞. A perfect stump gets infinite say. In practice, boosting stops since the model is already perfect.

## Q8 (Tricky Viva): Why does XGBoost use 2nd-order Taylor expansion while GBM uses only 1st-order gradient?
- XGBoost approximates the loss function using both the 1st derivative (gradient) and the 2nd derivative (Hessian).
- The Hessian provides curvature information — it tells not just the direction but also how much to adjust.
- This leads to better convergence — faster and more accurate optimization.
- The second derivative appears in the denominator of the Similarity Score as Σ[p(1−p)], which is the Hessian of log-loss for binary classification.
- GBM uses only the gradient (1st order) → less information → potentially worse convergence.

# TOPIC 12 — Quick Revision Summary
## All Key Formulas
- AdaBoost Total Error: ε = Σ weights of misclassified samples
- AdaBoost Amount of Say: = ½ × ln((1 − ε) / ε)
- AdaBoost Weight (wrong): w_new = w_old × e^(+AoS)
- AdaBoost Weight (correct): w_new = w_old × e^(−AoS)
- GBM/XGB Output: = Σ residuals / (Σ [p(1−p)] + λ)
- GBM/XGB Prediction: new log(odds) = prev log(odds) + η × Output
- Probability from log(odds): p = e^(log_odds) / (1 + e^(log_odds))
- XGB Similarity Score: = (Σ residuals)² / (Σ [p(1−p)] + λ)
- XGB Gain: = Similarity_left + Similarity_right − Similarity_parent
- XGB Pruning rule: if (Gain − γ) < 0 → prune; else → keep

# SMLC Session 6 Supplement — Stacking, Voting & Model Comparison
# TOPIC 01 — Hard Voting vs Soft Voting
## Q: What is Hard Voting in simple words?
- Imagine 4 friends guessing whether a movie is "Hit" or "Flop."
- Hard Voting: each friend gives a final answer — "Hit" or "Flop."
- You count votes. If 3 say "Hit" and 1 says "Flop" → majority wins → "Hit."
- It does NOT matter how confident each friend was — everyone gets exactly 1 vote.
- Analogy: Like a general election — each citizen casts one vote. The candidate with most votes wins.

## Q: What is Soft Voting in simple words?
- Soft Voting: each friend gives a probability — "I'm 90% sure it's a Hit" vs "I'm 55% sure."
- You average all the probabilities.
- If the average probability of "Hit" > 0.5 → final answer is "Hit."
- A very confident friend's opinion counts more naturally through the averaging.
- Analogy: Like an approval rating — each citizen rates candidates on a scale of 0–100. The candidate with the highest average rating wins.

## Q: What is the formal definition of Hard vs Soft Voting?
Hard Voting:
- Each model predicts a class label (e.g., 0 or 1).
- Final prediction = mode (most frequent label among all model predictions).
- Formula: Final = mode(y₁, y₂, ..., yₖ)
- Requires only that models can predict class labels (not probabilities).
- Use when models have similar accuracy.
- sklearn: `voting='hard'`
Soft Voting:
- Each model predicts a probability for each class (requires predict_proba).
- Final prediction = argmax of the average probabilities across all models.
- Formula: Final = argmax( avg(p₁, p₂, ..., pₖ) )
- Uses more information (confidence levels), so generally smarter than hard voting.
- Use when models have well-calibrated probabilities.
- sklearn: `voting='soft'`

## Q: What is Weighted Voting?
- You can assign different weights to different models.
- Better-performing models get more weight (more influence on the final prediction).
- Example: `VotingClassifier(estimators=..., voting='soft', weights=[2, 1, 1, 1])` → first model has 2× influence.
- The weighted average is: Σ(weight × probability) / Σ(weights).

## Q: Compare Hard Voting vs Soft Voting vs Stacking (point-wise)
- Input from models: Hard = class labels; Soft = class probabilities; Stacking = predictions (labels or probs).
- Combination method: Hard = majority count; Soft = average probabilities; Stacking = a meta-model (learned).
- Learns the combination? Hard = No; Soft = No; Stacking = Yes (meta-model is trained).
- Flexibility: Hard = Low; Soft = Medium; Stacking = High.
- Overfitting risk: Hard = Low; Soft = Low; Stacking = Medium (needs cross-validation to prevent leakage).
- Lab accuracy (Stack.csv): Hard = 84.7%; Soft = 80.8%; Stacking = 95.5% (best).
- When to use: Hard = quick baseline ensemble; Soft = when models have calibrated probabilities; Stacking = when maximum accuracy is needed.

## Q: Why did Soft Voting perform WORSE than Hard Voting in the lab?
- Soft voting averages probabilities.
- If some models produce poorly calibrated probabilities (e.g., Decision Tree outputs values close to 0 or 1, not smooth intermediate probabilities), the average becomes misleading.
- Hard voting only uses the final class labels — this is more robust when probability calibration is poor.
- Lab result: Hard Voting = 84.7%, Soft Voting = 80.8% (soft was worse here).
- Key lesson: Soft voting is NOT always better than hard voting. It depends on whether your models produce well-calibrated probabilities.

# TOPIC 02 — Stacking — Deep Dive
## Q: What is Stacking (full explanation)?
- Stacking = an ensemble that uses two levels of learning.
- Level 0 (Base Learners / Ground Floor): Multiple different models (heterogeneous — different algorithms like LR, KNN, DT, NB) each make their predictions independently.
- Level 1 (Meta-Learner / Top Floor): A single meta-model takes the Level 0 predictions as its input features and learns the best way to combine them.
- Analogy: Company decision-making. Level 0 = Department heads (Finance, Marketing, Tech, Operations) each give recommendations. Level 1 = The CEO (meta-model) has learned from experience which department is more trustworthy for which type of decision and makes the final call.
Formula:
- Stacking = f_meta( f₁(X), f₂(X), f₃(X), f₄(X) )
  - f₁, f₂, f₃, f₄ = base learners (models 1 to 4).
  - f_meta = meta-learner.
  - The meta-learner receives the outputs of all base learners as its features.

## Q: What are the steps of the Stacking Architecture?
Step 1 — Level 0 (Base Learners):
- Train K different models (LR, KNN, DT, NB etc.) on the training data.
- Each produces predictions on the data.

Step 2 — Cross-Validation Trick (to prevent data leakage):
- To avoid the meta-model learning from "cheated" predictions, base model predictions for the meta-model are generated using cross-validation (cv=5 in sklearn).
- Each base model predicts only on the fold it did NOT train on (out-of-fold predictions).
- This ensures the meta-model sees honest predictions, not inflated ones.
Step 3 — Level 1 (Meta-Learner):
- If 4 base models + cv=5 → a 100×4 matrix of meta-features (100 training samples × 4 model predictions).
- A meta-model (e.g., Logistic Regression) is trained on this matrix with the original target labels.
Step 4 — Prediction on New Data:
- New data → all base models predict → those predictions become features → meta-model makes final prediction.

sklearn syntax:
- `StackingClassifier(estimators=level_0, final_estimator=level_1, cv=5)`

## Q: Why does StackingClassifier use cross-validation internally?
- Without CV, base models would predict on data they already trained on.
- This produces overly optimistic meta-features — the meta-model would see "cheated" predictions.
- The meta-model would then overfit by learning from these inflated results.
- With CV (cv=5): each base model predicts on data it never trained on → honest out-of-fold predictions → meta-model learns from genuine performance.
- Analogy: If a department head recommends a project they already know was approved (data leakage), their recommendation is meaningless. CV ensures each department gives recommendations on projects they have NOT already seen.
- Mnemonic: "CV Prevents Cheating in Stacking."

## Q: Why does Stacking beat individual models?
- Each model has different strengths and weaknesses.
- KNN might be great on some patterns, while LR catches others.
- The meta-model learns patterns like: "When KNN says class 1 and Naive Bayes disagrees, KNN is usually right for this type of input."
- This learned combination is more powerful than any fixed rule (like simple voting).
- Lab proof: KNN (best individual) = 93.3%. Stacking = 95.5% — better than any single model and better than any voting strategy.

## Q: What is the meta-model in Stacking and what should it be?
- It learns the optimal way to combine base model outputs.
- In the lab notebook: Logistic Regression was used as the meta-learner.
- Best practice: use a simple model (like Logistic Regression) as the meta-learner.
- Reason: a complex meta-model risks overfitting the meta-features, which are already higher-level representations.

# TOPIC 03 — Lab Dataset and Results
## Q: What was the dataset used in this lab?
Dataset: Stack.csv
- Rows: 3000
- Features: 25 (Feature_1 to Feature_24 + column "24")
- Target: Binary (0 or 1)
- Train/Test Split: 80/20 (random_state = 42)
- Evaluation: RepeatedStratifiedKFold (n_splits=10, n_repeats=3) → gives 30 evaluations → reliable mean ± std.

## Q: What were the complete results from the lab?
Individual Models (CV Accuracy → Test Accuracy):
- Logistic Regression: 86.8% ± 2.3% → Test: 88.2%
- KNN: 93.3% ± 1.4% → Test: 93.7% ← Best individual model
- Decision Tree (CART): 80.5% ± 2.2% → Test: 81.7%
- Naive Bayes: 83.2% ± 2.4% → Test: 80.2%
Ensemble Models (Test Accuracy):
- Hard Voting (LR+KNN+DT+NB): Test: 84.7%
- Soft Voting (LR+KNN+DT+NB): Test: 80.8%
- Stacking (LR+KNN+DT+NB → LR meta): CV: 94.0% ± 1.1% → Test: 95.5% ← BEST MODEL
Key observations:
- Stacking (95.5%) beats the best individual model KNN (93.7%) by 1.8%.
- Stacking significantly beats Hard Voting (84.7%) by 10.8%.
- Hard Voting (84.7%) actually beat Soft Voting (80.8%) — soft is NOT always better!
- Stacking had the lowest standard deviation (±1.1%) — most consistent model.

## Q: What does RepeatedStratifiedKFold do and why use it?
- A simple train/test split gives one accuracy number — unreliable, depends on the random split.
- RepeatedStratifiedKFold gives multiple evaluations → a mean ± std.
- `n_splits=10` = 10-fold cross-validation.
- `n_repeats=3` = repeat the whole process 3 times with different random seeds = 30 evaluations total.
- "Stratified" = each fold preserves the class distribution (important for imbalanced data).
- Result: a reliable mean ± std instead of a single noisy number.

# TOPIC 04 — Numerical Examples
## Example 01 — EASY: Hard Voting
Problem: 4 models predict for a sample: LR → 1, KNN → 0, DT → 1, NB → 1. Hard voting prediction?
Count votes:
- Class 1 = 3 votes (LR, DT, NB)
- Class 0 = 1 vote (KNN)
- Mode = 1
Final prediction: Class 1

## Example 02 — EASY: Soft Voting
Problem: 4 models output P(class=1): LR → 0.6, KNN → 0.3, DT → 0.8, NB → 0.4. Soft voting prediction?
Average probability for class 1:
- = (0.6 + 0.3 + 0.8 + 0.4) / 4 = 2.1 / 4 = 0.525
- Since 0.525 > 0.5 → Final prediction: Class 1
Notice: With hard voting on these SAME models, if thresholded at 0.5:
- LR → 1, KNN → 0, DT → 1, NB → 0 → 2 vs 2 = tie (sklearn picks first class alphabetically or lowest class index).
- Soft voting broke the tie using probability information → more informative.

## Example 03 — MODERATE: Weighted Soft Voting
Problem: Same probabilities (LR=0.6, KNN=0.3, DT=0.8, NB=0.4) but weights = [2, 3, 1, 1] (KNN gets 3× weight).
Weighted average:
- = (2×0.6 + 3×0.3 + 1×0.8 + 1×0.4) / (2+3+1+1)
- = (1.2 + 0.9 + 0.8 + 0.4) / 7
- = 3.3 / 7 = 0.471
- Since 0.471 < 0.5 → Final prediction: Class 0
Key insight: The highly-weighted KNN (which predicted 0.3 for class 1 = skeptical about class 1) pulled the result toward class 0. Assigning 3× weight to KNN flipped the prediction from Class 1 (unweighted) to Class 0 (weighted).


## Example 04 — EXAM-LEVEL: Stacking — How Meta-Features Are Created

Problem: Training set has 100 samples, 4 base models, cv=5. How many meta-features are created? What does the meta-model train on?

Step 1: With cv=5, the training data is split into 5 folds of 20 samples each.
Step 2: For each base model:
- It trains on 4 folds (80 samples) and predicts on the held-out fold (20 samples).
- After 5 iterations (all folds have been held out once), every sample has an out-of-fold prediction from that model.
Step 3: This gives a 100×4 matrix of meta-features.
- 100 = all training samples (each got a prediction during their held-out fold).
- 4 = number of base models (each contributes 1 column of predictions).
Step 4: The meta-model (Logistic Regression) trains on this 100×4 matrix with the original target labels (y_train).
At test time: All 4 base models predict on test data → 4 predictions per test sample → meta-model predicts final class.

Why cv? Without cross-validation, base models would predict on data they already trained on → overly optimistic predictions → data leakage → meta-model overfits.

# TOPIC 05 — Common Exam Mistakes
## Mistake 1: Using the same model type for both base and meta in Stacking.
- While technically possible, it is better to use different types.
- The meta-model should be simple (Logistic Regression is the standard choice) to avoid overfitting the meta-features.
- Complex meta-models can memorize patterns in the small meta-feature set.
## Mistake 2: Forgetting the cv parameter in StackingClassifier.
- Default cv=5 is fine.
- Without CV, base models predict on their own training data → overly optimistic predictions → data leakage → the meta-model overfits.
- Always use cv ≥ 3. The default of 5 is generally safe.
## Mistake 3: Assuming Soft Voting is always better than Hard Voting.
- Wrong: "Soft voting always outperforms hard voting."
- Correct: Soft voting relies on well-calibrated probabilities. When some models (like Decision Trees) output extreme probabilities (0 or 1) rather than smooth probabilities, the average becomes distorted.
- Lab proof: Hard Voting (84.7%) > Soft Voting (80.8%) in this lab.
- Choose based on whether your models have calibrated probabilities.
## Mistake 4: Not evaluating with RepeatedStratifiedKFold.
- Simple train/test split gives one number — unreliable.
- RepeatedStratifiedKFold (n_splits=10, n_repeats=3) gives mean ± std over 30 evaluations — much more reliable.
- The ±std is important: a model with 94.0% ± 1.1% is more consistent and trustworthy than one with 95% ± 8%.
## Mistake 5: Including a very weak model in the ensemble.
- A terrible base model can drag down the ensemble, especially in voting.
- Check individual model performance first.
- Include only models that are at least somewhat competent (better than random guessing).
- In stacking, the meta-model can learn to ignore a weak base learner, but it still adds noise.
## Mistake 6: Expecting Stacking to always give massive improvements.
- If individual models already give 95%+ accuracy, stacking might give only 96%.
- Stacking shines when individual models are diverse (capture different patterns) and complementary (have different strengths).
- When all models already agree well, combining them adds little value.

# TOPIC 06 — Viva & Exam Questions

## Q1 (Easy): What is the difference between Hard and Soft Voting?

- Hard Voting: Takes each model's predicted class label → returns the majority (mode). One vote per model.
- Soft Voting: Takes each model's predicted probability → averages them → picks the class with highest average probability.
- Soft voting uses more information (confidence levels) but requires all models to output probabilities (predict_proba).

## Q2 (Easy): In the lab, which individual model performed best?

- KNN performed best among individual models.
- CV Accuracy = 93.3% ± 1.4%, Test Accuracy = 93.7%.
- But Stacking (95.5%) still beat it.
---

## Q3 (Easy): What is the meta-learner in Stacking?

- The meta-learner (Level 1) is a model that takes the predictions of all base models (Level 0) as its input features.
- It learns to optimally combine base model outputs.
- In the lab notebook: Logistic Regression was used as the meta-learner.
---

## Q4 (Medium): Why does StackingClassifier use cross-validation internally?

- To prevent data leakage.
- Without CV: base models predict on their own training data → overly optimistic meta-features → meta-model overfits.
- With CV (default cv=5): each base model predicts only on data it did NOT train on (out-of-fold predictions).
- These honest predictions become the training data for the meta-model → learns real, not inflated, patterns.

## Q5 (Medium): In the lab, Soft Voting (80.8%) performed worse than Hard Voting (84.7%). Why?

- Soft voting averages probabilities.
- Decision Trees typically output extreme probabilities (near 0 or 1) rather than smooth, calibrated probabilities.
- When probability calibration is poor, the averaged probabilities become misleading.
- Hard voting only uses the final labels (which are reasonable for all models) → more robust when probabilities are unreliable.

## Q6 (Tricky Viva): If you add a 5th base model with 50% accuracy (random guessing) to Stacking, would it help or hurt?

- It would most likely hurt.
- The meta-model receives a noisy 5th feature that provides no useful information.
- While a smart meta-model might learn to assign near-zero weight to it, the noise can confuse the meta-model, especially with limited training data.
- In practice: include only base models that are at least somewhat competent.


## Q7 (Tricky Viva): Can you use Stacking for regression?

- Yes — use StackingRegressor instead of StackingClassifier.
- Base models output continuous predictions (not class labels).
- A meta-regressor (e.g., LinearRegression, Ridge) learns to combine these continuous predictions.
- The principle is identical: base learner outputs → meta-features → meta-model predicts final value.
- Final output is a continuous value, not a class.

# TOPIC 08 — Quick Revision Summary
## Lab Results Table (must memorise)
- Dataset: Stack.csv — 3000 rows, 25 features, binary target.
- Logistic Regression: CV = 86.8%, Test = 88.2%.
- KNN: CV = 93.3%, Test = 93.7%. ← Best individual model.
- Decision Tree: CV = 80.5%, Test = 81.7%.
- Naive Bayes: CV = 83.2%, Test = 80.2%.
- Hard Voting: Test = 84.7%.
- Soft Voting: Test = 80.8% (worse than hard in this case!).
- Stacking (LR+KNN+DT+NB → LR): CV = 94.0% ± 1.1%, Test = 95.5% ← BEST.
'''



