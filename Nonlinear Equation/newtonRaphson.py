from math import cos, sin


# Fungsi rumus Newton Raphson
def newtonRaph(pers, x0, eps):
    # Terjemahkan input persamaan dari user ke dalam fungsi f(x)
    def f(x):
        return eval(pers, {"x": x, "cos": cos, "sin": sin})

    # Turunan menggunakan numerical approximation
    def df(x, h=1e-6):
        return (f(x + h) - f(x - h)) / (2 * h)

    x_old = x0  # simpan x0 sebagai x_old
    i = 0
    print("x" + str(i) + " ≈ " + str(x0))  # cetak x0

    # Lakukan iterasi untuk xi
    while True:
        i = i + 1  # hitung iterasi
        xi = x_old - (f(x_old) / df(x_old))  # hitung xi baru
        print("x" + str(i) + f" ≈ {xi:.14f}")  # cetak akar ke-i dengan 14 digit
        Er = abs(xi - x_old)  # perbarui galat

        # Cek apakah galat sudah di bawah epsilon
        if Er < eps:
            break
        # Jika belum, jadikan xi sebagai x_old
        # repeat iterasi
        x_old = xi

    print("======================")
    print(f"Hampiran akar x ≈ {xi:.14f}" + " pada iterasi ke-" + str(i))


# --- Interactive part ---
pers = input("Masukkan persamaan x (contoh, 'x - cos(x)'): ")
x0 = float(input("Masukkan nilai awal x0: "))
eps = float(input("Masukkan galat epsilon (contoh, 1e-6): "))

# Panggil Fungsi
newtonRaph(pers, x0, eps)
