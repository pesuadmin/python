# MATRIX OPERATIONS — Determinant, Inverse, Transpose

# Q1  | Determinant of 3x3 Matrix
# ---
# Find the determinant of A = [[2,4,5],[6,1,3],[4,0,7]]
#
# Formula (expand along Row 1):
#   det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
#   For A = | a b c |
#           | d e f |
#           | g h i |
#
# Identify: a=2, b=4, c=5, d=6, e=1, f=3, g=4, h=0, i=7
#
# M11 = det([[1,3],[0,7]]) = 1x7 - 3x0 = 7
# M12 = det([[6,3],[4,7]]) = 6x7 - 3x4 = 42 - 12 = 30
# M13 = det([[6,1],[4,0]]) = 6x0 - 1x4 = -4
#
# det(A) = 2(7) - 4(30) + 5(-4) = 14 - 120 - 20 = -126
#
# det(A) = -126. Since det != 0, the matrix is invertible (non-singular).
#
# Useful rules:
#   If det = 0   -> matrix is singular / vectors are linearly dependent
#   det(kA)      = k^n x det(A)   for n x n matrix
#   det(A^T)     = det(A)


# Q11  | Orthogonal Matrix — Verify A^(-1) = A^T
# ---
# Statement: For any orthogonal matrix, A^(-1) = A^T.
# Verify for A = (1/sqrt(2)) x [[1,1],[1,-1]]
#
# Definition: A matrix is orthogonal if A^T A = A A^T = I (Identity).
#   Equivalently: A^(-1) = A^T
#
# A = | 1/sqrt(2)   1/sqrt(2) |
#     | 1/sqrt(2)  -1/sqrt(2) |
#
# A^T = same (symmetric matrix, so A^T = A here)
#
# A^T x A:
#   [0,0]: 1/2 + 1/2 = 1
#   [0,1]: 1/2 - 1/2 = 0
#   [1,0]: 1/2 - 1/2 = 0
#   [1,1]: 1/2 + 1/2 = 1
#   Result = Identity matrix I
#
# A^T A = I, so A is orthogonal. Therefore A^(-1) = A^T. Statement is TRUE.
#
# Key checks:
#   Each column has unit norm: sqrt(1/2 + 1/2) = 1 (confirmed)
#   Columns are orthogonal: dot product = 1/2 - 1/2 = 0 (confirmed)
#   det(A) = +/-1 for orthogonal matrices.


# Q12  | Matrix Transpose Property: A^T B^T = (BA)^T
# ---
# Verify: A^T B^T = (BA)^T for A=[[1,4],[2,0]], B=[[2,1],[1,3]]
#
# Key Rule (Reversal Law):
#   (AB)^T = B^T A^T
#   (BA)^T = A^T B^T
#
# LHS: A^T = [[1,2],[4,0]], B^T = [[2,1],[1,3]]
#   A^T B^T = | 1x2+2x1  1x1+2x3 | = | 4  7 |
#             | 4x2+0x1  4x1+0x3 |   | 8  4 |
#
# RHS: BA first:
#   BA = | 2x1+1x2  2x4+1x0 | = | 4  8 |
#        | 1x1+3x2  1x4+3x0 |   | 7  4 |
#   (BA)^T = | 4  7 |
#            | 8  4 |
#
# LHS = RHS = [[4,7],[8,4]]. Statement is TRUE.


# Q105  | Determinant Equation — Find X
# ---
# Find X if det([[2,4],[5,1]]) = det([[2X,4],[6,X]])
#
# LHS: det([[2,4],[5,1]]) = 2x1 - 4x5 = 2 - 20 = -18
#
# RHS: det([[2X,4],[6,X]]) = 2X x X - 4 x 6 = 2X^2 - 24
#
# Equate: 2X^2 - 24 = -18
#   2X^2 = 6
#   X^2  = 3
#   X    = +/- sqrt(3) ≈ +/- 1.732


# LINEAR DEPENDENCE — Find m for Dependence

