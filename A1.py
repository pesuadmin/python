367/ suna88
352/naga28121998


import numpy as np
import pandas as pd
from scipy import stats
import sympy as sp
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

# Data Read
df = pd.read_csv('Dataset.csv')
df.columns = [c.strip() for c in df.columns]
print('Shape:', df.shape)
df.head(2)
age = pd.to_numeric(df['age'], errors='coerce').dropna()
tmp = df[['selfMade', 'finalWorth']].copy()
tmp['finalWorth'] = pd.to_numeric(tmp['finalWorth'], errors='coerce')
tmp = tmp.dropna()
# Ex 
self_made = tmp.loc[tmp['selfMade'] == True,  'finalWorth']
inherited = tmp.loc[tmp['selfMade'] == False, 'finalWorth']
#Ex
gdp_raw = df['gdp_country'].astype(str).str.replace('[$,]', '', regex=True).str.strip()
gdp = pd.to_numeric(gdp_raw, errors='coerce').dropna()
# Ex
reg_df = df[['age', 'finalWorth']].copy()
reg_df['age'] = pd.to_numeric(reg_df['age'], errors='coerce')
reg_df['finalWorth'] = pd.to_numeric(reg_df['finalWorth'], errors='coerce')
reg_df = reg_df.dropna()

# Bayes 
P(Disease) = 0.01
P(Test Positive | Disease) = 0.99
P(Test Positive) = 0.05

P_D = 0.01
P_Pos_given_D = 0.99
P_Pos = 0.05
P_D_given_Pos = (P_Pos_given_D * P_D) / P_Pos

print("Probability of Disease given Positive Test =", P_D_given_Pos)

# linearly independent?
v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])    # = 2*v1, clearly dependent
v3 = np.array([1, 0, 1])

M = np.column_stack([v1, v2, v3])
print('M =\n', M)
print('det(M) =', np.linalg.det(M))
print('rank(M) =', np.linalg.matrix_rank(M))
print('=> Linearly DEPENDENT (det=0, rank<3) because v2 = 2*v1')

print()
v2_new = np.array([0, 1, 4])
M2 = np.column_stack([v1, v2_new, v3])
print('M =\n', M2)

print('After replacing v2: det =', np.linalg.det(M2), ', rank =', np.linalg.matrix_rank(M2))
print('=> Linearly INDEPENDENT')

# eigenvalues/vectors and verify A v = lambda v.
A = np.array([[4, 2],
              [1, 3]], dtype=float)

eigvals, eigvecs = np.linalg.eig(A)
print('Eigenvalues:', eigvals)
print('Eigenvectors (columns):\n', eigvecs)

print('\nVerification A v = lambda v:')
for i in range(len(eigvals)):
    lhs = A @ eigvecs[:, i]
    rhs = eigvals[i] * eigvecs[:, i]
    print(f'  lambda={eigvals[i]:.4f}:  A v = {lhs},   lambda v = {rhs}')

print(f'\nTrace check: sum of eigvals = {eigvals.sum():.4f},  trace(A) = {np.trace(A)}')
print(f'Det check:   prod of eigvals = {np.prod(eigvals):.4f},  det(A) = {np.linalg.det(A):.4f}')

# PCA  
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler

data = load_wine()
X = data.data
print('Original shape:', X.shape)

# Step 1: standardize
X_std = StandardScaler().fit_transform(X)

# Step 2: covariance matrix
cov = np.cov(X_std, rowvar=False)

# Step 3: eigen decomposition
eigvals, eigvecs = np.linalg.eigh(cov)   # eigh for symmetric matrices

# Step 4: sort descending
order = np.argsort(eigvals)[::-1]
eigvals = eigvals[order]
eigvecs = eigvecs[:, order]

# Step 5: explained variance
explained = eigvals / eigvals.sum()
cum = np.cumsum(explained)
print('PC | Variance | Cumulative')
for i, (e, c) in enumerate(zip(explained, cum), 1):
    print(f'{i:2d} | {e:.4f}  | {c:.4f}')

k = int(np.searchsorted(cum, 0.95) + 1)
print(f'\n=> {k} principal components capture >= 95% variance')

# Step 6: project
W = eigvecs[:, :k]
X_pca = X_std @ W
print(f'Reduced shape: {X_pca.shape}  (from 13 features down to {k})')

# Derivative
import sympy as sp
# Symbolic derivatives with sympy
x = sp.symbols('x')
f = x**3 - 6*x**2 + 9*x + 2

f1 = sp.diff(f, x)
f2 = sp.diff(f, x, 2)

