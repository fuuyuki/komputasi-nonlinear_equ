def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    n = len(b)
    # initial guess
    x = [0.0] * n if x0 is None else x0[:]

    for k in range(max_iter):
        x_new = x[:]
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))  # updated values
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))  # old values
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]

        # convergence check (infinity norm)
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            print(f"Converged in {k + 1} iterations")
            return x_new
        x = x_new

    print("Did not converge within max_iter")
    return x


# --- Input selection ---
choice = input("Do you want to input the matrix manually? (Y/n): ").strip().lower()

if choice == "y":
    N = int(input("Enter the size of the matrix (N): "))

    A = []
    print("Enter the elements of matrix A row by row:")
    for i in range(N):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != N:
            raise ValueError("Each row must have exactly N elements.")
        A.append(row)

    print("Enter the elements of vector b:")
    b = list(map(float, input().split()))
    if len(b) != N:
        raise ValueError("Vector b must have exactly N elements.")

else:
    # Example system
    A = [[10, 2, -1], [-3, -6, 2], [1, 1, 5]]
    b = [27, -61.5, -21.5]
    print("Using example system:")
    print("A =", A)
    print("b =", b)

# Solve
solution = gauss_seidel(A, b)
solution = [round(val, 2) for val in solution]  # rounded solution
print("Solution vector x:", solution)
