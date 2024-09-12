# Metode regula falsi
def f(x):
    return pow(x,4) - 2 * pow(x,2) + x - 2

i = 2

xl = int(input("xl: "))
xu = int(input("xu: "))

xr = xu - ((f(xu) * (xl-xu))/(f(xl) - f(xu)))
es = 0.5
ea = 0

print(f"i : 1 - xl: {xl:.7f}, xu: {xu:.7f}, xr: {xr:.7f} | fxl: {f(xl):.7f}, fxu: {f(xu):.7f}, fxr: {f(xr):.7f} | e: {ea:.2f}\n")

while ea == 0 or abs(ea) >= es:

    fxl = f(xl)
    fxu = f(xu)

    if f(xl) * f(xr) < 0:
        xu = xr
    elif f(xl) * f(xr) > 0:
        xl = xr
    
    new_xr = xu - ((f(xu) * (xl-xu))/(f(xl) - f(xu)))

    galat = (new_xr - xr)/new_xr * 100
    ea = galat

    xr = new_xr

    print(f"i : {i:.7f} - xl: {xl:.7f}, xu: {xu:.7f}, xr: {xr:.7f} | fxl: {fxl:.7f}, fxu: {fxu:.7f}, fxr: {f(xr):.7f} | e: {ea:.2f}\n")

    i += 1