print('f(x)   =', f)
print("f'(x)  =", f1)
print('f"(x)  =', f2)

# Numeric: derivative at x=2
print(f'f\'(2) = {f1.subs(x, 2)}')
print(f'f"(2) = {f2.subs(x, 2)}')

#evalf
f1.evalf(subs={x: 2})
f2.evalf(subs={x: 2})


# Power: d/dx(x^n)=n*x^(n-1), Exponential: d/dx(e^x)=e^x, Logarithmic: d/dx(ln x)=1/x, Product: d/dx(u*v)=u'*v+u*v', Quotient: d/dx(u/v)=(u'*v-u*v')/v^2, Chain: d/dx[f(g(x))]=f'(g(x))*g'(x)
# Single variable # Find optima of f(x) = x^3 - 6x^2 + 9x + 2 
x = sp.symbols('x')
f = x**3 - 6*x**2 + 9*x + 2

f1 = sp.diff(f, x)
f2 = sp.diff(f, x, 2)
crit = sp.solve(f1, x)
print('Critical points:', crit)

for c in crit:
    s = f2.subs(x, c)
    nature = 'minimum' if s > 0 else ('maximum' if s < 0 else 'inflection / inconclusive')
    print(f'  x = {c}:  f({c}) = {f.subs(x, c)},  f"({c}) = {s}  -> local {nature}')




# two variable
# Find optima of f(x, y) = 2x^2 + xy + 5y^2 - 8x - 10y + 30
x, y = sp.symbols('x y')
f = 2*x**2 + x*y + 5*y**2 - 8*x - 10*y + 30

fx = sp.diff(f, x)
fy = sp.diff(f, y)
stationary = sp.solve([fx, fy], [x, y])
print('Stationary point:', stationary)

fxx = sp.diff(f, x, 2)
fyy = sp.diff(f, y, 2)
fxy = sp.diff(f, x, y)
D = fxx*fyy - fxy**2
print(f'f_xx = {fxx},  f_yy = {fyy},  f_xy = {fxy},  D = {D}')

if D > 0 and fxx > 0:
    nature = 'local MINIMUM'
elif D > 0 and fxx < 0:
    nature = 'local MAXIMUM'
elif D < 0:
    nature = 'SADDLE point'
else:
    nature = 'inconclusive'
print('Nature:', nature)

opt_value = sp.simplify(f.subs(stationary))
print(f'Optimal f value = {opt_value}  (~{float(opt_value):.4f})')

# Jacobian of f(x, y) = [x^2 + y, x*y, sin(x) + y^2]
x, y = sp.symbols('x y')
f1 = x**2 + y
f2 = x*y
f3 = sp.sin(x) + y**2

F = sp.Matrix([f1, f2, f3])
vars_ = sp.Matrix([x, y])
J = F.jacobian(vars_)

print('F(x, y) =', F.T)
print('\nJacobian matrix (3x2):')
sp.pprint(J)

# Evaluate at (x=1, y=2)
J_val = J.subs({x: 1, y: 2})
print('\nJacobian at (1, 2):')
sp.pprint(J_val)


# Hessian of f(x, y) = 2x^2 + xy + 5y^2 - 8x - 10y + 30
x, y = sp.symbols('x y')
f = 2*x**2 + x*y + 5*y**2 - 8*x - 10*y + 30

vars_ = [x, y]
H = sp.hessian(f, vars_)
print('Hessian:')
sp.pprint(H)

print('\ndet(H) =', H.det())
print('Eigenvalues of H:', H.eigenvals())

# Quick optimization use: at stationary point (70/39, 32/39), H is positive definite => min.
H_num = np.array(H).astype(float)
eigs = np.linalg.eigvalsh(H_num)
print('\nNumeric eigenvalues:', eigs)
print('All positive => Hessian is positive-definite => local MINIMUM')

def gradient_descent_example():
    def gradient_descent(f, df, x0, lr=0.1, epochs=20):
        x_vals = [x0]
        for _ in range(epochs):
            # next x value = current x value - learning rate * derivative of f at current x value
            x_next = x_vals[-1] - lr * df(x_vals[-1])

            if abs(x_next - x_vals[-1]) < 0.01:
                break
            x_vals.append(x_next)
        return x_vals

    # Define the function and its derivative
    f = lambda x: x**2 + 3*x + 2
    df = lambda x: 2*x + 3

    # Perform gradient descent
    x_vals = gradient_descent(f, df, x0=-1000, lr=0.01,epochs=1000)
    y_vals = [f(x) for x in x_vals]

    # Plot the optimization process
    x_space = np.linspace(-5, 5, 500)
    y_space = [f(x) for x in x_space]
    plt.plot(x_space, y_space, label="f(x) = x^2 + 3x + 2")
    plt.scatter(x_vals, y_vals, color='red', label="Gradient Descent Steps")
    plt.legend()
    plt.title("Gradient Descent")
    plt.show()

    print("final x value:", x_vals[-1])

