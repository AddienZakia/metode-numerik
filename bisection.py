# Metode Bisection
def bisec(parameter):
    return pow(parameter,4) - 2 * pow(parameter, 2) + parameter - 2

i = 1

xl = int(input("xl: "))
xu = int(input("xu: "))
ia = int(input("iterasi: "))

xr = (xl + xu)/2
es = 0.5
ea = 0

while i != ia or abs(ea) >= es:

    fxl = bisec(xl)
    fxu = bisec(xu)
    print(f"i : {i} - xl: {xl}, xu: {xu}, xr: {xr} | fxl: {fxl}, fxu: {fxu}, fxr: {bisec(xr)} | e: {ea}\n")

    if bisec(xl) * bisec(xr) < 0:
        xu = xr
    elif bisec(xl) * bisec(xr) > 0:
        xl = xr
    
    new_xr = (xl + xu)/2

    galat = (new_xr - xr)/new_xr * 100
    ea = galat

    xr = new_xr

    i += 1

