# ax + b = 0, дать a и b, найти чему равно x

a = float(input('Введите а: '))
b = float(input('Введите b: '))

if a == 0:
   if b == 0:
       print("Infinity more answers")
   else:
       print("No answer")
else:
    print(-b/a)

print("hello World")