gradient_descent_example()





# Normal Distribution
LESS THAN / AT MOST / BELOW       -> cdf()
GREATER THAN / AT LEAST / ABOVE   -> 1 - cdf()
BETWEEN                           -> cdf(upper) - cdf(lower)
OUTSIDE                           -> 1 - [cdf(upper) - cdf(lower)]
# Example: A factory produces bolts with mean length mu=50 mm, sigma=2 mm.
# Q1: What % of bolts are between 48 and 52 mm?
# Q2: What's the 95th percentile bolt length?

mu, sigma = 50, 2

# P(48 <= X <= 52)
p = stats.norm.cdf(52, mu, sigma) - stats.norm.cdf(48, mu, sigma)
print(f'P(48 <= X <= 52) = {p:.4f}  (~68% as expected from 1-sigma rule)')

# 95th percentile
p95 = stats.norm.ppf(0.95, mu, sigma)
print(f'95th percentile length = {p95:.3f} mm')

# Sample 1000 values to visualize
sample = stats.norm.rvs(mu, sigma, size=1000, random_state=42)
print(f'Sample mean = {sample.mean():.3f},  Sample std = {sample.std(ddof=1):.3f}')


# Confidence Interval
# Example: heights (cm) of 12 students. Build a 95% CI for mean height.
heights = np.array([168, 172, 165, 178, 170, 174, 169, 171, 167, 173, 175, 170])
n = len(heights)
xbar = heights.mean()
s = heights.std(ddof=1)
se = s / np.sqrt(n)
ci_low, ci_high = stats.t.interval(0.95, df=n-1, loc=xbar, scale=se)
print(f'n={n},  mean={xbar:.3f},  s={s:.3f},  SE={se:.3f}')
print(f'95% CI for mean height = ({ci_low:.3f}, {ci_high:.3f})')
print(f'Interpretation: with 95% confidence, true mean height lies between {ci_low:.2f} and {ci_high:.2f} cm.')

# Z-test :
# Example: A factory claims battery life has mean 500 hrs with sigma=20.
# Sample of 36 batteries gives mean 495 hrs. Test at alpha=0.05.
mu0, sigma, n, xbar = 500, 20, 36, 495
alpha = 0.05
z = (xbar - mu0) / (sigma / np.sqrt(n))
p = 2 * (1 - stats.norm.cdf(abs(z)))   # two-sided
print(f'Z = {z:.4f},  p-value = {p:.4f}')
# z_crit = stats.norm.ppf(1 - alpha/2)
# print(f'Critical Z (two-sided, alpha=0.05) = +/-{z_crit:.3f}')
print('Decision:', 'Reject H0' if p < alpha else 'Fail to reject H0')

# Type I and Type II Errors:

# Simulation: estimate alpha and beta for a one-sample Z-test.
# H0: mu = 100 vs H1: mu != 100.  True mu = 102, sigma = 10, n = 30, alpha = 0.05.

rng = np.random.default_rng(0)
mu0, sigma, n, alpha = 100, 10, 30, 0.05
true_mu_null  = 100   # H0 actually true
true_mu_alt   = 102   # H0 actually false (effect present)
z_crit = stats.norm.ppf(1 - alpha/2)

reps = 20000

# Type I: H0 true, how often do we wrongly reject?
samples = rng.normal(true_mu_null, sigma, size=(reps, n))
z_stats = (samples.mean(axis=1) - mu0) / (sigma/np.sqrt(n))
type1_rate = np.mean(np.abs(z_stats) > z_crit)

# Type II: H0 false, how often do we fail to reject?
samples = rng.normal(true_mu_alt, sigma, size=(reps, n))
z_stats = (samples.mean(axis=1) - mu0) / (sigma/np.sqrt(n))
type2_rate = np.mean(np.abs(z_stats) <= z_crit)
power = 1 - type2_rate

print(f'Estimated Type I error (alpha) = {type1_rate:.4f}  (expect ~0.05)')
print(f'Estimated Type II error (beta) = {type2_rate:.4f}')
print(f'Power = 1 - beta              = {power:.4f}')

# one -sample T-Test
# Example: a coffee shop claims average serving = 250 ml. Sample of 15 cups:
servings = np.array([248, 252, 247, 250, 249, 246, 251, 253, 245, 248, 250, 247, 249, 252, 250])
mu0, alpha = 250, 0.05