# Q17  | Linear Dependence — Find value of m | AMES Model 3 | 4 marks
# ---
# A=[1,2,-1], B=[3,-1,4], C=[2,m,5]. Vectors as columns in matrix M.
# For what value of m are vectors linearly dependent?
#
# Key Concept: Vectors are linearly dependent when det(M) = 0.
#
# M (vectors as COLUMNS):
#   | 1   3  2 |
#   | 2  -1  m |
#   |-1   4  5 |
#
# det(M) = 1[(-1)(5) - (m)(4)] - 3[(2)(5) - (m)(-1)] + 2[(2)(4) - (-1)(-1)]
#        = 1(-5 - 4m) - 3(10 + m) + 2(8 - 1)
#        = -5 - 4m - 30 - 3m + 14
#        = -21 - 7m
#
# Set det(M) = 0:
#   -21 - 7m = 0  =>  m = -3
#
# When m = -3, vectors are linearly dependent. Rank of M = 2.
# Note: Different variants may use different vectors but the same method applies.


# Q113  | Linear Independence of Vectors + Invertible Matrix
# ---
# Linear Independence:
#   Vectors v1, v2, ..., vn are linearly independent if the only solution to
#   c1*v1 + c2*v2 + ... + cn*vn = 0 is c1 = c2 = ... = cn = 0 (trivial only).
#
# Example (independent): [1,0,0], [0,1,0], [0,0,1] (standard basis vectors).
# Counter-example (dependent): [1,2] and [2,4] are DEPENDENT because [2,4] = 2x[1,2].
#
# Invertible (Non-Singular) Matrix:
#   A square matrix A is invertible if there exists A^(-1) such that A A^(-1) = I.
#   Conditions: det(A) != 0, rank(A) = n (full rank), all rows/columns linearly independent.
#   Example: A=[[1,2],[3,4]] -> det = -2 != 0 -> invertible.


# VECTOR PROJECTIONS & OPERATIONS

# Q31  | Vector Projection of a on b
# ---
# Find the vector projection of a = {5, 5} on b = {8, 2}
#
# Scalar Projection = (a . b) / ||b||
# Vector Projection = [ (a . b) / ||b||^2 ] x b
#
# Step 1 — Dot product a.b: 5x8 + 5x2 = 40 + 10 = 50
# Step 2 — ||b||^2:         8^2 + 2^2 = 64 + 4 = 68
#
# Vector Projection = (50/68) x [8, 2]
#                   = (25/34) x [8, 2]
#                   = [200/34, 50/34]
#                   = [100/17, 25/17]
#                   ≈ [5.88, 1.47]
#
# This is the component of a in the direction of b.


# Q52  | Covariance between Math and English Scores
# ---
# X = [60, 70, 80, 65, 75], Y = [62, 82, 78, 70, 80]
# Calculate covariance. Is the relationship positive or negative?
#
# Formula: Cov(X,Y) = Sum[ (Xi - X-bar)(Yi - Y-bar) ] / (n - 1)
#
# Step 1 — Means:
#   X-bar = (60+70+80+65+75)/5 = 350/5 = 70
#   Y-bar = (62+82+78+70+80)/5 = 372/5 = 74.4
#
# Step 2 — Deviations and products:
#   Xi=60, Yi=62: (60-70)x(62-74.4) = (-10)x(-12.4) = 124
#   Xi=70, Yi=82: (70-70)x(82-74.4) =   (0)x(7.6)   =   0
#   Xi=80, Yi=78: (80-70)x(78-74.4) =  (10)x(3.6)   =  36
#   Xi=65, Yi=70: (65-70)x(70-74.4) =  (-5)x(-4.4)  =  22
#   Xi=75, Yi=80: (75-70)x(80-74.4) =   (5)x(5.6)   =  28
#   Sum of products = 210
#
# Step 3 — Cov(X,Y): 210 / (5-1) = 210/4 = 52.5
#
# Cov(X,Y) = 52.5 > 0 => POSITIVE relationship.
# When Math scores increase, English scores also tend to increase.
# Note: Covariance is scale-dependent; use Pearson correlation (r) for standardized comparison.


