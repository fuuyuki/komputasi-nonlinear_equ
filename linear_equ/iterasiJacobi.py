def jacobi(A, b, x0=None, tol=1e-10, max_iter=100):
    """
    Solve Ax = b using the Jacobi iterative method.

    Parameters:
    A : list of lists
        Coefficient matrix (n x n)
    b : list
        Right-hand side vector (n)
    x0 : list
        Initial guess (default: zeros)
    tol : float
        Convergence tolerance
    max_iter : int
        Maximum number of iterations

    Returns:
    x : list
        Approximate solution vector
    """
    n = len(b)
    # initial guess
    x = [0.0] * n if x0 is None else x0[:]

    for k in range(max_iter):
        x_new = [0.0] * n
        for i in range(n):
            # compute sum excluding diagonal element
            sum_terms = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_terms) / A[i][i]

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
    A = [[10, 2, -1], [-3, -6, 2], [1, 1, 5]]
    b = [27, -61.5, -21.5]

    # Example system
    # A = [[2, -2, 2], [4, 2, -1], [2, -2, 4]]
    # b = [0, 7, 2]
    print("Using example system:")
    print("A =", A)
    print("b =", b)

# Solve
solution = jacobi(A, b)
solution = [round(val, 2) for val in solution]  # rounded solution
print("Solution vector x:", solution)