t_stat, p_val = stats.ttest_1samp(servings, mu0,alternative='two-sided')
# alternative="two-sided", "greater","less"
print(f'n = {len(servings)},  mean = {servings.mean():.3f},  s = {servings.std(ddof=1):.3f}')
print(f't = {t_stat:.4f},  p = {p_val:.4f}')
print('Decision:', 'Reject H0' if p_val < alpha else 'Fail to reject H0 — claim of 250 ml is consistent with data')

# two-sample t-test
# Example: test scores for two teaching methods.
method_A = np.array([78, 82, 85, 79, 88, 84, 80, 83, 81, 86])
method_B = np.array([72, 75, 78, 74, 80, 77, 73, 76, 79, 74])

t_stat, p_val = stats.ttest_ind(method_A, method_B, equal_var=True,alternative='two-sided')
# alternative="two-sided", "greater","less"
print(f'Mean A = {method_A.mean():.2f},  Mean B = {method_B.mean():.2f}')
print(f't = {t_stat:.4f},  p = {p_val:.6f}')
print('Decision:', 'Reject H0 — methods differ significantly' if p_val < 0.05 else 'No significant difference')

# 95% CI for the difference (mean_A - mean_B)
n1, n2 = len(method_A), len(method_B)
sp2 = ((n1-1)*method_A.var(ddof=1) + (n2-1)*method_B.var(ddof=1)) / (n1+n2-2)
se = np.sqrt(sp2*(1/n1 + 1/n2))
diff = method_A.mean() - method_B.mean()
ci = stats.t.interval(0.95, df=n1+n2-2, loc=diff, scale=se)
print(f'95% CI for (A - B): ({ci[0]:.3f}, {ci[1]:.3f})')

#Paired T-test
# blood pressure before and after a drug, same 10 patients.
before = np.array([140, 138, 145, 150, 142, 148, 139, 146, 143, 144])
after  = np.array([135, 134, 140, 144, 138, 141, 137, 140, 139, 142])

t_stat, p_val = stats.ttest_rel(before, after,alternative='two-sided')
diff = before - after
print(f'Mean reduction = {diff.mean():.3f} mmHg')
print(f't = {t_stat:.4f},  p = {p_val:.6f}')
print('Decision:', 'Reject H0 — drug significantly reduces BP' if p_val < 0.05 else 'No significant effect')

# Chi-square - Test of Independence
# Example: Is gender independent of preferred drink?
#                Tea  Coffee  Juice
#   Male          30     25      15
#   Female        20     35      25

obs = np.array([[30, 25, 15],
                [20, 35, 25]])

chi2, p_val, dof, expected = stats.chi2_contingency(obs)
print('Observed counts:\n', obs)
print('\nExpected counts (under H0 independence):\n', expected.round(2))
print(f'\nchi2 = {chi2:.4f},  dof = {dof},  p = {p_val:.4f}')
print('Decision:', 'Reject H0 — gender and drink preference are associated' if p_val < 0.05 else 'Fail to reject H0 — independent')

# Chi-square Goodness of Fit (GoF) test
# Example 1 — Is a 6-sided die fair?
# Roll the die 120 times, record observed frequencies.
observed = np.array([18, 22, 15, 25, 17, 23])     # sum = 120
expected = np.array([20, 20, 20, 20, 20, 20])     # uniform -> 120/6 = 20 each

chi2, p_val = stats.chisquare(f_obs=observed, f_exp=expected)
print('-- Example 1: Fairness of a die --')
print(f'Observed: {observed}')
print(f'Expected: {expected}')
print(f'chi2 = {chi2:.4f},  dof = {len(observed)-1},  p = {p_val:.4f}')
print('Decision:', 'Reject H0 — die is NOT fair' if p_val < 0.05 else 'Fail to reject H0 — die appears fair')

print()

# Example 2 — M&M colour distribution claim:
# Manufacturer claims  Red 20%, Green 20%, Blue 20%, Yellow 20%, Brown 20%
# Sample of 200 sweets gave the following counts:
obs2 = np.array([35, 50, 38, 42, 35])             # sum = 200
n = obs2.sum()
expected_props = np.array([0.20, 0.20, 0.20, 0.20, 0.20])
exp2 = expected_props * n                          # convert proportions to counts

