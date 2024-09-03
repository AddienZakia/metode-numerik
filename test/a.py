# def f(x):
#     return x**4 - 2*x**2 + x - 2

# def bisection(xl, xu, n, tol):
#     if f(xl)*f(xu) >= 0:
#         print("f(xl) dan f(xu) bertanda sama")
#         return
#     for _ in range(n):
#         xr = (xl + xu) / 2
#         print(f"Xl = {xl:.5f}, Xu = {xu:.5f}, Xr = {xr:.5f}, f(Xl) = {f(xl):.5f}, f(Xu) = {f(xu):5f}, f(Xr) = {f(xr):.5f}")
#         if abs(f(xr)) < tol:
#             return xr
#         if f(xl)*f(xr) < 0:
#             xu = xr
#         elif f(xl)*f(xr) > 0:
#             xl = xr
#         elif f(xl)*f(xr) == 0:
#             return xr
#     print("tidak ketemu")
#     return

# bisection(1, 2, 100, 1e-5)

print(int.bit_length)