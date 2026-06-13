# Gradient descent.  => Linear Regression  + X and Y
import numpy as np
import matplotlib.pyplot as plt

# Input 

# Dataset

X = np.array([1,2,3,4,5,6], dtype=float)
Y = np.array([10,14,18,22,25,33], dtype=float)

# X = np.array([0.0, 0.3, 0.7, 1.0])
# Y = np.array([1.0, 1.2, 0.8, 1.5])

# Initial parameters
a = 0.5      # slope
b = 0.3      # intercept

# Learning rate
alpha = 0.05

# Number of iterations / epochs
iterations = 5

# Loss Function
# "MSE"  -> Mean Squared Error
# "SSE"  -> Sum of Squared Errors
loss_type = "MSE"

# Optional stopping criterion
tolerance = 0.01

# Gradient descent code starts

n = len(X)

print("Initial Values")
print(f"a = {a:.6f}, b = {b:.6f}")

for epoch in range(1, iterations + 1):

    # Predictions
    Y_pred = a * X + b

    # Errors
    errors = Y - Y_pred

    # Loss
    if loss_type.upper() == "MSE":
        loss = np.mean(errors**2)

        grad_b = (-2 / n) * np.sum(errors)
        grad_a = (-2 / n) * np.sum(X * errors)

    else:   # SSE
        loss = np.sum(errors**2)

        grad_b = -2 * np.sum(errors)
        grad_a = -2 * np.sum(X * errors)

    # Store old values
    a_old = a
    b_old = b

    # Update weights
    a = a - alpha * grad_a
    b = b - alpha * grad_b

    # Print every iteration
    print(
        f"Epoch {epoch:3d}: "
        f"a={a:.6f}, b={b:.6f}, Loss={loss:.6f}"
    )

    # Optional convergence check
    if (abs(a - a_old) < tolerance and
        abs(b - b_old) < tolerance):
        print(f"\nConverged at Epoch {epoch}")
        break

# Final Result

print("\nOptimized Parameters")
print(f"a = {a:.6f}")
print(f"b = {b:.6f}")

Y_final = a * X + b

# Plot

plt.figure(figsize=(7,5))

plt.scatter(X, Y, label="Actual Data")

