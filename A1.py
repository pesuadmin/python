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
