import numpy as np
import pandas as pd
from scipy import stats
import sympy as sp
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')


# Calculate mean and Standard Deviation
import numpy as np

# data
ddof = 1
samples = {
    "Sample 1": np.array([10, 9, 8, 10, 11, 8, 9, 11, 8, 9, 14, 6, 7, 8, 9, 8, 7, 10]),
    "Sample 2": np.array([10, 6, 10, 6, 8, 10, 8, 6])  ,
    "Sample 3": np.array([2, 10])  
}

# Calc
std_dict = {}
for name, sample in samples.items():
    n = len(sample)
    mean = np.mean(sample)
    std = np.std(sample, ddof=ddof)
    std_dict[name] = std
    print(f'{name} -> n={n}, mean={mean:.3f}, s={std:.3f}')
highest_sample = max(std_dict, key=std_dict.get)
print("\nHighest Standard Deviation:")
print(f'{highest_sample} = {std_dict[highest_sample]:.3f}')


# Find the Z-test given  the value of $X = 40$, where mean = 45, standard deviation = 5.

# Data
mu0, sigma, n, xbar = 45, 5, 1, 40
#Calc
alpha = 0.05

z = (xbar - mu0) / (sigma / np.sqrt(n))   # with n=1: z = (X - mu) / sigma
print(f'Z-score = {z:.4f}')


# Normal Distribution

from scipy.stats import norm

# Data.  # Use required if statement from Calc

mu = 6000
sigma = 100

question_type = "less_than"

# less_than / greater_than / between / percentile

x = 6250          # for less_than or greater_than

x1 = 5800         # lower bound for between
x2 = 5900         # upper bound for between

area = 0.05       # percentile questions
                  # Exceeded by 95% => 0.05
                  # Top 15%       => 0.85
                  # Bottom 15%    => 0.15

# Calc

if question_type == "less_than":
    z = (x - mu) / sigma
    prob = norm.cdf(z)
    print(f"Z = {z:.4f}")
    print(f"P(X < {x}) = {prob:.4f}")

elif question_type == "greater_than":
    z = (x - mu) / sigma
    prob = 1 - norm.cdf(z)
    print(f"Z = {z:.4f}")
    print(f"P(X > {x}) = {prob:.4f}")

elif question_type == "between":
    z1 = (x1 - mu) / sigma
    z2 = (x2 - mu) / sigma
    prob = norm.cdf(z2) - norm.cdf(z1)
    print(f"Z1 = {z1:.4f}")
    print(f"Z2 = {z2:.4f}")
    print(f"P({x1} < X < {x2}) = {prob:.4f}")

elif question_type == "percentile":
    z = norm.ppf(area)
    x = mu + z * sigma
    print(f"Z = {z:.4f}")
    print(f"X = {x:.4f}")


# Confidence interval - One Sample t-test - if greater or lesser not given - go with two sided

#Inference 
# We are 95% confident that the true average app rating lies between the lower and upper confidence limits.
# Since the ratings are close to 5, user satisfaction appears high.

import numpy as np
from scipy import stats

# Data

# data = [7.5, 6.8, 7.2, 6.5, 7.0, 6.9, 6.7, 7.3, 6.6, 6.8, 7.1, 6.9]
data = (7.5, 6.8, 7.2, 6.5, 7.0, 6.9, 6.7, 7.3, 6.6, 6.8, 7.1, 6.9)
test_type = 'two-sided'  # greater - right  or less - left
alpha = 0.05  # 95% Confidence Interval
mu0 = None      # Put hypothesized mean if t-test needed
               # Example: 30, 5.2, 7
               # Leave None if only CI needed

# Stats
n = len(data)
xbar = np.mean(data)
s = np.std(data, ddof=1)
se = s / np.sqrt(n)
print(f"n = {n}")
print(f"Mean = {xbar:.4f}")
print(f"Std Dev = {s:.4f}")

# Normality Test
print("\n--- Normality Test (Shapiro-Wilk) ---")
shapiro_stat, shapiro_p = stats.shapiro(data)
print(f"Statistic = {shapiro_stat:.4f}")
print(f"P-value   = {shapiro_p:.4f}")

if shapiro_p > alpha:
    print("Fail to Reject H0")
    print("Data appears Normal")
else:
    print("Reject H0")
    print("Data is NOT Normal")

