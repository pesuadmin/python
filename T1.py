# DESCRIPTIVE STATISTICS
# Mean, SD, Variance, Z-Score, CV, IQR

# Q1-Q2 | Measures of Central Tendency + SD & Variance
# ---
# MEASURES OF CENTRAL TENDENCY
# 1. Mean (mu or x-bar):
#    Sum of all values divided by count. Most common average.
#    Formula: x-bar = (Sum of xi) / n
#
# 2. Median:
#    Middle value when sorted. Not affected by outliers.
#    Odd n: take the middle value
#    Even n: average of the two middle values
#
# 3. Mode:
#    Most frequently occurring value.
#    Can have multiple modes — bimodal or multimodal.
#
# STANDARD DEVIATION & VARIANCE
# Variance (sigma-squared):
#    Average of squared deviations from the mean.
#    Population: sigma^2 = Sum(xi - mu)^2 / N
#    Sample:     s^2     = Sum(xi - x-bar)^2 / (n - 1)
#
# Standard Deviation (sigma or s):
#    Square root of variance. Same units as the data.
#    Formula: sigma = sqrt(variance)
#    Low SD  -> data points are close to the mean
#    High SD -> data points are spread out


# Q3 | Greatest Standard Deviation — Which dataset?
# ---
# Question: Which dataset has the greatest SD?
#   a. [98, 99, 100, 101, 102]
#   b. [2, 4, 6, 8, 10]
#   c. [2, 10]
#
# Dataset a: Mean = 100. Deviations: -2, -1, 0, 1, 2
#   Variance = 10/4 = 2.5  =>  SD = 1.58
#
# Dataset b: Mean = 6. Deviations: -4, -2, 0, 2, 4
#   Variance = 40/4 = 10   =>  SD = 3.16
#
# Dataset c: Mean = 6. Deviations: -4, 4
#   Variance = 32/1 = 32   =>  SD = 5.66
#
# Answer: Dataset c has the greatest SD = 5.66
# Rule: SD measures SPREAD, not magnitude.
# Only 2 values far apart => maximum spread.
# Dataset a values are close together despite being large numbers.


# Q4 | Compare Two Samples — Mean and Standard Deviation
# ---
# Question:
#   Sample 1: [10, 9, 8, 7, 8, 6, 10, 6]
#   Sample 2: [10, 6, 10, 6, 8, 10, 8, 6]
#   Compare their mean and SD.
#
# Sample 1 — Mean:
#   (10+9+8+7+8+6+10+6) / 8 = 64/8 = 8.0
# Sample 1 — SD:
#   Deviations from 8: [2, 1, 0, -1, 0, -2, 2, -2]
#   Variance = (4+1+0+1+0+4+4+4) / 7 = 18/7 = 2.57
#   SD = 1.60
#
# Sample 2 — Mean:
#   (10+6+10+6+8+10+8+6) / 8 = 64/8 = 8.0
# Sample 2 — SD:
#   Deviations from 8: [2, -2, 2, -2, 0, 2, 0, -2]
#   Variance = (4+4+4+4+0+4+0+4) / 7 = 24/7 = 3.43
#   SD = 1.85
#
# Both samples have the same mean (8.0).
# Sample 2 has higher SD (1.85 vs 1.60) => more variability/spread.


# Q5 | Compute Mean of field_1
# ---
# field_1 = [10, 9, 8, 10, 11, 8, 9, 11, 8, 9, 14, 6, 7, 8, 9, 8, 7, 10]
#
# Sum = 10+9+8+10+11+8+9+11+8+9+14+6+7+8+9+8+7+10 = 162
# n = 18
# Mean = 162 / 18 = 9.0
#
# Python: np.mean([10,9,8,10,11,8,9,11,8,9,14,6,7,8,9,8,7,10])


# Q6 | Coefficient of Variation — Order Variables
# ---
# Question: Order from highest to lowest CV for the following:
#   Item_Weight      (mean=11.68, std=5.78)
#   Item_Visibility  (mean=0.066, std=0.052)
#   Item_MRP         (mean=141,   std=62.26)
#   Item_Outlet_Sales(mean=2181,  std=1706)
#   Profit           (mean=13.4,  std=1.7)
#
# Formula: CV = (Standard Deviation / Mean) x 100%
#
# Item_Weight:       5.78  / 11.68 x 100 = 49.5%
# Item_Visibility:   0.052 / 0.066 x 100 = 78.8%
# Item_MRP:          62.26 / 141   x 100 = 44.1%
# Item_Outlet_Sales: 1706  / 2181  x 100 = 78.2%
# Profit:            1.7   / 13.4  x 100 = 12.7%
#
# Ranking (High to Low):
# Item_Visibility (78.8%) > Item_Outlet_Sales (78.2%) > Item_Weight (49.5%)
#   > Item_MRP (44.1%) > Profit (12.7%)
#
# CV is useful for comparing variability across variables with different units.
# Higher CV = more variability relative to the mean.


