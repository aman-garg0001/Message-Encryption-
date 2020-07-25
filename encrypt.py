import numpy as np

def chartoint(c):
    if(c >= '0' and c <= '9'):
        return int(c) - int('0')
    elif(c == '.'):
        return 36
    elif(c == ' '):
        return 37
    elif(c >= 'a' and c <= 'z'):
        return ord(c) - ord('a') + 38
    else:
        return ord(c) - ord('A') + 10

def encode(s):
    return [chartoint(char) for char in s]

input = open('message.txt', 'r')
s = input.read()
s = encode(s)

dim = len(s) + 1
D1 = np.zeros((dim, dim), dtype = int)

for i in range(dim-1):
    D1[i, i+1] = D1[i+1, i] = s[i]

D2 = np.random.randint(0, 64, (dim, dim))

for i in range(dim-1):
    D2[i, i+1] = D2[i+1, i] = s[i]

B = np.dot(D1, D2)

A = np.ones((dim, dim), dtype = int)
for i in range(dim):
    for j in range(dim):
        if(i < j):
            A[i, j] = 0

BA = np.dot(B, A)

file_to_be_sent = open('encrypted.txt', 'w')

string = str(dim) + ' ' + str(dim) + ' '
for i in range(dim):
    for j in range(dim):
        string += str(BA[i, j]) + ' '


for i in range(dim):
    for j in range(dim):
        string += str(D2[i, j]) + ' '

file_to_be_sent.write(string)
file_to_be_sent.close()