# Q128-Q129  | Angle Between Vectors
#
# ---
# Formula: cos(theta) = (a . b) / (||a|| x ||b||)
#          theta = cos^(-1) [ (a . b) / (||a|| x ||b||) ]
#
# Variant A: a=[1,2], b=[9,3]
#   a.b = 9+6 = 15
#   ||a|| = sqrt(5) ≈ 2.236, ||b|| = sqrt(90) ≈ 9.487
#   cos(theta) = 15 / sqrt(5 x 90) = 15 / sqrt(450) = 15/21.21 = 0.7071
#   theta = cos^(-1)(0.7071) ≈ 45 degrees
#
# Variant B: a=[2,-4], b=[11,2]
#   a.b = 22 - 8 = 14
#   ||a|| = sqrt(20), ||b|| = sqrt(125)
#   cos(theta) = 14 / sqrt(2500) = 14/50 = 0.28
#   theta ≈ 73.7 degrees
#
# Variant C: a=[4,2], b=[1,3]
#   a.b = 4+6 = 10
#   ||a|| = sqrt(20), ||b|| = sqrt(10)
#   cos(theta) = 10 / sqrt(200) = 10/14.14 = 0.7071
#   theta ≈ 45 degrees
#
# Variant D: a=[3,4], b=[6,8]  (also appears in Q112)
#   a.b = 18+32 = 50
#   ||a|| = 5, ||b|| = 10
#   cos(theta) = 50/50 = 1.0
#   theta = cos^(-1)(1) = 0 degrees -> vectors are PARALLEL (b = 2a)
#
# Quick reference:
#   theta = 0 degrees   -> parallel vectors
#   theta = 90 degrees  -> perpendicular vectors
#   theta = 180 degrees -> anti-parallel vectors


# Q122  | Partial Derivatives of Loss Function L(w0, w1)
# ---
# L(w0, w1) = (y_hat_i - (w0 + w1*xi))^2
# Find dL/dw0 and dL/dw1
#
# Let u = y_hat_i - (w0 + w1*xi), so L = u^2
#
# dL/dw0 (chain rule):
#   = 2u x du/dw0
#   = 2(y_hat_i - w0 - w1*xi) x (-1)
#   = -2(y_hat_i - w0 - w1*xi)
#
# dL/dw1 (chain rule):
#   = 2u x du/dw1
#   = 2(y_hat_i - w0 - w1*xi) x (-xi)
#   = -2*xi*(y_hat_i - w0 - w1*xi)
#
# These are gradient components used in gradient descent to update weights:
#   w0 = w0 - alpha x dL/dw0
#   w1 = w1 - alpha x dL/dw1


# CALCULUS — Critical Points, Concavity, Jacobian, Marginal Revenue

# Q65  | Inflection, Local Maxima & Minima
# ---
# f(x) = 5x^3 + 2x^2 - 3x. Find: point of inflection, local max and min in (-2, 3).
#
# Rules:
#   Critical points: f'(x) = 0
#   If f''(x) < 0 at critical point -> Local Maximum
#   If f''(x) > 0 at critical point -> Local Minimum
#   Inflection point: f''(x) = 0
#
# Step 1 — f'(x) = 15x^2 + 4x - 3
# Step 2 — Solve f'(x) = 0:
#   15x^2 + 4x - 3 = 0
#   x = (-4 +/- sqrt(16+180)) / 30 = (-4 +/- 14) / 30
#   x1 = 10/30 = 1/3
#   x2 = -18/30 = -3/5
#
# Step 3 — f''(x) = 30x + 4:
#   At x = 1/3:  f''(1/3)  = 10+4 = 14 > 0  -> Local Minimum
#   At x = -3/5: f''(-3/5) = -18+4 = -14 < 0 -> Local Maximum
#
# Step 4 — Inflection: f''(x) = 0
#   30x + 4 = 0 => x = -4/30 = -2/15 ≈ -0.133
#
# Summary: Local Max at x=-0.6, Local Min at x=0.333, Inflection at x=-0.133


