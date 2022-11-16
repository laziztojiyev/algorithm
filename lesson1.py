# 1 - problem
# a = [i * i if not i % 2 else (1 if not i % 5 else i) for i in range(1, 102) if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0)]
# print(a)

# 2-problem
# t = (2, 3, 4, 5)
# a = [i * i if not i % 3 else i for i in t]
# print(tuple(a))

# 3-problem
# d = (2, 9, 4, 5, 8, 3, 3, 2, 2, 2)
# a = list(d)
# for i, x in enumerate(a):
#     if x == 2:
#         print(i, end=" ")

# 4-problem
# from math import sqrt
#
# x, y = map(int, input().split())
# surat = y ** (x - 5) + sqrt((x ** (y - 5) + (y + 5) ** x) ** (x - y))
# maxraj = (x + 1) ** (y - 7) + x * y
# print(f'{surat / maxraj : .2f}')


# 5-problem
# from math import exp
#
# x = int(input())
#
# S = exp(2) + exp(x) / 12 + 2 ** (x + 1) + x + 20
#
# print(f'{S: .2f}')


# 6-problem

# a, b = map(float, input().split())
# print(["<", ">", "="][1 if a > b else (0 if a < b else 2)])


# 7-problem

# a, b, c = map(int, input().split())
#
# print(f'{(a + b + c) / 3 * (a * b * c) ** (1 / 3) : .1f}')

# 8-problem

# x, n = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += (x + 1) ** (1 / i)
#
# print(f'{s: .2f}')

# 9-problem
# from math import pi
#
# r1, r2, r3 = map(int, input().split())
#
# print(f'{pi * r1 * r1: .2f} {pi * r2 * r2: .2f} {pi * r3 * r3: .2f}')


# 10-problem
# from math import factorial
#
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += x ** i * factorial(i + 1) / factorial(i)
# print(int(s))


# from math import log
#
# n, x, y = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += (2 * i - 1) * log(y, x) / (2 ** i)
# print(f'{s:.2f}')

# n, x = map(int, input().split())
#
# s = 0
# for i in range(1, n + 1):
#     s += i / x ** i
# print(f'{s:.2f}')


# from math import sqrt, sin
#
# x, a = map(float, input().split())
#
# y = x ** (4 / 3) + x * sin(x) * a
# print(f'{y:.2f}')

# a, b = map(int, input().split())
# print([a * b, a + b][0 if a < b else 1],[a * b, a + b][0 if a > b else 1])

# a, b, c = map(int, input().split())
# print([a + b + c, a * b * c][0 if a > 0 and b > 0 and c > 0 else 1])


# n, a, b = map(int, input().split())
#
# s = 0
#
# for x in range(1, n + 1):
#     s += (a * x + b) ** 2
# print(s)


# from math import cos
#
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += cos(i) / i
# print(f'{s:.2f}')


# n = int(input())
# print('double' if not n % 6 else 2 if not n & 1 else 3 if not n % 3 else 'none')


# a = int(input())
# l = list(map(int, input().split()))
#
# s = 0
# i = 0
#
# while i < len(l):
#     s += l[i]
#     i += 1
#
# print(s)


# s, h = map(int, input().split())
# a = s * 2 / h
# print(f'{a: .2f}')


# from math import pi
#
# r = int(input())
#
# c = 4 * pi * r ** 2
# print(f'{c:.2f}')

# n = int(input())
# print(bin(n).count('1'))


# a, b, c = map(int, input().split())
#
# print(f'{(a + b + c) / 2 :.2f} ')


# from math import pi
#
# h, a = map(int, input().split())
# v = 0
#
# v += (1 / 3 * pi * (a ** 2)) * h
#
# print(f'{v : .2f}')

# v, s = map(int, input().split())
# print(f'{s / v : .2f}')

# from math import sqrt
#
# h = int(input())
# g = 9.8
# t = sqrt(2 * h / g)
# print(f'{t:.2f}')


