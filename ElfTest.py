def digamma(n, k):
    """
    Calculate the value of Digamma(n, k) based on the formula:
    Digamma(n, k) = 1 + 10^(k-1) + (10n * (10^(k-2) - 1)) / 9
    """
    if k == 1:
        return 1  # Special case when k = 1
    return 1 + 10**(k-1) + (10 * n * (10**(k-2) - 1)) // 9


def get_factors(num):
    """
    Return all factors of a given number as a list.
    """
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:  # Avoid adding the square root twice for perfect squares
                factors.append(num // i)
    return sorted(factors)


# Main program with continuous loop
if __name__ == "__main__":
    print("Welcome to the Digamma Function Calculator!")
    
    # Step 1: Get initial inputs from the user
    while True:
        try:
            n = int(input("Enter the sandwiched digit (n, between 1 and 9): "))
            if n < 0 or n > 9:
                print("The sandwiched digit must be between 0 and 9. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 9.")
    
    while True:
        try:
            k = int(input("Enter the initial number of digits (k, a positive integer): "))
            if k < 1:
                print("The number of digits must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    while True:
        try:
            k_final = int(input("Enter the final number of digits (k_final, a positive integer >= k): "))
            if k_final < k:
                print("The final number of digits must be greater than or equal to the initial number of digits. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    while True:
        try:
            step = int(input("Enter the step size for increasing k (a positive integer): "))
            if step < 1:
                print("The step size must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    # Step 2: Continuously calculate Digamma(n, k) with increasing k
    print("\nCalculating Digamma(n, k)...")
    while k <= k_final:
        # Compute Digamma(n, k)
        result = digamma(n, k)
        print(f"Digamma({n}, {k}) = {result}")
        
        # Check if the result is divisible by 11
        if result % 11 == 0:
            print(f"The number {result} is divisible by 11.")
        else:
            print("No")
        
        # Increment k by the step size
        k += step
    
    print(f"\nReached the final number of digits (k_final = {k_final}). Exiting the program. Goodbye!")