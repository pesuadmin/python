import os
print("Current Directory:")
print(os.getcwd())
print("\nFiles in Current Directory:")
print(os.listdir())


# Image Processing
import numpy as np
import matplotlib.pyplot as plt
!pip install opencv-python
import os
import cv2

# Original
img = cv2.imread("dolphin.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# GaussianBlur
gaussian_blur = cv2.GaussianBlur(img_rgb, (5, 5), 0)

# Sharpening
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharpened = cv2.filter2D(img_rgb, -1, kernel)

# Negative
negative = 255 - img_rgb

# ResizeHalf
h, w = img_rgb.shape[:2]
resize_half = cv2.resize(img_rgb, (w // 2, h // 2))

# Translate 100 right _50 down
M1 = np.float32([[1, 0, 100],
                 [0, 1, 50]])
translate_100_50 = cv2.warpAffine(img_rgb, M1, (w, h))

# Grayscale
gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# MedianBlur.  - Kerbel size = 5
median_blur = cv2.medianBlur(gray, 5)

# EdgeDetection
edges = cv2.Canny(median_blur, 100, 200)

# Scale by 1.5
scale_1_5 = cv2.resize(img_rgb, None, fx=1.5, fy=1.5)

# Translate by 0.2 and 0.1
tx = int(0.2 * w)
ty = int(0.1 * h)

M2 = np.float32([[1, 0, tx],
                 [0, 1, ty]])

translate_factor = cv2.warpAffine(img_rgb, M2, (w, h))

# Rotate43
center = (w // 2, h // 2)
R = cv2.getRotationMatrix2D(center, 43, 1)
rotate_43 = cv2.warpAffine(img_rgb, R, (w, h))

# Scale49Percent
scale_49 = cv2.resize(img_rgb, None, fx=0.49, fy=0.49)

# Display
images = [
    img_rgb,
    gaussian_blur,
    sharpened,
    negative,
    resize_half,
    translate_100_50,
    gray,
    median_blur,
    edges,
    scale_1_5,
    translate_factor,
    rotate_43,
    scale_49
]

titles = [
    "Original",
    "Gaussian Blur",
    "Sharpening",
    "Negative",
    "Resize Half",
    "Translate 100,50",
    "Grayscale",
    "Median Blur",
    "Canny Edge",
    "Scale 1.5",
    "Translate 0.2,0.1",
    "Rotate 43",
    "Scale 49%"
]

plt.figure(figsize=(16, 12))

for i in range(len(images)):
    plt.subplot(4, 4, i + 1)

    if len(images[i].shape) == 2:
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(images[i])

    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()





# Compute the following **convolution** for the middle pixel with intensity 99. What visual effect will the following convolution have on the image?
#
# **Image patch:**
#
# \[
# \begin{array}{|c|c|c|}
# \hline
# 138 & 134 & 101 \\
# \hline
# 119 & **99** & 83 \\
# \hline
# 84 & 80 & 79 \\
# \hline
# \end{array}
# \]
#
# **Kernel:**
#
# \[
# \begin{array}{|c|c|c|}
# \hline
# 0 & -1 & 0 \\
# \hline
# -1 & 5 & -1 \\
# \hline
# 0 & -1 & 0 \\
# \hline
# \end{array}
# \]

import numpy as np

image_patch = np.array([
    [138, 134, 101],
    [119,  99,  83],
    [ 84,  80,  79]
])

kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

result = np.sum(image_patch * kernel)

print("Convolution Result =", result)
print("\nConvolution Result =", result)
print("\nINFERENCE — Visual Effect: This is a SHARPENING kernel (Laplacian-based).")
print("  Center pixel weight = +5 (amplified); Neighbour weights = -1 (subtracted).")
print("  Effect: Enhances edges and fine details, increases local contrast




      # Consider a 3×3 image $A$ with values:
#
# $$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$$
#
# and a 2×2 kernel matrix $K$ with values:
#
# $$K = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$$
#
# **Perform the convolution operation.**

import numpy as np

# Image matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Kernel matrix
K = np.array([
    [ 1, -1],
    [-1,  1]
])

# Output size
out_rows = A.shape[0] - K.shape[0] + 1
out_cols = A.shape[1] - K.shape[1] + 1

# Convolution result
output = np.zeros((out_rows, out_cols), dtype=int)

for i in range(out_rows):
    for j in range(out_cols):
        region = A[i:i+K.shape[0], j:j+K.shape[1]]
        output[i, j] = np.sum(region * K)

print("Image A:")
print(A)

print("\nKernel K:")
print(K)

print("\nConvolution Output:")
print(output)




# The following box was applied transformation:
#
# $$T = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$$
#
# Calculate the distance between the new points that are obtained from [1, 0] and [1, 1].

import numpy as np

T = np.array([[1, 2],
              [0, 1]])

P1 = np.array([1, 0])
P2 = np.array([1, 1])

P1_new = T @ P1
P2_new = T @ P2

distance = np.linalg.norm(P2_new - P1_new)

print("P1' =", P1_new)
print("P2' =", P2_new)
print("Distance =", distance)



# Calculate the **angle between two given vectors**:
#
# $$\mathbf{a} = 4\mathbf{i} + 2\mathbf{j}, \quad \mathbf{b} = \mathbf{i} + 3\mathbf{j}$$

import numpy as np

# Given vectors
a = np.array([4, 2])
b = np.array([1, 3])

# Dot product
dot_product = np.dot(a, b)

# Magnitudes
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)

# Angle
cos_theta = dot_product / (norm_a * norm_b)
theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)

print("Angle (radians):", theta_rad)
print("Angle (degrees):", theta_deg)



# Consider the vectors $\mathbf{a} = [1, 2, 3]$ and $\mathbf{b} = [4, 5, 6]$.
#
# (i) Calculate $\|\mathbf{a} - \mathbf{b}\|_1$ (L1 norm of the difference). **(2 marks)**
#
# (ii) Calculate $\|\mathbf{a} - \mathbf{b}\|_2$ (L2 norm / Euclidean distance). **(1 mark)**
#
# (iii) Find the **angle** $\theta$ between $\mathbf{a}$ and $\mathbf{b}$. **(1 mark)**
#
# (iv) Find the **unit vector** along $\mathbf{a} + \mathbf{b}$. **(1 mark)**

import numpy as np

# Given vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Difference vector
diff = a - b

# (i) L1 Norm
l1_norm = np.linalg.norm(diff, ord=1)
print("(i) L1 Norm =", l1_norm)

# (ii) L2 Norm (Euclidean Distance)
l2_norm = np.linalg.norm(diff)
print("(ii) L2 Norm =", l2_norm)

# (iii) Angle between a and b
dot_product = np.dot(a, b)
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)

cos_theta = dot_product / (norm_a * norm_b)
theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)

print("(iii) Angle (radians) =", theta_rad)
print("(iii) Angle (degrees) =", theta_deg)

# (iv) Unit vector along (a + b)
sum_vector = a + b
unit_vector = sum_vector / np.linalg.norm(sum_vector)

print("(iv) Unit Vector along (a + b) =")
print(unit_vector)

# Define a **scalar** and a **vector**. Give one example of each.
#
# Calculate the **angle** between two given vectors:
#
# $$\mathbf{a} = 3\mathbf{i} + 4\mathbf{j}, \quad \mathbf{b} = 6\mathbf{i} + 8\mathbf{j}$$

import math

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def mag(v):
    return math.hypot(v[0], v[1])

def angle_deg(a, b):
    ma, mb = mag(a), mag(b)
    if ma == 0 or mb == 0:
        raise ValueError("Zero-length vector")
    cos_theta = max(-1.0, min(1.0, dot(a, b) / (ma * mb)))
    return math.degrees(math.acos(cos_theta))

if __name__ == "__main__":
    a = (3, 4)
    b = (6, 8)
    print("Scalar: magnitude only (e.g., temperature = 20°C)")
    print("Vector: magnitude + direction (e.g., velocity = 5 m/s east)\n")
    print(f"a = {a}, b = {b}")
    print(f"Dot product = {dot(a,b)}")
    print(f"|a| = {mag(a)}, |b| = {mag(b)}")
    print(f"Angle between a and b = {angle_deg(a,b):.6f} degrees")
#  INFERENCE
print("\nINFERENCE: b = (6,8) = 2 × (3,4) = 2a → vectors are PARALLEL.")
print("   Parallel vectors have angle = 0° between them.")


# The following box was **rotated at an angle of 60° counter-clockwise** around the origin (or point A).
#
# Find out the **distance between the coordinate point of the box** which passes through the y-axis (excluding the origin or the point A) **after the transformation** and the point A.
#
# *(The box has corners at A=(0,0) and another point on the y-axis at (0,2))*
#
# Steps:
# 1. Apply the 2D rotation matrix for 60°:
# $$R = \begin{bmatrix} \cos 60° & -\sin 60° \\ \sin 60° & \cos 60° \end{bmatrix}$$
# 2. Find the new coordinates of the point (0, 2) after rotation.
# 3. Calculate the distance from the new point to the origin A.

import numpy as np

# Point on y-axis
P = np.array([0, 2])

# Rotation angle
theta = np.radians(60)

# Rotation matrix
R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# Rotated point
P_new = R @ P

# Distance from origin
distance = np.linalg.norm(P_new)

print("New Coordinates:", P_new)
print("Distance from Origin:", distance)


# In the plot shown below, the **dark shaded portion** represents the original coordinates of an object and the **lightly shaded object** represents the same after transformation.
#
# **Write the coordinates, the transformation matrix and the coordinates after transformation.**
#
# *(The original shape has vertices approximately at: (0,0), (2,0), (2,2), (0,2); the transformed shape appears scaled/sheared)*
#
# Steps:
# 1. Identify the original coordinates from the plot.
# 2. Identify the transformed coordinates.
# 3. Determine the transformation matrix $T$ such that: $X' = T \cdot X$
# 4. Verify by applying $T$ to the original coordinates.

import numpy as np

X = np.array([
    [0,2,2,0],
    [0,0,2,2]
])

T = np.array([
    [1,1],
    [0,1]
])

X_prime = T @ X

print(X_prime)

# A particle travels along the path given by the function $f(x) = 2\sin(x) + 3\cos(x)$, where $x$ represents time in seconds.
#
# 1. **Plot the path function** of the particle.
# 2. **Find the rate of change** of the path of the particle:
#    - Using the limit concept.
#    - Using the differential function.
# 3. **Plot the rate of change** of the path of the particle.
# 4. **Find the rate of change** of path at $x = 60°$ (or $\pi/3$ radians):
#    - Using the limit concept.
#    - Using the differential function.
# 5. **Plot the rate of change** of the path at $x = 60°$.

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Symbolic setup
x = sp.symbols('x')
f_sym = 2*sp.sin(x) + 3*sp.cos(x)

# 1. Path function
f = sp.lambdify(x, f_sym, 'numpy')

# 2. Derivative symbolically
f_prime_sym = sp.diff(f_sym, x)
f_prime = sp.lambdify(x, f_prime_sym, 'numpy')

# 2a. Rate of change by the limit definition
h = sp.symbols('h')
limit_def = sp.limit((f_sym.subs(x, x+h) - f_sym.subs(x, x))/h, h, 0)
limit_func = sp.lambdify(x, limit_def, 'numpy')

# 4. Rate of change at x = pi/3
x_val = sp.pi/3
rate_limit_at = limit_def.subs(x, x_val)
rate_diff_at = f_prime_sym.subs(x, x_val)

print("Function f(x) =", f_sym)
print("Derivative f'(x) =", f_prime_sym)
print("Rate of change by limit definition f'(x) =", limit_def)
print()
print("Rate of change at x = pi/3 using limit:", sp.simplify(rate_limit_at))
print("Rate of change at x = pi/3 using derivative:", sp.simplify(rate_diff_at))

# Numeric arrays for plots
xs = np.linspace(0, 2*np.pi, 400)
ys = f(xs)
ys_prime = f_prime(xs)

# 1. Plot the path function
plt.figure(figsize=(10, 4))
plt.plot(xs, ys, label='f(x) = 2 sin(x) + 3 cos(x)')
plt.scatter([np.pi/3], [f(np.pi/3)], color='red', label='x = π/3')
plt.xlabel('x (radians)')
plt.ylabel('f(x)')
plt.title('Particle Path')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# 3. Plot the rate of change
plt.figure(figsize=(10, 4))
plt.plot(xs, ys_prime, label="f'(x) = 2 cos(x) - 3 sin(x)")
plt.scatter([np.pi/3], [f_prime(np.pi/3)], color='red', label='x = π/3')
plt.xlabel('x (radians)')
plt.ylabel("f'(x)")
plt.title('Rate of Change of Particle Path')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# 5. Plot the rate of change at x = 60°
plt.figure(figsize=(6, 4))
plt.plot(xs, ys_prime, label="f'(x)")
plt.scatter([np.pi/3], [f_prime(np.pi/3)], color='red', s=80, label='x = π/3')
plt.axvline(np.pi/3, color='gray', linestyle='--', alpha=0.6)
plt.xlabel('x (radians)')
plt.ylabel("f'(x)")
plt.title('Rate of Change at x = 60° (π/3)')
plt.legend()
plt.grid(alpha=0.3)
plt.show()




