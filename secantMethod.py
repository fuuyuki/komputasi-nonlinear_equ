from math import cos, sin


# Fungsi rumus Secant
def Secant(pers, x0, x1, eps):
    # Terjemahkan input persamaan dari user ke dalam fungsi f(x)
    def f(x):
        return eval(pers, {"x": x, "cos": cos, "sin": sin})

    # Turunan menggunakan numerical approximation
    def df(x, h=1e-6):
        return (f(x + h) - f(x - h)) / (2 * h)

    x_oldbanget = x0  # simpan x0 sebagai x_oldbanget (xi-1)
    x_old = x1  # simpan x1 sebagai x_old (xi)
    i = 0
    print("x" + str(i) + " ≈ " + str(x0))  # cetak x0
    print("x" + str(++i) + " ≈ " + str(x1))  # cetak x1

    # Lakukan iterasi untuk xi
    while True:
        i = i + 1  # hitung iterasi
        # hitung xi baru (xi+1)
        xi = x_old - (f(x_old) / (f(x_old) - f(x_oldbanget))) * (x_old - x_oldbanget)
        print("x" + str(i) + f" ≈ {xi:.14f}")  # cetak akar ke-i dengan 14 digit
        Er = abs(xi - x_old)  # perbarui galat

        # Cek apakah galat sudah di bawah epsilon
        if Er < eps:
            break

        # Jika belum, jadikan xi sebagai x_old
        # repeat iterasi
        x_oldbanget = x_old
        x_old = xi

    print("======================")
    print(f"Hampiran akar x ≈ {xi:.14f}" + " pada iterasi ke-" + str(i))


# --- Interactive part ---
pers = input("Masukkan persamaan x (contoh, 'x - cos(x)'): ")
x0 = float(input("Masukkan nilai x0: "))
x1 = float(input("Masukkan nilai x1: "))
eps = float(input("Masukkan galat epsilon (contoh, 1e-6): "))

# Panggil Fungsi
Secant(pers, x0, x1, eps)
