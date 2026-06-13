# Assume level of significance = 0.05 unless stated otherwise.
# Find the determinant of the matrix $A$:
import sympy as sp

# Define matrix
A = sp.Matrix([
    [2, 4, 5],
    [6, 1, 3],
    [4, 0, 7]
])
# Determinant
det_A = A.det()

print("Determinant =", det_A)
if det_A != 0:
    print("Matrix is non-singular (invertible).")
else:
    print("Matrix is singular (not invertible).")

# Calculate the following for the matrices $A$, $B$, $C$, and $D$ where $I$ is a 3×3 Identity matrix:
#
# - $|A + I|$
# - $BC$
# - $AB$
# - $A^2$
# - Value of $D^2 - 5D - 2I$
#
# $$A = \begin{bmatrix} 5 & 6 & 2 \\ 4 & 7 & 19 \\ 0 & 3 & 12 \end{bmatrix}, \quad B = \begin{bmatrix} 14 \\ 4 \\ 5 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}, \quad D = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$$

import numpy as np

# Define matrices A, B, C, D and 3x3 Identity matrix I
A = np.array([[5, 6, 2], [4, 7, 19], [0, 3, 12]], dtype=float)

B = np.array([[14], [4], [5]], dtype=float)

C = np.array([[1, 2, 3]], dtype=float)

D = np.array([[1, 2], [3, 4]], dtype=float)

I3 = np.eye(3)
I2 = np.eye(2)

# 1. |A + I|
det_A_plus_I = np.linalg.det(A + I3)

# 2. BC
BC = B @ C

# 3. AB
AB = A @ B

# 4. A^2
A_squared = A @ A

# 5. D^2 - 5D - 2I
D_result = (D @ D) - (5 * D) - (2 * I2)

# Print results
print("det(A + I) =", det_A_plus_I)
print("\nBC =\n", BC)
print("\nAB =\n", AB)
print("\nA^2 =\n", A_squared)
print("\nD^2 - 5D - 2I =\n", D_result)

# Consider the following matrices:
#
# $$A = \begin{bmatrix} 2 & 4 \\ 1 & 3 \end{bmatrix}, \quad B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$$
#
# 1. Find the result of the matrix addition $(A + B)$.
# 2. Calculate the matrix multiplication $(A \times B)$.
# 3. Find the transpose of matrix $A$.
# 4. Calculate the determinant of matrix $B$.
# 5. Verify if matrix $A$ is invertible by calculating its determinant and, if it is invertible, find the inverse of $A$.

import numpy as np

# Define matrices A and B
A = np.array([[2, 4], [1, 3]], dtype=float)

B = np.array([[5, 6], [7, 8]], dtype=float)

# 1. Find the result of the matrix addition (A + B)
A_plus_B = A + B

# 2. Calculate the matrix multiplication (A x B)
A_times_B = A @ B

# 3. Find the transpose of matrix A
A_T = A.T

# 4. Calculate the determinant of matrix B
det_B = np.linalg.det(B)

# 5. Verify if matrix A is invertible by calculating its determinant
# If it is invertible, find the inverse of A
det_A = np.linalg.det(A)
is_invertible = not np.isclose(det_A, 0)
inv_A = np.linalg.inv(A) if is_invertible else None

# Print results
print("1. A + B =\n", A_plus_B)
print("\n2. A x B =\n", A_times_B)
print("\n3. Transpose of A =\n", A_T)
print("\n4. det(B) =", det_B)
print("\n5. det(A) =", det_A)
print("   Is A invertible? :", is_invertible)
print("   Inverse of A =\n", inv_A)

# Find the inverse of the following matrix:
#
# $$A = \begin{bmatrix} 1 & 5 & 7 \\ 2 & 6 & 0 \\ 3 & 5 & 1 \end{bmatrix}$$

import numpy as np

# Define the matrix A
A = np.array([[1, 5, 7], [2, 6, 0], [3, 5, 1]], dtype=float)

# Calculate the determinant to check for invertibility
det_A = np.linalg.det(A)
is_invertible = not np.isclose(det_A, 0)

# Calculate the inverse if the determinant is non-zero
inv_A = np.linalg.inv(A) if is_invertible else None

