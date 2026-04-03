def gauss_jordan(a, b):
    """
    Solve system of linear equations Ax = b using Gauss-Jordan elimination.
    a : coefficient matrix (list of lists)
    b : constants vector (list)
    Returns solution vector x
    """
    n = len(b)

    # Augment matrix A with vector b
    for i in range(n):
        a[i].append(b[i])

    # Perform Gauss-Jordan elimination
    for i in range(n):
        # Pivoting
        if a[i][i] == 0:
            for j in range(i + 1, n):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    break

        pivot = a[i][i]
        if pivot == 0:
            raise ValueError("Matrix is singular or nearly singular.")

        # Normalize pivot row
        for j in range(i, n + 1):
            a[i][j] /= pivot

        # Eliminate all other rows
        for k in range(n):
            if k != i:
                factor = a[k][i]
                for j in range(i, n + 1):
                    a[k][j] -= factor * a[i][j]

    # Extract solution
    x = [a[i][n] for i in range(n)]
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
solution = gauss_jordan(A, b)
solution = [round(val, 2) for val in solution]  # rounded solution
print("Solution vector x:", solution)
