import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import ttest_ind, ttest_1samp, chi2_contingency
import sympy as sp
from numpy.linalg import matrix_rank, det, eig
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings('ignore')




# 1a) Descriptive vs Inferential Statistics
#   Descriptive  : Summarizes the data you have (mean, median, SD, charts).
#   Inferential  : Draws conclusions about a population from a sample
#                  (hypothesis tests, CIs, regression).

# 1b) Scatter plot vs Correlation coefficient (r)
#   Scatter plot : Visual — reveals shape, clusters, outliers.
#   r in [-1,+1] : Numeric — strength & direction of the LINEAR association.

# 1c) Conditional probability — P(A|B) = P(A∩B)/P(B)
#   Example: P(Purchase | Added-to-cart) = 0.12 / 0.40 = 0.30

# 1d) Type I (α) vs Type II (β) errors
#   Type I  — False Positive : Reject H₀ when H₀ is true.
#   Type II — False Negative : Fail to reject H₀ when H₀ is false.

# 1e) Local vs Global minima in gradient descent
#   Gradient descent only uses local slope → may converge to a local minimum
#   on non-convex surfaces.  On convex surfaces every local min is global.

# 1f) Second derivative test for f(x)
#   f''(x*) > 0 → local min | f''(x*) < 0 → local max | f''(x*) = 0 → inconclusive


# =============================================================================
# SECTION B — Statistics on Billionaires Dataset
# =============================================================================

df = pd.read_csv(r'C:\Users\Mohan BN\Downloads\Vinci\ESA,GA,SN\ESA\SQL\Billionaires Statistics Dataset (1).csv')
df.columns = [c.strip() for c in df.columns]
print('Shape:', df.shape)
print(df.head(2))


# ---------------------------------------------------------------------------
# 2a) One-sample t-test on age  (claim: mean age = 60)  — 8 marks
# ---------------------------------------------------------------------------
age = pd.to_numeric(df['age'], errors='coerce').dropna()
mu0   = 60
alpha = 0.05

t_stat, p_val = ttest_1samp(age, mu0)
print(f'\n--- 2a) One-sample t-test: age ---')
print(f'n = {len(age)},  mean = {age.mean():.3f},  sd = {age.std(ddof=1):.3f}')
print(f't-statistic = {t_stat:.4f},  p-value = {p_val:.6f}')
print('Decision:', 'Reject H0 — mean age differs from 60' if p_val < alpha else 'Fail to reject H0')

se = age.std(ddof=1) / np.sqrt(len(age))
ci_low, ci_high = stats.t.interval(0.95, df=len(age) - 1, loc=age.mean(), scale=se)
print(f'95% CI for mean age: ({ci_low:.3f}, {ci_high:.3f})')


# ---------------------------------------------------------------------------
# 2b) Two-sample t-test: Self-made vs Inherited net worth — 8 marks
# ---------------------------------------------------------------------------
alpha = 0.01
tmp = df[['selfMade', 'finalWorth']].copy()
tmp['finalWorth'] = pd.to_numeric(tmp['finalWorth'], errors='coerce')
tmp = tmp.dropna()

self_made = tmp.loc[tmp['selfMade'] == True,  'finalWorth']
inherited = tmp.loc[tmp['selfMade'] == False, 'finalWorth']

t_stat, p_val = ttest_ind(self_made, inherited, equal_var=True)
print(f'\n--- 2b) Two-sample t-test: Self-made vs Inherited ---')
print(f'Self-made: n={len(self_made)}, mean={self_made.mean():.2f}')
print(f'Inherited: n={len(inherited)}, mean={inherited.mean():.2f}')
print(f't-statistic = {t_stat:.4f},  p-value = {p_val:.6f}')
print('Decision:', 'Reject H0 — significant difference' if p_val < alpha
      else 'Fail to reject H0 — no significant difference')

