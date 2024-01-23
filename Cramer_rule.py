import numpy as np

n = int(input('Enter number of unknowns: '))
A = np.zeros((n,n+1)) 

print('Enter Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        A[i][j] = float(input( 'A['+str(i)+']['+ str(j)+']='))
    
def det2x2(A): 
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def det3x3(A):
    print('compute 3 x 3 det of')
    print(A)
    a,b,c = A[0]
    c1 = a * det2x2(A[1:3,[1,2]])
    c2 = b * det2x2(A[1:3,[0,2]])
    c3 = c * det2x2(A[1:3,[0,1]])
    return c1 - c2 + c3
         
print('solve this given array:')
print(A, '\n')
D = det3x3(A[:,[0,1,2]])
print('D =', D, '\n')
Dx = det3x3(A[:,[3,1,2]])
print('Dx =', Dx, '\n')
Dy = det3x3(A[:,[0,3,2]])
print('Dy =', Dy, '\n')
Dz = det3x3(A[:,[0,1,3]])
print('Dz =', Dz, '\n')

print("solution")
print(f"x = {Dx*1.0/D:.2f}")
print(f"y = {Dy*1.0/D:.2f}")
print(f"z = {Dz*1.0/D:.2f}\n")

