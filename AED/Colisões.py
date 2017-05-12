entrada = input()
list(entrada)
x = entrada.split(" ")
quad1 = []
quad2 = []
test1 = false
test2 = false
for i in range(len(x)):
    if (i<4):
        quad1.append(x[i])
    else:
        quad2.append(x[i])

if (quad1[0] >= quad2[0] and quad1[1] <= quad2[1]) or (quad1[0] <= quad2[0] and quad1[1] >= quad2[1]):
    test1 = True
if (quad1[2] >= quad2[2] and quad1[3] <= quad2[3]) or (quad1[2] <= quad2[2] and quad1[3] >= quad2[3]):
    test2 = True

if (test1 and test2):
    print(1)