# T-Test
if mu0 is not None:

    print("\n--- One Sample t-test ---")
    t_stat, p_value = stats.ttest_1samp(data, popmean=mu0, alternative = test_type) 
    print(f"t statistic = {t_stat:.4f}")
    print(f"p-value     = {p_value:.4f}")

    if p_value < alpha:
        print("Reject H0")
    else:
        print("Fail to Reject H0")

# CI

print("\n--- 95% Confidence Interval ---")
t_critical = stats.t.ppf(1-alpha/2, df=n-1)
ME = t_critical * se
lower = xbar - ME
upper = xbar + ME

print(f"CI = ({lower:.4f}, {upper:.4f})")


# Two Sample - Independent - t-test

import numpy as np
from scipy import stats

# input

sample1 = np.array([3.1, 2.9, 3.5, 3.2, 3.0, 3.3, 2.8, 3.4, 3.1, 3.2])
sample2 = np.array([2.2, 2.5, 2.3, 2.1, 2.4, 2.0, 2.3, 2.5, 2.2, 2.1])

alpha = 0.05
# Test Type
test_type = 'greater'     # 'two-sided', 'greater', 'less'
# Variance Assumption
equal_var = True            # True = pooled t-test # equal homogeneity variance
                            # False = Welch's t-test # no equal Variance and SD are different
confidence_level = 0.95

# Calc
n1 = len(sample1)
n2 = len(sample2)
mean1 = np.mean(sample1)
mean2 = np.mean(sample2)
s1 = np.std(sample1, ddof=1)
s2 = np.std(sample2, ddof=1)
print("GROUP 1")
print("n =", n1)
print("mean =", mean1)
print("std =", s1)

print("\nGROUP 2")
print("n =", n2)
print("mean =", mean2)
print("std =", s2)

# Hypothesis Test
t_stat, p_value = stats.ttest_ind(sample1,sample2,equal_var=equal_var,alternative=test_type)

print("\nT-TEST")
print("t statistic =", t_stat)
print("p-value =", p_value)

if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to Reject H0")

# CI

diff = mean1 - mean2

if equal_var:

    sp2 = (((n1-1)*(s1**2)) +((n2-1)*(s2**2))) / (n1+n2-2)
    se = np.sqrt(sp2*(1/n1 + 1/n2))
    df = n1 + n2 - 2

else:

    se = np.sqrt((s1**2)/n1 + (s2**2)/n2)
    df = (((s1**2/n1 + s2**2/n2)**2)/(((s1**2/n1)**2)/(n1-1)+((s2**2/n2)**2)/(n2-1)))

alpha_ci = 1 - confidence_level

t_critical = stats.t.ppf(1 - alpha_ci/2,df)

ME = t_critical * se

lower = diff - ME
upper = diff + ME

print("\nCONFIDENCE INTERVAL")
print(f"{confidence_level*100:.0f}% CI")
print((lower, upper))


# Two Sample - Paired - t-test

# ============================================================
# PAIRED T-TEST 
# Supports:
#   alternative = "greater"   -> mean(before-after) > 0
#   alternative = "less"      -> mean(before-after) < 0
#   alternative = "two-sided" -> mean(before-after) != 0
#
# Examples:
#   Height Increase      -> alternative = "less"
#   Sugar Higher Before  -> alternative = "greater"
#   Body Fat Decrease    -> alternative = "greater"
#   Cholesterol Decrease -> alternative = "greater"
# ============================================================

import numpy as np
from scipy import stats

#Input
before = [200, 190, 220, 180, 170, 170, 180]
after  = [150, 140, 140, 130, 130, 120, 140]

alpha = 0.05
alternative = "greater"      # "greater", "less", "two-sided"

# Normality Check
diff = np.array(before) - np.array(after)
shapiro_stat, shapiro_p = stats.shapiro(diff)
print("===== NORMALITY TEST (Shapiro-Wilk) =====")
print(f"Statistic = {shapiro_stat:.4f}")
print(f"P-value   = {shapiro_p:.4f}")

if shapiro_p > alpha:
    print("Conclusion: Differences are normally distributed.")
    print("Appropriate Test: Paired t-test")
else:
    print("Conclusion: Differences are NOT normally distributed.")
    print("Appropriate Test: Wilcoxon Signed-Rank Test")