# Q72, Q103  | Concave or Convex
# ---
# Rule: Compute second derivative f''(x).
#   f''(x) < 0 for all x in interval -> CONCAVE (opens downward)
#   f''(x) > 0 for all x in interval -> CONVEX  (opens upward)
#
# Case A: f(x) = -x^2 - 7x
#   f'(x)  = -2x - 7
#   f''(x) = -2 (constant negative everywhere) -> CONCAVE
#
# Case B: f(x) = -8x^2 + 15
#   f'(x)  = -16x
#   f''(x) = -16 (constant negative everywhere) -> CONCAVE
#
# Both have constant negative second derivatives => CONCAVE everywhere.
#
# Special case: f(x) = x^4 - 6x^2 on (-1, 1)
#   f'  = 4x^3 - 12x, f'' = 12x^2 - 12
#   At x=0: f'' = -12 < 0 -> concave
#   At x=+/-1: f'' = 0 -> inflection
#   Mixed behaviour -> neither purely concave nor convex on (-1,1).


# Q73-Q75  | Minimum Value — Functions on Restricted Domain
#
# ---
# Case A: f(x) = x^3 + 2x on (-5, -2)
#   f'(x) = 3x^2 + 2. Set = 0: 3x^2 + 2 = 0 => x^2 = -2/3 => No real solution.
#   f'(x) = 3x^2+2 > 0 always => f is strictly increasing on (-5,-2).
#   On a strictly increasing function, minimum is at the LEFT ENDPOINT: x = -5.
#   f(-5) = (-5)^3 + 2(-5) = -125 - 10 = -135 (minimum value)
#
# Case B: f(x) = 3x^6 + 5x^4 + 1, x < 5
#   f'(x) = 18x^5 + 20x^3 = 2x^3(9x^2 + 10)
#   Set f'(x) = 0: x = 0 (since 9x^2+10 > 0 always)
#   f(0) = 1. Check: f(-0.1) > 1 => x=0 is minimum.
#   Minimum value = f(0) = 1
#
# Case C: f(x) = x^4 + x^2 + 1, x < 5
#   f'(x) = 4x^3 + 2x = 2x(2x^2 + 1). Set = 0: x = 0
#   f''(x) = 12x^2 + 2; f''(0) = 2 > 0 => x=0 is local minimum.
#   Minimum value = f(0) = 0 + 0 + 1 = 1
#
# Rule for B and C: "Even-power sum + constant" functions always have min value
# equal to the constant, occurring at x = 0.


# Q78  | Jacobian Matrix — f1=x^3*y, f2=(x^2+y^2)/y
# ---
# f1(x,y) = x^3*y, f2(x,y) = (x^2 + y^2) / y
#
# Jacobian formula:
#   J = | df1/dx  df1/dy |
#       | df2/dx  df2/dy |
#
# For f1 = x^3*y:
#   df1/dx = 3x^2*y
#   df1/dy = x^3
#
# For f2 = (x^2 + y^2)/y = x^2/y + y:
#   df2/dx = 2x/y
#   df2/dy = -x^2/y^2 + 1
#
# Jacobian:
#   J = | 3x^2*y        x^3        |
#       | 2x/y    -x^2/y^2 + 1    |
#
# The Jacobian generalises the "derivative" for vector-valued functions.
# Used in gradient-based optimisation.
# Another variant: f2 = x^2/y + y^2 => df2/dy = -x^2/y^2 + 2y


# Q79  | Jacobian Matrix — F(x) = [x1^2+5x2-5, sin(x1/x2)+x2^2*x1]
#
# ---
# f1 = x1^2 + 5x2 - 5
# f2 = sin(x1/x2) + x2^2*x1
#
# For f1:
#   df1/dx1 = 2x1
#   df1/dx2 = 5
#
# For f2:
#   df2/dx1 = cos(x1/x2) x (1/x2) + x2^2
#   df2/dx2 = cos(x1/x2) x (-x1/x2^2) + 2x2*x1
#
# Jacobian:
#   J = |          2x1                         5             |
#       | cos(x1/x2)/x2 + x2^2   -x1*cos(x1/x2)/x2^2 + 2x1x2 |


