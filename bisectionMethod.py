from math import cos, sin

# Fungsi rumus Bisection
def bisection(pers, a, b, eps):
	# Terjemahkan input persamaan dari user ke dalam fungsi f(x)
	def f(x):
		return eval(pers, {"x":x, "cos": cos, "sin": sin})

	# Turunan menggunakan numerical approximation
	def df(x, h=1e-6):
		return (f(x+h) - f(x-h)) / (2*h)

	i = 0

    # Lakukan iterasi untuk xi
    while True:
	c = (a+b)/2 # hitung batas baru c
	i = i+1 # hitung iterasi
        if (f(a) * f(c) < 0):
           b = c
        else:
           a = c
        print("c" + str(i) + f" ≈ {c:.14f}") # cetak akar ke-i dengan 14 digit
        Er = abs(b-a)/2 # perbarui galat

        # Cek apakah galat sudah di bawah epsilon
        if Er < eps:
            break

    print("======================")
    print(f"Hampiran akar c ≈ {c:.14f}" + " pada iterasi ke-" + str(i))

# --- Interactive part ---
pers = input("Masukkan persamaan x (contoh, 'x - cos(x)'): ")
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
eps = float(input("Masukkan galat epsilon (contoh, 1e-6): "))

# Panggil Fungsi
bisection(pers, a, b, eps)
