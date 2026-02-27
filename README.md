# komputasi-nonlinear_equ
Ini adalah tugas mata kuliah Komputasi Numeris

This repository contains Python implementations of numerical methods for solving nonlinear equations. This repo contains these methods:
- Bisection Method
- Newton–Raphson Method
- Secant Method

Each script is interactive: when you run it, the program will ask for the equation, initial guesses, and tolerance (epsilon).

# Usage
Clone the repository:
```bash
git clone https://github.com/fuuyuki/komputasi-nonlinear_equ.git
cd komputasi-nonlinear_equ
```
Run the desired method:
# Bisection Method
```bash
python bisectionMethod.py //or
python3 bisectionMethod.py
```
You will be prompted for:
- Equation (e.g. `x - cos(x)`)
- Interval `[a, b]` (must bracket the root, i.e. f(a) and f(b) have opposite signs)
- Tolerance

# Newton–Raphson
```bash
python newtonRaphson.py //or
python3 newtonRaphson.py
```

You will be prompted for:
- Equation (e.g. `x - cos(x)`)
- Initial guess `x0`
- Tolerance (e.g. `1e-6`)

# Secant Method
```bash
python secantMethod.py //or
python3 secantMethod.py
```

You will be prompted for:
- Equation (e.g. `x - cos(x)`)
- Two initial guesses `x0`, `x1`
- Tolerance

# Example Run
```Text
Masukkan persamaan x (contoh, 'x - cos(x)'): 3*x**2 - x - 2
Masukkan nilai a(x0): 0.5
Masukkan nilai b(x1): 1.5
Masukkan galat epsilon (contoh, 1e-6): 5e-2
Iterasi 1: [0.50000000000000, 1.50000000000000], c ≈ 1.00000000000000
======================
Hampiran akar x ≈ 1.00000000000000 pada iterasi ke-1
```