print("det(A) =", det_A)
print("Is A invertible? :", is_invertible)
print("Inverse of A =\n", inv_A)

# Find the inverse of the following matrix using the **adjoint method**:
#
# $$A = \begin{bmatrix} 1 & 5 & 7 \\ 2 & 6 & 0 \\ 0 & 3 & 5 \end{bmatrix}$$

!pip install sympy
import numpy as np
import sympy as sp

# Define the matrix symbols using sympy to perform analytical adjoint calculations
A_sym = sp.Matrix([[1, 5, 7], [2, 6, 0], [0, 3, 5]])

# 1. Calculate the determinant
det_A = A_sym.det()

# 2. Calculate the matrix of cofactors (Adjoint matrix is the transpose of the cofactor matrix)
# In sympy, the adjugate() function computes the analytical Adjoint matrix directly.
adj_A = A_sym.adjugate()

# 3. Calculate the inverse using the formula: Inverse = Adjoint / Determinant
inv_A = adj_A / det_A

# Convert to float arrays for clean numerical outputs
A_num = np.array(A_sym).astype(float)
adj_num = np.array(adj_A).astype(float)
inv_num = np.array(inv_A).astype(float)

print("Matrix A =\n", A_num)
print("\n1. Determinant of A =", float(det_A))
print("\n2. Adjoint of A =\n", adj_num)
print("\n3. Inverse of A (Adjoint Method) =\n", inv_num)

# Given $A = \begin{bmatrix} 1 & 0 & -1 \\ 2 & 1 & 0 \\ 3 & 0 & 5 \end{bmatrix}$, find $AA^T$. Also verify that $AA^T$ is symmetric.

import numpy as np

# Define the matrix A
A = np.array([[1, 0, -1], [2, 1, 0], [3, 0, 5]], dtype=float)

# 1. Find the transpose of A
A_T = A.T

# 2. Compute the product A * A^T
AA_T = A @ A_T

# 3. Verify that AA_T is symmetric by checking if it equals its own transpose
# A matrix M is symmetric if M == M^T
is_symmetric = np.allclose(AA_T, AA_T.T)

print("Matrix A =\n", A)
print("\nTranspose of A (A^T) =\n", A_T)
print("\nProduct AA_T =\n", AA_T)
print("\nIs AA_T symmetric? :", is_symmetric)

# INFERENCE
# (A*A^T)^T = (A^T)^T * A^T = A * A^T — so AA^T is ALWAYS symmetric for any matrix A.
print("\n Mathematical property: AA^T is always symmetric for any real matrix A.")

# Find $X$ and $Y$, if:
#
# $$2X + 3Y = \begin{bmatrix} 2 & 3 \\ 4 & 0 \end{bmatrix} \quad \text{and} \quad 3X + 2Y = \begin{bmatrix} 2 & -2 \\ -1 & 5 \end{bmatrix}$$

import numpy as np

M1 = np.array([[2, 3],
               [4, 0]], dtype=float)

M2 = np.array([[2, -2],
               [-1, 5]], dtype=float)

# Coefficients from:
# 2X + 3Y = M1
# 3X + 2Y = M2

a, b = 2, 3
c, d = 3, 2

# Determinant of coefficient matrix
det = a * d - b * c

# Solve using elimination formula
X = (d * M1 - b * M2) / det
Y = (a * M2 - c * M1) / det

print("Determinant =", det)

print("\nMatrix X =\n", X)
print("\nMatrix Y =\n", Y)

# Verification
print("\nVerification:")
print("2X + 3Y =", np.allclose(2 * X + 3 * Y, M1), "(matches M1)")
print("3X + 2Y =", np.allclose(3 * X + 2 * Y, M2), "(matches M2)")

# Find the number of independent vectors (rank) in the following matrix:
#
# $$A = \begin{bmatrix} 1 & 3 & 5 & 6 \\ 3 & 5 & 0 & 7 \\ 2 & 6 & 2 & 0 \\ 7 & 5 & 1 & 0 \end{bmatrix}$$

import numpy as np

# Define the matrix A
A = np.array([[1, 3, 5, 6], [3, 5, 0, 7], [2, 6, 2, 0], [7, 5, 1, 0]], dtype=float)