plt.plot(
    X,
    Y_final,
    marker='o',
    label="Regression Line"
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gradient Descent Linear Regression")
plt.legend()
plt.grid(True)

plt.show()

# Consider the function $f(x) = x^2 + 4x + 5$.
#
# 1. Derive the **gradient** (first derivative) of $f(x)$.
# 2. Suppose the current point is $x = 2$. Calculate the gradient at this point.
# 3. If we apply one step of gradient descent from $x = 2$ with learning rate $\alpha = 0.1$, calculate the updated value of $x$.
# 4. Explain why gradient descent moves towards a minimum in this function.

import numpy as np
import matplotlib.pyplot as plt

def f(x): return x**2 + 4*x + 5
def df(x): return 2*x + 4

x0 = 2.0
alpha = 0.1

grad = df(x0)
x_new = x0 - alpha * grad

print(f"f'(x) = 2x + 4")
print(f"Gradient at x = {x0}: {grad}")
print(f"Updated x after one GD step (alpha={alpha}): {x_new}")
print(f"f({x0}) = {f(x0):.6f}, f({x_new}) = {f(x_new):.6f}")

# Optional visualization
xs = np.linspace(-5, 2.5, 400)
plt.figure(figsize=(6,4))
plt.plot(xs, f(xs), label='f(x)')
plt.scatter([x0, x_new], [f(x0), f(x_new)], color=['C1','C2'], zorder=5)
plt.arrow(x0, f(x0), x_new-x0, f(x_new)-f(x0), head_width=0.2, length_includes_head=True, color='gray')
plt.legend(); plt.xlabel('x'); plt.ylabel('f(x)'); plt.title('Gradient step from x0 to x_new')
plt.grid(alpha=0.3); plt.show()

# Gradient Descent  -- Single Variable  - only x and X,Y table data is not given
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Input

x = sp.symbols('x')

# Function
f = x**2 + 4*x + 5

# Starting point
x_current = 2

# Learning rate
alpha = 0.1

# Number of iterations
iterations = 5

# Derivatives

gradient = sp.diff(f, x)

print("Function:")
sp.pprint(f)

print("\nGradient:")
sp.pprint(gradient)

# Gradient Descent

x_history = [x_current]
y_history = [float(f.subs(x, x_current))]

print("\nGradient Descent Iterations")

for i in range(iterations):

    grad_value = float(gradient.subs(x, x_current))

    x_new = x_current - alpha * grad_value

    y_new = float(f.subs(x, x_new))

    print(
        f"Iteration {i+1}: "
        f"x = {x_new:.4f}, "
        f"f(x) = {y_new:.4f}"
    )

    x_current = x_new

    x_history.append(x_current)
    y_history.append(y_new)

# Final Calculation

print("\nFinal x =", x_current)
print("Final f(x) =", float(f.subs(x, x_current)))

# Plot

x_vals = np.linspace(
    min(x_history) - 2,
    max(x_history) + 2,
    500
)

f_numpy = sp.lambdify(x, f, 'numpy')
y_vals = f_numpy(x_vals)

plt.figure(figsize=(8,5))

# Function curve
plt.plot(x_vals, y_vals, label='f(x)')

# GD points
plt.scatter(
    x_history,
    y_history,
    marker='o',
    label='Gradient Descent Steps'
)

# Connect steps
plt.plot(
    x_history,
    y_history,
    linestyle='--'
)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent on f(x)')
plt.legend()
plt.grid(True)

plt.show()

# Gradient descent. - Polynomial and no data given --> expression has x and y

import numpy as np
import matplotlib.pyplot as plt

# Data

X = np.array([1,2,3,4])

Y = np.array([1,4,9,16])
a = 0
b = 0

c = 0

alpha = 0.001

iterations = 500

# Gradient Descent

n = len(X)

for epoch in range(iterations):

    Y_pred = a*X**2 + b*X + c

    errors = Y - Y_pred

    grad_a = (-2/n)*np.sum(X**2 * errors)

    grad_b = (-2/n)*np.sum(X * errors)

    grad_c = (-2/n)*np.sum(errors)

    a = a - alpha*grad_a

    b = b - alpha*grad_b

    c = c - alpha*grad_c

print(a,b,c)

# Plot

x_curve = np.linspace(min(X),max(X),100)

y_curve = a*x_curve**2 + b*x_curve + c

plt.scatter(X,Y)

plt.plot(x_curve,y_curve)

plt.grid()

plt.show()

# Find the points of local maxima, local minima of the function:

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Data

x = sp.symbols('x')

f = x**3 - 6*x**2 + 9*x + 5

# Optional interval
interval_start = -10
interval_end = 10

# First Derivative

f1 = sp.diff(f, x)

print("f'(x) =")
sp.pprint(f1)

# Critical Points

critical_points = sp.solve(f1, x)

print("\nCritical Points:")
print(critical_points)

# Second Derivative

f2 = sp.diff(f1, x)

print("\nf''(x) =")
sp.pprint(f2)

# Critical Points

print("\nCritical Point Analysis")

for cp in critical_points:

    second_derivative = f2.subs(x, cp)

    function_value = f.subs(x, cp)

    print("\nPoint:", cp)
    print("f(x) =", function_value)

    if second_derivative > 0:
        print(
        f"Local Minimum at x={cp}, "
        f"value={function_value}"
    )

    elif second_derivative < 0:
        print(
        f"Local Maximum at x={cp}, "
        f"value={function_value}"
    )

    else:
        print("Inconclusive")

# Inflection Point

inflection_points = sp.solve(f2, x)

print("\nInflection Points:")

for ip in inflection_points:

    print(
        f"x = {ip}, "
        f"f(x) = {f.subs(x, ip)}"
    )

# Plot

f_np = sp.lambdify(x, f, 'numpy')

x_vals = np.linspace(interval_start,interval_end,500)

y_vals = f_np(x_vals)

plt.figure(figsize=(8,5))

plt.plot(x_vals, y_vals)

# Critical points
for cp in critical_points:

    cp_num = float(cp)

    plt.scatter(
        cp_num,
        float(f.subs(x, cp))
    )

# Inflection points
for ip in inflection_points:

    ip_num = float(ip)

    plt.scatter(
        ip_num,
        float(f.subs(x, ip)),
        marker='x'
    )

plt.grid()

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function Analysis")

plt.show()

# Find out the derivative of the following function using the **chain rule**. Perform step-wise operation:
#
# $$f(x) = \cos\left(\frac{1}{\sqrt{1+x^2}}\right)$$
#
# Also, find the **Hessian Matrix** of the following function:
#
# $$f(x, y) = x^2y^2 + \frac{x}{y^2}$$

import sympy as sp

# Chain Rule Derivative

x = sp.symbols('x')

f = sp.cos(1 / sp.sqrt(1 + x**2))

df_dx = sp.diff(f, x)

print("Derivative of f(x):")
sp.pprint(sp.simplify(df_dx))

# Hessian Matrix

x, y = sp.symbols('x y')

g = x**2 * y**2 + x / y**2

# Hessian Matrix
H = sp.hessian(g, (x, y))

print("\nHessian Matrix:")
sp.pprint(H)

# Find the **Jacobian matrix** of $F(x)$:
#
# $$F(x) = \begin{pmatrix} f_1(x_1, x_2) \\ f_2(x_1, x_2) \end{pmatrix} = \begin{pmatrix} x_1^2 + 5x_2 - 5 \\ \sin\frac{x_1}{x_2} + x_2^2 x_1 \end{pmatrix}$$

import sympy as sp

# Define symbols
x1, x2 = sp.symbols('x1 x2')

# Define functions
f1 = x1**2 + 5*x2 - 5
f2 = sp.sin(x1/x2) + x2**2 * x1

# Jacobian matrix
J = sp.Matrix([
    [sp.diff(f1, x1), sp.diff(f1, x2)],
    [sp.diff(f2, x1), sp.diff(f2, x2)]
])

print("Jacobian Matrix:")
sp.pprint(J)

# If $f(x_1, x_2) = (w_0 - w_1 x_1 - w_2 x_2)^2$, find $\frac{\partial f}{\partial x_1}$ and $\frac{\partial f}{\partial x_1}$.
#
# Also calculate $[3\ 4] - \eta \times \nabla f|_{(1,1)}$ if $w_0 = 1$, $w_1 = -1$, $w_2 = -2$ and $\eta = 1.2$.

import sympy as sp

w0, w1, w2, x1, x2, eta = sp.symbols('w0 w1 w2 x1 x2 eta')
f = (w0 - w1*x1 - w2*x2)**2

df_dx1 = sp.diff(f, x1)
df_dx2 = sp.diff(f, x2)

values = {w0: 1, w1: -1, w2: -2, x1: 1, x2: 1, eta: 1.2}

grad = [df_dx1.subs(values), df_dx2.subs(values)]
updated = sp.Matrix([3, 4]) - values[eta] * sp.Matrix(grad)

print("df/dx1 =", df_dx1)
print("df/dx2 =", df_dx2)
print("gradient at (1,1) =", grad)
print("updated vector =", updated)

# A stone is dropped into a quiet lake and waves move in circles at a speed of **5 cm per second**. At the instant when the radius of the circular wave is **8 cm**, how fast is the enclosed area increasing?

import sympy as sp

# symbols
r, dr_dt = sp.symbols('r dr_dt')

# area
A = sp.pi * r**2

# derivative dA/dt
dA_dt = sp.diff(A, r) * dr_dt

# substitute values
value = dA_dt.subs({r: 8, dr_dt: 5})

print("dA/dt =", value, "cm^2/s")
import math as _math
print(f"\ndA/dt = 80π ≈ {80*_math.pi:.4f} cm²/s")
print("INFERENCE: At r = 8cm, the enclosed area is increasing at ≈ 251.33 cm²/s.")

# **Statement:** For any orthogonal matrix, the inverse is the same as the transpose. 
#
# Check whether the following matrix is orthogonal. Verify the statement:
#
# $$A = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}$$

import numpy as np

A = np.array([
    [1/np.sqrt(2),  1/np.sqrt(2)],
    [1/np.sqrt(2), -1/np.sqrt(2)]
])

AT = A.T

print("A^T A =")
print(np.round(AT @ A, 5))

print("\nA^-1 =")
print(np.round(np.linalg.inv(A), 5))

print("\nA^T =")
print(np.round(AT, 5))

# **Mr. Johns** sells Mango, Apple, and Peach.
#
# - The price of **1 kg Mango, 3 kgs Apple, and 1 kg Peach** is Rs 145.
# - The price of **3 kgs Mango, 4 kgs Apple, and 1 kg Peach** is Rs 280.
# - The price of **2 kgs Apple and 1 kg Peach** is Rs 65.
#
# Find the price of **1 kg of each fruit**.

import numpy as np

# Coefficient matrix
A = np.array([
    [1, 3, 1],
    [3, 4, 1],
    [0, 2, 1]
])

# Constants
B = np.array([145, 280, 65])

# Solve
prices = np.linalg.solve(A, B)

print("Mango =", prices[0])
print("Apple =", prices[1])
print("Peach =", prices[2])

# **Mr. Murgan** sells 3 different products X, Y & Z.
#
# - If he sells 1 unit of X, 5 units of Y, and 1 unit of Z he makes a profit of Rs 1080.
# - If he sells 1 unit of Y and 1 unit of Z he makes a profit of Rs 540.
# - If he sells 2 units of X and **buys** 2 units of Y and 1 unit of Z from another seller at the same selling price, he incurs a **loss of Rs 180**.
#
# Find the price of each product X, Y, and Z.

import numpy as np

A = np.array([
    [1, 5, 1],
    [0, 1, 1],
    [2, -2, -1]
])

B = np.array([1080, 540, -180])

X, Y, Z = np.linalg.solve(A, B)

print("X =", X)
print("Y =", Y)
print("Z =", Z)

# **Mr. X** is an investor. His portfolio primarily tracks the performance of the Nifty index and he wants to add the stock of company 'A'.
# Before adding the stock, he wants to assess if there exists a relationship between Nifty and Stock A.
#
# \[
# \begin{array}{|c|c|c|}
# \hline
# Year & Nifty & Stock A \\
# \hline
# 2015 & 1692 & 68 \\
# \hline
# 2016 & 1978 & 102 \\
# \hline
# 2017 & 1884 & 110 \\
# \hline
# 2018 & 2151 & 112 \\
# \hline
# 2019 & 2519 & 154 \\
# \hline
# \end{array}
# \]
#
# **Help Mr. X to assess the relationship** between Nifty and Stock A.

import numpy as np

nifty = np.array([1692, 1978, 1884, 2151, 2519])
stockA = np.array([68, 102, 110, 112, 154])

r = np.corrcoef(nifty, stockA)[0, 1]

print("Correlation Coefficient =", round(r, 4))
print(f"\n INFERENCE: r = {round(r,4)} indicates very strong positive linear relationship.")
print("Nifty and Stock A move closely together — adding Stock A mirrors Nifty performance.")

# **Headphone manufacturer** problem:
#
# In order to sell $x$ units, the price per unit must be $p(x) = 1000 - x$.
# The total cost of producing $x$ units is $C(x) = 3000 + 20x$.
#
# (i) Find the total revenue $R(x)$.
# (ii) Find the total profit $P(x)$.
# (iii) How many units must be produced and sold to **maximize profit**?
# (iv) What is the **maximum profit**?
# (v) What **price per unit** must be charged to make this maximum profit?

import numpy as np

# Price and Cost functions
def p(x):
    return 1000 - x

def C(x):
    return 3000 + 20 * x

# Revenue function
def R(x):
    return x * p(x)

# Profit function
def P(x):
    return R(x) - C(x)

# Maximum profit occurs at vertex of parabola
# P(x) = -x^2 + 980x - 3000
a = -1
b = 980
x_max = -b / (2 * a)
max_profit = P(x_max)
price_at_max = p(x_max)

print("Revenue Function: R(x) = 1000x - x^2")
print("Profit Function : P(x) = -x^2 + 980x - 3000")
print("\nUnits for Maximum Profit =", x_max)
print("Maximum Profit = Rs.", max_profit)
print("Price per Unit for Maximum Profit = Rs.", price_at_max)

# Find out whether the function is **increasing or decreasing**:
#
# $$f(x) = -8x^2 + 15$$

import sympy as sp
x = sp.symbols('x')
f = -8*x**2 + 15
# Derivative
f_prime = sp.diff(f, x)
print("f(x) =", f)
print("f'(x) =", f_prime)

print("\nIncreasing on (-∞, 0)")
print("Decreasing on (0, ∞)")

# Find out whether the function is **concave or convex**:
#
# $$f(x) = -8x^2 + 15$$

import sympy as sp
x = sp.symbols('x')
f = -8*x**2 + 15
# Second derivative
f_double_prime = sp.diff(f, x, 2)
print("f''(x) =", f_double_prime)
if f_double_prime < 0:
    print("The function is Concave.")
else:
    print("The function is Convex.")

# For the interval $(-1, 1)$ determine if:
#
# $$f(x) = x^4 - 6x^2$$
#
# is **convex or concave**.

import sympy as sp
x = sp.symbols('x')
f = x**4 - 6*x**2
# Second derivative
f2 = sp.diff(f, x, 2)
print("f''(x) =", f2)

# Check sign in (-1,1), e.g., x = 0
print("f''(0) =", f2.subs(x, 0))

if f2.subs(x, 0) < 0:
    print("The function is Concave on (-1,1)")
else:
    print("The function is Convex on (-1,1)")

# ADDED: Rigorous proof for the full interval
# f''(x) = 12x^2 - 12 = 12(x^2 - 1)
# For ALL x in (-1, 1): x^2 < 1 → x^2 - 1 < 0 → 12(x^2-1) < 0
print("\n Rigorous Proof: f''(x) = 12x² - 12 = 12(x²-1)")
print("   For ALL x in (-1,1): x²<1, so f''(x)<0 → CONCAVE on the entire interval.")

#  ADDED: Rigorous proof for the entire interval
# f''(x) = 12x^2 - 12 = 12(x^2 - 1). For ALL x in (-1,1): x^2 < 1 => f''(x) < 0.
print("\n Rigorous: f''(x) = 12(x²-1) < 0 for ALL x in (-1,1) since x²<1 in that interval.")
print("   The function is CONCAVE on the ENTIRE interval (-1, 1), not just at x=0.")

# Find $X$ if:
#
# $$\det\begin{pmatrix} 2 & 4 \\ 5 & 1 \end{pmatrix} = \det\begin{pmatrix} 2X & 4 \\ 6 & X \end{pmatrix}$$

import math

# Given matrices
A = [[2, 4],
     [5, 1]]

# Left determinant
detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]  # 2*1 - 4*5 = -18