# Q81  | Marginal Revenue — R(x) = 3000x - 20x^2 + 200
# ---
# Revenue R(x) = 3000x - 20x^2 + 200
# Find marginal revenue when x = 10.
#
# Marginal Revenue = dR/dx (rate of change of revenue with respect to units)
#
# dR/dx = 3000 - 40x
# At x = 10: dR/dx = 3000 - 40(10) = 3000 - 400 = 2600
#
# When the 10th employee is hired, revenue increases by 2600.
# Maximum revenue: set dR/dx = 0 => 3000 - 40x = 0 => x = 75 employees.


# Q102  | Increasing or Decreasing — f(x) = -8x^2 + 15
# ---
# Rule: f'(x) > 0 -> INCREASING | f'(x) < 0 -> DECREASING
#
# f'(x) = -16x
# f'(x) = 0 at x = 0 (critical point / vertex)
#
# For x < 0: f'(x) = -16x > 0 -> INCREASING
# For x > 0: f'(x) = -16x < 0 -> DECREASING
#
# f(x) increases on (-inf, 0) and decreases on (0, +inf).
# Maximum at x=0, f(0)=15 (downward-opening parabola).


# Q111  | Max/Min of y = x^2 - 4x
# ---
# y' = 2x - 4. Set = 0: 2x = 4 => x = 2
# y'' = 2 > 0 => x=2 is a MINIMUM
# y(2) = 4 - 8 = -4 (minimum value)
#
# Vertex form: y = (x-2)^2 - 4, confirming minimum of -4 at x=2.
# The parabola opens upward (no maximum in the domain).
#
# For y = -x^2 + 4x:
#   y' = -2x + 4 = 0 => x=2 => maximum value of 4 (opens downward).


# Q114, Q120  | Second Derivative Test + First Derivative Intervals
#
# ---
# FIRST DERIVATIVE TEST — INCREASE/DECREASE
#   f'(x) > 0 on (a,b) -> f is INCREASING on (a,b)
#   f'(x) < 0 on (a,b) -> f is DECREASING on (a,b)
#   f'(x) = 0 at x=c   -> x=c is a CRITICAL POINT
#
# Example: f(x) = x^3 - 3x
#   f'(x) = 3x^2 - 3 = 3(x-1)(x+1)
#   f' > 0 for x in (-inf,-1) union (1,inf) -> increasing
#   f' < 0 for x in (-1, 1) -> decreasing
#   Critical points at x=-1 (local max) and x=1 (local min)
#
# SECOND DERIVATIVE TEST
#   At critical point x=c where f'(c)=0:
#   f''(c) > 0 -> Local Minimum (concave up)
#   f''(c) < 0 -> Local Maximum (concave down)
#   f''(c) = 0 -> Inconclusive (may be inflection — use 3rd derivative test)
#
# Inflection Point: where f''(x) changes sign (concavity changes)
#
# Example: f(x) = x^3 - 6x^2 + 9x + 5
#   f'(x)  = 3x^2 - 12x + 9 = 3(x-1)(x-3) => critical points x=1 and x=3
#   f''(x) = 6x - 12
#   f''(1) = 6-12 = -6 < 0 => x=1 is Local Maximum, f(1) = 9
#   f''(3) = 18-12 = 6 > 0  => x=3 is Local Minimum, f(3) = 5


# IMAGE PROCESSING — Convolution, Transformations, RGB

# Q87  | RGB Image Concatenation — What changes?
# ---
# New image = concat(img[:,:63,1], img[:,63:126,:2], img[:,126:,0])
# RGB channels: 0=Red, 1=Green, 2=Blue.  Shape: img[row, col, channel]
#
# Part 1: img[:,:63,1]      -> Left third, only GREEN channel (greyscale of green)
# Part 2: img[:,63:126,:2]  -> Middle third, channels 0+1 = Red+Green only (no Blue)
# Part 3: img[:,126:,0]     -> Right third, only RED channel (greyscale of red)
#
# The new image will appear visually different from the original:
#   Left section:   Greyscale (green intensity only)
#   Middle section: Yellow-ish tint (Red+Green, no Blue)
#   Right section:  Greyscale (red intensity only)
# The original full-colour image becomes a patchwork of single/partial channel extracts.


