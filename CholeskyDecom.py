import numpy as np

def cholesky_decomposition(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i + 1):
            if i == j:  # Diagonal elements
                L[i][j] = np.sqrt(A[i][i] - np.sum(L[i][:j] ** 2))
            else:
                L[i][j] = (A[i][j] - np.sum(L[i][:j] * L[j][:j])) / L[j][j]
    return L

def main():
    # Step 1: Get the number of rows and columns
    n = int(input("Enter the number of rows and columns (matrix must be square): "))
    
    # Step 2: Initialize matrix A
    A = np.zeros((n, n))
    
    # Step 3: Get elements from user
    print("Enter the elements of the matrix:")
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input(f"Element at position ({i+1}, {j+1}): "))
    
    # Step 4: Perform Cholesky decomposition
    try:
        L = cholesky_decomposition(A)
        print("Lower triangular matrix L:")
        print(L)
        print("Transpose of lower triangular matrix L.T:")
        print(L.T)
    except np.linalg.LinAlgError as e:
        print("Error:", e)

# Uncomment the following line to run the main function
main()