# n = input()
# l = list(map(int, input().split()))
# s = max(l)
#
# for i in l:
#     a = i / s + 0.000001
#     print(f'{a : .2f}', end='')


# n = input()
# l = list(map(int, input().split()))
# s = 0
#
# for i, v in enumerate(l, 1):
#     if i % 2 == 1:
#         s += v
# print(s)

# n = input()
# m = list(map(int, input().split()))
# s = []
# for i in m:
#     if i % 2 == 1:
#         s.append(i)
# print(f'{sum(s) / len(s) + 0.00001: .2f}')


# n = input()
# m = list(map(int, input().split()))
# x, y = map(int, input().split())
#
# c = 0
#
# for i in m:
#     if not x <= i <= y:
#         c += 1
# print(c)


# s = 31536000
# x = int(input())
# print(int(s * x / 1000))

# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += i
# print(s)


# m = int(input())
# print(f'{m * 9.8 : .2f}')

# m, a = map(int, input().split())
# print(m * a)


# u, r = map(int, input().split())
# print(f'{u / r : .3f}')


# r1, r2, r3 = map(int, input().split())
# r = r1 * r2 * r3 / (r2 * r3 + r1 * r2 + r1 * r3)
# print(f'{r : .2f}')


# from math import exp, fabs
#
# x, y = map(float, input().split())
# c1 = ((x + y) / (y ** 2 + fabs(y ** 2 + 2) / fabs(x + x ** 3 / 5))) + exp(y + 2)
# print(f'{c1 : .2f}')


# from math import tan, pi, cos, log
#
# x, y = map(float, input().split())
#
# f1 = (2 * tan(x + pi / 6) / ((1 / 3) + cos(y + x ** 2) ** 2)) + log(x ** 2 + 2, 2)
# print(f'{f1 : .2f}')

# from math import exp, atan, cos
#
# x, y = map(float, input().split())
#
# f2 = (1 / (x + 2 / x ** 2 + 3 / x ** 3) + exp(x ** 2 + 3 * x)) / (atan(x + y) + abs(5 + x) ** 2) - cos(
#     y ** 2 + x ** 2 / 2) ** 2
# print(f'{f2:.2f}')


# from math import log, sqrt, cos
#
# x, y = map(int, input().split())
#
# z = log(abs((x + y) ** 2 + sqrt(abs(y) + 2) - (x - (x * y / (x ** 2 / 2 - 5))))) + cos(x + y) ** 2 / (x + y) ** (1 / 3)
# print(f'{z : .2f}')


# from math import cos, sin
#
# x, y = map(float, input().split())
#
# T11 = (x * x + 1) / (x * x + (x * y + y * y) / (y * y + (y + x * y) / (abs(x * y) + 5))) + 1 / (1 + cos(x) + 1 / sin(x))
#
# print(f'{T11:.2f}')


# from math import log, sqrt, cos
#
# x, y = map(int, input().split())
#
# z = log((x + y) ** 2 + sqrt(abs(y) + 2) - (x - (x * y) / ((x * x) / 2 - 5))) + (cos(x + y) ** 2 / (x + y) ** (1 / 3))
# print(f'{z : .2f}')


# from math import sqrt
#
# a, b = map(float, input().split())
# t = pow(a, 1 / 5) + pow(b * (a + b) / (2 * b + a * b), 1 / 4) * (a ** 2 + b ** 2 + 2)
# print(f'{t:.2f}')


# from math import sin, sqrt, tan
#
# x1, x2, c, d = input().split()
#
# x1, x2, c, d = float(x1), float(x2), int(c), int(d)
#
# f = abs(sin(abs(c * x2 ** 3) + d * x1 ** 3 - c * d) ** 2 / sqrt(c * x1 ** 2 + d * x2 ** 2 + 7)) + tan(
#     x1 * x2 ** 2 + d ** 3)
# print(f'{f : .2f}')