# Q7 | Mean and SD of [10, 15, 20, 25, 30]
# ---
# Mean: (10+15+20+25+30) / 5 = 100/5 = 20
#
# Deviations from 20: [-10, -5, 0, 5, 10]
# Variance (sample): (100+25+0+25+100) / (5-1) = 250/4 = 62.5
# SD = sqrt(62.5) = 7.906
#
# Mean = 20, SD ≈ 7.91
# Note: Arithmetic progression with equal spacing of 5.
# For evenly spaced data, mean = middle value.


# Q8-Q9 | Z-Score Calculation
# ---
# Formula: Z = (X - mu) / sigma
#
# Q8: X=40, mu=45, sigma=5
#   Z = (40 - 45) / 5 = -5/5 = -1.0
#   Z = -1 means X=40 is exactly 1 SD BELOW the mean.
#
# Q9: X=30, mu=35, sigma=5
#   Z = (30 - 35) / 5 = -5/5 = -1.0
#   Same pattern — both values are 1 SD below their respective means.
#
# Z-score interpretation:
#   Z = 0      -> at the mean
#   Z = +2     -> 2 SD above the mean
#   |Z| > 2    -> potential outlier
#   |Z| > 3    -> likely outlier


# Q11 | Box-Plot Interpretation — Shape & Spread, 1996/1997/1998
# ---
# A box-plot displays: Min | Q1 | Median (Q2) | Q3 | Max
# Box = IQR (Q1 to Q3) — middle 50% of data
# Whiskers = range excluding outliers
# x marks = outliers
#
# Reading box-plots for 1996-1998 exam marks out of 100:
#
# 1998: Wide box (large IQR), long whiskers -> High spread/variability.
#       Median near center -> roughly symmetric distribution.
#
# 1997: Medium-width box, slightly asymmetric whiskers -> Moderate spread,
#       slight right skew (median closer to Q1).
#
# 1996: Narrower box than 1998 -> Lower spread.
#       Symmetric whiskers -> roughly normal distribution.
#
# Pass Percentage (pass mark = 50):
#   Median in all three years appears above 50 (around 60-70).
#   => Well over 50% of students passed each year.
#   1998 shows most variability (widest spread), 1996 shows least.
#
# Key box-plot rules:
#   Median above box centre  -> right skew
#   Median below box centre  -> left skew
#   Wide box                 -> high variability
#   Narrow box               -> low variability
#   Long upper whisker       -> few very high scores
#   Pass % ≈ proportion of box + upper whisker above the pass mark


# Q12 | Effect of Adding 7 to All Scores
# ---
# Question: Mean=75, SD=8. If 7 is added to every score, what happens?
#
# Rules for Transformations:
#   Adding/subtracting constant c: New Mean = Old Mean +/- c | New SD = UNCHANGED
#   Multiplying by constant k:     New Mean = k x Old Mean   | New SD = k x Old SD
#
# New Mean = 75 + 7 = 82
# New SD   = 8 (unchanged)
#
# Adding a constant shifts the distribution but does not change its spread.
# Shape remains identical, just translated 7 units to the right.
# If multiplied by 2: New Mean = 150, New SD = 16 (both change proportionally).


# Q13-Q14 | IQR, Quartiles
# ---
# Q13: Definition — Quartiles and IQR
#
# Quartiles: Values that divide sorted data into 4 equal parts.
#   Q1 (25th percentile): Below this, 25% of data falls
#   Q2 (50th percentile / Median): Middle of data
#   Q3 (75th percentile): Below this, 75% of data falls
#
# IQR (Interquartile Range) = Q3 - Q1
# Measures spread of the middle 50% of data. Robust to outliers.
#
# Q14: Calculate IQR for [4, 7, 12, 5, 15, 9, 2]
#   Step 1 — Sort: [2, 4, 5, 7, 9, 12, 15] (n=7)
#   Step 2 — Q2 (Median): Middle value = 7 (position 4)
#   Step 3 — Q1: Lower half = [2, 4, 5] -> median = 4
#   Step 4 — Q3: Upper half = [9, 12, 15] -> median = 12
#   IQR = Q3 - Q1 = 12 - 4 = 8
#
# Outlier rule:
#   Below Q1 - 1.5 x IQR = 4 - 12 = -8   -> outlier
#   Above Q3 + 1.5 x IQR = 12 + 12 = 24  -> outlier
#   No outliers present in this dataset.


