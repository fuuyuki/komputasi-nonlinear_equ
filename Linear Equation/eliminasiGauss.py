def gauss_elimination(a, b):
    n = len(b)

    # Forward elimination
    for i in range(n):
        # Pivoting
        if a[i][i] == 0:
            for j in range(i + 1, n):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    b[i], b[j] = b[j], b[i]
                    break

        pivot = a[i][i]
        if pivot == 0:
            raise ValueError("Matrix is singular or nearly singular.")

        # Normalize pivot row
        for j in range(i, n):
            a[i][j] /= pivot
        b[i] /= pivot

        # Eliminate below
        for k in range(i + 1, n):
            factor = a[k][i]
            for j in range(i, n):
                a[k][j] -= factor * a[i][j]
            b[k] -= factor * b[i]

    # Back substitution
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]

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
    A = [[6, -2, 2, 4], [12, -8, 6, 10], [3, -13, 9, 3], [-6, 4, 1, -18]]
    b = [16, 26, -19, -34]
    print("Using example system:")
    print("A =", A)
    print("b =", b)

# Solve
solution = gauss_elimination(A, b)
print("Solution vector x:", solution)