# Compute the rank (number of linearly independent vectors) of the matrix
# As specified in the quick-reference card of the notebook template
rank_A = np.linalg.matrix_rank(A)

print("rank(A) =", rank_A)

# INFERENCE
print(f"\nRank = {rank_A} → {rank_A} linearly independent row(s)/column(s) out of {A.shape[0]}")
if rank_A < A.shape[0]:
    print(f"{A.shape[0]-rank_A} row(s) are linearly dependent.")
else:
    print("Matrix is full rank — all rows are linearly independent.")

# Verify that the vectors $[2\ 2\ 1]$, $[-4\ 6\ 5]$, $[1\ 0\ 0]$ are linearly independent.

import numpy as np

# Define the vectors as arrays
v1 = np.array([2, 2, 1])
v2 = np.array([-4, 6, 5])
v3 = np.array([1, 0, 0])

# Stack the vectors as columns to form a square matrix M
M = np.column_stack([v1, v2, v3])
print("M =\n", M)

# Calculate the determinant and rank to check for linear independence
det_M = np.linalg.det(M)
rank_M = np.linalg.matrix_rank(M)

print("det(M) =", det_M)
print("rank(M) =", rank_M)

# A matrix with det != 0 and rank == dimension contains linearly independent vectors
if not np.isclose(det_M, 0) and rank_M == 3:
    print("=> Linearly INDEPENDENT (det!=0, rank=3)")
else:
    print("=> Linearly DEPENDENT")

# Given $A = \begin{bmatrix} 2 & 3 \\ x & y \end{bmatrix}$ has eigenvalues $\lambda_1 = 4$, $\lambda_2 = 8$. Find $x$ and $y$.

import numpy as np

# Find x and y given A = [[2,3],[x,y]] with eigenvalues 4 and 8
# KEY PROPERTIES:
#   Trace(A)  = sum of eigenvalues  → 2 + y = λ1 + λ2
#   Det(A)    = product of eigenvalues → 2y - 3x = λ1 × λ2

lambda1, lambda2 = 4, 8

# From trace: 2 + y = 4 + 8 = 12  =>  y = 10
y_val = (lambda1 + lambda2) - 2
print("Trace:   2 + y =", lambda1 + lambda2, "  =>  y =", y_val)

# From determinant: 2y - 3x = 4 × 8 = 32  =>  x = (2y - 32)/3
det_val = lambda1 * lambda2
x_val = (2 * y_val - det_val) / 3
print("Det:  2y - 3x =", det_val, "  =>  x =", x_val)

print(f"\n Answer: x = {x_val}, y = {y_val}")

# Verification
A_check = np.array([[2, 3], [x_val, y_val]])
eigvals_check = np.linalg.eigvals(A_check)
print("Verification — Eigenvalues:", np.round(sorted(eigvals_check), 4),
      "(expected [4, 8])")

# INFERENCE: Trace and determinant are eigenvalue-invariant properties.
# They provide a quick algebraic path to recover unknown matrix entries.

# Consider the following vectors where $m$ is an unknown scalar:
#
# $$A = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}, \quad B = \begin{bmatrix} 3 \\ -1 \\ 4 \end{bmatrix}, \quad C = \begin{bmatrix} 2 \\ m \\ 5 \end{bmatrix}$$
#
# (i) Form a matrix $M$ with these vectors as columns. For what value of $m$, if any, do the vectors become linearly dependent? Also, find the rank of the matrix for this value of $m$. **(4 marks)**
#
# (ii) Check if the matrix $M$ is an orthogonal matrix when $m = 1$. **(3 marks)**

import sympy as sp

m = sp.symbols('m')

A = sp.Matrix([1, 2, -1]) # for 3 X1 matrix
# A = sp.Matrix([[1, 2, -1]]) for 1X 3  matrix
B = sp.Matrix([3, -1, 4])
C = sp.Matrix([2, m, 5])

M = sp.Matrix.hstack(A, B, C)

# (i) Find m so columns are linearly dependent
m_vals = sp.solve(M.det(), m)
print("m values giving det(M)=0:", m_vals)

m_val = m_vals[0]
M_dep = M.subs(m, m_val)
print("rank at m =", m_val, "is", M_dep.rank())