# Q15 | Measures of Dispersion
# ---
# Measures of Dispersion describe how spread out data is around the central value.
#
# Range                 = Max - Min               | Simplest, affected by outliers
# Variance              = Sum(x - x-bar)^2 / (n-1)| Squared deviations
# Standard Deviation    = sqrt(Variance)           | Same units as data
# IQR                   = Q3 - Q1                 | Robust to outliers
# Coefficient of Variation = (SD / Mean) x 100%   | Relative measure, unit-free


# PROBABILITY — Basic Rules, Bayes Theorem, Conditional Probability

# Q16 | P(A) and P(B) from Sample Space
# ---
# Sample space = {a, b, c, d, e} with P = {0.1, 0.1, 0.2, 0.4, 0.2}
# A = {a, b, c}, B = {c, d, e}
#
# P(A) = P(a)+P(b)+P(c) = 0.1+0.1+0.2 = 0.4
# P(B) = P(c)+P(d)+P(e) = 0.2+0.4+0.2 = 0.8
#
# Check: P(A)+P(B) = 1.2 > 1 => A and B overlap at c  (P(A ∩ B) = P(c) = 0.2)
# A and B are NOT mutually exclusive.
# P(A ∪ B) = P(A)+P(B)-P(A ∩ B) = 0.4+0.8-0.2 = 1.0 = entire sample space.


# Q17 | P(e1) — 4 times as likely as others
# ---
# 4 outcomes: e1 is 4x as likely as each of the other 3. Find P(e1).
#
# Let P(e2) = P(e3) = P(e4) = x. Then P(e1) = 4x.
# All probabilities sum to 1: 4x + x + x + x = 1 => 7x = 1 => x = 1/7
# P(e1) = 4x = 4/7 ≈ 0.571


# Q18 | Identify Type I / Type II Error
# ---
# Question:
#   i.  Disease test is negative but patient IS infected.
#   ii. Biometric says person IS in the list when they are NOT.
#
# Case i: Test says NEGATIVE, patient is ACTUALLY POSITIVE (infected)
#   H0: "Patient is healthy" -> we FAIL TO REJECT H0
#   But H0 is FALSE (patient is infected)
#   => Type II Error (False Negative / beta error)
#
# Case ii: Biometric says IS in list, but person is NOT in list
#   H0: "Person is NOT in list" -> we REJECT H0 incorrectly
#   But H0 is TRUE
#   => Type I Error (False Positive / alpha error)
#
# Error table:
#   H0 True + Reject H0      = Type I Error (alpha)
#   H0 True + Fail to Reject = Correct
#   H0 False + Reject H0     = Correct (Power)
#   H0 False + Fail to Reject= Type II Error (beta)


# Q19 | Bayes — High Quality Light Bulbs (Warehouse)
# ---
# Proportions: High:Medium:Low = 1:2:2
# P(unsatisfactory): High=0.0, Medium=0.1, Low=0.2
# Two bulbs tested SATISFACTORY. Find P(high quality box).
#
# Bayes Formula:
#   P(Hi | E) = P(E | Hi) x P(Hi) / Sum_j[ P(E | Hj) x P(Hj) ]
#
# Priors: P(H) = 1/5 = 0.2, P(M) = 2/5 = 0.4, P(L) = 2/5 = 0.4
# P(sat) per bulb: P(sat|H)=1.0, P(sat|M)=0.9, P(sat|L)=0.8
# P(2 sat): P(sat^2|H)=1.0^2=1.0, P(sat^2|M)=0.9^2=0.81, P(sat^2|L)=0.8^2=0.64
#
# Numerator (High): 1.0 x 0.2 = 0.2
# Denominator:      0.2x1.0 + 0.4x0.81 + 0.4x0.64 = 0.2+0.324+0.256 = 0.78
#
# P(High | 2 satisfactory) = 0.2 / 0.78 = 0.256 ≈ 25.6%