#
# from math import cos
# a, b, c, d, x = map(float, input().split())
#
# y2 = (a * x ** 2) + (b * x) + c / (x * a ** 3) + (a ** 2) + a ** (b - c) + cos(
#     abs((a * x + b) / c * x + d + 2 ** c))
# print(f'{y2}:.2f')

# from math import sqrt, cos
#
# a, b, c, x = map(float,input().split())
# W1 = 0.75+(8.2*x**2+sqrt(abs(x**3+3*x)+cos(x-2)))/(a/4+b/3+c/2+1)
# print(f'{W1:.2f}')


# a, b, c = map(int, input().split())
# y = 0
# x = 1
# while x <= 20:
#     y += (a * x * x + b * x + c) / (a * a + b * b + x * x)
#     x += 5
# print(f'{y:.2f}')


# from math import sqrt, cos
#
# x, y, c, d = map(int, input().split())
# S = 0
# P = 1
# SP = 0
# for a in range(1, x + 1):
#     S += ((2 * a) + cos(a)) ** 2
#
# for a in range(1, y + 1):
#     P *= (a + 6) / sqrt(a ** 2 + 2)
#
# for k in range(1, c + 1):
#     D = 0
#     for y in range(1, d + 1):
#         D += ((k ** 2) + y) / sqrt(k ** 2 + y ** 2)
#     SP += D
#
# print(f'{S:.2f} {P:.2f} {SP:.2f}')

# from math import cos, sin
#
# x, y, a, b = map(int, input().split())
#
# S = 0
# for k in range(1, x + 1):
#     S += (k * k + sin(k) + 5) / ((k ** 7 + 1) ** (1 / 5))
#
# P = 1
# for n in range(1, y + 1):
#     P *= (n + (n ** (1 / 2))) / (n - (n + 1) ** (1 / 5))
#
# SP = 0
# for k in range(1, a + 1):
#     _SP = 1
#     for i in range(1, b + 1):
#         _SP *= ((i * i) + ((k * k) ** (1 / i))) / (((sin(i) + cos(k)) * (i ** k)))
#     SP += _SP
#
# print(f'{S:.2f} {P:.2f} {SP :.2f}')


# from math import sqrt, cos, e
#
# x, y, c, d = map(int, input().split())
# S = 0
# for i in range(1, x + 1):
#     S += (i ** 4 + i ** 2 + 3) / sqrt(i + e ** i)
# P = 0
# for k in range(1, y + 1):
#     P += (k + 1) / (k ** 3 + 5 * k)
# SP = 0
# for m in range(1, c + 1):
#     PS = 1
#     for n in range(1, d + 1):
#         PS *= sqrt(abs(m ** n - n ** m) / (m ** n + n ** m))
#     SP += PS
#
# print(f'{S:.2f} {P:.2f} {SP:.2f}')

# from math import cos, log
#
# x, y, c, d = map(int, input().split())
# S = 0
# for a in range(1, x + 1):
#     S += (4 * a + 6 * log(a)) / (a ** 2 + a)
# P = 1
# for a in range(1, y + 1):
#     P *= abs(a - 6 * cos(a)) / (a ** 2 + a ** (log(a)))
# SP = 0
# for k in range(1, c + 1):
#     PS = 1
#     for a in range(1, d + 1):
#         PS *= (a * k + x) / (k ** 2 + y ** 2)
#     SP += PS
#
# print(f'{S:.2f} {P:.2f} {SP:.2f}')


# s = input().split()
# i, j = map(int, input().split())
# s[i - 1], s[j - 1] = s[j - 1], s[i - 1]
# print(' '.join(s))


# input()
# a = list(map(int, input().split()))
# mi = min(a)
# ma = max(a)
#
# print(sum([1 for i in a if mi < i < ma]))


# input()
# l = list(map(int, input().split()))
# s = i = 0
#
# while i < len(l):
#     s += l[i]
#     i += 1
#
# print(s)

