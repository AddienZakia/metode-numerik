# Metode Bisection
def bisec(parameter):
    return pow(parameter,4) + 2 * pow(parameter, 2) - parameter - 3

i = 2

xl = int(input("xl: "))
xu = int(input("xu: "))

xr = (xl + xu)/2
es = 0.5
ea = 0

print(f"i : 1 - xl: {xl:.7f}, xu: {xu:.7f}, xr: {xr:.7f} | fxl: {bisec(xl):.7f}, fxu: {bisec(xu):.7f}, fxr: {bisec(xr):.7f} | e: {ea:.2f}\n")

while ea == 0 or abs(ea) >= es:

    fxl = bisec(xl)
    fxu = bisec(xu)

    if bisec(xl) * bisec(xr) < 0:
        xu = xr
    elif bisec(xl) * bisec(xr) > 0:
        xl = xr
    
    new_xr = (xl + xu)/2

    galat = (new_xr - xr)/new_xr * 100
    ea = galat

    xr = new_xr

    print(f"i : {i} - xl: {xl:.7f}, xu: {xu:.7f}, xr: {xr:.7f} | fxl: {fxl:.7f}, fxu: {fxu:.7f}, fxr: {bisec(xr):.7f} | e: {ea:.2f}\n")

    i += 1