# Q20 | Total Probability — Lamps lasting >100 hours
# ---
# Lamp types: 20% type1 (P=0.7), 30% type2 (P=0.4), 50% type3 (P=0.3)
# Find P(lamp lasts > 100 hrs).
#
# Total Probability Formula:
#   P(A) = P(A|T1)xP(T1) + P(A|T2)xP(T2) + P(A|T3)xP(T3)
#
# P(>100hrs) = 0.7x0.20 + 0.4x0.30 + 0.3x0.50
#            = 0.14 + 0.12 + 0.15
#            = 0.41
#
# 41% probability that a randomly selected lamp lasts more than 100 hours.


# Q21-Q23 | Bayes Theorem — Formula & Definition
# ---
# Bayes Theorem:
#   Describes how to update the probability of a hypothesis given new evidence.
#
# Formula: P(A|B) = [ P(B|A) x P(A) ] / P(B)
#
# Where:
#   P(A|B)  = Posterior probability  (what we want)
#   P(B|A)  = Likelihood             (probability of evidence given hypothesis)
#   P(A)    = Prior probability      (initial belief)
#   P(B)    = Marginal probability   (normalizing constant)
#
# Example: Medical testing.
#   A doctor uses a positive test result (B) to update the probability
#   that a patient has a disease (A).


# Q24 | Two Dice — Sum at least 9
# ---
# Two dice rolled simultaneously. Find P(sum >= 9).
#
# Total outcomes = 6 x 6 = 36
# Favorable outcomes:
#   Sum=9:  (3,6),(4,5),(5,4),(6,3)      = 4 outcomes
#   Sum=10: (4,6),(5,5),(6,4)            = 3 outcomes
#   Sum=11: (5,6),(6,5)                  = 2 outcomes
#   Sum=12: (6,6)                        = 1 outcome
#   Total favorable = 10
#
# P(sum >= 9) = 10/36 = 5/18 ≈ 0.278


# Q25 | Probability Not Blue — Marble Bag
# ---
# Total marbles: 5 red + 3 blue + 2 green = 10
# P(blue)     = 3/10
# P(not blue) = 1 - 3/10 = 7/10 = 0.7
#
# 70% probability of NOT picking a blue marble.
# Complement rule: P(not A) = 1 - P(A)


# Q26 | Medical Test — P(A), P(A'), P(B|A), P(B|A')
# ---
# Disease prevalence 1%. True positive = 95%. False positive = 3%.
# Events: A = has disease, B = test positive.
#
# P(A)   = 0.01  (1% have disease)
# P(A')  = 0.99  (99% do not have disease)
# P(B|A) = 0.95  (if diseased, test correctly identifies 95% of time)
# P(B|A')= 0.03  (if healthy, test incorrectly says positive 3% of time)
#
# Using Bayes:
#   P(A|B) = (0.95 x 0.01) / (0.95 x 0.01 + 0.03 x 0.99)
#          = 0.0095 / 0.0392
#          ≈ 24.2%
#
# Even with 95% accuracy, only ~24% of positive tests are truly diseased.
# This is due to low disease prevalence (base rate effect).


# Q28 | Fisherman — Where Most Likely if No Fish Caught?
# ---
# Priors: P(sea)=1/2, P(river)=1/4, P(lake)=1/4
# P(no fish|sea)=0.2, P(no fish|river)=0.6, P(no fish|lake)=0.4
#
# P(no fish) = 0.2x0.5 + 0.6x0.25 + 0.4x0.25 = 0.1+0.15+0.1 = 0.35
#
# P(sea|no fish)   = 0.2x0.5 / 0.35 = 0.10 / 0.35 = 0.286
# P(river|no fish) = 0.6x0.25 / 0.35 = 0.15 / 0.35 = 0.429
# P(lake|no fish)  = 0.4x0.25 / 0.35 = 0.10 / 0.35 = 0.286
#
# Most likely location: RIVER (43% probability)
# River has the highest probability of catching nothing.


# Q29 | Hypothesis Statements — Carrot Fields
# ---
# Farmer wants to know if carrot sizes DIFFER between fields.
#
# H0 (Null):        mu1 = mu2  (mean carrot size in field_1 = field_2, no difference)
# H1 (Alternative): mu1 != mu2 (mean carrot size differs, two-tailed test)
#
# Test to use: Independent two-sample t-test (comparing means of two groups)