# n = int(input())
# print(bin(n).count('1'))

# from math import e, sqrt
#
# x, y, c, d = map(int, input().split())
#
# S =  0
# for k in range(1, x + 1):
#     S += (k ** 3 + e ** k)
#
# P = 1
# for a in range(3, y + 1):
#     P *=  (a * x) / sqrt((a * a) +( x * x))
#
# SP = 0
# for i in range(1, c + 1 ):
#     ps = 1
#     for j in range(1, d + 1):
#         ps *= (i * x + j * j) / sqrt(i * i  + j * y)
#     SP += ps
#
# print(f'{S:.2f}', f'{abs(P):.2f}', f'{SP:.2f}')
#


# from math import e,sin,sqrt, log
#
# a, x,y=input().split()
#
# a,x,y = int(a), float(x),float(y)
#
# w2 = sqrt(e**(x*y)-x*sin(a*x)-(x**2+2)/(abs(x)+5)) + sqrt(log(x*x+2)+5)
#
# print(f'{w2:.2f}')

# from math import cos
#
# a, b, c, d, x = input().split()
# x = float(x)
# a, b, c, d = map(int, [a, b, c, d])
#
# if a == 0:
#     y2 = cos((a * x + b) / (c * x + d + 2 ** c))
# else:
#     y2 = (a * x ** 2 + b * x + c) / (x * a ** 3 + a ** 2 + pow(a, b - c)) + cos((a * x + b) / (c * x + d + 2 ** c))
#
# print(f'{y2:.2f}')

# x, y, z = input().split()
# x, y, z = float(x), float(y), float(z)
#
#
# maximal = max(x + y + z, x, y, z)
# minimal = min(x + y / 2, x, y, z) ** 2
#
# print(f'{maximal:.2f} {minimal:.2f}')

# x, y, z = input().split()
# x, y, z = float(x), float(y), float(z)
#
# if x > y > z or x > z > y:
#     print(x, z)
# if y > z > x or y > x > z:
#     print(y, x)
# if z > x > y or z > y > x:
#     print(z, y)


# a, b = map(float, input().split())
#
# u = min(a, b)
# v = min(a * b, max(a, b))
# s = min(u + v, 3.14)
#
# print(f'{u : .2f} {v : .2f} {s : .2f}')


# from math import sqrt, tan, cos, sin
#
# x = float(input())
# AA = sqrt((tan(x + 2) * 2 - cos(x + 2 ** x)) / (1 + cos(x + 2) ** 2)) + (sin(x ** 2)) / (x ** 2 + 3)
# print(f'{AA:.2f}')


# from math import sin, log10, cos
#
# a, x = map(float, input().split())
# BB1 = x * sin(x / 2 + x / 3 + x / 4) + (log10(x ** 2 - 2) + 3 ** a) / (cos(x + 3) * sin(x + 3) + 8)
# print(f'{BB1:.2f}')


# a, b = map(int, input().split())
#
# if a > b:
#     print(a)
# else:
#     print(a, b)

# a, b = map(int, input().split())
# if a <= b:
#     a = 0
#     print(a, b)
# else:
#     print(a, b)


# a, b, c = map(float, input().split())
#
# if a <= 3 and a >= 1:
#     print(a)
# if b <= 3 and b >= 1:
#     print(b)
# if c <= 3 and c >= 1:
#     print(c)


# a, b, c = map(int, input().split())
#
# if a > 0:
#     a *= a
# if b > 0:
#     b *= b
# if c > 0:
#     c *= c
# print(a, b, c)

# from math import sin
#
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += sin(i) / (2 ** i)
# print(f'{s : .2f}')


# from math import factorial
#
# n = int(input())
# s = 0
#
# for i in range(1, n + 1):
#     s += ((-1) ** (i - 1)) * (1 / factorial(2 * i - 1))
# print(f'{s : .4f}')


# a, b = map(float, input().split())
# print(f'{max(a, b): .100f}')


# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += ((-1) ** (i - 1)) * (1 / (x ** (2 * i)))
# print(f'{s : .3f}')


# n, x = map(int, input().split())
#
# s = 0
#
# for i in range(1, n + 1):
#     s += i / x ** (2 * i)
# print(f'{s : .3f}')


# from math import sin
#
# n, x = map(int, input().split())
#
# s = 0
#
# for i in range(1, n + 1):
#     s += (-1) ** (i - 1) * (1 / i) * sin(i * x)
# print(f'{s : .3f}')


# from math import sqrt
#
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += x ** i / sqrt(i)
# print(f'{s:.3f}')

# from math import factorial
#
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += x ** i / factorial(i)
# print(f'{s : .3f}')


# from math import factorial
#
# n, x = map(int, input().split())
# s = 0
#
# for i in range(1, x + 1):
#     s += (-1) ** (i - 1) * x ** (2 * i - 1) / factorial(2 * i - 1)
#
# print(f'{s:.3f}')


# from math import factorial
#
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += (-1) ** (i - 1) * x ** (2 * i - 2) / factorial(2 * i - 2)
# print(f'{s : .3f}')


# from math import factorial
#
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += x ** (2 * i - 2) / factorial(2 * i - 2)
# print(f'{s : .3f}')


# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += x ** (2 * i - 1) / (2 * i - 1)
#
# print(f'{s : .3f}')


# s = input()
# c = 0
# for i, w in enumerate(s.split()):
#     if w[0].isupper():
#         c += 1
# print(c)


# from math import factorial
#
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += x ** (2 * i - 1) / factorial(2 * i - 1)
# print(f'{s : .3f}')


# from math import cos, sin
#
# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)
# y = 0
# for x in range(a, c + 1, 3):
#     y += pow(((a * x + b) / (b ** 2 + cos(x) ** 2)), 1 / 3) - (sin(x ** 2) / (a * b))
# print(f'{y:.2f}')


# a, b, c = map(int, input().split())
# y = 0
# for x in range(a, b + 1, 2):
#     y += (a ** b + b ** x + c ** a) / ((2 * x ** 2) + (3 * a ** x))
# print(f'{y:.2f}')


# from math import pi, cos
#
# a = int(input())
# y = 0
# h = pi / 19
# x = -pi / 2
# while x <= pi:
#     y += (a ** a) ** (1 / 3) + x * x * cos(a * x)
#     x += h
#
# print(f'{y:.2f}')


# from math import cos, sin
#
# a = int(input())
# x, y, h = 0, 0, 0.5
# while 0 <= x <= 10:
#     y += a * cos(x) - sin(x * x)
#     x += h
# print(f'{y:.2f}')


# from math import pi, sin, exp, atan, log
#
# a, b, c = map(int, input().split())
# x = -pi
# s = 0
# while x <= pi:
#     s += (log(a ** (2 * sin(x))) + exp(2 * x)) / (atan(x) + b) + c
#     x += pi / 10
# print(f'{s:.2f}')


# from math import cos, sin
#
# a, b = map(float, input().split())
# s, h = 0, 2
# for x in range(1, 13, h):
#     s += (a ** 2) + ((b + sin(x)) / ((a ** 3) + cos(x ** 3) ** 2)) ** (1 / 5)
# print(f'{s:.2f}')


# a, b, c = map(float, input().split())
#
# s = 0
# h = 3
# for x in range(1, 11, h):
#     s += ((a * (x ** 2)) / b) + (x / c)
#
# print(f'{s:.2f}')


# a, b, c = map(int, input().split())
# s, h = 0, 0.5
# x = 5
# while 5 <= x <= 10:
#     s += ((a * a) + (b * x) + (x ** c)) / ((a * a) + (b * b) + (x * x))
#     x += h
# print(f'{s:.2f}')


