import numpy as np


VY = np.array([25.5, 31.2, 25.9, 38.4, 18.4, 26.7,
               26.4, 25.9, 32, 25.2, 39.7, 35.7, 26.5])
VX = np.array([
    [1.74, 6.32, 6.22, 10.52, 1.19, 1.22, 4.1, 6.32, 4.08, 4.15, 10.15,1.72, 1.7],
    [5.3, 5.42, 8.41, 4.63, 11.6, 5.85, 6.62, 8.72, 4.42, 7.6, 4.83, 3.12,5.3],
    [10.8, 9.4, 7.2, 8.5, 9.4, 9.9, 8, 9.1, 8.7, 9.2, 9.4, 7.6, 8.2]
  ]
)

n = len(VX[0])
VX = np.insert(VX, 0, np.ones(n), axis=0)
k = len(VX)


g = np.zeros(k)
A = np.zeros((k, k))


for i in range(0, k):
    for j in range(0, k):
        A[i, j] = sum(VX[i, :]*VX[j, :])
    g[i] = sum(VX[i, :]*VY)

b = np.dot(np.linalg.inv(A), g)


VX = np.delete(VX, 0, axis=0)

e2 = np.zeros(n)

# no borrar xD

aux = 0
bx= b[1:k]
b0 = b[0]

for i in range (0,n):
    for j in range (0, k-1):
        aux = aux - (bx[j]*VX[j,i])
    e2[i] = (VY[i]-b0 + aux)**2
    aux=0


for i in range (0,k):
    print("b%d = %f." %(i,b[i]))

print("\nSr = ",sum(e2))