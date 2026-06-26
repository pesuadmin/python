"""


# SESSION 3 — KNN & Naive Bayes Classifier
# PART A — K-NEAREST NEIGHBOURS (KNN)
# TOPIC 01 — What is KNN?

## Q: What is KNN in simple words?
- Imagine you are new at school. You do not know if you should sit at the "gamers" table or the "sports" table in the cafeteria.
- So you look at the K closest people near you. If 4 out of 5 nearest people are gamers, you sit with gamers!
- That is KNN — look at your nearest neighbours, see what most of them are, and become that.
- "K" = how many neighbours to check (you choose this number).
- "Nearest" = measured by distance (like measuring with a ruler on a graph).
- "Neighbours" = the data points closest to the new point.
- It is a lazy learner — it does not study beforehand. It looks up answers at test time!

## Q: What is the formal definition of KNN?
- KNN is a non-parametric, lazy, instance-based supervised learning algorithm.
- It classifies a new data point by finding the K closest data points (neighbours) in the training set.
- It then assigns the majority class label among those K neighbours to the new point.


## Q: What are the key properties of KNN?
- Instance-based: Uses actual training instances directly to make predictions. No model is built.
- Lazy learner: There is NO training phase. All computation happens at prediction time.
- Non-parametric: Makes no assumptions about the shape or distribution of the data.
- Requires normalization: Features MUST be scaled. Without scaling, high-range features dominate the distance calculation.


# TOPIC 02 — Distance Measures

## Q: What are proximity measures? What are the two types?
- KNN works by calculating distance between the new point and all training points.
- There are two types of proximity:
  - Similarity matrix: Diagonal = 1 (object is 100% similar to itself). Range: 1 = identical, 0 = completely different.
  - Dissimilarity matrix: Diagonal = 0 (zero distance from itself). Range: 0 = identical, 1 (or more) = completely different.
- Relationship: Dissimilarity = 1 − Similarity (when normalized to 0-1).

## Q: What is Euclidean Distance?
- Also called L2 Norm.
- It is the straight-line (as-the-crow-flies) distance between two points.
- Analogy: Flying distance — straight line like a bird from Koramangala to MG Road.

Formula:
- d(X,Y) = √[ Σ(xᵢ − yᵢ)² ]
  - For each dimension: subtract the coordinates, square the result.
  - Sum all squared differences.
  - Take the square root of the total.

Example: Between (5,6) and (1,3):
- = √[(5−1)² + (6−3)²] = √[16 + 9] = √25 = 5

## Q: What is Manhattan Distance?
- Also called L1 Norm, Taxicab distance, City-Block distance, or "Snake" distance.
- It measures distance by travelling along grid lines (no diagonal shortcuts).
- Analogy: Auto-rickshaw distance — you must follow the grid of roads.

Formula:
- d(X,Y) = Σ |xᵢ − yᵢ|
  - For each dimension: take the absolute difference (no squaring, no square root).
  - Sum all absolute differences.

Example: Between (5,6) and (1,3):
- = |5−1| + |6−3| = 4 + 3 = 7


## Q: What is Minkowski Distance?
- Also called Lp Norm.
- It is the generalized form of distance that includes both Manhattan and Euclidean.

Formula:
- d(X,Y) = ( Σ |xᵢ − yᵢ|ᵖ )^(1/p) where p > 0
  - p = a parameter you choose.
  - When p = 1 → becomes Manhattan distance.
  - When p = 2 → becomes Euclidean distance.

Example: Between (5,6) and (1,3) with p=4:
- = (|5−1|⁴ + |6−3|⁴)^(1/4) = (256 + 81)^0.25 = (337)^0.25 ≈ 4.28

## Q: What is Chebyshev Distance?
- Also called L∞ Norm (L-infinity norm).
- It measures the maximum difference in any single dimension.
- Analogy: The King's movement in chess — the farthest you move in any single direction.

Formula:
- d(X,Y) = max |xᵢ − yᵢ|
  - For each dimension, find the absolute difference.
  - Take the maximum of all those differences.

Example: Between (5,6) and (1,3):
- = max(|5−1|, |6−3|) = max(4, 3) = 4


## Q: What is the important ordering relationship between distances?
- For the same two points, the distances always follow this order:
- Chebyshev ≤ Euclidean ≤ Manhattan
- Mnemonic: C.E.M. → Chebyshev is always smallest, Manhattan is always largest.
- Verified with (5,6) and (1,3): Chebyshev = 4, Euclidean = 5, Manhattan = 7. 


## Q: What are distance measures for string/text data?
- Cosine distance.
- Edit distance (Levenshtein).
- Longest Common Subsequence.
- Hamming distance.

## Q: What are the properties a valid distance metric must satisfy?
- Non-negativity: Distance is always ≥ 0.
- Identity: d = 0 if and only if both points are the same point.
- Symmetry: d(X,Y) = d(Y,X) — distance from A to B equals distance from B to A.
- Triangle inequality: d(X,Z) ≤ d(X,Y) + d(Y,Z) — the direct path is never longer than going via a third point.

# TOPIC 03 — KNN Procedure & Choosing K

## Q: What are the steps to classify a new point using KNN?
1. Choose a distance measure (usually Euclidean) and a value for K.
2. Compute the distance from the new point to every single training point.
3. Sort all distances in ascending order (smallest to largest).
4. Pick the top K nearest points. Count the class labels among them.
5. Assign the majority class label (maximum voting) to the new point.

Mnemonic: DCSA → Dal Chawal Sabzi Achar
- D = Choose Distance measure.
- C = Calculate distances.
- S = Sort them.
- A = Assign majority class.

## Q: How does the choice of K affect the model?
- Small K (e.g., 1–3): Low bias, high variance. The model is sensitive to noise — one wrong neighbour flips the prediction. Risk: Overfitting.
- Large K (e.g., equal to N): High bias, low variance. Every new point gets classified as the majority class in the entire dataset. Risk: Underfitting.
- K must be just right — use cross-validation (GridSearchCV) to find the optimal K.

## Q: What is the tie-breaking rule for choosing K?
- Even number of classes (e.g., 2 classes: Yes/No) → choose K to be odd (to avoid 50-50 ties).
- Odd number of classes (e.g., 3 classes) → choose K to be even.
- Mnemonic: They are opposite to avoid ties.

## Q: What is Weighted KNN?
- In standard KNN, all K neighbours vote equally.
- In Weighted KNN, closer neighbours have higher weight.
- Weight formula = 1/distance (inverse of distance).
- This makes the algorithm less sensitive to the choice of K.
- Points very close to the test point have more influence than distant ones.

## Q: Why must we normalize data before using KNN?
- KNN relies entirely on distance calculations.
- If one feature ranges 0–25 and another ranges −100 to 2000, the second feature completely dominates the distance.
- The smaller-range feature becomes irrelevant even if it is actually important.
- Normalization (using StandardScaler or MinMaxScaler) puts all features on the same scale.
- Analogy: Comparing marks (0–100) with salary (₹10,000–₹2,00,000). Salary numbers are 1000× bigger, so KNN would think salary matters way more. Normalization converts everything to the same percentile scale.

## Q: What are the advantages of KNN?
- Easy to implement.
- No training phase required.
- New data can be added anytime without retraining.
- Effective when the training dataset is large.
- No assumptions about the data distribution.

## Q: What are the disadvantages of KNN?
- Hard to choose the right K.
- Computationally expensive at prediction time (must compute distance to all training points).
- Cannot tell which features matter most.
- Suffers from the curse of dimensionality in high-dimensional data.
- Performs poorly with missing data.

## Q: What is the Curse of Dimensionality in KNN?
- In very high-dimensional spaces, all data points become approximately equidistant from each other.
- The concept of "nearest neighbour" loses meaning — there is no meaningful "near" vs "far".
- The volume of the space grows exponentially with dimensions, so data becomes very sparse.
- You would need exponentially more training data for KNN to work well in high dimensions.

# PART B — NAIVE BAYES CLASSIFIER

# TOPIC 04 — What is Naive Bayes?

## Q: What is Naive Bayes in simple words?
- Think of your email inbox. Some emails are important (ham), others are junk (spam).
- If an email contains words like "money" and "horoscope", there is a higher chance it is spam.
- If it says "work" and "good", it is probably ham.
- Naive Bayes calculates the probability of each class based on the features, then picks the most likely class.
- "Naive" = assumes every feature is independent — one word does not affect another.
- "Bayes" = uses Bayes' Theorem — a formula to update your belief when you get new evidence.
- It is an eager learner — it studies the training data first, then classifies quickly!

## Q: What is the formal definition of Naive Bayes?
- Naive Bayes is a probabilistic, eager-learning classifier based on Bayes' Theorem.
- It assumes all features are conditionally independent given the class label.
- It assumes all features have equal importance.
- It computes the posterior probability for each class and assigns the class with the highest probability.

# TOPIC 05 — Probability Basics (Prerequisites)

## Q: What are the probability formulas needed for Naive Bayes?
Basic Probability:
- P(event) = (Number of favourable outcomes) / (Total outcomes)

Conditional Probability:
- P(A | B) = P(A ∩ B) / P(B)
  - P(A|B) = probability of A given that B has already happened.
  - P(A ∩ B) = probability of both A and B happening together.
  - P(B) = probability of B happening.

Multiplication Rule:
- P(A ∩ B) = P(A|B) · P(B) = P(B|A) · P(A)
  - Can be used to find joint probability from conditional probability.

# TOPIC 06 — Bayes' Theorem

## Q: What is Bayes' Theorem?
Formula:
- P(t | x) = [ P(t) · P(x | t) ] / P(x)
  - P(t|x) = Posterior = probability of class t given features x. This is what we want.
  - P(t) = Prior = probability of class t from training data (before seeing any features).
  - P(x|t) = Likelihood = probability of seeing feature x in class t.
  - P(x) = Evidence = overall probability of feature x (the same for all classes).

- Posterior P(t|x) = P(spam | "money")
- Prior P(t) = P(spam) = 0.15 (15% of emails are spam)
- Likelihood P(x|t) = P("money" | spam) = 0.42 (42% of spam emails contain the word "money")
- Evidence P(x) = P("money") overall

Mnemonic: P.L.E.P. (Posterior = Likelihood × Evidence | Prior)
- Think: "PLEP!" — like the sound of a notification when your email is classified.
- Posterior = Likelihood × Prior / Evidence.
---

# TOPIC 07 — Naive Bayes Assumptions & Classification Formula

## Q: What are the two key assumptions of Naive Bayes?
Assumption 1 — Feature Independence (Conditional Independence):
- All features are independent of each other given the class.
- This means: P(x₁, x₂ | t) = P(x₁|t) · P(x₂|t)
- In reality, words in an email ARE correlated ("urgent" often appears with "action required"), but Naive Bayes ignores this for simplicity.

Assumption 2 — Equal Feature Importance:
- No single feature has more weight or influence than another in determining the class.

Mnemonic: I.E. — the assumptions are: features are Independent and have Equal importance.

## Q: What is the Naive Bayes Classification Formula?
Formula:
- P(t | X) ∝ P(t) · P(x₁|t) · P(x₂|t) · ... · P(xₙ|t)
  - P(t) = prior probability of class t.
  - P(xᵢ|t) = likelihood of feature i given class t.
  - Multiply all likelihoods together, then multiply by the prior.
  - The denominator P(x) is dropped since it is constant across all classes — only the numerators are compared.

- Assign the class label t that maximizes this expression.


## Q: Why is the denominator P(x) dropped?
- P(x) is the same for all classes (it is the probability of the observed features regardless of class).
- Since we are comparing posteriors across classes to find the maximum, a common factor in all comparisons does not change which class wins.
- Dropping it simplifies calculation without affecting the final classification decision.

## Q: What are the steps to classify a new point using Naive Bayes?
1. Obtain the frequency table of each feature per class from training data.
2. Compute likelihoods (e.g., P(word|spam)) and prior probabilities P(class).
3. For a new instance, compute the posterior for each class using: P(t) × Π P(xᵢ|t).
4. Assign the class with the highest posterior probability.

# TOPIC 08 — Zero Probability Problem & Laplace Smoothing

## Q: What is the Zero Probability Problem?
- If a feature value never appeared with a particular class in training data, its count = 0.
- This means its likelihood P(word|class) = 0/total = 0.
- Since Naive Bayes multiplies all likelihoods, multiplying by 0 makes the entire posterior = 0 — regardless of all other features.
- Even if 100 other features strongly indicate spam, one unseen word makes the whole posterior zero.
- This is called the zero-frequency problem.

## Q: What is Laplace Smoothing and how does it work?
- Laplace Smoothing (also called Add-α smoothing) prevents any probability from ever being zero.
- It adds a small count α (usually α = 1) to every feature count before computing probabilities.

Formula:
- P(word | class) = (count + α) / (total + α × number_of_unique_words)
  - count = original count of the word in that class.
  - α = smoothing parameter (default = 1).
  - total = total words in that class (original total).
  - number_of_unique_words = vocabulary size (how many distinct words exist).

- Without smoothing: P(Snacks|Spam) = 0/50 = 0 (breaks everything).
- With Laplace (α=1): P(Snacks|Spam) = (0+1) / (50 + 1×6) = 1/56 = 0.018 (safe!).

Key note on denominator: When you add α to each count, the denominator increases by α × number_of_unique_feature_values. Students often forget to adjust the denominator.

Mnemonic: "Add ONE, worry NONE" — Add α=1 to every count so zero probability never happens.

Analogy: If a restaurant has 0 ratings, does that mean it is terrible? No — it just means nobody rated it yet. Laplace smoothing gives every restaurant 1 default rating so nobody has zero.

---
# TOPIC 09 — Types of Naive Bayes

## Q: What are the three types of Naive Bayes in Scikit-Learn?
GaussianNB:
- Feature type: Continuous (floating point numbers).
- Distribution assumed: Normal/Gaussian distribution.
- Use case: Medical diagnosis, admission prediction, any data where features are continuous.
- Example: Predict diabetes based on blood pressure, glucose level, BMI.

MultinomialNB:
- Feature type: Count or frequency data.
- Distribution assumed: Multinomial distribution.
- Use case: Document classification, spam detection, text analytics.
- Example: Classify emails based on word counts.

BernoulliNB:
- Feature type: Binary features (0 or 1).
- Distribution assumed: Bernoulli distribution.
- Use case: When you only care about whether a word is present or absent.
- Example: "Does the word 'money' appear in this email? Yes=1, No=0."

## Q: What are the advantages of Naive Bayes?
- Great for text classification (spam, sentiment analysis).
- Very fast training and prediction.
- Handles multi-class problems well.
- Performs better with categorical features than many other algorithms.
- Handles missing data well — just ignores missing features in the calculation.

## Q: What are the disadvantages of Naive Bayes?
- The independence assumption is rarely true in real data.
- Zero-frequency problem (needs Laplace smoothing to fix).
- Cannot learn feature interactions.
- Performs poorly when there are many correlated numeric features.
- Probability estimates are often not accurate (though classification decisions usually are).

# TOPIC 10 — KNN vs Naive Bayes Comparison

## Q: Compare KNN and Naive Bayes (point-wise)
- Learning type: KNN = Lazy (no training); Naive Bayes = Eager (learns from training data first).
- Model type: KNN = Instance-based, non-parametric; Naive Bayes = Probabilistic, parametric.
- Core idea: KNN = majority vote of nearest neighbours; Naive Bayes = class with highest posterior probability.
- Key parameter: KNN = K (number of neighbours); Naive Bayes = α (Laplace smoothing).
- Assumptions: KNN = none about data distribution; Naive Bayes = feature independence + equal importance.
- Feature scaling: KNN = REQUIRED (normalization is critical); Naive Bayes = NOT required.
- Best for: KNN = small datasets, numeric features; Naive Bayes = text/categorical data, large datasets.
- Prediction speed: KNN = Slow (computes distances to all training points at test time); Naive Bayes = Very fast (just multiplies probabilities).
- Training speed: KNN = Zero (no training at all); Naive Bayes = Fast.
- Missing data handling: KNN = Poorly; Naive Bayes = Well (just ignores missing features).
- Generative vs Discriminative: KNN = neither clearly (often called discriminative); Naive Bayes = Generative.
## Q: Compare all four distance measures (point-wise)
- Manhattan (L1): Formula = Σ|xᵢ−yᵢ|. Grid-like path. Best for high-dimensional, sparse data.
- Euclidean (L2): Formula = √Σ(xᵢ−yᵢ)². Straight line. Best for general purpose (default in KNN).
- Minkowski (Lp): Formula = (Σ|xᵢ−yᵢ|ᵖ)^(1/p). Generalized form. Flexible; subsumes L1 and L2.
- Chebyshev (L∞): Formula = max|xᵢ−yᵢ|. Maximum axis difference. Best for chess king movement, warehouse robots.
- Ordering (always): Chebyshev ≤ Euclidean ≤ Manhattan for the same two points.
- Minkowski special cases: p=1 → Manhattan; p=2 → Euclidean; p→∞ → Chebyshev.

# TOPIC 11 — Numerical Examples

## Example 01 — EASY: All Four Distances

Problem: Find Euclidean, Manhattan, Chebyshev, and Minkowski (p=4) distances between (5,6) and (1,3).
Euclidean:
- √[(5−1)² + (6−3)²] = √[16 + 9] = √25 = 5
Manhattan:
- |5−1| + |6−3| = 4 + 3 = 7
Chebyshev:
- max(|5−1|, |6−3|) = max(4, 3) = 4
Minkowski (p=4):
- (|5−1|⁴ + |6−3|⁴)^(1/4) = (256 + 81)^0.25 = (337)^0.25 ≈ 4.28
Verification of ordering: Chebyshev (4) ≤ Euclidean (5) ≤ Manhattan (7) 

## Example 02 — MEDIUM: Full KNN Classification (Rain Prediction)

Problem: 15 observations of Humidity & Temperature. Predict if it rains when Humidity=84, Temp=34 with K=5, Euclidean distance.

Step 1: K=5, Euclidean distance chosen.
Step 2: Compute distances. Example for Obs 1: √[(58−84)² + (19−34)²] = √[676+225] = √901 ≈ 31.62
Step 3: Sort all 15 distances. Top 5 nearest:
- Obs 5: distance = 18.25 → Rain = 1
- Obs 12: distance = 18.97 → Rain = 1
- Obs 6: distance = 21.02 → Rain = 1
- Obs 7: distance = 21.59 → Rain = 1
- Obs 9: distance = 22.36 → Rain = 0
Step 4: Among K=5 neighbours → Rain=1 appears 4 times, Rain=0 appears 1 time.
Step 5: Maximum voting → Prediction: Rain = 1 (Yes, it will rain!)

## Example 03 — EXAM-LEVEL: 3D KNN Classification

Problem: 6 points in 3D space. Classify P=(4,3,5) with K=3 using Euclidean.
Training data:
- A=(2,3,4) → Red, B=(5,1,6) → Blue, C=(3,4,5) → Red
- D=(6,2,3) → Blue, E=(4,4,6) → Red, F=(5,3,4) → Blue
Computing distances from P=(4,3,5):
- d(P,A) = √[(4−2)²+(3−3)²+(5−4)²] = √[4+0+1] = √5 ≈ 2.24 → Red
- d(P,B) = √[(4−5)²+(3−1)²+(5−6)²] = √[1+4+1] = √6 ≈ 2.45 → Blue
- d(P,C) = √[(4−3)²+(3−4)²+(5−5)²] = √[1+1+0] = √2 ≈ 1.41 → Red
- d(P,D) = √[(4−6)²+(3−2)²+(5−3)²] = √[4+1+4] = √9 = 3.00 → Blue
- d(P,E) = √[(4−4)²+(3−4)²+(5−6)²] = √[0+1+1] = √2 ≈ 1.41 → Red
- d(P,F) = √[(4−5)²+(3−3)²+(5−4)²] = √[1+0+1] = √2 ≈ 1.41 → Blue
Sort and pick top 3: C (1.41, Red), E (1.41, Red), F (1.41, Blue)
Vote: 2 Red vs 1 Blue → P is classified as Red 


## Example 04 — EASY: Naive Bayes — Spam or Ham? ("Good Work")

Problem: Given P(Spam)=0.15, P(Ham)=0.85. Likelihoods: P(Good|Spam)=0.04, P(Good|Ham)=0.25, P(Work|Spam)=0.10, P(Work|Ham)=0.30. Classify "Good Work".
Calculate Posterior for Spam:
- P(Spam | Good, Work) = 0.15 × 0.04 × 0.10 = 0.0006
Calculate Posterior for Ham:
- P(Ham | Good, Work) = 0.85 × 0.25 × 0.30 = 0.0638
Compare: 0.0638 > 0.0006 → Classified as Ham!
Normalized probability: P(Ham) = 0.0638 / (0.0638 + 0.0006) = 99.1% confident.

## Example 05 — MEDIUM: Naive Bayes with Laplace Smoothing ("Horoscope Money Money Snack")

Problem: P(Spam)=0.15, P(Ham)=0.85.
Original frequency table (6 unique words):
- Good: Spam=2, Ham=10
- Lonely: Spam=2, Ham=1
- Horoscope: Spam=20, Ham=5
- Work: Spam=5, Ham=12
- Snacks: Spam=0 (problem!), Ham=5
- Money: Spam=21, Ham=7
- Totals: Spam=50, Ham=40
Problem spotted: P(Snacks|Spam) = 0/50 = 0 → entire product becomes 0! Need Laplace Smoothing (α=1).
Laplace-smoothed likelihoods (add 1 to every count; denominator += 1×6=6):
- P(Horoscope|Spam) = (20+1)/(50+6) = 21/56 = 0.375
- P(Horoscope|Ham) = (5+1)/(40+6) = 6/46 = 0.130
- P(Money|Spam) = (21+1)/(50+6) = 22/56 = 0.393
- P(Money|Ham) = (7+1)/(40+6) = 8/46 = 0.174
- P(Snacks|Spam) = (0+1)/(50+6) = 1/56 = 0.018
- P(Snacks|Ham) = (5+1)/(40+6) = 6/46 = 0.130
Classify "Horoscope, Money, Money, Snacks":
- P(Spam|H,M,M,S) = 0.15 × 0.375 × 0.393 × 0.393 × 0.018 ≈ 0.000156
- P(Ham|H,M,M,S) = 0.85 × 0.130 × 0.174 × 0.174 × 0.130 ≈ 0.000044
Compare: 0.000156 > 0.000044 → Classified as Spam!


## Example 06 — EXAM-LEVEL: Conditional Probability (Dice)
Problem: Two fair dice are rolled. The sum is 6. Find P(one die shows 2 | sum = 6).
Event A (sum=6): {(1,5), (2,4), (3,3), (4,2), (5,1)} → 5 outcomes out of 36.
Event B (one die shows 2): All combinations where at least one die is 2 → 11 outcomes out of 36.
A ∩ B (sum=6 AND a die shows 2): {(2,4), (4,2)} → 2 outcomes.
Apply conditional probability:
- P(B|A) = P(A ∩ B) / P(A) = (2/36) / (5/36) = 2/5 = 0.4

# TOPIC 12 — Common Exam Mistakes
## KNN Mistakes:
Mistake 1: Forgetting to normalize features before applying KNN.
- Fix: Always use StandardScaler or MinMaxScaler. KNN is distance-based — without scaling, large-range features dominate.
Mistake 2: Choosing even K for binary (2-class) classification → causes ties.
- Fix: Use odd K for 2 classes; use even K for 3 classes. They are opposite.
Mistake 3: Confusing Euclidean with Manhattan formula.
- Wrong: Forgetting the square root in Euclidean, or using absolute values wrong.
- Fix: Euclidean = √(sum of squares). Manhattan = sum of |differences|. No square root in Manhattan!
Mistake 4: Not sorting distances before picking K neighbours.
- Fix: Always sort all distances in ascending order FIRST, then pick the top-K smallest.
Mistake 5: Calling KNN an "eager" learner.
- Fix: KNN is LAZY — it does zero work during training. All work happens at prediction time.
Mistake 6: Applying KNN to high-dimensional data without caution.
- Fix: KNN suffers from the curse of dimensionality — distance becomes meaningless in very high dimensions.

## Naive Bayes Mistakes:
Mistake 1: Forgetting Laplace smoothing when a feature has count = 0.
- Fix: Always check for zero counts. Add α=1 to numerator AND adjust denominator by +α×V.
Mistake 2: Not dropping the denominator P(x) when comparing classes.
- Fix: P(x) is constant across classes — you compare only the numerators (prior × likelihoods).
Mistake 3: Calling Naive Bayes a "lazy" learner.
- Fix: NB is EAGER — it trains first (computes priors and likelihoods), then predicts.
Mistake 4: Confusing Prior, Likelihood, Posterior, and Evidence.
- Fix: Use the PLEP mnemonic: Posterior ∝ Likelihood × Prior (Evidence is dropped).
Mistake 5: Adding α only to numerator but NOT adjusting the denominator.
- Fix: New denominator = original total + (α × number of unique feature values).
Mistake 6: Thinking Naive Bayes requires feature scaling.
- Fix: Naive Bayes does NOT need normalization — it works with probabilities, not distances.

# TOPIC 13 — Viva & Exam Questions

## KNN Questions

Q1 (Easy): What type of learner is KNN?
- KNN is a lazy, instance-based, non-parametric learner.
- It stores all training data and performs all computation only at prediction time.

Q2 (Easy): Why is normalization important for KNN?
- KNN relies on distance calculations.
- Features with larger ranges dominate the distance metric, making smaller-range features irrelevant.
- Normalization puts all features on the same scale so each feature contributes fairly.

Q3 (Easy): What is the relationship between Minkowski, Euclidean, and Manhattan distances?
- Minkowski is the generalized form.
- When p=1 → becomes Manhattan.
- When p=2 → becomes Euclidean.
- When p→∞ → becomes Chebyshev.

Q4 (Medium): What happens when K=1 vs K=N?
- K=1 → Overfitting (high variance, low bias). One wrong neighbour flips the prediction. Sensitive to noise.
- K=N → Underfitting (high bias, low variance). Every new point gets classified as the majority class in the entire training set.

Q5 (Medium): How does Weighted KNN differ from standard KNN?
- Standard KNN: all K neighbours vote equally.
- Weighted KNN: closer neighbours have higher weight (weight = 1/distance).
- This makes the algorithm less sensitive to the choice of K.

Q6 (Medium): Can KNN be used for regression?
- Yes. Instead of majority voting, use the average (or weighted average) of the K neighbours' target values as the prediction.

Q7 (Tricky Viva): Is KNN a discriminative or generative model?
- KNN is neither exactly — it does not explicitly model P(y|x) or P(x,y).
- It is a non-parametric method that directly maps inputs to outputs using stored instances.
- It is often categorized as discriminative since it learns decision boundaries implicitly.

Q8 (Tricky Viva): Why does KNN suffer from the curse of dimensionality?
- In high-dimensional spaces, all points become approximately equidistant — the concept of "nearest" loses meaning.
- The volume of the space grows exponentially with dimensions, so data becomes very sparse.
- You would need exponentially more training data for KNN to remain effective.


## Naive Bayes Questions

Q1 (Easy): What does "Naive" mean in Naive Bayes?
- "Naive" refers to the simplifying assumption that all features are conditionally independent of each other given the class label.
- This is rarely true in practice but simplifies computation enormously.

Q2 (Easy): What is the zero-frequency problem?
- If a feature value never appears with a particular class in training data, its likelihood = 0.
- Since Naive Bayes multiplies likelihoods, the entire posterior becomes 0 regardless of other features.
- Solution: Laplace smoothing — add α to every count.

Q3 (Easy): Why can we drop the denominator P(x) when classifying?
- P(x) is the same for all classes (probability of observed features).
- Since we only compare posteriors across classes, a common factor does not change the result.
- Dropping it simplifies calculation without affecting which class wins.

Q4 (Medium): When would you choose MultinomialNB over GaussianNB?
- MultinomialNB: when features are counts or frequencies (e.g., word counts in text).
- GaussianNB: when features are continuous and approximately normally distributed (e.g., height, weight, temperature).

Q5 (Medium): What changes if P(Spam) = 0.50 instead of 0.15?
- The prior probability for spam increases significantly.
- The classifier is now more likely to classify borderline cases as spam.
- The prior acts as a "base rate" — a higher prior means the algorithm starts with a stronger belief that something is spam before even looking at features.

Q6 (Medium): How does Laplace smoothing affect the denominator?
- When you add α to each count, the total increases by α × (number of unique feature values).
- Example: 6 unique words, α=1 → new total = original total + 6.
- This is a critical step students often skip.

Q7 (Tricky Viva): Is Naive Bayes a generative or discriminative model?
- Naive Bayes is Generative.
- It models the joint probability P(x, class) = P(x|class) · P(class).
- It learns how data is generated per class (the likelihoods) and can theoretically generate new data points.
- Contrast: KNN and Logistic Regression are discriminative.

Q8 (Tricky Viva): If the independence assumption is usually violated, why does NB still work well?
- Even though probability estimates are often wrong, classification only requires the correct class to have the highest posterior — not the perfectly accurate posterior.
- The ranking among classes can be correct even with inaccurate absolute probabilities.
- This makes NB a surprisingly effective classifier despite its "naive" assumption.

# SMLC Session 4 — Decision Trees for Classification

# TOPIC 01 — What is a Decision Tree?
## Q: What is a Decision Tree in simple words?
- Imagine you are playing 20 Questions. Your friend thinks of something, and you keep asking Yes/No questions: "Is it alive?", "Can it fly?", "Is it bigger than a cat?"
- A Decision Tree does exactly the same thing with data.
- It asks a series of questions about the features (columns) of the data.
- Based on the answers, it arrives at a decision (like "Approve Loan" or "Reject Loan").
- It is a flowchart-like classifier with nodes (questions), edges/branches (answers), and leaf nodes (decisions).

## Q: What are the parts of a Decision Tree?
Root Node:
- The topmost node.
- Has no incoming edges (nothing above it).
- The feature with the highest Information Gain goes here.
- It is the first question asked.
Internal Node (Branch Node):
- A middle node with exactly one incoming edge and one or more outgoing edges.
- It represents a question/split that leads to further sub-questions.
Leaf Node (Terminal Node):
- A bottom node with one incoming edge and no outgoing edges.
- It holds the final class label — the decision.
- No more questions are asked after a leaf.
Pure Node:
- A node where all data points belong to the same class.
- Entropy = 0 at a pure node.
- When a node is pure, it automatically becomes a leaf — no need to split further.
Mnemonic: RIL → Root → Internal → Leaf (like Reliance Industries Limited).
- Root is the boss, Internals are managers, Leaves are workers who make the final call.

# TOPIC 02 — Information Theory & Entropy
## Q: What is Information Theory?
- Information Theory is a branch of mathematics that quantifies "surprise" in data.
- Key idea: Rare events carry more information than common events.
- Example: "The sun rose this morning" → No information (you expected it).
- Example: "There was a solar eclipse!" → Maximum information (very unexpected).

## Q: What is Self-Information?
- Self-Information measures how much information a single specific event provides.
Formula:
- I(x) = −log₂ P(x) [units: bits]
  - P(x) = probability of the event.
  - The negative sign makes the result positive (since log of a fraction is negative).
  - Low probability event → high self-information (big surprise).
  - High probability event → low self-information (not surprising).
## Q: What is Shannon's Entropy?
- Entropy measures the average uncertainty (impurity) across all classes in a dataset.
- It tells us how mixed-up (impure) a group is.
- Analogy: A bag of only red candies → zero surprise (Entropy = 0). Half red, half blue → maximum surprise (Entropy = 1 for binary). Entropy measures "how shuffled" your data is.
Formula:
- E = −Σ pᵢ · log₂(pᵢ) (sum over all classes)
  - pᵢ = proportion of samples in class i.
  - For each class: multiply its proportion by the log₂ of that proportion.
  - Sum all those terms, then negate the entire sum (the minus sign is OUTSIDE).
  - Result is always ≥ 0.
Special convention: When pᵢ = 0, the term 0 × log₂(0) = 0 by convention. Do NOT try to compute log(0) — it is undefined, but the limit is 0.
## Q: What are the key entropy values to remember?
- At a pure node (all same class): Entropy = 0 (no uncertainty at all).
- At 50-50 split (binary): Entropy = 1 (maximum confusion).
- Entropy is maximum at p = 0.5 and zero at the extremes.
- The entropy curve is an inverted U shape.
Entropy behaviour table (binary case):
- P(Class 1) = 0.0 → Entropy = 0
- P(Class 1) = 0.1 → Entropy = 0.47
- P(Class 1) = 0.3 → Entropy = 0.88
- P(Class 1) = 0.5 → Entropy = 1.00 (maximum)
- P(Class 1) = 0.7 → Entropy = 0.88
- P(Class 1) = 0.9 → Entropy = 0.47
- P(Class 1) = 1.0 → Entropy = 0
Mnemonic: "50-50 = Maximum Confusion" — coin flip = max entropy = 1.
## Q: What is Conditional Entropy?
- Conditional Entropy is the leftover entropy after you have asked a question and split the data.
- It is the weighted average of the entropies of all sub-groups created by the split.
Formula:
- E(T|X) = Σ P(c) · E(c) (weighted sum over categories of feature X)
  - For each category c of feature X:
    - Find what proportion of the data falls into that category: P(c) = (size of category c) / (total data).
    - Compute the entropy of just that category's data: E(c).
    - Multiply: P(c) × E(c).
  - Sum all these weighted entropies.
Interpretation:
- If a question perfectly separates things → Conditional Entropy = 0.
- If a question does not help at all → Conditional Entropy stays the same as before.

# TOPIC 03 — Information Gain
## Q: What is Information Gain (IG)?
- Information Gain is the reduction in entropy after splitting the data on a feature.
- It tells us how much a feature reduces our uncertainty about the target variable.
- We always pick the feature with the highest IG to split on — it cleans up the mess the most.
- IG(T, X) = E(T) − E(T|X)
  - E(T) = entropy of the target variable before the split (on the full dataset at this node).
  - E(T|X) = conditional entropy of target after splitting on feature X.
  - IG = the drop in entropy.
Key properties:
- IG is always ≥ 0. After splitting, purity can only stay the same or improve — entropy never increases after a split.
- IG = 0 means the feature tells us nothing useful.
- Higher IG → better split → use this feature.
Mnemonic: E-C-I-G → Every Clever Investor Gains
- Entropy first → Conditional Entropy next → Information Gain = E − C.

# TOPIC 04 — Gini Index & Classification Error
## Q: What is the Gini Index?
- Gini Index is another way to measure the impurity (messiness) of a node.
- It measures the probability that a randomly chosen sample from the node is misclassified.
- Analogy: A shopping bag with only apples → Gini = 0 (pure). A bag with apples, oranges, bananas equally → Gini is high. "If I randomly grabbed two items, how likely are they to be different?"
Formula:
- Gini = 1 − Σ pᵢ²
  - For each class: square its proportion.
  - Sum all squared proportions.
  - Subtract from 1.
Mnemonic: "GINI = Goes INto Impurity" → 1 minus something. "G" sounds like "G-one" → 1 minus squares.
Key values:
- Pure node (all same class): Gini = 0.
- 50-50 split (binary): Gini = 0.5 (maximum for binary).
- Range for binary classification: 0 to 0.5.
IG using Gini:
- IG(T, X) = Gini(T) − Gini(T|X)
- Same idea as entropy-based IG — compute before and after, pick highest.
## Q: What is Classification Error?
- The simplest impurity measure.
- It measures how many samples from the minority class would be misclassified if we just assigned the majority class to everyone.
Formula:
- Error = 1 − max(pᵢ)
  - max(pᵢ) = proportion of the majority (most common) class.
  - Subtract from 1.
Mnemonic: "1 minus the Boss" → The "boss" class (majority) is subtracted from 1. Bigger boss = smaller error.
Key values:
- Pure node: Error = 0.
- 50-50 split: Error = 0.5 (maximum for binary).
- Range for binary: 0 to 0.5.
Important: Classification Error is the least sensitive measure. It is NOT recommended for building trees — use Entropy or Gini instead. It only looks at the majority class and ignores the distribution of minority classes.

## Q: Compare Entropy vs Gini Index vs Classification Error — point-wise
- Formula: Entropy = −Σ pᵢ log₂(pᵢ); Gini = 1 − Σ pᵢ²; Class. Error = 1 − max(pᵢ).
- Range (binary): Entropy = 0 to 1; Gini = 0 to 0.5; Class. Error = 0 to 0.5.
- At pure node: All three = 0.
- At 50-50 split: Entropy = 1; Gini = 0.5; Class. Error = 0.5.
- Computation speed: Entropy is slowest (log calculation); Gini is faster (only squares); Class. Error is fastest (just find max).
- Sensitivity: Entropy is most sensitive to impurity; Gini is moderately sensitive; Class. Error is least sensitive.
- Used by: Entropy → ID3, C4.5, C5.0; Gini → CART (sklearn default); Class. Error → rarely used.
- Recommendation: Use Entropy when you want sensitivity; use Gini for speed; avoid Class. Error for tree building.

# TOPIC 05 — Building a Decision Tree (Step-by-Step)
## Q: What is the complete step-by-step process to build a Decision Tree?
Step 1: Calculate Entropy of the target variable E(T) using the full dataset at this level.
Step 2: For each feature X, build a contingency table with the target variable.
Step 3: Compute Conditional Entropy E(T|X) for each feature.
Step 4: Compute Information Gain = E(T) − E(T|X) for each feature.
Step 5: The feature with highest IG becomes the node (root if first split). Split the data on this feature.
Step 6: For each branch (category of the chosen feature), check if the child node is pure. If yes → stop, make it a leaf node.
Step 7: If not pure → repeat Steps 1–6 on the subset of data for that branch, using only remaining features (recursive).
Step 8: Stop when all nodes are pure OR all features have been exhausted.
Short version (mnemonic: E-C-I-G):
① E(Target) → ② E(Target|each feature) → ③ IG for each → ④ Highest IG = node → ⑤ Split → ⑥ Repeat on subset → ⑦ Stop when pure or no features left.

---
# TOPIC 06 — Handling Numeric (Continuous) Features
## Q: How does a Decision Tree handle numeric features?
- Numeric features have many possible values (e.g., Age: 21, 31, 45, 54...).
- We must convert them to binary "threshold" splits by finding the best cut point.
Step 1: Sort the data by the numeric feature in ascending order.
Step 2: Compute midpoints between consecutive distinct values.
- Example: Ages 21 and 31 → midpoint = (21+31)/2 = 26.
- If a value repeats (like 45 appears twice), it is only used once when computing midpoints.
Step 3: For each midpoint, split data into two groups: "≤ midpoint" and "> midpoint".
Step 4: Calculate Information Gain for each midpoint split.
Step 5: The midpoint with the highest IG becomes the threshold for that feature.
- Example: If midpoint 26 gives the highest IG, the feature becomes: Age ≤ 26 vs Age > 26.
Analogy: On Flipkart, you drag a price slider to filter phones. The midpoint method tries every possible slider position and picks the one that best separates "good" phones from "bad" phones.
---
# TOPIC 07 — Decision Tree Algorithms
## Q: What are the main Decision Tree algorithms?
Hunt's Algorithm:
- The foundation for all other Decision Tree algorithms.
- Based on recursive partitioning into purer subsets.
ID3 (Iterative Dichotomiser 3):
- Created by Ross Quinlan.
- Uses Entropy and Information Gain for splitting.
- Handles categorical data only — cannot handle numeric features.
- Produces multi-way splits (one branch per category value).
- Prone to overfitting.
- Does NOT handle missing values.
C4.5:
- Extension of ID3 by the same author (Quinlan).
- Uses Gain Ratio instead of Information Gain (Gain Ratio = IG / SplitInfo — reduces bias toward high-cardinality features).
- Handles categorical + numeric features.
- Handles missing data (represented as '?').
- Produces multi-way splits.
- Adds pruning to reduce overfitting.
C5.0:
- Improved version of C4.5.
- Uses Gain Ratio.
- Faster and more memory-efficient.
- Creates smaller trees.
- Better pruning.
- Handles categorical + numeric + missing data.
CART (Classification and Regression Trees):
- Created by Breiman et al.
- Uses Gini Index for classification.
- Produces binary splits only (two branches per split, regardless of how many categories a feature has).
- Can handle both classification (class labels) and regression (continuous output).
- Scikit-learn uses CART (DecisionTreeClassifier uses Gini by default).
- Uses surrogate splits for missing data.
---
## Q: Compare the four Decision Tree algorithms — point-wise
- Splitting criterion: ID3 = Entropy/IG; C4.5 = Gain Ratio; C5.0 = Gain Ratio; CART = Gini Index.
- Data types: ID3 = categorical only; C4.5 = categorical + numeric; C5.0 = categorical + numeric; CART = categorical + numeric.
- Missing values: ID3 = cannot handle; C4.5 = yes (uses '?'); C5.0 = yes; CART = surrogate splits.
- Tree type: ID3/C4.5/C5.0 = multi-way splits; CART = binary splits only.
- Speed: C5.0 and CART are fast; ID3 and C4.5 are moderate.
- Overfitting: ID3 is prone; C4.5/C5.0/CART add pruning.
- Sklearn: Uses CART (so default is Gini; you can switch to 'entropy').
- Mnemonic: "I Can Count" → ID3, C4.5, C5.0. Each one is better than the last.
---
## Q: What is Information Gain vs Gain Ratio?
- Information Gain (IG): IG = E(T) − E(T|X). Biased towards features with many categories (like Student ID which has 100 unique values — trivially creates pure nodes but overfits badly).
- Gain Ratio (GR): GR = IG / SplitInfo(X). Normalizes IG by the split information, which penalizes features with too many categories. Reduces the bias.
- Used by: IG → ID3; Gain Ratio → C4.5 and C5.0.
## Q: Compare Classification Tree vs Regression Tree
- Target variable: Classification Tree = categorical (class labels); Regression Tree = continuous (numeric).
- Split criteria: Classification = Entropy, Gini, Classification Error; Regression = Variance Reduction / MSE.
- Leaf output: Classification = class label (majority vote); Regression = mean or median of values.
- Example use: Classification = Approve/Reject loan; Regression = Predict house price.
# TOPIC 08 — Numerical Examples
## Example 01 — EASY: Calculate Entropy
Problem: 35 people — 20 Not-Obese, 15 Obese. Find the entropy.
Step 1: Find probabilities:
- P(Not-Obese) = 20/35 = 0.571
- P(Obese) = 15/35 = 0.429
Step 2: Apply formula E = −Σ pᵢ log₂(pᵢ):
- E = −[0.571 × log₂(0.571) + 0.429 × log₂(0.429)]
- E = −[0.571 × (−0.808) + 0.429 × (−1.222)]
- E = −[−0.461 + (−0.524)]
- E = −(−0.985)
- E = 0.985
Interpretation: Close to 1 → data is quite mixed (impure). Maximum for binary = 1.0 (at 50-50 split).

## Example 02 — EASY: Calculate Gini Index
Problem: Same dataset — 20 Not-Obese, 15 Obese. Find the Gini Index.
Step 1: Probabilities: P(Not-Obese) = 0.571, P(Obese) = 0.429.
Step 2: Apply Gini = 1 − Σ pᵢ²:
- Gini = 1 − [(0.571)² + (0.429)²]
- Gini = 1 − [0.326 + 0.184]
- Gini = 1 − 0.510
- Gini = 0.490 (close to max impurity of 0.5)
## Example 03 — MODERATE: Conditional Entropy & Information Gain
Problem (Obesity & Smoker feature): Total = 35 (20 Not-Obese, 15 Obese). Smoker feature: 22 smokers, 13 non-smokers.
The slide computes conditional entropy by looking at class groups:
For 20 Not-Obese people (15 are smokers, 5 are non-smokers):
- E(Not-Obese) = −(15/20)log₂(15/20) − (5/20)log₂(5/20)
- = −(0.75)(−0.415) − (0.25)(−2.0)
- = 0.311 + 0.500 = 0.811
For 15 Obese people (7 are smokers, 8 are non-smokers):
- E(Obese) = −(7/15)log₂(7/15) − (8/15)log₂(8/15)
- = −(0.467)(−1.100) − (0.533)(−0.907)
- = 0.514 + 0.483 = 0.997
Conditional Entropy:
- E(Obesity|Smoker) = P(Not-Obese) × E(Not-Obese) + P(Obese) × E(Obese)
- = (20/35)(0.811) + (15/35)(0.997)
- = (0.571)(0.811) + (0.429)(0.997)
- = 0.463 + 0.428
- E(Obesity|Smoker) = 0.890
Information Gain:
- IG = E(Obesity) − E(Obesity|Smoker) = 0.985 − 0.890 = 0.095
Interpretation: Knowing whether someone smokes reduces uncertainty about obesity by only 0.095 bits — relatively low information gain.
---
## Example 04 — EXAM-LEVEL: Build a Decision Tree
Problem: Loan dataset with 4 features. Information Gains computed:
- Employed = 0.030
- Credit Score = 0.331 (highest)
- Income = 0.185
- Dependents = 0.282
Step 1: Highest IG = Credit Score (0.331) → becomes Root Node.
Step 2: Split on Credit Score:
- Credit Score = High → all 7 records are "Approved" → Pure node (Leaf) 
- Credit Score = Low → 8 records, mix of Approved & Rejected → Not pure, continue splitting.
Step 3: For the Low Credit Score subset, recompute IG on remaining 3 features:
- Employed = 0.159
- Income = 0.610
- Dependents = 0.954 (highest)
Step 4: Split on Dependents:
- Dependents = Yes → all Rejected → Leaf: Reject 
- Dependents = No → all Approved → Leaf: Approve 
Final Decision Tree:
```
         Credit Score?
        /             \
      High             Low
       |                 |
   APPROVE         Dependents?
                   /          \
                 Yes            No
                  |              |
              REJECT          APPROVE
```
## Example 05 — EXAM-LEVEL: Information Gain for a Numeric Feature
Problem: Age and Loan data (sorted):
- Ages: 21, 31, 45, 45, 54, 56, 58
- Loans: Appr, Rej, Appr, Rej, Appr, Rej, Rej
Step 1: Compute midpoints (between consecutive distinct values; 45 appears twice, use once):
- (21+31)/2 = 26
- (31+45)/2 = 38
- (45+54)/2 = 49.5
- (54+56)/2 = 55
- (56+58)/2 = 57
Step 2: Try midpoint = 26:
- Age ≤ 26: {21} → 1 Approved, 0 Rejected → E = 0 (pure!)
- Age > 26: {31, 45, 45, 54, 56, 58} → 2 Approved, 4 Rejected
E(target) = −(3/7)log₂(3/7) − (4/7)log₂(4/7) = 0.985
E(≤26) = 0 (pure)
E(>26) = −(2/6)log₂(2/6) − (4/6)log₂(4/6)
= −(0.333)(−1.585) − (0.667)(−0.585) = 0.528 + 0.390 = 0.918
E(T|Age≤26) = (1/7)(0) + (6/7)(0.918) = 0.787
IG = 0.985 − 0.787 = 0.198 (for midpoint 26)
Step 3: Repeat for all midpoints. From the slides, midpoint 26 gives the highest IG ≈ 0.592. So the final split threshold is: Age < 26.
Key note: Repeated values (like 45 appearing twice) are only considered once when computing midpoints.
# TOPIC 09 — Common Exam Mistakes
## Mistake 1: Forgetting the negative sign in the entropy formula.
- Wrong: E = Σ pᵢ log₂(pᵢ) → this gives a negative number.
- Correct: Entropy = MINUS Σ pᵢ log₂(pᵢ). Since log of a fraction is always negative, the minus sign makes the result positive.
- If your entropy answer is negative → you forgot the sign!
## Mistake 2: Using ln (natural log) instead of log₂.
- Decision trees use log base 2 (giving units of "bits").
- Using natural log gives different numerical values.
- Always check what the question asks for.
## Mistake 3: Trying to compute 0 × log₂(0).
- By convention: 0 × log₂(0) = 0.
- Do NOT try to compute log(0) — it is undefined.
- But the mathematical limit of p × log(p) as p → 0 is 0, so we just set the whole term to 0.
## Mistake 4: Not recomputing entropy on the subset.
- Wrong: Using the full dataset entropy at every level of the tree.
- Correct: At each level, you work on a subset of data. You MUST recalculate the entropy of the target for that subset.
- The original full-data entropy only applies at the root level.
## Mistake 5: Confusing Gini range with Entropy range.

- Binary case: Entropy max = 1, Gini max = 0.5.
- Do NOT say "Gini max is 1" — it is 0.5 for binary.
- All three measures (Entropy, Gini, Class. Error) = 0 at pure nodes.
## Mistake 6: Saying "Information Gain can be negative."
- IG is always ≥ 0. Entropy never increases after a split.

## Mistake 7: Forgetting to use the weighted average in Conditional Entropy.
- Wrong: Just averaging the sub-group entropies.
- Correct: E(T|X) is a weighted sum — each branch's entropy is multiplied by the proportion of samples going into that branch.
- Weight = (number of samples in that branch) / (total samples at this node).
## Mistake 8: Forgetting to sort before computing midpoints for numeric features.
- Wrong: Computing midpoints on unsorted data.
- Correct: Always sort ascending first, then compute midpoints between consecutive distinct values.
## Mistake 9: Picking the lowest IG instead of the highest.
- Wrong: "Pick the feature with lowest IG for the root."
- Correct: Always pick the feature with HIGHEST Information Gain. Higher IG = more useful feature = better split.
## Mistake 10: Thinking Classification Error is a good criterion for building trees.
- Classification Error is the least sensitive measure.
- It only considers the majority class and ignores minority class distribution.
- Example: A node with (0.5, 0.3, 0.2) and one with (0.5, 0.25, 0.25) have the same Classification Error (0.5) but different Entropy and Gini.
- Use Entropy or Gini for tree building. Classification Error is for rough estimation only.

# TOPIC 10 — Viva & Exam Questions
## Q1 (Easy): What is entropy in the context of decision trees?
- Entropy measures the impurity or heterogeneity of a dataset.
- It tells us how mixed the classes are.
- Entropy = 0 means pure (all same class).
- Entropy = 1 (binary) means maximum confusion (50-50 split).
- Formula: E = −Σ pᵢ log₂(pᵢ).
## Q2 (Easy): What is the difference between a root node and a leaf node?
- Root node: topmost node, no incoming edges, contains the feature with highest IG, the first question asked.
- Leaf node: bottom node, one incoming edge, no outgoing edges, holds the final class label (the decision).
## Q3 (Easy): Can Information Gain ever be negative?
- No. After splitting, purity can only increase or stay the same.
- Entropy either decreases or stays the same after a split.
- Therefore IG = E(before) − E(after) is always ≥ 0.
## Q4 (Medium): How does a decision tree handle numeric features?
1. Sort the numeric feature in ascending order.
2. Compute midpoints between consecutive distinct values.
3. For each midpoint, split data into ≤ midpoint and > midpoint.
4. Calculate IG for each midpoint split.
5. Pick the midpoint with the highest IG as the threshold.
## Q5 (Medium): Compare Entropy and Gini Index. When would you prefer one?
- Both measure impurity — lower is purer.
- Entropy uses logarithms (range 0–1 binary), is more sensitive to changes, used by ID3/C4.5.
- Gini uses squared probabilities (range 0–0.5 binary), is faster to compute, used by CART/sklearn.
- Use Gini for speed; use Entropy when you want more sensitivity to impurity.
## Q6 (Medium): What happens when two features have the same Information Gain?
- Typically, the first feature encountered (left to right in dataset) is chosen.
- Some implementations try both and evaluate which model performs better overall.
## Q7 (Tricky Viva): Why is Classification Error not recommended for tree building?
- It is the least sensitive measure.
- It only considers the majority class, ignoring the distribution among minority classes.
- Example: A node with (0.5, 0.3, 0.2) and one with (0.5, 0.25, 0.25) have the SAME Classification Error = 0.5.
- But they have different Entropy and Gini values, so Entropy/Gini can distinguish them while Classification Error cannot.
- This makes Classification Error a poor splitting criterion.
## Q8 (Tricky Viva): A feature has 100 unique values (e.g., Student ID). Will it have high IG? Is this a problem?
- Yes, it will likely have very high IG — splitting on 100 unique values can make each leaf contain exactly one sample (trivially pure).
- This is the "IG bias towards high-cardinality features" problem.
- C4.5 addresses this by using Gain Ratio = IG / SplitInfo, which penalizes features with too many categories.

# TOPIC 12 — Quick Revision Summary
## All Formulas
- Self-Information: I(x) = −log₂ P(x)
- Entropy: E = −Σ pᵢ · log₂(pᵢ)
- Conditional Entropy: E(T|X) = Σ P(c) · E(c)  [weighted sum]
- Information Gain: IG(T, X) = E(T) − E(T|X)
- Gini Index: Gini = 1 − Σ pᵢ²
- IG using Gini: IG(T,X) = Gini(T) − Gini(T|X)
- Classification Error: Error = 1 − max(pᵢ)
- Gain Ratio: GR = IG / SplitInfo(X)
"""