# Q90  | 2D Convolution — 3x3 image * 2x2 kernel
# ---
# A = [[1,2,3],[4,5,6],[7,8,9]],  K = [[1,-1],[-1,1]]
#
# Formula (valid convolution, no padding):
#   Output[i,j] = Sum Sum A[i+m, j+n] x K[m,n]
#   Output size = (image_size - kernel_size + 1) = (3-2+1) x (3-2+1) = 2x2
#
# Output[0,0]: 1x1 + 2x(-1) + 4x(-1) + 5x1 = 1-2-4+5 = 0
# Output[0,1]: 2x1 + 3x(-1) + 5x(-1) + 6x1 = 2-3-5+6 = 0
# Output[1,0]: 4x1 + 5x(-1) + 7x(-1) + 8x1 = 4-5-7+8 = 0
# Output[1,1]: 5x1 + 6x(-1) + 8x(-1) + 9x1 = 5-6-8+9 = 0
#
# Result: Output = [[0,0],[0,0]]
#
# All zeros because kernel [[1,-1],[-1,1]] detects diagonal differences.
# For a uniformly increasing image like [1..9], each 2x2 patch has equal diagonal
# sums, resulting in zero response.


# Q91  | Transformation Matrix T=[[0,-1],[1,0]] on P(2,3)
#
# ---
# T = [[0,-1],[1,0]] applied to P = [2,3]
#
# P' = T x P = | 0  -1 | | 2 | = | 0(2) + (-1)(3) | = | -3 |
#              | 1   0 | | 3 |   | 1(2) +  0(3)   |   |  2 |
#
# P' = (-3, 2)
# Pattern: (x,y) -> (-y, x) => this is ROTATION OF 90 DEGREES COUNTER-CLOCKWISE
# Verify: |OP| = |OP'| = sqrt(13) (rotation preserves distance)
#
# Common 2D rotation and reflection matrices:
#   90 deg CCW:        [[0,-1],[1,0]]
#   90 deg CW:         [[0,1],[-1,0]]
#   180 deg:           [[-1,0],[0,-1]]
#   Reflection Y-axis: [[-1,0],[0,1]]
#   Reflection X-axis: [[1,0],[0,-1]]


# Q92  | Reflection Matrix along Y-axis
# ---
# Reflection along y-axis: (x, y) -> (-x, y)
#
# T_reflect_y = | -1  0 |
#               |  0  1 |
#
# Verification: T x [3,2]^T = [-3, 2]^T (confirmed)
#
# Transformation summary:
#   Reflect along X-axis:  [[1,0],[0,-1]]   (x,y) -> (x,-y)
#   Reflect along Y-axis:  [[-1,0],[0,1]]   (x,y) -> (-x,y)
#   Reflect along y=x:     [[0,1],[1,0]]    (x,y) -> (y,x)
#   Rotate 90 deg CCW:     [[0,-1],[1,0]]   (x,y) -> (-y,x)
#   Scale by factor k:     [[k,0],[0,k]]    (x,y) -> (kx,ky)


# Q108  | Affine Transformations — Translation, Rotation, Scaling
# ---
# An affine transformation preserves: points, straight lines, and planes.
# Parallel lines remain parallel.
# Includes: translation, rotation, scaling, shearing, and reflection.
#
# In 2D, use homogeneous coordinates [x, y, 1]^T to handle translation with
# matrix multiplication.
#
# Translation by (tx, ty):
#   T = | 1  0  tx |
#       | 0  1  ty |
#       | 0  0   1 |
#   Effect: (x,y,1) -> (x+tx, y+ty, 1)
#
# Rotation by angle theta (counter-clockwise):
#   R = | cos(theta)  -sin(theta)  0 |
#       | sin(theta)   cos(theta)  0 |
#       |     0            0       1 |
#
# Scaling by (sx, sy):
#   S = | sx  0   0 |
#       |  0  sy  0 |
#       |  0   0  1 |