chi2, p_val = stats.chisquare(f_obs=obs2, f_exp=exp2)
print('-- Example 2: M&M colour distribution --')
print(f'Observed: {obs2}')
print(f'Expected: {exp2}')
print(f'chi2 = {chi2:.4f},  dof = {len(obs2)-1},  p = {p_val:.4f}')
print('Decision:', 'Reject H0 — observed colours differ from claim' if p_val < 0.05 else 'Fail to reject H0 — fits the claim')

# one way ANOVA
# Example: yields (kg) of 3 fertilizers, 8 plots each.
fert_A = np.array([20, 22, 19, 24, 25, 23, 21, 22])
fert_B = np.array([28, 30, 27, 26, 29, 31, 28, 30])
fert_C = np.array([18, 20, 17, 19, 21, 18, 20, 19])

f_stat, p_val = stats.f_oneway(fert_A, fert_B, fert_C)
print(f'Means: A={fert_A.mean():.2f}, B={fert_B.mean():.2f}, C={fert_C.mean():.2f}')
print(f'F = {f_stat:.4f},  p = {p_val:.6f}')
print('Decision:', 'Reject H0 — at least one fertilizer differs' if p_val < 0.05 else 'No significant difference')


 1.⁠ ⁠Bayes Theorem
(theory only — no code, as requested)

Formula
P(A∣B)=P(B∣A)P(A)P(B),P(B)=∑iP(B∣Ai)P(Ai) 

Words: Bayes' theorem updates the probability of a hypothesis  A  given new evidence  B . It flips a known conditional probability  P(B|A)  into the desired direction  P(A|B) .

Terminology

P(A)  — prior (belief before seeing evidence)
P(B∣A)  — likelihood (how probable the evidence is if A is true)
P(B)  — marginal / evidence (overall probability of the evidence)
P(A∣B)  — posterior (updated belief)
Classic exam example — disease testing

A disease affects 1% of a population. A test is 99% sensitive (true positive) and 95% specific (true negative). If a person tests positive, what is  P(Disease∣+) ?

P(D∣+)=P(+∣D)P(D)P(+∣D)P(D)+P(+∣D¯)P(D¯)=0.99×0.010.99×0.01+0.05×0.99=0.00990.0594≈0.1667

Key insight: Even with a 99% accurate test, only ~17% of positives are truly diseased — because the disease itself is rare (low prior). This is why doctors confirm with a second test.

Where it appears in DS/AI: Naive Bayes classifier, Bayesian inference, A/B testing, spam filters.

 2.⁠ ⁠Normal Distribution
Definition. A continuous distribution symmetric about its mean  μ , with spread controlled by standard deviation  σ :
f(x)=1σ2π−−√exp(−(x−μ)22σ2) 

Key properties (memorize for exam):

Mean = Median = Mode =  μ 
Symmetric, bell-shaped
68-95-99.7 rule: ~68% of values lie within  μ±σ , ~95% within  μ±2σ , ~99.7% within  μ±3σ 
Standard normal  Z∼N(0,1) : obtained by  Z=(X−μ)/σ 
The Central Limit Theorem (CLT) says sample means are approximately normal for large  n  — this is why the normal shows up everywhere
When you'll use it: to compute probabilities, percentiles, critical values for Z/t-tests.

 3.⁠ ⁠Confidence Interval (CI)
Definition. A range that has a specified probability (e.g. 95%) of containing the true population parameter if we repeated the sampling many times.

Formula for a population mean (σ unknown — use t):
x¯±tα/2,n−1⋅sn−−√ 
where  x¯  = sample mean,  s  = sample SD,  n  = sample size,  tα/2,n−1  = critical t-value.

Steps

Compute  x¯  and  s  from data.
Compute standard error  SE=s/n−−√ .
Look up  tα/2  for confidence level  (1−α)  at  n−1  degrees of freedom.
CI =  (x¯−t⋅SE,x¯+t⋅SE) .
Interpretation: "We are 95% confident the true mean lies in this interval." It does not mean a single interval has 95% probability of containing  μ  —  μ  is fixed; the interval is random.

Part B — Hypothesis Testing
General hypothesis-testing recipe (use for every test below)
State  H0  (null) and  H1  (alternative).
Choose significance level  α  (usually 0.05).
Compute the test statistic from data.
Find the p-value (or compare statistic to critical value).
Decide: if p-value < α → Reject  H0 ; else → Fail to reject  H0 .
Conclude in plain English (about the population).

 4.⁠ ⁠Z-test
Use when: comparing a sample mean to a known population mean and the population standard deviation σ is known (or the sample is very large so  s≈σ ).

Test statistic:
Z=x¯−μ0σ/n−−√ 

Decision: for two-sided test at α=0.05, reject  H0  if  |Z|>1.96 .

