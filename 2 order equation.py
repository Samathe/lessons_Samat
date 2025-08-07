# ax**2 + bx + c = 0, a, b, c are numbers
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b ** 2 - 4 * a * c

if a != 0:
    if D > 0:
        print("two answers")
        print((-b + math.sqrt(D)) / (2 * a))
        print((-b - math.sqrt(D)) / (2 * a))
    elif D == 0:
        print("one answer")
        print(-b / (2 * a))
    else:
        print("No answer")
else:
    if b == 0:
        if c == 0:
            print("Infinity more answers")
        else:
            print("No answer")
    else:
        print("one answer")
        print(-c / b)
