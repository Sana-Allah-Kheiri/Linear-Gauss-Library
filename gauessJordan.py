import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    # Form the augmented matrix
    M = np.hstack([A, b.reshape(-1, 1)])

    for i in range(n):
        # Make the diagonal contain all 1's
        diag_element = M[i][i]
        if diag_element == 0:
            for k in range(i + 1, n):
                if M[k][i] != 0:
                    M[[i, k]] = M[[k, i]]
                    diag_element = M[i][i]
                    break
        M[i] = M[i] / diag_element
        
        # Make the other elements in the current column 0
        for j in range(n):
            if i != j:
                M[j] = M[j] - M[j][i] * M[i]
    
    # Extract solution
    x = M[:, -1]
    return x

def main():
    # Step 1: Get the number of variables
    n = int(input("Enter the number of variables: "))
    
    # Step 2: Initialize matrix A and vector b
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    # Step 3: Get coefficients from user
    print("Enter the coefficients for each variable:")
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input(f"Coefficient for variable {j+1} in equation {i+1}: "))
    
    # Step 4: Get constants from user
    print("Enter the constants:")
    for i in range(n):
        b[i] = float(input(f"Constant in equation {i+1}: "))
    
    # Step 5: Solve the system using Gauss-Jordan elimination
    try:
        x = gauss_jordan(A, b)
        print("Solution: ")
        for i in range(n):
            print(f"Variable {i+1}: {x[i]}")
    except Exception as e:
        print("Error:", e)

# Uncomment the following line to run the main function
main()