# (ii) Check orthogonality when m = 1
M1 = M.subs(m, 1)
print("\nM when m = 1:")
print(M1)

print("\nM^T * M when m = 1:")
print(M1.T * M1)

is_orthogonal = (M1.T * M1) == sp.eye(3)
print("Is M orthogonal when m = 1?", is_orthogonal)

# Consider the matrix:
#
# $$A = \begin{bmatrix} 1 & 2 & 1 \\ 5 & 1 & 4 \\ 7 & 6 & 9 \end{bmatrix}$$
#
# - Step 1: Find the Eigenvalues of $A$.
# - Step 2: Find the Eigenvalues of $A^2$.
# - Step 3: Find the Eigenvalues of $A^{-1}$.
# - Step 4: Interpret Results.
#
# **Note:** The eigenvalues of $A^2$ are the squares of the eigenvalues of $A$. The eigenvalues of $A^{-1}$ are the reciprocals of the eigenvalues of $A$.

# Example: compute eigenvalues/vectors and verify A v = lambda v.
A = np.array([
    [1, 2, 1],
    [5, 1, 4],
    [7, 6, 9]
])

eigvals, eigvecs = np.linalg.eig(A)
print('Eigenvalues:', eigvals)
print('Eigenvectors (columns):\n', eigvecs)

# Step 1: Eigenvalues of A
eig_A, _ = np.linalg.eig(A)

print("Eigenvalues of A:")
print(eig_A)

# Eigenvalues of A^2
A2 = A @ A
eig_A2, _ = np.linalg.eig(A2)

print("\nEigenvalues of A^2:")
print(eig_A2)

# Eigenvalues of A^-1
A_inv = np.linalg.inv(A)
eig_A_inv, _ = np.linalg.eig(A_inv)

print("\nEigenvalues of A^-1:")
print(eig_A_inv)

# Interpretation
print("\nVerification:")

print("\n(lambda of A)^2:")
print(eigvals**2)  # FIXED: was eig_A (undefined)

print("\n1/(lambda of A):")
print(1/eigvals)   # FIXED: was eig_A (undefined)

print('\nVerification A v = lambda v:')
for i in range(len(eigvals)):
    lhs = A @ eigvecs[:, i]
    rhs = eigvals[i] * eigvecs[:, i]
    print(f'  lambda={eigvals[i]:.4f}:  A v = {lhs},   lambda v = {rhs}')

print(f'\nTrace check: sum of eigvals = {eigvals.sum():.4f},  trace(A) = {np.trace(A)}')
print(f'Det check:   prod of eigvals = {np.prod(eigvals):.4f},  det(A) = {np.linalg.det(A):.4f}')

# **(a)** Find the Vector Projection and Scalar Projection of $\mathbf{u}$ on $\mathbf{v}$:
# - $\mathbf{u} = [6, 7, 8]$
# - $\mathbf{v} = [2, 3, -1]$
# **(b)** Verify that $Q$ is orthogonal:
# $$Q = \frac{1}{3} \begin{bmatrix} 2 & -2 & 1 \\ 1 & 2 & 2 \\ 2 & -1 & -2 \end{bmatrix}$$
# (i) Find the **scalar projection** of $\mathbf{u}$ on $\mathbf{v}$. *(3 marks)*
# $$\text{Scalar Projection} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|}$$
# (ii) Find the **vector projection** of $\mathbf{u}$ on $\mathbf{v}$. *(3 marks)*
# $$\text{Vector Projection} = \left(\frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2}\right) \mathbf{v}$$

import numpy as np

# Part (a)
u = np.array([6, 7, 8])
v = np.array([2, 3, -1])

dot = np.dot(u, v)
norm_v = np.linalg.norm(v)

scalar_projection = dot / norm_v
vector_projection = (dot / (norm_v ** 2)) * v

print("Scalar projection of u on v:", scalar_projection)
print("Vector projection of u on v:", vector_projection)

# Part (b)
Q = (1/3) * np.array([
    [2, -2, 1],
    [1, 2, 2],
    [2, 1, -2]  # FIXED: was [2,-1,-2] (sign error in row 3, col 2)
])

QtQ = Q.T @ Q
print("\nQ^T * Q =\n", QtQ)
print("Is Q orthogonal?", np.allclose(QtQ, np.eye(3)))

