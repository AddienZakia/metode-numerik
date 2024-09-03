# Metode Newton - Raphson.
def f(x):
    return pow(x,4) - 2 * pow(x,2) + x - 2

def df(x):
    return 4 * pow(x,3) - 4 * x + 1

i = 1
ea = 1
x0 = int(input("x0: "))
galat_s = float(input("es: "))

print (f"i: 0 | x: {x0:.7f} | f(x): {f(x0):.7f}, f'(x): {df(x0):.7f} | e: 0")


while abs(ea) > galat_s:

    new_x = x0 - (f(x0)/df(x0))
    
    galat = (new_x - x0)/new_x * 100
    ea = galat

    x0 = new_x

    print (f"i: {i} | x: {x0:.7f} | f(x): {f(x0):.7f}, f'(x): {df(x0):.7f} | e: {ea:.7f}")
    i += 1