# Right determinant for unknown X:
# det([[2X, 4],
#      [6,  X]]) = (2X)*X - 4*6 = 2*X**2 - 24
# Solve 2*X**2 - 24 = detA  =>  2*X**2 = detA + 24

rhs = (detA + 24) / 2  # ( -18 + 24 ) / 2 = 3

if rhs < 0:
    print("No real solutions")
else:
    x1 = math.sqrt(rhs)
    x2 = -math.sqrt(rhs)
    print(f"det(A) = {detA}")
    print(f"X^2 = {rhs}  =>  X = ±{math.sqrt(rhs):.6f}")
    print("Solutions:", x1, x2)

    # Optional verification
    def det_2x2(m):
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    for x in (x1, x2):
        B = [[2*x, 4],
             [6,   x]]
        print(f"det(B) for X={x:.6f} ->", det_2x2(B))

# What is the **effect of higher learning rate** in the Gradient Descent algorithm? Explain briefly.

# Effect of a Higher Learning Rate in Gradient Descent
#
# The learning rate (α) determines the size of the steps taken toward the minimum of the loss function during each iteration of Gradient Descent.
#
# Advantages of a Higher Learning Rate
# Faster movement toward the minimum.
# Reduces the number of iterations required for convergence.
# Training may complete more quickly.
# Disadvantages of a Higher Learning Rate
# May overshoot the minimum point.
# Can cause the algorithm to oscillate around the minimum.
# May fail to converge and even diverge if the learning rate is too large.
# Results in unstable training and inaccurate model parameters.
# Conclusion
#
# A higher learning rate speeds up learning but increases the risk of instability and non-convergence. Therefore, the learning rate should be chosen carefully to balance speed and accuracy.
#
# Answer: A higher learning rate makes Gradient Descent take larger steps toward the minimum, which can speed up convergence, but if it is too high, it may overshoot the optimum, oscillate, or fail to converge.

