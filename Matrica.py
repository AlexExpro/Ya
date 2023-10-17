def signum(a):
    kol = 0
    for i in range(len(a)): 
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                kol += 1
    return 1 - 2(kol % 2)

def monom(a):
    monom = 1
    global matr
    for i in range(len(a)):
        monom= matr[i][a[i]-1]
    return monom

def heapPermutation(a, size):
    if (size == 1):
        global det
        #print(a)
        #print(signum(a))
        #print(monom(a))
        det += signum(a)*monom(a)
        return
 
    for i in range(size):
        heapPermutation(a, size - 1)
        if (size % 2 == 1):
            a[0], a[size - 1] = a[size - 1], a[0];
            # a,b = b,a
        else:
            a[i], a[size - 1] = a[size - 1], a[i];

det = 0
matr = []
n = int(input())
for i in range(n):
    matr.append( [int(x) for x in input().split() ] )

a = [ 1, 2, 3, 4, 5, 6, 7 ]
heapPermutation(a, 7)
print(det)