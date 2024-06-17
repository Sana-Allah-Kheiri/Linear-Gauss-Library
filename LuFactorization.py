import numpy as np

def lu_decomposition(A):
    n, m = A.shape
    if n != m:
        raise ValueError("Matrix must be square for LU decomposition.")
    
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    for i in range(n):
        # Upper triangular matrix
        for k in range(i, n):
            U[i][k] = A[i][k] - sum(L[i][j] * U[j][k] for j in range(i))
        
        # Lower triangular matrix
        for k in range(i, n):
            if i == k:
                L[i][i] = 1
            else:
                L[k][i] = (A[k][i] - sum(L[k][j] * U[j][i] for j in range(i))) / U[i][i]
    
    return L, U

def main():
    # Step 1: Get the number of rows and columns
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))
    
    # Check if the matrix is square
    if n != m:
        print("Matrix must be square for LU decomposition.")
        return
    
    # Step 2: Initialize matrix A
    A = np.zeros((n, m))
    
    # Step 3: Get elements from user
    print("Enter the elements of the matrix:")
    for i in range(n):
        for j in range(m):
            A[i][j] = float(input(f"Element at position ({i+1}, {j+1}): "))
    
    # Step 4: Perform LU decomposition
    try:
        L, U = lu_decomposition(A)
        print("Lower triangular matrix L:")
        print(L)
        print("Upper triangular matrix U:")
        print(U)
    except Exception as e:
        print("Error:", e)

# Uncomment the following line to run the main function
main()