# Paired Test
print("\n===== PAIRED T-TEST =====")

t_stat, p_value = stats.ttest_rel(before, after)
# Convert two-sided p-value to requested alternative
if alternative == "greater":
    if t_stat > 0:
        p_value = p_value / 2
    else:
        p_value = 1 - (p_value / 2)

elif alternative == "less":
    if t_stat < 0:
        p_value = p_value / 2
    else:
        p_value = 1 - (p_value / 2)

# For two-sided keep original p-value

print(f"Alternative Hypothesis: {alternative}")
print(f"t-statistic = {t_stat:.4f}")
print(f"p-value     = {p_value:.6f}")

if p_value < alpha:
    print("Decision: Reject H0")
else:
    print("Decision: Fail to Reject H0")

# Mean
n = len(diff)
mean_diff = np.mean(diff)
sd_diff = np.std(diff, ddof=1)
se = sd_diff / np.sqrt(n)

print("\n===== MEAN DIFFERENCE =====")
print(f"Mean Difference (Before - After) = {mean_diff:.4f}")

# CI 
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)

lower = mean_diff - t_critical * se
upper = mean_diff + t_critical * se

print("\n===== 95% CONFIDENCE INTERVAL =====")
print(f"({lower:.4f}, {upper:.4f})")

# Interpretation
print("\n===== INTERPRETATION =====")
print(f"Test Statistic = {t_stat:.4f}")
print("The test statistic measures how many standard errors")
print("the observed mean difference is from 0.")

print(f"\nP-value = {p_value:.6f}")
print("The p-value is the probability of observing a result")
print("at least as extreme as this assuming H0 is true.")


# ONE-WAY ANOVA TEMPLATE

import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Input
groups = {
    "Nozzle 1": [0.78, 0.80, 0.81, 0.75, 0.77, 0.78],
    "Nozzle 2": [0.85, 0.85, 0.92, 0.86, 0.81, 0.83],
    "Nozzle 3": [0.93, 0.92, 0.95, 0.89, 0.89, 0.83],
    "Nozzle 4": [1.14, 0.97, 0.98, 0.88, 0.86, 0.83],
    "Nozzle 5": [0.97, 0.86, 0.78, 0.76, 0.76, 0.75]
}

alpha = 0.05

# Hypothesis
print("===== HYPOTHESES =====")
print("H0: All population means are equal")
print("H1: At least one population mean differs")

# Normality
print("\n===== NORMALITY CHECK (Shapiro-Wilk) =====")

normal = True

for name, values in groups.items():
    stat, p = stats.shapiro(values)

    print(f"{name}: p-value = {p:.4f}")

    if p < alpha:
        normal = False

if normal:
    print("\nConclusion: Normality assumption satisfied.")
else:
    print("\nConclusion: Normality assumption violated.")

# Anova
anova_stat, anova_p = stats.f_oneway(*groups.values())

print("\n===== ONE-WAY ANOVA =====")
print(f"F-statistic = {anova_stat:.4f}")
print(f"p-value     = {anova_p:.6f}")

if anova_p < alpha:
    print("Decision: Reject H0")
    print("Conclusion: Significant difference exists among group means.")
else:
    print("Decision: Fail to Reject H0")
    print("Conclusion: No significant difference among group means.")

# Group means
print("\n===== GROUP MEANS =====")

means = {}

for name, values in groups.items():
    mean_val = np.mean(values)
    means[name] = mean_val
    print(f"{name}: {mean_val:.4f}")

highest = max(means, key=means.get)
lowest = min(means, key=means.get)

print(f"\nHighest Mean : {highest} ({means[highest]:.4f})")
print(f"Lowest Mean  : {lowest} ({means[lowest]:.4f})")


# TUKEY POST-HOC TEST

if anova_p < alpha:

    all_values = []
    labels = []

    for name, values in groups.items():
        all_values.extend(values)
        labels.extend([name] * len(values))

    tukey = pairwise_tukeyhsd(
        endog=np.array(all_values),
        groups=np.array(labels),
        alpha=alpha
    )

    print("\n===== TUKEY HSD POST-HOC TEST =====")
    print(tukey)

# Interpretation
print("\n===== INTERPRETATION =====")