# A point $P(2, 3)$ is transformed using the affine transformation matrix $A$ given below. Compute the new coordinates $P'(x', y')$ after the transformation. The transformation follows the equation: $P' = A \times P$.
# $$A = \begin{bmatrix} 1 & 2 & 1 \\ 0 & 1 & 3 \end{bmatrix}, \quad P = \begin{bmatrix} 2 \\ 3 \\ 1 \end{bmatrix}$$

import numpy as np
A = np.array([[1, 2, 1],
              [0, 1, 3]])
P = np.array([2, 3, 1])
P_prime = A @ P
print("P' =", P_prime)

# For what value of $x$ does the function:
# $$y = x^2 - 4x$$
# have the **maximum or minimum value**? Find that value.

import sympy as sp

x = sp.symbols('x')
y = x**2 - 4*x
dy_dx = sp.diff(y, x)
critical_points = sp.solve(dy_dx, x)

for cp in critical_points:
    value = y.subs(x, cp)
    print("x =", cp, "y =", value)

#  ADDED: Second derivative test
d2y_dx2 = sp.diff(dy_dx, x)
print("f''(x) =", d2y_dx2)
for cp in critical_points:
    val = y.subs(x, cp)
    sec = d2y_dx2.subs(x, cp)
    nature = "LOCAL MINIMUM" if sec > 0 else ("LOCAL MAXIMUM" if sec < 0 else "SADDLE")
    print(f"x={cp}, y={val}, f''={sec} → {nature}")
