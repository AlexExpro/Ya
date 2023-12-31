def signum(a):
    kol = 0
    for i in range(len(a)): 
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                kol += 1
    return 1 - 2*(kol % 2)

#Три действия Гаусса
def change_row(x, y, matr):
    for i in range(n):
        # поменять matr[x][i] и matr[y][i]
        temp = matr[x][i]
        matr[x][i] = matr[y][i]
        matr[y][i] = temp

def mult_row(i, y, matr):
    for j in range(len(matr[0])):
        matr[i][j] = matr[i][j] * y

def raznost(i, k, y, matr):
    for j in range(len(matr[0])):
        matr[i][j] = matr[i][j] - y * matr[k][j]

def raz_s_1_str(matr):
    for j in range(1, len(matr[0])):
        k = matr[j][0] / matr[0][0]
        raznost(j, 0, k, matr)

def monom(a):
    monom = 1
    global matr
    for i in range(len(a)):
        monom = matr[i][a[i]-1]
    return monom

def heapPermutation(a, size):
    if (size == 1):
        global det
        det = det + signum(a) * monom(a)
        return


    for i in range(size):
        heapPermutation(a, size - 1)
        if (size % 2 == 1):
            a[0], a[size - 1] = a[size - 1], a[0];
            # a,b = b,a
        else:
            a[i], a[size - 1] = a[size - 1], a[i];

def show(matr):
    for row in matr:
        print (row)

det = 0
matr = []

f = open("in.txt", "r");
n = int(f.readline())
for i in range(n):
    matr.append( [int(x) for x in f.readline().split() ] )
show(matr)
raz_s_1_str(matr)
print()
show(matr)

# a = [ 1, 2, 3 ]
# a = [i for i in range(1,n+1)]
# heapPermutation(a, n)
# print(det)