# Q110  | Affine Transform P' = A x P
# ---
# A = [[1,2,1],[0,1,3]], P = [2,3,1]^T
# Compute P' = A x P
#
# A is 2x3, P is 3x1 => P' will be 2x1
#
# P'[0] = 1x2 + 2x3 + 1x1 = 2+6+1 = 9
# P'[1] = 0x2 + 1x3 + 3x1 = 0+3+3 = 6
#
# P' = [9, 6]
#
# Point P(2,3) in homogeneous coordinates maps to P'(9,6) after transformation.
# The extra "1" in P allows translation to be included in matrix multiplication.


# DISTANCE METRICS & CHESSBOARD QUEEN

# Q95  | Chessboard Queen — Distance Metric
# ---
# Which distance metric calculates least moves for the Queen on a chessboard?
#
# Answer: Chebyshev Distance (also called L-infinity norm / chessboard distance)
#
# Formula: d_Chebyshev(A, B) = max(|xA - xB|, |yA - yB|)
#
# Why? The Queen can move diagonally, horizontally, or vertically.
# The minimum number of moves = max of the x or y distance.
#
# All Distance Metrics — Quick Reference:
#   Euclidean (L2): sqrt( Sum(xi - yi)^2 )   -> Straight-line distance, KNN
#   Manhattan (L1): Sum |xi - yi|             -> Grid movement (rook on chessboard)
#   Chebyshev (L-inf): max(|xi - yi|)         -> Queen on chessboard
#   Minkowski: ( Sum |xi - yi|^p )^(1/p)      -> Generalises L1, L2 with parameter p
#
# Example: From A=(1,2) to B=(4,5):
#   Chebyshev = max(|1-4|, |2-5|) = max(3,3) = 3 moves.


# THEORY — Gradient Descent, PCA, Local/Global Minima

# Q106  | Effect of Learning Rate in Gradient Descent
#
# ---
# Learning rate (alpha) controls how large a step we take in the direction of
# the negative gradient during each iteration.
#
# Update rule: theta_new = theta_old - alpha x gradient_of_L(theta)
#
# Too High alpha (large steps):  Fast initially, but may OVERSHOOT minimum,
#   oscillate, or DIVERGE (loss increases).
#
# Too Low alpha (small steps):   Slow convergence, may get stuck in local minima.
#
# Optimal alpha:                 Smooth convergence to global minimum efficiently.
#
# In practice: use learning rate scheduling or adaptive optimisers (Adam, RMSProp).


# Q119  | Local vs Global Minima in Gradient Descent
# ---
# Global Minimum: The point where the function has the lowest value across its
#   entire domain. There is only ONE global minimum.
#
# Local Minimum: A point lower than all nearby points, but not necessarily the
#   lowest overall. There can be MANY local minima.
#
# In Gradient Descent:
#   GD follows the negative gradient -> always moves downhill.
#   It may GET STUCK in a local minimum instead of finding the global minimum.
#   Solutions: Random restarts, Momentum, Adam optimiser, Simulated annealing.
#
# Convex functions (e.g., MSE in linear regression): only one minimum.
#   => GD always finds global minimum.
#
# Non-convex functions (e.g., neural networks): many local minima.
#   => GD may converge to any of them.


# Q109  | Maximization vs Minimization Problem
# ---
# Maximization Problem:
#   Find values of variables that make the objective function as LARGE as possible.
#   Example: Maximize Profit P(x) = Revenue - Cost
#   Method: Set P'(x) = 0 and verify P''(x) < 0 (concave down)
#
# Minimization Problem:
#   Find values of variables that make the objective function as SMALL as possible.
#   Example: Minimize Cost C(x), or minimize MSE in machine learning.
#   Method: Set C'(x) = 0 and verify C''(x) > 0 (concave up)
#
# In ML: Loss function minimization via gradient descent is the most common
#   minimization problem.