# PROBABILITY DISTRIBUTIONS — Binomial, Poisson, Markov

# Q30, Q32 | Conditions for Binomial Distribution
# ---
# 5 Conditions for Binomial Distribution:
#   1. Fixed number of trials: n
#   2. Each trial has exactly TWO outcomes: Success (p) or Failure (1-p)
#   3. Trials are INDEPENDENT (outcome of one doesn't affect others)
#   4. Probability of success (p) is CONSTANT across all trials
#   5. We count the number of successes X in n trials
#
# Formula: P(X=k) = C(n,k) x p^k x (1-p)^(n-k)
#
# Examples: Tossing a coin n times, defective items in a batch, pass/fail in QC.


# Q31 | Discrete vs Continuous Probability Distributions
# ---
# Discrete Variable:
#   Countable values (0, 1, 2, ...)
#   P(X=x) can be non-zero
#   Described by PMF (Probability Mass Function)
#   P(a <= X <= b) = Sum of P(X=x)
#   Examples: Binomial, Poisson
#
# Continuous Variable:
#   Any value in a range
#   P(X=x) = 0 always (probability of exact value is zero)
#   Described by PDF (Probability Density Function)
#   P(a <= X <= b) = Integral of f(x) dx
#   Examples: Normal, Exponential


# Q36 | Binomial — 8 Computers, P(1 fails)
# ---
# n=8 computers, p=0.005 (probability of failure). Find P(exactly 1 fails).
#
# Formula: P(X=k) = C(n,k) x p^k x (1-p)^(n-k)
#
# P(X=1) = C(8,1) x (0.005)^1 x (0.995)^7
#         = 8 x 0.005 x 0.9654
#         = 0.0386 ≈ 3.86%
#
# About 3.86% chance that exactly 1 of the 8 computers fails on a given day.


# Q37 | Identify Distribution — Covid cases, Defects
# ---
# i)  Number of Covid cases per day        -> Poisson Distribution
#     Reason: Counts rare events in a fixed time interval at a known average rate.
#
# ii) Number of defects from inspected sample of size n -> Binomial Distribution
#     Reason: Fixed n trials, each item is defective or not (binary), constant p.
#
# Quick reference:
#   Fixed trials, binary outcome       -> Binomial
#   Rare events over time/space        -> Poisson
#   Continuous measurements            -> Normal
#   Waiting time between events        -> Exponential


# Q43 | Markov Chain — Transition Matrix & State Diagram
# ---
# Transition matrix P for states {1, 2, 3}:
#
#   P = | 1/2  1/4  1/4 |
#       | 1/3   0   2/3 |
#       | 1/2  1/2   0  |
#
# Each row = "from state"; each column = "to state".
#   From state 1: go to 1 (50%), to 2 (25%), to 3 (25%)
#   From state 2: go to 1 (33%), stay in 2 (0%), to 3 (67%)
#   From state 3: go to 1 (50%), to 2 (50%), stay in 3 (0%)
#
# Each row must sum to 1 (all transition probabilities sum to 1). Verified: TRUE.


# Q130 | Poisson — P(exactly 5 customers) at bank, lambda=3
# ---
# Average 3 customers per 15 minutes (lambda=3). Find P(exactly 5 in next 15 min).
#
# Formula: P(X=k) = (e^-lambda x lambda^k) / k!
#
# lambda=3, k=5
# P(X=5) = e^-3 x 3^5 / 5!
#         = 0.04979 x 243 / 120
#         = 12.098 / 120
#         = 0.1008 ≈ 10.08%
#
# Approximately 10% chance of exactly 5 customers arriving in any 15-minute interval.


# SAMPLING & CENTRAL LIMIT THEOREM

# Q44-Q46 | Central Limit Theorem — Definition & Usefulness
# ---
# Central Limit Theorem (CLT):
#   As sample size n increases (n >= 30), the sampling distribution of the sample
#   mean (x-bar) approaches a NORMAL DISTRIBUTION, regardless of the shape of
#   the population distribution.
#
# Mathematically: x-bar ~ N(mu, sigma^2 / n)
#   where mu = population mean, sigma^2 = population variance, n = sample size
#
# Usefulness:
#   1. Allows use of normal distribution tables for hypothesis testing even when
#      population is not normal.
#   2. Justifies z-tests and t-tests for large samples.
#   3. Enables confidence interval construction.
#   4. As n increases, standard error (sigma/sqrt(n)) decreases -> more precise estimates.
#
# CLT requires: random sampling, independent observations, n >= 30
#   (or smaller for already-normal populations).


