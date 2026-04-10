import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def rsa():
    print("\n" + "="*50)
    print("   RSA ALGORITHM   ")
    print("="*50)

    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    e = int(input("Enter public exponent e: "))
    m = int(input("Enter message (as integer): "))

    print("\n--- STEP 1: KEY GENERATION ---")
    # 1. Calculate n
    n = p * q
    print(f"[Step] Calculate n = p * q")
    print(f"       {p} * {q} = {n}")

    # 2. Calculate Euler's Totient phi(n)
    phi = (p - 1) * (q - 1)
    print(f"[Step] Calculate phi(n) = (p-1)(q-1)")
    print(f"       ({p}-1) * ({q}-1) = {phi}")

    # 3. Verify e is valid
    if gcd(e, phi) != 1:
        print(f"!!! Error: e({e}) and phi({phi}) are not coprime. RSA cannot proceed.")
        return

    # Calculate Private Key d
    d = None
    for i in range(1, phi):
        if (e * i) % phi == 1:
            d = i
            break

    print(f"[Step] Find private key 'd' using (e * d) mod phi(n) = 1")
    print(f"       ({e} * {d}) mod {phi} = 1")
    print(f"       Computed d = {d}")

    print(f"\n>>> Public Key: (e={e}, n={n})")
    print(f">>> Private Key: (d={d}, n={n})")

    # --- STEP 2: ENCRYPTION ---
    print("\n--- STEP 2: ENCRYPTION (Alice sends to Bob) ---")
    # Formula: C = M^e mod n
    c = pow(m, e, n)
    print(f"[Step] Formula: C = M^e mod n")
    print(f"       C = {m}^{e} mod {n}")
    print(f"Resulting Ciphertext (C): {c}")

    # --- STEP 3: DECRYPTION ---
    print("\n--- STEP 3: DECRYPTION (Bob receives and decodes) ---")
    # Formula: M = C^d mod n
    decoded_m = pow(c, d, n)
    print(f"[Step] Formula: M = C^d mod n")
    print(f"       M = {c}^{d} mod {n}")
    print(f"Resulting Plaintext (M): {decoded_m}")

    # Final Summary
    print("\n" + "="*50)
    print(f"Original Message: {m}")
    print(f"Decrypted Message: {decoded_m}")
    if m == decoded_m:
        print("SUCCESS: Message recovered correctly!")
    print("="*50)


rsa()
