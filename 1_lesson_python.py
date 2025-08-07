
n = 10
a = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        a[2] = [1,2,3,4,5,3,5,6,7,12]
        a[1][3] = 3
        #print(a[i][j], end = ' ')
    #print()

#list(map(print, a))
print(a[1])
print(a[1][3])
