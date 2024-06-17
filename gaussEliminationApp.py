import numpy as np

def solve_system_of_equations():
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
    
    # Step 5: Solve the system of equations
    try:
        x = np.linalg.solve(A, b)
        print("Solution: ")
        for i in range(n):
            print(f"Variable {i+1}: {x[i]}")
    except np.linalg.LinAlgError as e:
        print("Error:", e)

# Uncomment the following line to run the function
solve_system_of_equations()