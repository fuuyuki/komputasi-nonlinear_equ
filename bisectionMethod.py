from math import cos, sin


# Fungsi rumus Bisection
def bisectionMethod(pers, a, b, eps):
    # Terjemahkan input persamaan dari user ke dalam fungsi f(x)
    def f(x):
        return eval(pers, {"x": x, "cos": cos, "sin": sin})

    i = 0
    while True:
        i = i + 1  # hitung iterasi
        c = (a + b) / 2  # hitung titik tengah c
        print(
            "Iterasi " + str(i) + f": [{a:.14f}" + f", {b:.14f}" + f"], c ≈ {c:.14f}"
        )  # cetak iterasi

        if f(c) == 0:  # jika c adalah akar persamaan
            print("======================")
            print(f"Hampiran akar x ≈ {c:.14f}" + " pada iterasi ke-" + str(i))
            break

        elif f(a) * f(c) < 0:  # jika akar berada di interval [a, c]
            b = c  # perbarui b menjadi c
        else:  # jika akar berada di interval [c, b]
            a = c  # perbarui a menjadi c

        if abs(b - a) < eps:  # cek apakah interval sudah lebih kecil dari epsilon
            print("======================")
            print(f"Hampiran akar x ≈ {c:.14f}" + " pada iterasi ke-" + str(i))
            break


# --- Interactive part ---
pers = input("Masukkan persamaan x (contoh, 'x - cos(x)'): ")
a = float(input("Masukkan nilai a(x0): "))
b = float(input("Masukkan nilai b(x1): "))
eps = float(input("Masukkan galat epsilon (contoh, 1e-6): "))

bisectionMethod(pers, a, b, eps)
