# komputasi-nonlinear_equ
Ini adalah tugas mata kuliah Komputasi Numeris

This repository contains Jupyter Notebooks showcasing fundamental numerical methods for solving equations and analyzing data. Each notebook focuses on a specific class of problems and algorithms.

---

## 📘 Contents

### 1. Numerical - Linear Solutions.ipynb
- **Purpose:** Solve systems of linear equations using direct and iterative methods.
- **Implemented Methods:**
  - **Gauss Elimination:** Forward elimination and back substitution.
  - **Gauss-Jordan Elimination:** Full elimination to reduced row echelon form.
  - **Gauss-Seidel Iteration:** Iterative refinement using updated values.
  - **Jacobi Iteration:** Iterative refinement using old values.
- **Features:**
  - Pivoting to avoid division by zero.
  - Convergence checks for iterative methods.
  - Example system provided:
    ```
    A = [[10, 2, -1], [-3, -6, 2], [1, 1, 5]]
    b = [27, -61.5, -21.5]
    ```
- **Output:** Solution vector `x` for each method, with iteration counts for Gauss-Seidel and Jacobi.

---

### 2. Numerical - NonLinear Root Finding.ipynb
- **Purpose:** Find roots of nonlinear equations using iterative methods.
- **Equation Example:**
```equation
f(x) = x - cos(x)
```
- **Implemented Methods:**
- **Bisection Method:** Interval halving until tolerance is met.
- **Secant Method:** Uses two initial guesses, iterates with secant formula.
- **Newton-Raphson Method:** Uses derivative (approximated numerically) for fast convergence.
- **Features:**
- Interactive input for equation, initial guesses, and tolerance.
- Iteration logs showing progress toward the root.
- Numerical derivative approximation for Newton-Raphson.
- **Output:** Approximate root with iteration count for each method.

---

### 3. Numerical - Fitting Regression.ipynb
- **Purpose:** Fit data to different regression models using normal equations.
- **Models Implemented:**
- Linear regression.
- Quadratic regression.
- Cubic polynomial regression.
- Custom nonlinear regression:
  

\[
  f(x) = a \ln(x) + b \cos(x) + c e^x
  \]


- **Features:**
- Tabular expansion with sums for normal equations.
- Explicit matrix construction and solution using `numpy.linalg.solve`.
- Error function evaluation:
  

\[
  \Phi = \sum (f(x_i) - y_i)^2
  \]


- **Output:** Coefficients for each model, plots comparing fits, and error values.

---

### 4. Numerical - Interpolation.ipynb
- **Purpose:** Interpolate data points using classical polynomial interpolation methods.
- **Implemented Methods:**
- **Lagrange Interpolation:** Direct formula using basis polynomials.
- **Newton Interpolation:** Divided differences and recursive polynomial construction.
- **Features:**
- Functions to evaluate interpolation at any point.
- Continuous evaluation across a range of x-values.
- Comparison plots of Lagrange and Newton interpolations against original data.
- **Output:** Interpolated curves and numerical comparisons at selected points.

---

## 🚀 How to Use
1. Open each notebook in Jupyter Lab or Jupyter Notebook.
2. Run cells sequentially to see calculations, iteration logs, and plots.
3. Modify input data (`A`, `b`, `x`, `y`, equations) to experiment with your own problems.
4. Compare methods by checking both numerical results and visual plots.

---

## 📊 Applications
- **Linear Solutions:** Engineering systems, circuit analysis, balance equations.
- **NonLinear Root Finding:** Physics problems, optimization, equilibrium analysis.
- **Fitting Regression:** Data modeling, curve fitting, trend analysis.
- **Interpolation:** Estimating values between known data points, numerical analysis.

---

## 🛠 Requirements
- Python 3.x
- NumPy
- Matplotlib
- Pandas (for regression tables)

