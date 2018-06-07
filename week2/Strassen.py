import numpy as np
import sys, time

def main():
    if (len(sys.argv) != 2):
        print("usage: python %s N" % sys.argv[0])
        quit()

    n = int(sys.argv[1])
    a = np.zeros((n, n)) # Matrix A
    b = np.zeros((n, n)) # Matrix B

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i

    begin = time.time()
    #######################################
    c= strassen(a, b, n)
    #######################################
    end = time.time()
    print("time: %.6f sec" % (end - begin))

    # Print C for debugging. Comment out the print before measuring the execution time.
    total = 0
    for i in range(n):
        for j in range(n):
            # print c[i, j]
            total += c[i, j]
    # Print out the sum of all values in C.
    # This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
    print("sum: %.6f" % total)

def strassen(A, B, n):
    if n == 1 :
        return A*B
    elif n%2!= 0: #deal with odd numbers
        A= expandMatrix(A)
        B= expandMatrix(B)
        n+= 1
        C= strassen(A, B, n)
        return contractMatrix(C)

    newSize= int(n/2)
    a11, a12, a21, a22= splitMatrix(A, newSize)
    b11, b12, b21, b22= splitMatrix(B, newSize)

    p1= strassen( np.add(a11, a22), np.add(b11, b22), newSize)       #(a11+a22)(b11+b22)
    p2= strassen( np.add(a21, a22), b11, newSize)                    #(a21+a22)b11
    p3= strassen( a11, np.subtract(b12, b22), newSize)               #a11(b12-b22)
    p4= strassen( a22, np.subtract(b21, b11), newSize)               #a22(b21-b11)
    p5= strassen( np.add(a11, a12), b22, newSize)                    #(a11+a12)b22
    p6= strassen( np.subtract(a21, a11), np.add(b11, b12), newSize)  #(a21-a11)(b11+b12)
    p7= strassen( np.subtract(a12, a22), np.add(b21, b22), newSize)  #(a12-a22)(b21+b22)

    c11= p1+ p4- p5+ p7
    c12= p3+ p5
    c21= p2+ p4
    c22= p1+ p3- p2+ p6

    C= np.zeros((n,n))
    for i in range(newSize):
        for j in range(newSize):
            C[i,j]= c11[i,j]
            C[i,j+newSize]= c12[i,j]
            C[i+newSize, j]= c21[i,j]
            C[i+newSize, j+newSize]= c22[i,j]
    return C

def expandMatrix(matrix):
    size= len(matrix)
    newMatrix= np.zeros((size+1, size+1))
    for i in range(size):
        for j in range(size):
            newMatrix[i,j]= matrix[i,j]
    return newMatrix

def contractMatrix(matrix):
    size= len(matrix)
    newMatrix= np.zeros((size-1, size-1))
    for i in range(size-1):
        for j in range(size-1):
            newMatrix[i,j]= matrix[i,j]
    return newMatrix

def splitMatrix(matrix, size):
    return matrix[:size, :size], matrix[:size, size:], matrix[size:, :size], matrix[size:, size:]

if __name__== "__main__":
    main()