n1, n2 = len(self_made), len(inherited)
s1, s2 = self_made.var(ddof=1), inherited.var(ddof=1)
sp2    = ((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2)
se_diff = np.sqrt(sp2 * (1 / n1 + 1 / n2))
diff    = self_made.mean() - inherited.mean()
ci_low, ci_high = stats.t.interval(0.99, df=n1 + n2 - 2, loc=diff, scale=se_diff)
print(f'99% CI for (Self-made − Inherited): ({ci_low:.2f}, {ci_high:.2f})')


# ---------------------------------------------------------------------------
# 2c) One-sample t-test on gdp_country (claim: mean = 1 trillion USD) — 8 marks
# ---------------------------------------------------------------------------
gdp_raw = df['gdp_country'].astype(str).str.replace('[$,]', '', regex=True).str.strip()
gdp     = pd.to_numeric(gdp_raw, errors='coerce').dropna()
mu0     = 1_000_000_000_000
alpha   = 0.05

t_stat, p_val = ttest_1samp(gdp, mu0)
print(f'\n--- 2c) One-sample t-test: GDP ---')
print(f'n = {len(gdp)},  mean GDP = {gdp.mean():,.0f}')
print(f't-statistic = {t_stat:.4f},  p-value = {p_val:.6f}')
print('Decision:', 'Reject H0 — mean GDP differs from 1T' if p_val < alpha else 'Fail to reject H0')

se = gdp.std(ddof=1) / np.sqrt(len(gdp))
ci_low, ci_high = stats.t.interval(0.95, df=len(gdp) - 1, loc=gdp.mean(), scale=se)
print(f'95% CI for mean GDP: ({ci_low:,.0f}, {ci_high:,.0f})')


# ---------------------------------------------------------------------------
# 2d) Linear regression: finalWorth ~ age — 8 marks
# ---------------------------------------------------------------------------
reg_df = df[['age', 'finalWorth']].copy()
reg_df['age']        = pd.to_numeric(reg_df['age'],        errors='coerce')
reg_df['finalWorth'] = pd.to_numeric(reg_df['finalWorth'], errors='coerce')
reg_df = reg_df.dropna()

model = ols('finalWorth ~ age', data=reg_df).fit()
print(f'\n--- 2d) Linear Regression: finalWorth ~ age ---')
print(model.summary().tables[1])
print(f'R-squared      = {model.rsquared:.6f}')
print(f'p-value (age)  = {model.pvalues["age"]:.6f}')

pred_55 = model.params['Intercept'] + model.params['age'] * 55
print(f'Predicted finalWorth for age=55: {pred_55:.2f} (millions USD)')

alpha = 0.05
print('Significance:', 'Age is a significant predictor'
      if model.pvalues['age'] < alpha else 'Age is NOT a significant predictor')
print('R² interpretation: only ~{:.2%} of variance in finalWorth is explained by age — weak fit.'.format(
    model.rsquared))


# ---------------------------------------------------------------------------
# 2e) Chi-square test of independence: Region vs Source — 8 marks
# ---------------------------------------------------------------------------
region_map = {
    'United States': 'Americas', 'Canada': 'Americas', 'Mexico': 'Americas',
    'Brazil': 'Americas', 'Chile': 'Americas', 'Argentina': 'Americas',
    'Colombia': 'Americas', 'Peru': 'Americas', 'Venezuela': 'Americas', 'Uruguay': 'Americas',
    'United Kingdom': 'Europe', 'Germany': 'Europe', 'France': 'Europe',
    'Italy': 'Europe', 'Spain': 'Europe', 'Switzerland': 'Europe',
    'Sweden': 'Europe', 'Norway': 'Europe', 'Denmark': 'Europe',
    'Finland': 'Europe', 'Netherlands': 'Europe', 'Belgium': 'Europe',
    'Austria': 'Europe', 'Ireland': 'Europe', 'Portugal': 'Europe',
    'Greece': 'Europe', 'Russia': 'Europe', 'Poland': 'Europe',
    'Czech Republic': 'Europe', 'Romania': 'Europe', 'Hungary': 'Europe',
    'Liechtenstein': 'Europe', 'Monaco': 'Europe', 'Cyprus': 'Europe',
    'China': 'Asia', 'India': 'Asia', 'Japan': 'Asia', 'South Korea': 'Asia',
    'Hong Kong': 'Asia', 'Taiwan': 'Asia', 'Singapore': 'Asia',
    'Indonesia': 'Asia', 'Thailand': 'Asia', 'Malaysia': 'Asia',
    'Philippines': 'Asia', 'Vietnam': 'Asia', 'Kazakhstan': 'Asia',
    'Israel': 'Asia', 'Turkey': 'Asia', 'United Arab Emirates': 'Asia',
    'Saudi Arabia': 'Asia', 'Qatar': 'Asia', 'Lebanon': 'Asia',
    'Australia': 'Oceania', 'New Zealand': 'Oceania',
    'South Africa': 'Africa', 'Egypt': 'Africa', 'Nigeria': 'Africa',
    'Morocco': 'Africa', 'Tanzania': 'Africa', 'Algeria': 'Africa', 'Zimbabwe': 'Africa',
}

tmp = df[['country', 'source']].dropna().copy()
tmp['region'] = tmp['country'].map(region_map).fillna('Other')

ct = pd.crosstab(tmp['region'], tmp['source'])
chi2, p_val, dof, expected = chi2_contingency(ct)
print(f'\n--- 2e) Chi-square test: Region vs Source ---')
print('Contingency table shape:', ct.shape)
print(f'Chi-square = {chi2:.4f},  dof = {dof},  p-value = {p_val:.6f}')
alpha = 0.05
print('Decision:', 'Reject H0 — Source of wealth is NOT independent of region (they are associated).'
      if p_val < alpha else 'Fail to reject H0 — independence holds.')


# =============================================================================
# SECTION C — Mathematics
# =============================================================================

# ---------------------------------------------------------------------------
# 3a) Linear dependence, rank, orthogonality — 6 marks
# ---------------------------------------------------------------------------
print('\n--- 3a) Linear dependence, rank, orthogonality ---')
m_sym = sp.symbols('m')
M_sym = sp.Matrix([[1, 3, 2],
                   [5, 2, m_sym],
                   [-1, 4, 1]])

det_M  = sp.simplify(M_sym.det())
print('det(M) =', det_M)
m_dep  = sp.solve(det_M, m_sym)
print('Linearly dependent when m =', m_dep)

if m_dep:
    M_dep = np.array(M_sym.subs(m_sym, m_dep[0])).astype(float)
    print(f'Rank of M at m={m_dep[0]}:', matrix_rank(M_dep))

M1 = np.array(M_sym.subs(m_sym, 1)).astype(float)
print('\nM at m=1:\n', M1)
print('M^T M =\n', M1.T @ M1)
is_ortho = np.allclose(M1.T @ M1, np.eye(3))
print('Orthogonal at m=1?', is_ortho)
print('Conclusion: M is NOT orthogonal at m=1 — columns are not unit / not mutually perpendicular.')


# ---------------------------------------------------------------------------
# 3b) Critical points of f(x) = x³ − 3x + 4 — 6 marks
# ---------------------------------------------------------------------------
print('\n--- 3b) Critical points ---')
x = sp.symbols('x')
f_x = x**3 - 3*x + 4
f1  = sp.diff(f_x, x)
f2  = sp.diff(f1,  x)
crit = sp.solve(f1, x)
print('Critical points:', crit)
for c in crit:
    s      = f2.subs(x, c)
    nature = 'min' if s > 0 else ('max' if s < 0 else 'inconclusive')
    print(f'  x={c}: f({c})={f_x.subs(x, c)}, f\'\'={s} -> {nature}')


# ---------------------------------------------------------------------------
# 3c) Eigenvalues of F and determinant via eigenvalues — 8 marks
# ---------------------------------------------------------------------------
print('\n--- 3c) Eigenvalues and determinant ---')
F = np.array([[1, 2, 1],
              [5, 1, 4],
              [7, 6, 9]], dtype=float)

eigvals, eigvecs = eig(F)
print('Eigenvalues of F:')
for v in eigvals:
    print(f'  {v:.6f}')

det_via_eig = np.prod(eigvals).real
print(f'\ndet(F) via product of eigenvalues = {det_via_eig:.6f}')
print(f'det(F) directly (verification)    = {det(F):.6f}')


# ---------------------------------------------------------------------------
# 3d) PCA on Wine dataset — components for 95% variance — 10 marks
# ---------------------------------------------------------------------------
print('\n--- 3d) PCA on Wine dataset ---')
data = load_wine()
X    = data.data

print('Original shape:', X.shape)

X_std = StandardScaler().fit_transform(X)
cov   = np.cov(X_std, rowvar=False)

eig_vals, eig_vecs = np.linalg.eigh(cov)
order    = np.argsort(eig_vals)[::-1]
eig_vals = eig_vals[order]
eig_vecs = eig_vecs[:, order]

explained = eig_vals / eig_vals.sum()
cum        = np.cumsum(explained)
for i, (e, c) in enumerate(zip(explained, cum), 1):
    print(f'PC{i:2d}: variance = {e:.4f}, cumulative = {c:.4f}')

k = int(np.searchsorted(cum, 0.95) + 1)
print(f'\nNumber of PCs to capture 95% variance: {k}')

W     = eig_vecs[:, :k]
X_pca = X_std @ W
print('Projected shape:', X_pca.shape)


# ---------------------------------------------------------------------------
# 3e) Stationary point and minimum cost of f(x,y) — 10 marks
#     f(x,y) = 2x² + xy + 5y² − 8x − 10y + 30
# ---------------------------------------------------------------------------
print('\n--- 3e) Stationary point and minimum cost ---')
x, y = sp.symbols('x y')
f_xy = 2*x**2 + x*y + 5*y**2 - 8*x - 10*y + 30

fx = sp.diff(f_xy, x)
fy = sp.diff(f_xy, y)
stationary = sp.solve([fx, fy], [x, y])
print('Stationary point:', stationary)

fxx = sp.diff(f_xy, x, 2)
fyy = sp.diff(f_xy, y, 2)
fxy = sp.diff(f_xy, x, y)
H   = sp.Matrix([[fxx, fxy], [fxy, fyy]])
D   = sp.simplify(H.det())
print(f'f_xx = {fxx},  det(H) = {D}')

if fxx > 0 and D > 0:
    print('=> Local minimum (Hessian is positive definite)')
elif fxx < 0 and D > 0:
    print('=> Local maximum')
elif D < 0:
    print('=> Saddle point')

min_val = sp.simplify(f_xy.subs(stationary))
print('Minimum cost value =', min_val, '≈', float(min_val))


# =============================================================================
# Appendix — Hessian / Second-Derivative Test Decision Logic
# =============================================================================
# D = f_xx * f_yy - (f_xy)²
#
# D > 0 and f_xx > 0  →  Local minimum
# D > 0 and f_xx < 0  →  Local maximum
# D < 0               →  Saddle point
# D = 0               →  Inconclusive
#
# Applied to 3e: f_xx = 4 > 0, D = 39 > 0