Difference from t-test: the Z-test uses the known σ and the standard normal distribution; the t-test uses the sample SD  s  and the t-distribution.

 5.⁠ ⁠Type I & Type II Errors
H0  True	 H0  False
Reject  H0 	Type I error (probability = α)	Correct decision (Power = 1−β)
Fail to reject  H0 	Correct decision (1−α)	Type II error (probability = β)
Type I (α): false alarm — concluding an effect exists when it doesn't.
Type II (β): missed detection — failing to detect a real effect.
Power = 1 − β: probability of correctly detecting a true effect. Increased by larger  n , larger effect size, larger α.
Trade-off: Lowering α (e.g. 0.01) makes Type I rarer but Type II more likely (β rises). The only way to reduce both simultaneously is to collect more data.

 6.⁠ ⁠One-sample t-test
Use when: comparing a sample mean to a hypothesized value, with σ unknown (use sample SD  s ).

Hypotheses:  H0:μ=μ0  vs  H1:μ≠μ0  (two-sided).

Test statistic:
t=x¯−μ0s/n−−√,df=n−1 

Assumptions: data approximately normal (or  n  large by CLT), random sample.

 7.⁠ ⁠Two-sample (independent) t-test
Use when: comparing means of two independent groups (e.g. drug vs placebo, men vs women).

Hypotheses:  H0:μ1=μ2  vs  H1:μ1≠μ2 .

Test statistic (equal variance assumed — pooled):
t=x¯1−x¯2sp1n1+1n2−−−−−−√,s2p=(n1−1)s21+(n2−1)s22n1+n2−2,df=n1+n2−2 

Welch's t-test (use if variances clearly unequal): same formula but  s21/n1+s22/n2  in the denominator (no pooling) and a different df formula. Set equal_var=False in scipy.

 8.⁠ ⁠Paired t-test
Use when: the same subjects are measured twice (e.g. before vs after, left vs right hand, weight before/after diet). The samples are paired/matched, not independent.

Idea: compute differences  di=x(after)i−x(before)i , then run a one-sample t-test on the differences with  H0:μd=0 .

Test statistic:
t=d¯−0sd/n−−√,df=n−1 

Why "paired" is more powerful: subject-level variation (which is large) cancels out, so smaller effects become detectable.

 9.⁠ ⁠Chi-square Tests
The chi-square statistic compares observed counts to expected counts. There are two flavours you must know:

Variant	Question it answers	scipy call
9a. Test of Independence	Are two categorical variables related? (uses a contingency table)	stats.chi2_contingency(table)
9b. Goodness of Fit (GoF)	Does my single observed distribution match a hypothesized one?	stats.chisquare(obs, exp)
Common formula (both):
χ2=∑(O−E)2E 
where  O  = observed count,  E  = expected count. Reject  H0  when  χ2  is large (p < α).

Assumption (both): every expected count  E≥5  (otherwise use Fisher's exact test or pool categories).

9a) Chi-square Test of Independence
Use when: testing whether two categorical variables are independent. Data is presented in a contingency table (rows = categories of variable 1, columns = categories of variable 2).

Hypotheses:

H0 : the two variables are independent
H1 : the two variables are associated
Expected counts under independence:
Eij=(row totali)×(column totalj)grand total 

Degrees of freedom:  df=(r−1)(c−1)  where  r  = #rows,  c  = #cols.

9b) Chi-square Goodness of Fit (GoF) test
Use when: comparing one observed frequency distribution to a hypothesized / theoretical distribution (no second variable involved). Examples:

Is a die fair? (expected = 1/6 in each face)
Do customer arrivals follow a Poisson distribution?
Do M&M colour proportions match the manufacturer's claim?
Hypotheses:

H0 : observed frequencies match the expected distribution
H1 : observed frequencies differ from the expected distribution
Test statistic:
χ2=∑i=1k(Oi−Ei)2Ei,df=k−1−p 
where  k  = number of categories and  p  = number of distribution parameters estimated from the data ( p=0  if the expected proportions are fully specified in advance).

Important:  ∑Oi=∑Ei  (both must equal the total sample size). If you specify expected proportions, multiply them by  n  first.

Decision: large  χ2  ⇒ small p ⇒ reject  H0  ⇒ data does not fit the claimed distribution.

10.⁠ ⁠One-way ANOVA
Use when: comparing the means of 3 or more groups simultaneously.

Hypotheses:

H0:μ1=μ2=⋯=μk  (all means equal)
H1 : at least one mean differs
Test statistic:
F=MS betweenMS within=SSB/(k−1)SSW/(N−k) 