print("ANOVA checks whether all population means are equal.")
print("A small p-value (< 0.05) indicates that at least one group mean differs significantly from the others.")

print("\nBased on means:")
print(f"{highest} has the highest average value.")
print(f"{lowest} has the lowest average value.")


# CHI-SQUARE GOODNESS 
# Examples: Grade Distribution, Demand by Day, Dice Fairness, Candy Flavors, Defect Types


import numpy as np
from scipy.stats import chisquare, chi2

# Input

observed = [14, 18, 32, 20, 16]      # Replace with observed frequencies
alpha = 0.05

# Expected probabilities
# Uniform distribution:
probabilities = None

# OR specify probabilities explicitly:
# probabilities = [0.20,0.20,0.20,0.20,0.20]


print("===== HYPOTHESIS =====")

print("H0: Observed distribution follows expected distribution")
print("H1: Observed distribution does NOT follow expected distribution")


n = sum(observed)
k = len(observed)

if probabilities is None:
    expected = [n / k] * k
else:
    expected = [n * p for p in probabilities]

print("\nObserved Frequencies:")
print(observed)

print("\nExpected Frequencies:")
print([round(x, 4) for x in expected])

chi_stat, p_value = chisquare(f_obs=observed,f_exp=expected)
df = k - 1
critical_value = chi2.ppf(1 - alpha,df)

print("\n===== CHI-SQUARE TEST =====")

print(f"Chi-Square Statistic = {chi_stat:.4f}")
print(f"Degrees of Freedom   = {df}")
print(f"P-value              = {p_value:.6f}")
print(f"Critical Value       = {critical_value:.4f}")

print("\n===== CRITICAL VALUE APPROACH =====")

if chi_stat > critical_value:
    print("Reject H0")
else:
    print("Fail to Reject H0")

print("\n===== P-VALUE APPROACH =====")

if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to Reject H0")

print("\n===== INTERPRETATION =====")

if p_value < alpha:
    print("There is significant evidence that the observed distribution differs from the expected distribution.")
else:
    print("There is insufficient evidence to conclude that the observed distribution differs from the expected distribution.")


# CHI-SQUARE TEST OF INDEPENDENCE - Age Group vs Ice Cream Flavor, Machine vs Defect Status, Gender vs Product Preference, Department vs Satisfaction Level


import numpy as np
from scipy.stats import chi2_contingency


# INPUT

table = np.array([
    [45, 35, 20, 25],
    [30, 40, 25, 25],
    [20, 25, 30, 25]
])

alpha = 0.05


print("===== HYPOTHESIS =====")
print("H0: Variables are independent")
print("H1: Variables are dependent (associated)")

chi2_stat, p_value, dof, expected = chi2_contingency(table)

print("\n===== RESULTS =====")
print(f"Chi-Square Statistic = {chi2_stat:.4f}")
print(f"Degrees of Freedom   = {dof}")
print(f"P-value              = {p_value:.6f}")

print("\nExpected Frequencies")
print(expected)

print("\n===== DECISION =====")

if p_value < alpha:
    print("Reject H0")
    print("Variables are associated.")
else:
    print("Fail to Reject H0")
    print("No evidence of association.")


# Binomial Distribution  # Fixed number of customers/items/trials (n) Two outcomes (default / no default) Constant probability (p)
from scipy.stats import binom

n = 20      # total trials
p = 0.25    # success probability
k =  3 #  What is being asked as variable in question
# Exactly k
binom.pmf(k, n, p) # repalce k

# At most k
binom.cdf(k, n, p) # repalce k

# At least k
1 - binom.cdf(k-1, n, p)

# More than k
1 - binom.cdf(k, n, p)


# Poisson Distribution # Events occur randomly over time/space. # An average rate is given (e.g., sales, arrivals, defects, calls). #You are asked for probabilities of 0, 1, 2, ... events in a time interval.
from scipy.stats import poisson


# Variables
average_events = 8
original_period = 275
new_period = 60
k = 2

lam = average_events * (new_period / original_period)
print("Lambda =", lam)
print("Exactly k      :", poisson.pmf(k, lam))
print("At most k      :", poisson.cdf(k, lam))
print("Less than k    :", poisson.cdf(k-1, lam))
print("At least k     :", 1-poisson.cdf(k-1, lam))
print("More than k    :", 1-poisson.cdf(k, lam))