# Q47 | Sample Size for CLT + Skewed Distributions
# ---
# Typical sample size for CLT: n >= 30 is the commonly accepted threshold.
#
# For highly skewed distributions:
#   More data needed — typically n >= 100 or even larger.
#   More skewed the population => larger n required for CLT to apply.
#   For extremely skewed distributions: n >= 200+ may be needed.
#   Alternative: Use non-parametric tests (Mann-Whitney, Kruskal-Wallis)
#   that do not require normality.


# Q48-Q52 | Point Estimate, Interval Estimate, Bootstrapping, Sampling Types, Monte Carlo
#
# ---
# POINT ESTIMATE VS INTERVAL ESTIMATE
# Point Estimate: Single value estimate of a population parameter.
#   Example: x-bar = 5.2 kg is a point estimate of mu (population mean weight).
#
# Interval Estimate (Confidence Interval):
#   Range of values likely to contain the true parameter.
#   Example: 95% CI = (4.8, 5.6) kg means we are 95% confident mu lies in this range.
#
# BOOTSTRAPPING
#   Resampling technique: draw repeated samples WITH REPLACEMENT from original data
#   to estimate sampling distributions and confidence intervals.
#   Use when: small sample size, unknown distribution, complex statistics.
#   Advantage: No assumption about population distribution required.
#
# TYPES OF SAMPLING (4 Types)
#   1. Simple Random Sampling: Every member has equal chance of selection.
#   2. Systematic Sampling: Every k-th member selected (e.g., every 10th person).
#   3. Stratified Sampling: Population divided into subgroups (strata); sample from each.
#   4. Cluster Sampling: Population divided into clusters; entire clusters selected randomly.
#
#   PES scenario (3 per batch): Stratified Sampling (batches = strata, 3 from each).
#
# MONTE CARLO ASSUMPTIONS
#   1. Random number generation is truly random.
#   2. Sufficient number of iterations for convergence.
#   3. The model accurately represents the real system.
#   4. Input parameters follow known probability distributions.
#   5. Independence between random samples.


# HYPOTHESIS TESTING — Theory, Conditions, Test Selection

# Q60-Q62 | Type I Error, Type II Error — Definitions & Examples
#
# ---
# Type I Error (alpha — False Positive):
#   Rejecting H0 when it is actually TRUE.
#   Example: Concluding a new drug works when it actually doesn't.
#   Example: Convicting an innocent person.
#   P(Type I Error) = alpha = significance level (usually 0.05)
#
# Type II Error (beta — False Negative):
#   Failing to reject H0 when it is actually FALSE.
#   Example: Concluding drug doesn't work when it actually does.
#   Example: Acquitting a guilty person.
#   P(Type II Error) = beta | Power of test = 1 - beta
#
# Drug Trial context:
#   Type I = saying drug works when it doesn't (dangerous — false hope)
#   Type II = saying drug doesn't work when it does (dangerous — missed benefit)
#
# Quality Control context:
#   Type II = passing a defective batch (dangerous)


# Q63-Q65 | t-test vs z-test Conditions + Z-test Statistic Formula
#
# ---
# When to use z-test: n >= 30 (large sample) AND population SD (sigma) is known.
# When to use t-test: n < 30 (small sample) AND/OR population SD unknown (use s).
#   t-test assumes population is approximately normal.
#
# One-sample t-test preferred when:
#   n < 30 and/or population SD unknown
#   Comparing sample mean to known population mean mu0
#   Population is approximately normal
#
# Z-test Statistic (Single Sample):
#   Z = (x-bar - mu0) / (sigma / sqrt(n))
#   x-bar = sample mean
#   mu0   = claimed population mean
#   sigma = population SD
#   n     = sample size


# Q66 | Normality Test Before t-test
# ---
# Yes, checking normality before a t-test is recommended,
# especially for small samples (n < 30).
#
# Preferred Normality Test: Shapiro-Wilk Test
#   Most powerful normality test for small-medium samples.
#   H0: data is normally distributed.
#   If p-value > 0.05  -> fail to reject H0 -> assume normality (OK to proceed)
#   If p-value <= 0.05 -> reject H0 -> data not normal -> use non-parametric test
#
# Other options: Q-Q plot (visual), Kolmogorov-Smirnov test (large samples)
#
# Python: from scipy.stats import shapiro; stat, p = shapiro(data)