# Consider the matrix $D$:
#
# $$D = \begin{bmatrix} 3 & 1 & 1 \\ -1 & 3 & 1 \end{bmatrix}$$
# (i) Perform the Singular Value Decomposition (SVD) of matrix $D$. **(3 marks)**
# (ii) Reconstruct matrix $D$ using only the first singular value and its corresponding vectors from $U$, $\Sigma$, and $V^T$. 

import numpy as np

M = np.array([[4, 2, 0],
              [1, -1, 3]], dtype=float)

# Singular Value Decomposition
U, S, Vt = np.linalg.svd(M, full_matrices=False)

Sigma = np.diag(S)

print("U =\n", U)
print("\nSigma =\n", Sigma)
print("\nV^T =\n", Vt)

# Reconstruct original matrix using all singular values
M_full = U @ Sigma @ Vt

print("\nReconstructed Matrix (Full SVD):\n")
print(M_full)

# Use the FIRST singular value and its corresponding singular vectors.
# NumPy returns singular values in descending order, so the
# FIRST singular value is also the LARGEST singular value.

#
# Rank-1 Approximation Formula:
# M_approx = σ₁ · u₁ · v₁ᵀ

sigma1 = S[0]
u1 = U[:, 0:1]
v1t = Vt[0:1, :]

M_approx = sigma1 * (u1 @ v1t)

print("\nApproximation using first/largest singular value only:\n")
print(M_approx)

print("\nOriginal Matrix:\n")
print(M)

print("\nDifference (Original - Approximation):\n")
print(M - M_approx)

print("\nFull reconstruction correct:",
      np.allclose(M, M_full))

import numpy as np

A = np.array([[4, 2, 0],
              [1, -1, 3]], dtype=float)

U, S, Vt = np.linalg.svd(A, full_matrices=False)
Sigma = np.diag(S)

print("U =\n", U)
print("Sigma =\n", Sigma)
print("V^T =\n", Vt)

# Reconstruct full A
A_full = U @ Sigma @ Vt
print("\nReconstructed A (full SVD):\n", A_full)

# Use only the largest singular value/vector
sigma1 = S[0]
u1 = U[:, 0]
v1t = Vt[0, :]

A_approx = sigma1 * np.outer(u1, v1t)
print("\nApproximation using largest singular value only:\n", A_approx)

print("\nOriginal A:\n", A)
print("\nDifference A - A_approx:\n", A - A_approx)

# Transform the following basis into an orthogonal basis using the Gram-Schmidt Process:
#
# $$U_1 = (2, 1, 0), \quad U_2 = (3, 2, 1), \quad U_3 = (4, 1, 2)$$

import numpy as np

#  Gram-Schmidt on U1=(2,1,0), U2=(3,2,1), U3=(4,1,2)

def gram_schmidt(vectors):
    """Returns orthogonal (NOT orthonormal) basis via Gram-Schmidt."""
    basis = []
    for v in vectors:
        w = v.copy().astype(float)
        for b in basis:
            proj = np.dot(w, b) / np.dot(b, b) * b
            w = w - proj
        if not np.allclose(w, 0):
            basis.append(w)
    return basis

U1 = np.array([2, 1, 0], dtype=float)
U2 = np.array([3, 2, 1], dtype=float)
U3 = np.array([4, 1, 2], dtype=float)

orthogonal_basis = gram_schmidt([U1, U2, U3])

print("Orthogonal Basis:")
for idx, v in enumerate(orthogonal_basis, 1):
    print(f"  v{idx} = {np.round(v, 6)}")

# Verify orthogonality: each pair should have dot product ≈ 0
print("\nOrthogonality checks (dot products should be ≈ 0):")
v1, v2, v3 = orthogonal_basis
print(f"  v1·v2 = {np.dot(v1,v2):.6f}")
print(f"  v1·v3 = {np.dot(v1,v3):.6f}")
print(f"  v2·v3 = {np.dot(v2,v3):.6f}")

# Orthonormal basis (unit vectors)
orthonormal_basis = [v / np.linalg.norm(v) for v in orthogonal_basis]
print("\nOrthonormal Basis (unit vectors):")
for idx, v in enumerate(orthonormal_basis, 1):
    print(f"  q{idx} = {np.round(v, 6)}")