print("\n INFERENCE: x=2 gives a LOCAL MINIMUM at y=-4 (parabola opens upward).")

# Find the **Jacobian** $J(u, v)$ for the system:
#
# $$u = x + 2y, \quad v = 3x - y$$

import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define functions
u = x + 2*y
v = 3*x - y

# Jacobian matrix
J = sp.Matrix([
    [sp.diff(u, x), sp.diff(u, y)],
    [sp.diff(v, x), sp.diff(v, y)]
])

# Jacobian determinant
jacobian = J.det()

print("Jacobian Matrix:")
print(J)

print("\nJacobian J(u,v):")
print(jacobian)

# In simple linear regression for a single data point $(x_i, y_i)$, we define loss as:
#
# $$L(w_0, w_1) = \left(\hat{y}_i - (w_0 + w_1 x_i)\right)^2$$
#
# where $\hat{y}_i$ is the predicted value for $y_i$.
#
# Find:
#
# $$\frac{\partial L}{\partial w_0} \quad \text{and} \quad \frac{\partial L}{\partial w_1}$$

import sympy as sp

# Define symbols
w0, w1, xi, y_hat = sp.symbols('w0 w1 xi y_hat')

# Loss function
L = (y_hat - (w0 + w1 * xi))**2

# Partial derivatives
dL_dw0 = sp.diff(L, w0)
dL_dw1 = sp.diff(L, w1)

