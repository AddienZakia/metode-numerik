# Method Secant

def f(x):
    return pow(x,4) + 2 * pow(x, 2) - x - 3

i = 2
xim1 = int(input("x0: ")) # x i - 1
x1 = int(input("x1: "))
xi = x1
ea = 0
es = 0.5

xip1 =  xi - ((f(xi) * (xim1 - xi))/(f(xim1) - f(xi))) # x i + 1

print(f"i = 1 | xi-1: {xim1:.7f}, xi: {xi:.7f}, xi+1: {xip1:.7f} | fxi-1: {f(xim1):.7f}, fxi: {f(xi):.7f}, fx+1: {f(xip1):.7f} | e: {ea:.2f}\n")

# ea == 0 or abs(ea) >= es or 
while ea == 0 or abs(ea) >= es:
    xim1 = xi
    xi = xip1

    new_xip1 = xi - ((f(xi) * (xim1 - xi))/(f(xim1) - f(xi))) # x i + 1

    galat = (new_xip1 - xip1)/new_xip1 * 100
    ea = galat

    xip1 = new_xip1

    print(f"x - {i} | xi-1: {xim1:.7f}, xi: {xi:.7f}, xi+1: {xip1:.7f} | fxi-1: {f(xim1):.7f}, fxi: {f(xi):.7f}, fx+1: {f(xip1):.7f} | e: {ea:.2f}\n")

    i += 1