# Q76 | Two-Sample t-test — Regular vs Low Fat Sales (GA dataset) | 4 marks
# ---
# Question: Is mean sales from Regular and Low Fat Item_Fat_Content the same?
#
# H0: mu_Regular = mu_Low_Fat (no difference in mean sales)
# H1: mu_Regular != mu_Low_Fat (means differ) — Two-tailed test
# alpha = 0.05
#
# Test to Use: Independent two-sample t-test
#   Reason: Comparing means of two independent groups (Regular vs Low Fat),
#   continuous target variable (Item_Outlet_Sales), normal distribution assumed.
#
# Python Steps:
#   Step 1 — Separate groups:
#     low_fat_sale = data[data['Item_Fat_Content']=='Low Fat']['Item_Outlet_Sales']
#     reg_sale     = data[data['Item_Fat_Content']=='Regular']['Item_Outlet_Sales']
#   Step 2 — Run t-test:
#     t_stat, p_val = stats.ttest_ind(low_fat_sale, reg_sale)
#   Step 3 — Decision rule:
#     If p_val < 0.05  -> Reject H0 -> Means are significantly different
#     If p_val >= 0.05 -> Fail to reject H0 -> No significant difference
#
# Expected result (based on dataset): p-value > 0.05 -> Fail to reject H0
# -> No significant difference in mean sales between Regular and Low Fat items.


# ANOVA — Theory & ANOVA Table

# Q85-Q86 | ANOVA — Definition, Purpose, vs Multiple t-tests
#
# ---
# ANOVA = Analysis of Variance
# Purpose: Tests whether means of THREE OR MORE groups are significantly different.
#
# H0: mu1 = mu2 = mu3 = ... = muk (all group means are equal)
# H1: At least one group mean differs
#
# Why preferred over multiple paired t-tests?
#   With k groups, we need C(k,2) = k(k-1)/2 t-tests.
#   For 3 groups -> 3 t-tests; for 5 groups -> 10 t-tests.
#   Each test at alpha=0.05 -> Type I error inflates:
#     1 - (0.95)^3 ≈ 14.3% for 3 tests alone.
#   ANOVA controls family-wise error rate in a single test.
#   More efficient and statistically sound.


# Q87 | Fill ANOVA Table — Version 1
# ---
# Given: SS_treatment=1000, SS_total=1500, df_error=3, MS_error=166
#
# ANOVA Table Relationships:
#   SS_total   = SS_treatment + SS_error
#   MS         = SS / df
#   F          = MS_treatment / MS_error
#   df_total   = df_treatment + df_error = N - 1
#
# SS_error        = 1500 - 1000 = 500
# Verify:  MS_error = 500 / 3 = 166.7 ≈ 166 (confirmed)
# df_total = 27, df_error = 3 => df_treatment = 27 - 3 = 24
# MS_treatment    = 1000 / 24 = 41.67
# F               = 41.67 / 166 = 0.251
#
# F = 0.251 < 1 -> Treatment effect is LESS than random error variation.
# => NOT significant. Fail to reject H0.


# Q88 | Fill ANOVA Table — Version 2
# ---
# Given: SS_treatment=2000, df_error=4, SS_total=2500, df_total=29
#
# SS_error        = 2500 - 2000 = 500
# df_treatment    = df_total - df_error = 29 - 4 = 25
# MS_treatment    = 2000 / 25 = 80
# MS_error        = 500 / 4 = 125
# F               = 80 / 125 = 0.64
#
# F = 0.64 < 1 -> No significant treatment effect. Fail to reject H0.


# Q93 | Landing Page Conversion — Statistical Test Name
# ---
# Comparing conversion rates (binary: purchase or not) among 3 landing page designs (A, B, C).
#
# Test to use: Chi-Square Test of Independence
#   Reason: Comparing proportions across 3 groups with categorical data (purchased: yes/no).
#   A contingency table is built (3 designs x 2 outcomes).
#   Chi-square tests if design and conversion are independent.
#
# Alternative: If comparing MEAN conversion rates -> One-Way ANOVA.


# CHI-SQUARE TEST — Theory