# INFERENCE
print("\Gram-Schmidt converts any linearly independent set into an orthogonal basis.")
print("   The original span is preserved — only the direction of basis vectors changes.")

# Given the matrix:
#
# $$A = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 0 & 2 \\ 1 & 1 & 3 \end{bmatrix}$$
#
# (i) Use the **Gram-Schmidt Process** to convert the columns of matrix $A$ into an orthonormal set of vectors.
#
# (ii) Form a matrix $Q$ using these orthonormal vectors as columns and confirm orthonormality ($Q^T Q = I$).

import numpy as np

A = np.array([[1, 2, 1],
              [2, 0, 2],
              [1, 1, 3]], dtype=float)#

def gram_schmidt_columns(X):
    n = X.shape[1]
    Q = np.zeros_like(X, dtype=float)
    for j in range(n):
        v = X[:, j].copy()
        for i in range(j):
            qi = Q[:, i]
            proj = np.dot(qi, v) * qi
            v = v - proj
        norm = np.linalg.norm(v)
        if norm < 1e-12:
            raise ValueError(f"Column {j} is linearly dependent on previous columns")
        Q[:, j] = v / norm
    return Q

Q = gram_schmidt_columns(A)

print("Q =")
print(Q)
print("\nQ^T Q =")
print(Q.T @ Q)
print("\nIs Q orthonormal?", np.allclose(Q.T @ Q, np.eye(Q.shape[1])))

# Find the covariance for the following set of vectors:
#
# $$A = \begin{bmatrix} -1 & 2 \\ 3 & 5 \\ 0 & 1 \\ 4 & 2 \\ 6 & 1 \end{bmatrix}$$

import numpy as np

A = np.array([
    [-1, 2],
    [3, 5],
    [0, 1],
    [4, 2],
    [6, 1]
], dtype=float)# row wise observations

# Each column is a variable, each row is an observation
cov_matrix = np.cov(A, rowvar=False, ddof=1)

print("Covariance matrix:\n", cov_matrix)

#  INFERENCE
print("\nCovariance Interpretation:")
print(f"  Var(X1) = {cov_matrix[0,0]:.4f}  | Var(X2) = {cov_matrix[1,1]:.4f}")
print(f"  Cov(X1, X2) = {cov_matrix[0,1]:.4f}")
direction = 'POSITIVE' if cov_matrix[0,1] > 0 else 'NEGATIVE'
print(f"  {direction} covariance — variables tend to {'move together' if cov_matrix[0,1]>0 else 'move in opposite directions'}.")

# The following table lists the weight and heights of 5 boys. Find the **covariance matrix** for the data:
#
# \[
# \begin{array}{|c|c|c|c|c|c|}
# \hline
# Boy & 1 & 2 & 3 & 4 & 5 \\
# \hline
# Weight (lb) & 120 & 125 & 125 & 135 & 145 \\
# \hline
# Height (in.) & 61 & 60 & 64 & 68 & 72 \\
# \hline
# \end{array}
# \]
#
#
# Calculate the covariance between the Math scores $X$ and the English scores $Y$. What does the value of the covariance signify? Is there a positive or negative relationship?
#
# - Math Scores $X$: [60, 70, 80, 65, 75]
# - English Scores $Y$: [62, 82, 78, 70, 80]

import numpy as np

data = np.array([
    [120, 125, 125, 135, 145],  # weights
    [61,  60,  64,  68,  72]    # heights
], dtype=float)

cov_matrix = np.cov(data, ddof=1)  # rowvar=True by default
print("Covariance matrix:\n", cov_matrix)

# INFERENCE 
print("\nCovariance Matrix Interpretation:")
print(f"  Var(Weight) = {cov_matrix[0,0]:.4f}")
print(f"  Var(Height) = {cov_matrix[1,1]:.4f}")
print(f"  Cov(Weight, Height) = {cov_matrix[0,1]:.4f}")
if cov_matrix[0, 1] > 0:
    print("  POSITIVE covariance: Boys who weigh more tend to be taller.")
else:
    print("  NEGATIVE covariance: Heavier boys tend to be shorter.")