# Q112  | Define Scalar + Vector + Angle Calculation
# ---
# Scalar: A quantity described by MAGNITUDE only. No direction.
#   Examples: Temperature 37°C, Mass 5 kg, Speed 60 km/h
#
# Vector: A quantity described by both MAGNITUDE AND DIRECTION.
#   Examples: Velocity 60 km/h North, Force 10N at 45 degrees, Displacement [3,4] m
#
# Angle between a=3i+4j and b=6i+8j:
#   a.b = 3x6 + 4x8 = 18+32 = 50
#   ||a|| = sqrt(9+16) = sqrt(25) = 5
#   ||b|| = sqrt(36+64) = sqrt(100) = 10
#   cos(theta) = 50 / (5 x 10) = 50/50 = 1.0
#   theta = cos^(-1)(1) = 0 degrees -> a and b are PARALLEL (b = 2a)
#
# Since b = 2a, they point in exactly the same direction.
# Angle between parallel vectors is 0 degrees.


# Q125  | PCA — When Eigenvalues are Roughly Equal
# ---
# Question: What happens when eigenvalues are roughly equal in PCA?
#   Option I:   Performs outstandingly
#   Option II:  Performs badly
#   Option III: Can't say
#
# Answer: Option II — PCA will perform BADLY
#
# Why?
#   PCA identifies principal components by finding directions of maximum variance
#   (largest eigenvalues).
#   When eigenvalues are roughly equal:
#     All directions explain similar amounts of variance.
#     There is no clear "dominant" direction to project onto.
#     No natural dimensionality reduction is possible.
#     The choice of principal components becomes arbitrary.
#
# This happens when data is ISOTROPIC (uniform variance in all directions).
# PCA performs BEST when eigenvalues vary greatly — one or two dominate —
# meaning the data has clear principal directions that capture most variance.


# Q115  | Descriptive vs Inferential Statistics
# ---
# Descriptive Statistics:
#   Summarises and describes data collected from a sample or population.
#   Tools: mean, median, mode, std, histogram, boxplot.
#   Example: "The average age of 100 students is 22 years."
#
# Inferential Statistics:
#   Uses sample data to make inferences/predictions about a larger population.
#   Tools: hypothesis testing, confidence intervals, regression, ANOVA.
#   Example: "Based on a sample, we infer that 65% of voters support the candidate."


# Q116  | Scatter Plot vs Correlation Coefficient
# ---
# Scatter Plot:
#   Visual display of two variables. Shows pattern, direction, and outliers.
#   Cannot quantify the strength of the relationship.
#
# Correlation Coefficient (r):
#   Numerical measure of linear relationship strength: r in [-1, +1].
#   r = +1 -> perfect positive linear relationship
#   r = -1 -> perfect negative linear relationship
#   r =  0 -> no linear relationship
#
# Limitation: r only measures LINEAR relationships.
# Scatter plot can reveal non-linear patterns that r would miss.


# Q117  | Conditional Probability
# ---
# Conditional Probability P(A|B):
#   Probability of event A given that B has already occurred.
#
# Formula: P(A|B) = P(A ∩ B) / P(B)
#
# Business example:
#   P(purchase | visited website) = 0.15
#   => 15% of website visitors make a purchase.


# Q118  | Type I and Type II Errors (cross-reference)
# ---
# (Covered in detail under SMDM Q60-Q62 and Q18 above. Summary below.)
#
# Type I Error (False Positive / alpha):
#   Rejecting H0 when it is actually TRUE.
#   Example: Concluding a medicine works when it doesn't.
#   Probability = significance level alpha.
#
# Type II Error (False Negative / beta):
#   Failing to reject H0 when it is actually FALSE.
#   Example: Concluding a medicine doesn't work when it actually does.
#   Power of test = 1 - beta.
#
# Trade-off: Reducing alpha increases beta, and vice versa.