print("∂L/∂w0 =")
print(sp.simplify(dL_dw0))

print("\n∂L/∂w1 =")
print(sp.simplify(dL_dw1))

# Consider the **cost function**:
#
# $$C(x, y) = x^2 + xy + y^2 - 6x - 9y + 14$$
#
# (i) **Find the stationary points** using partial derivatives. **(4 marks)**
#
# $$\frac{\partial C}{\partial x} = 0 \quad \text{and} \quad \frac{\partial C}{\partial y} = 0$$
#
# (ii) **Verify that the stationary point is indeed an extremum** by checking the sign of partial derivatives around the point. **(4 marks)**
#
# (iii) **Calculate the minimum cost value** at the stationary point. **(2 marks)**

import sympy as sp

# Variables
x, y = sp.symbols('x y')

# Cost function
C = x**2 + x*y + y**2 - 6*x - 9*y + 14

# Partial derivatives
Cx = sp.diff(C, x)
Cy = sp.diff(C, y)

print("∂C/∂x =", Cx)
print("∂C/∂y =", Cy)

# Solve for stationary point
stationary_point = sp.solve([Cx, Cy], (x, y))
print("\nStationary Point:", stationary_point)

# Minimum cost
x0 = stationary_point[x]
y0 = stationary_point[y]

min_cost = C.subs({x: x0, y: y0})
print("Minimum Cost =", min_cost)