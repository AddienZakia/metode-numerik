# Metode iterative fixed point
def f1(x):
    return pow(-2 * pow(x,3) + x + 3, 1/4)

def f2(x):
    return pow((-1 * pow(x, 4) + x + 3)/2, 1/3)

def f3(x):
    return pow(x,4) + 2 * pow(x,3) - x - 3

i = 100
new_x = 1.0
x = 1

while True:
    res = f3(new_x)

    print(f"i: {x} | x: {round(res.real,4)}")
    if (round(res.real,4) == round(new_x.real,4)):
        break
        
    x += 1
    new_x = res