# 1. Import the **Iris dataset** from `sklearn.datasets`.
# 2. Preprocess the data by subtracting the mean and dividing by the standard deviation of each attribute value. The resulting data should be zero-mean with variance 1. **(2 marks)**
# 3. Compute the **covariance matrix**. **(2 marks)**
# 4. Factorize the covariance matrix using **Singular Value Decomposition (SVD)** and obtain the eigenvalues and eigenvectors. **(2 marks)**
# 5. Find the **principal components**. **(1 mark)**

import numpy as np
from sklearn.datasets import load_iris

# 1. Load data
iris = load_iris()
X = iris.data  # shape (150, 4)

# 2. Standardize (zero mean, variance 1)
mu = X.mean(axis=0)
sigma = X.std(axis=0, ddof=0)   # population std so variance = 1 after scaling
X_std = (X - mu) / sigma

print("Means after standardization (should be ~0):", X_std.mean(axis=0))
print("Variances after standardization (should be 1):", X_std.var(axis=0))

# 3. Covariance matrix (use ddof=0 to match the standardization above)
cov = np.cov(X_std, rowvar=False, ddof=0)
print("\nCovariance matrix:\n", cov)

# 4. SVD of covariance and eigenvalues/eigenvectors
U, S, Vt = np.linalg.svd(cov, full_matrices=False)
eigenvalues = S            # for symmetric PSD matrix, singular values == eigenvalues
eigenvectors = Vt.T        # columns are eigenvectors
print("\nEigenvalues (from SVD):\n", eigenvalues)
print("\nEigenvectors (columns):\n", eigenvectors)

# 5. Principal components (project standardized data onto eigenvectors)
principal_components = X_std @ eigenvectors
print("\nPrincipal components shape:", principal_components.shape)
print("First 5 rows of principal components:\n", principal_components[:5])

# Apply **PCA step by step** on the **Wine dataset** and find the principal components that capture **95% variance**.
# ```

import numpy as np  # ADDED: was missing in original
# PCA from scratch on the wine dataset — find PCs that capture >= 95% variance.
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler

data = load_wine()#
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

k = int(np.searchsorted(cum, 0.95) + 1)#
print(f'\n=> {k} principal components capture >= 95% variance')

# Step 6: project
W = eigvecs[:, :k]
X_pca = X_std @ W
print(f'Reduced shape: {X_pca.shape}  (from 13 features down to {k})')

# Compute **PCA** on the following data:
#
# \[
# \begin{array}{|c|c|c|}
# \hline
# Data Point & X1 & X2 \\
# \hline
# 1 & 2 & 4 \\
# \hline
# 2 & -3 & 5 \\
# \hline
# 3 & 5 & 4 \\
# \hline
# 4 & 6 & 7 \\
# \hline
# 5 & 7 & 6 \\
# \hline
# \end{array}
# \]
#
# Steps:
# 1. Centre the data
# 2. Calculate Covariance Matrix
# 3. Compute Eigenvalues and Eigenvectors
# 4. Select principal components
# 5. Transform the data

import numpy as np

X = np.array([
    [2, 4],
    [-3, 5],
    [5, 4],
    [6, 7],
    [7, 6]
])

print("Original Data:\n", X)

# Step 1: Center the data
mean = np.mean(X, axis=0)
X_centered = X - mean

print("\nMean:", mean)
print("\nCentered Data:\n", X_centered)

# Step 2: Covariance Matrix
cov_matrix = np.cov(X_centered, rowvar=False)

print("\nCovariance Matrix:\n", cov_matrix)

# Step 3: Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)

# Step 4: Sort eigenvalues in descending order
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("\nSorted Eigenvalues:\n", eigenvalues)
print("\nSorted Eigenvectors:\n", eigenvectors)

# First Principal Component
pc1 = eigenvectors[:, 0]
print("\nFirst Principal Component:\n", pc1)

# Step 5: Transform the data
X_pca = X_centered @ eigenvectors

print("\nTransformed Data:\n", X_pca)

# Variance explained
explained_variance_ratio = eigenvalues / np.sum(eigenvalues)

print("\nExplained Variance Ratio:")
for i, ratio in enumerate(explained_variance_ratio, start=1):
    print(f"PC{i}: {ratio:.4f}")

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
