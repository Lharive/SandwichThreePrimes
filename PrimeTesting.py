def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False

    # Write n-1 as d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Miller-Rabin bases for n < 2^64 (deterministic)
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in bases:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def main():
    k = 3
    more = "Y"
    
    while more == "Y":
        # Calculate current number using integer arithmetic
        N = (4 * 10 ** (k-1) - 7) // 3
        
        # Check primality
        prime_status = is_prime(N)
        print("")
        print("")
        print(f"For k={k}, η(k) = {N}")
        print("")
        print(f"Prime: {prime_status}\n")
        print("")
        print("")
        
        # Get user input for continuation
        more = input("Check next k? (Y/N): ").strip().upper()
        
        # Increment k by 2 for next odd number
        if more == "Y":
            k += 2

if __name__ == "__main__":
    main()





