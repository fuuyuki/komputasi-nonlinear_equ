# komputasi-nonlinear_equ
Ini adalah tugas mata kuliah Komputasi Numeris

# Numerical Methods Collection

This repository contains a set of Jupyter Notebooks demonstrating core numerical methods in applied mathematics and computational science. Each notebook focuses on a different theme: solving equations, regression fitting, and interpolation.

---

## 📘 Contents

### 1. Numerical - Linear Solutions.ipynb
- **Purpose:** Demonstrates solving systems of linear equations using normal equations and matrix algebra.
- **Key Topics:**
  - Construction of normal equations from tabular sums.
  - Solving for coefficients in linear and polynomial regression models.
  - Visualization of fitted lines against data points.
- **Output:** Coefficients of linear models and plots showing the fit.

---

### 2. Numerical - NonLinear Root Finding.ipynb
- **Purpose:** Explores methods for finding roots of nonlinear equations.
- **Key Topics:**
  - Iterative methods such as Newton–Raphson, Bisection, and Secant.
  - Convergence behavior and stopping criteria.
  - Comparison of accuracy and efficiency across methods.
- **Output:** Step-by-step iterations, convergence tables, and plots of function vs. root approximations.

---

### 3. Numerical - Fitting Regression.ipynb
- **Purpose:** Fits data to different models (linear, quadratic, cubic polynomial, and custom nonlinear).
- **Key Topics:**
  - Building tabular data with powers and cross-terms.
  - Normal equations for linear, quadratic, and cubic polynomial regression.
  - Custom nonlinear regression with basis functions: `ln(x)`, `cos(x)`, and `exp(x)`.
  - Error function evaluation:  
    

\[
    \Phi = \sum (f(x_i) - y_i)^2
    \]


- **Output:** Coefficients for each model, comparison plots, and error values to assess fit quality.

---

### 4. Numerical - Interpolation.ipynb
- **Purpose:** Performs interpolation of data points using Lagrange and Newton methods.
- **Key Topics:**
  - Lagrange interpolation formula.
  - Newton interpolation with divided differences.
  - Evaluation of interpolated values across a continuous range.
  - Comparison of both methods visually and numerically.
- **Output:** Interpolated curves plotted against original data points, with optional tables comparing values at selected test points.

---

## 🚀 How to Use
1. Open each notebook in Jupyter Lab or Jupyter Notebook.
2. Run cells sequentially to see calculations, tables, and plots.
3. Modify the data arrays (`x`, `y`) to experiment with your own datasets.
4. Compare methods by checking both visual plots and numerical error values.

---

## 📊 Applications
- **Linear Solutions:** Engineering systems, balance equations.
- **NonLinear Root Finding:** Physics problems, optimization, equilibrium analysis.
- **Fitting Regression:** Data modeling, curve fitting, trend analysis.
- **Interpolation:** Estimating values between known data points, numerical analysis.

---

## 🛠 Requirements
- Python 3.x
- NumPy
- Pandas
- Matplotlib
