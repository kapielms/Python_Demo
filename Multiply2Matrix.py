m1 = [
[1,2,3],
[4,5,6],
[7,8,9]
]
m2 = [
[1,2,3],
[4,5,6],
[7,8,9]
]
m3 = [
[0,0,0],
[0,0,0],
[0,0,0]
]

for i in range (len(m1)):
    for j in range(len(m2[0])):
        for k in range (len(m2)):
            m3[i][j] += m1[i][k] * m2[k][j]

for r in m3:
    print(r)