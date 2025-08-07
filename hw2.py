def MAX_2_ARRAY(a):
    b = []
    for i in a:
        maximum = i[0]
        for j in i:
            if maximum < j:
                maximum = j
        b.append(maximum)
    return b

a = [[1, 3, 7], [8, 9], [-1, -2]]
print(a)
print(MAX_2_ARRAY(a))