# Q94 | Chi-Square Goodness of Fit — Brief Explanation
# ---
# Chi-Square Goodness of Fit Test:
#   Tests whether observed frequencies match expected frequencies from a
#   theoretical distribution.
#
# H0: Data follows the specified distribution (observed = expected)
# H1: Data does NOT follow the specified distribution
#
# Formula: chi^2 = Sum [ (Oi - Ei)^2 / Ei ]
#   where Oi = observed frequency, Ei = expected frequency
#
# df = k - 1  (k = number of categories)
# Reject H0 if chi^2 > chi^2_critical   OR   p-value < alpha
#
# Example: Test if a die is fair — expect each face to appear n/6 times.
# Compare observed counts to expected counts using this formula.


# THEORY DEFINITIONS — p-value, Normal Distribution, Data Scales, etc.

# Q121 | Standard Normal Distribution
# ---
# Standard Normal Distribution:
#   A special case of the normal distribution with:
#   Mean (mu) = 0 and Standard Deviation (sigma) = 1
#   Notation: Z ~ N(0, 1)
#
# Any normal distribution X ~ N(mu, sigma^2) can be standardized using:
#   Z = (X - mu) / sigma
#
# Properties:
#   Bell-shaped, symmetric about z = 0
#   68% of data within +/- 1 sigma
#   95% of data within +/- 2 sigma
#   99.7% of data within +/- 3 sigma
#   Total area under curve = 1


# Q122, Q128 | p-value Definition
# ---
# p-value:
#   The probability of observing a test statistic as extreme as (or more extreme than)
#   the one computed, ASSUMING H0 is TRUE.
#
# Interpretation:
#   p-value <= alpha (e.g., 0.05) -> Reject H0 -> Result is statistically significant
#   p-value > alpha               -> Fail to reject H0 -> Insufficient evidence
#
# Very low p-value means:
#   The observed result is highly unlikely by chance alone if H0 were true.
#   Strong evidence against H0 => reject H0.
#
# p = 0.001 -> Very strong evidence against H0 (0.1% chance under H0)
# p = 0.03  -> Significant at alpha=0.05 (reject H0)
# p = 0.12  -> Not significant (fail to reject H0)
#
# Note: p-value does NOT measure effect size or practical significance.
#
# Common misinterpretations to AVOID:
#   WRONG: "p=0.05 means 5% chance H0 is true"
#   WRONG: "p=0.05 means 95% chance result is real"
#   CORRECT: "p=0.05 means if H0 were true, we'd see this result only 5% of the time"


# Q123 | Ordinal vs Interval Data Scales
# ---
# Ordinal Scale:
#   Yes order (ranked). No equal intervals. No true zero.
#   Math: rank comparison only. Stats: median, mode valid.
#   Example: Movie ratings (1-5 stars), Education level
#
# Interval Scale:
#   Yes order. Yes equal intervals. No true zero.
#   Math: addition/subtraction valid. Stats: mean, SD valid.
#   Example: Temperature (degrees C), IQ scores
#
# Key difference:
#   Ordinal: gap between 1st and 2nd rank may NOT equal gap between 2nd and 3rd.
#   Interval: gaps between any consecutive values ARE equal.


# Q124 | Inferential Statistics
# ---
# Inferential Statistics:
#   Using data from a sample to draw conclusions about the larger population.
#   Example: Surveying 1000 voters to predict election outcome for 10 million voters.


# Q125 | Histogram vs Boxplot
# ---
# Histogram:
#   Shows distribution shape and frequency.
#   Outliers not explicitly shown.
#   Hard to compare multiple groups.
#   Skewness visible in shape.
#
# Boxplot:
#   Shows summary statistics (Q1, Q2, Q3).
#   Outliers explicitly shown as dots.
#   Easy to compare multiple groups.
#   Skewness visible from median position in box.


# Q126 | Marginal vs Conditional Probability
# ---
# Marginal Probability P(A):
#   Probability of event A regardless of any other event.
#   Example: P(customer buys) = 0.3
#
# Conditional Probability P(A|B):
#   Probability of A GIVEN that B has already occurred.
#   Formula: P(A|B) = P(A ∩ B) / P(B)
#   Example: P(buys | viewed ad) = 0.5 -> those who saw the ad buy more.


# Q129 | t-test vs z-test Comparison
# ---
# z-test: n >= 30, population SD known (sigma), uses normal distribution.
#   Formula: z = (x-bar - mu) / (sigma / sqrt(n))
#   df: Not needed
#
# t-test: n < 30, population SD unknown (use s), uses t-distribution.
#   Formula: t = (x-bar - mu) / (s / sqrt(n))
#   df = n - 1
