# Metode Gauss-Seidel

# iterasi berhenti belum
x1 = 0 
x2 = 0 
x3 = 0
x4 = 0

err = [0,0,0,0]

def f1():
    return 1/10 * (x2 - 2 * x3 + 6)

def f2():
    return 1/11 * (x1 + x3 - 3 * x4 + 25)

def f3():
    return 1/10 * (-2* x1 + x2 + x4 - 11)

def f4():
    return 1/8 * (-3 * x2 + x3 + 15)

def e(xr, new_xr):
    return abs((new_xr - xr)/new_xr)

iterasi = 6

print(f"i = {0} | x1: {x1:.4f}, x2: {x2:.4f}, x3: {x3:.4f}, x4: {x4:.4f}")
for i in range (1,iterasi):
    xlama = [x1, x2, x3, x4]

    x1 = f1()
    x2 = f2()
    x3 = f3()
    x4 = f4()

    err[0] = e(xlama[0], x1)
    err[1] = e(xlama[1], x2)
    err[2] = e(xlama[2], x3)
    err[3] = e(xlama[3], x4)

    print(f"i = {i} | x1: {x1:.4f}, x2: {x2:.4f}, x3: {x3:.4f}, x4: {x4:.4f} | e1: {err[0]:.5f}, e2: {err[1]:.5f}, e3: {err[2]:.5f}, e4: {err[3]:.5f}")