# from math import sin, cos
#
# a, b, c = map(int, input().split())
# y, h = 0, 0.25
# x = -1
# while x <= 1:
#     y += ((sin(a * x) + b ** c) / (b ** 2 + cos(x) ** 2)) ** (1 / 3) - sin(x ** 2) / (a * b)
#     x += h
# print(f'{y:.2f}')


# from math import cos, sin
#
# a, b, c = map(int, input().split())
# s, h = 0, 0.25
# x = c
# while c <= x <= b:
#     s += ((a * a) * cos(x)) + (sin(x) / 2) + (b * x ** 2)
#     x += h
# print(f'{s:.2f}')


# from math import cos, sin, pi
#
# a = int(input())
# s = 0
# x = -pi / 2
# while x <= pi:
#     s += 2 * ((a ** sin(2 * x)) ** (1 / 3)) + (x * x * cos(a * x))
#     x += pi / 10
# print(f'{s:.2f}')


# from math import sin, cos, pi
#
# a, b, c, d = map(int, input().split())
# y, h = 0, 1.5
# x = d
# while d <= x <= c:
#     y += ((a * x + b) / (b * b + cos(x) ** 2)) ** (1 / 5) - (sin(x * x) / (a * b))
#     x += h
# print(f'{y:.2f}')

# from math import sin, cos, pi, sqrt
#
# a, b, c = map(int, input().split())
# y, h = 0, 0.25
# x = 0
# while 0 <= x <= 1:
#     y += sqrt((sin(a * x) + (b ** c)) / (b * b + cos(x) ** 2)) - (sin(x * x) / (a * b))
#     x += h
# print(f'{y:.2f}')


# from math import pi, sin, exp, atan, log
#
# a, b, c = map(int, input().split())
# h = -pi
# s = 0
# while h <= pi:
#     s += (log(a ** (2 * sin(h))) + exp(2 * h)) / (atan(h) + b) + c
#     h += pi / 10
# print(f'{s:.2f}')


# from math import log
#
# a, b, c, d = map(int, input().split())
#
# S = 0
# for m in range(1, a + 1):
#     S += (3 * m ** 3 + 4 * m + 5) / (m ** 3 + log(m))
#
# P = 1
# for k in range(1, b + 1):
#     P *= k / (k ** 3 + 7 * k + 5)
#
# SP = 0
# for i in range(1, c + 1):
#     _SP = 1
#     for m in range(1, d + 1):
#         _SP *= (log(i) + m ** i) / m ** i
#     SP += _SP
#
# print(f'{S:.2f} {P:.2f} {SP :.2f}')

# from math import sqrt, cos, e, log, sin
#
# x, y, c, d = map(int, input().split())
# S = 0
# for n in range(1, x + 1):
#     S += 1 / (5 - 17 * n + n ** 3)
# P = 1
# for m in range(1, y + 1):
#     P *= sqrt(abs(m - 5) + 1) / (m ** 2 + 4 * m - 1)
# SP = 0
# for i in range(1, c + 1):
#     PS = 1
#     for k in range(1, d + 1):
#         PS *= ((-1) ** i) * pow((abs(sin(k) + e ** k)), 1 / 7) / (2 * abs(
#             4 * i ** 3 - k ** 4))
#     SP += PS
#
# print(f'{S:.2f} {P:.2f} {SP:.2f}')


# n = int(input())
# a = list(map(int, input().split()))
# k, l = map(int, input().split())
#
# s = 0
# c = 0
# for i, v in enumerate(a, 1):
#     if k <= i <= l:
#         s += v
#         c += 1
#
# print(f'{s / c:.1f}')


# l = list(map(int, input().split()))
# k = min(l)
# last = l[-1]
#
# for index, value in enumerate(l):
#     if value == k:
#         l[index], l[-1] = last, k
# print(*l)


# from math import factorial
#
# n, k = map(int, input().split())
# s = 0
# for i in range(0, n + 1):
#     s += ((-1) ** i * k ** i) / factorial(i)
# print(f'{s:.3f}')
