import numpy as np

file = open('encrypted.txt', 'r')

string = file.read()
string = string.split()

dim = int(string[0])
D2 = np.zeros((dim, dim), dtype = int)
BA = np.zeros((dim, dim), dtype = int)

ptr = 2
for i in range(dim):
    for j in range(dim):
        BA[i, j] = int(string[ptr])
        ptr += 1

for i in range(dim):
    for j in range(dim):
        D2[i, j] = int(string[ptr])
        ptr += 1

A = np.ones((dim, dim), dtype = int)

for i in range(dim):
    for j in range(dim):
        if(i < j):
            A[i, j] = 0

D2_inv = np.linalg.inv(D2) #inverse of D2

A_inv = np.linalg.inv(A) #inverse of A

B = np.dot(BA, A_inv) #B = B*A*inverse(A) = D1*D2

D1 = np.dot(B, D2_inv) #D1 = D1*D2*inverse(D2)

def inttochar(x):
    if(x >= 0 and x <= 9):
        return str(x)
    elif(x >= 10 and x <= 35):
        return chr(int(x + ord('A') - 10))
    elif(x == 36):
        return '.'
    elif(x == 37):
        return ' '
    elif(x >= 38 and x <= 63):
        return chr(int(x + ord('a') - 38))

decoded_message = ''
for i in range(dim - 1):
    decoded_message += inttochar(round(D1[i, i + 1]))

print(decoded_message)