SSB  = variability between group means
SSW  = variability within groups (residual)
If significant, follow up with a post-hoc test (e.g. Tukey HSD) to find which groups differ. Assumptions: normality within each group, equal variances, independent samples.

Part C — Linear Algebra
11.⁠ ⁠Linear Dependence & Independence
Definitions:

A set of vectors  {v1,v2,…,vk}  is linearly independent if the only solution to  c1v1+c2v2+⋯+ckvk=0  is  c1=c2=⋯=ck=0 .
Otherwise they are linearly dependent (one vector can be written as a combination of the others — it carries no new information).
How to check (for  k  vectors in  Rn ,  k=n ):

Stack the vectors as columns into a square matrix  M .
Compute  det(M) .
If  det(M)=0  → linearly dependent. Otherwise → independent.
Rank of  M  = number of linearly independent columns (or rows). Rank < dimension → vectors are dependent.

12.⁠ ⁠Eigenvalues & Eigenvectors
Definition. For a square matrix  A , a non-zero vector  v  is an eigenvector with eigenvalue  λ  if:
Av=λv 
Geometrically:  A  stretches/shrinks  v  by factor  λ  without changing its direction.

How to find them:

Solve the characteristic equation:  det(A−λI)=0  → gives eigenvalues  λi .
For each  λi , solve  (A−λiI)v=0  → gives the eigenvector.
Key properties (memorize):

det(A)=∏iλi  (product of eigenvalues)
trace(A)=∑iλi  (sum of eigenvalues = sum of diagonal)
Eigenvalues of  Ak  are  λki 
Eigenvalues of  A−1  are  1/λi

13.⁠ ⁠PCA from Scratch
Goal: reduce the dimensionality of data by projecting it onto the directions of maximum variance (the principal components).

Step-by-step algorithm:

Standardize the data (mean=0, std=1 for each feature) — required when features have different scales.
Compute the covariance matrix  Σ=1n−1X⊤stdXstd .
Compute its eigenvalues  λi  and eigenvectors  vi .
Sort eigenvalues in descending order; eigenvectors give the principal-component directions.
Explained variance ratio =  λi/∑jλj . Choose the top  k  PCs whose cumulative ratio ≥ desired threshold (e.g. 0.95).
Project:  Xpca=Xstd⋅Wk  where  Wk  is the matrix of top- k  eigenvectors.
Why it works: the eigenvectors of the covariance matrix are the orthogonal axes along which the data has the most variance — losing the small-variance axes loses the least information.

Part D — Calculus & Optimization
14.⁠ ⁠Derivatives
Definition. The derivative  f′(x)  measures the instantaneous rate of change of  f  at  x :
f′(x)=limh→0f(x+h)−f(x)h 

Common rules (memorize):

ddx(xn)=nxn−1 
ddx(ex)=ex ,  ddx(lnx)=1/x 
Product:  (uv)′=u′v+uv′ 
Quotient:  (u/v)′=(u′v−uv′)/v2 
Chain:  ddxf(g(x))=f′(g(x))⋅g′(x) 
Second derivative  f′′(x)  measures curvature:  >0  concave up (cup),  <0  concave down (cap).

15.⁠ ⁠Optimization — Single Variable
Goal: find values of  x  where  f(x)  is maximum or minimum.

Procedure (second-derivative test):

Compute  f′(x)  and solve  f′(x)=0  → these are critical points.
Compute  f′′(x)  at each critical point:
f′′(x∗)>0  → local minimum
f′′(x∗)<0  → local maximum
f′′(x∗)=0  → inconclusive (check sign change of  f′′  → could be point of inflection).
Evaluate  f  at each critical point to get the actual min/max value.

16.⁠ ⁠Optimization — Two Variables
Goal: find  (x,y)  that maximize/minimize  f(x,y) .

Procedure (Hessian / second-derivative test):

Compute partial derivatives  fx=∂f/∂x ,  fy=∂f/∂y .
Solve the system  fx=0, fy=0  → stationary points.
Compute the Hessian determinant:  D=fxxfyy−(fxy)2 .
Classify:
Condition	Conclusion
D>0, fxx>0 	Local minimum
D>0, fxx<0 	Local maximum
D<0 	Saddle point
D=0 	Inconclusive
Plug the stationary point back into  f  to get the optimal value.

17.⁠ ⁠Jacobian Matrix
Definition. For a vector-valued function  f:Rn→Rm , the Jacobian  J  is the  m×n  matrix of all first-order partial derivatives:
Jij=∂fi∂xj 

Special cases:

If  f  is scalar-valued ( m=1 ), the Jacobian is just the gradient row vector  ∇f .
If  m=n ,  det(J)  is used in change-of-variables for integrals (e.g. polar/spherical coords).
Where it appears in DS/AI: backpropagation in neural networks, sensitivity analysis, Newton's method for systems of equations.
18.⁠ ⁠Hessian Matrix
Definition. For a scalar function  f(x1,…,xn) , the Hessian  H  is the  n×n  matrix of all second-order partial derivatives:
Hij=∂2f∂xi∂xj 

For  f(x,y) :
H=[fxxfyxfxyfyy] 

Uses:

Optimization classification: sign of  det(H)  and  fxx  tells min/max/saddle 
Newton's method: update step  xt+1=xt−H−1∇f .
A symmetric matrix (Schwarz's theorem:  fxy=fyx  for smooth  f ).
Positive-definite  H  (all eigenvalues > 0) ⇔ local minimum at that point.

Z-test	One mean, σ known, large n	(xbar-mu0)/(sigma/sqrt(n)) then stats.norm.cdf
One-sample t	One mean, σ unknown	stats.ttest_1samp(data, mu0)
Two-sample t (independent)	Compare 2 group means	stats.ttest_ind(g1, g2, equal_var=True)
Paired t	Same subjects, before vs after	stats.ttest_rel(before, after)
Chi-square independence	2 categorical vars, contingency table	stats.chi2_contingency(table)
Chi-square goodness of fit	1 observed dist vs hypothesized dist	stats.chisquare(obs, exp)
One-way ANOVA	3+ group means	stats.f_oneway(g1, g2, g3, ...)
Linear regression	Predict numeric y from x	statsmodels.formula.api.ols('y ~ x', df).fit()
Decision rule everywhere: if p < α → Reject  H0 . Otherwise fail to reject.


Calculate 95% confidence intervals for mean Selling_Price across different Fuel_Type categories. Interpret and discuss whether the intervals overlap.

Concept

Confidence Interval estimates the range in which the true population mean is likely to lie with 95% confidence.

Formula:

CI = x̄ ± t(α/2) × (s/√n)

Where:
•⁠  ⁠x̄ = Sample Mean
•⁠  ⁠s = Sample Standard Deviation
•⁠  ⁠n = Sample Size
•⁠  ⁠t(α/2) = Critical t-value

Python Code

import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('car_data.csv')

for fuel in df['Fuel_Type'].unique():

    group = df[df['Fuel_Type'] == fuel]['Selling_Price']

    n = len(group)
    mean = group.mean()
    se = group.std(ddof=1) / np.sqrt(n)

    ci = stats.t.interval(
        confidence=0.95,
        df=n-1,
        loc=mean,
        scale=se
    )

    print(f"{fuel}: Mean={mean:.2f}, 95% CI=({ci[0]:.2f}, {ci[1]:.2f}), n={n}")



#OLS

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)


# STEP 1 : LOAD DATA


df = pd.read_csv("data.csv")


# STEP 2 : DEFINE X AND Y


X = df[['Feature1', 'Feature2', 'Feature3']]
y = df['Target']
# STEP 3 : ADD INTERCEPT (β0)
X = sm.add_constant(X)

# STEP 4 : TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# STEP 5 : FIT OLS MODEL

model = sm.OLS(y_train, X_train).fit()

# STEP 6 : COMPLETE REPORT


print(model.summary())

# STEP 7 : COEFFICIENTS


print("\nCoefficients")
print(model.params)

# STEP 8 : P-VALUES


print("\nP-values")
print(model.pvalues)

# STEP 9 : CONFIDENCE INTERVALS

print("\n95% Confidence Intervals")
print(model.conf_int())

# STEP 10 : PREDICTIONS

y_pred = model.predict(X_test)

# STEP 11 : MODEL EVALUATION

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nEvaluation Metrics")
print("MSE :", mse)
print("RMSE:", rmse)
print("MAE :", mae)
print("R²  :", r2)

# STEP 12 : ADJUSTED R²

print("\nAdjusted R²")
print(model.rsquared_adj)

# STEP 13 : F-STATISTIC

print("\nF Statistic")
print(model.fvalue)

print("\nF-test p-value")
print(model.f_pvalue)

# STEP 14 : RESIDUALS

residuals = model.resid

print("\nResidual Mean")
print(np.mean(residuals))

# STEP 15 : PREDICT NEW DATA

new_data = pd.DataFrame({
    'Feature1':[10],
    'Feature2':[20],
    'Feature3':[30]
})

new_data = sm.add_constant(new_data)

prediction = model.predict(new_data)

print("\nPrediction:")
print(prediction)

