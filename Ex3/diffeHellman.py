def diffie_hellman():
    print("\n" + "="*60)
    print("   DIFFIE-HELLMAN KEY EXCHANGE   ")
    print("="*60)

    # 1. Inputs
    print("\n--- STEP 1: PUBLIC PARAMETERS ---")
    p = int(input("Enter a large prime number (p): "))
    g = int(input("Enter a primitive root / base (g): "))

    print(f"\n[Info] Publicly Shared Parameters:")
    print(f"       Prime (p) = {p}")
    print(f"       Base  (g) = {g}")

    # 2. Private Keys
    print("\n--- STEP 2: PRIVATE KEYS (Kept Secret) ---")
    a = int(input("Alice: Enter your private key (a): "))
    b = int(input("Bob: Enter your private key (b): "))

    print(f"\n[Info] Private Keys:")
    print(f"       Alice's Secret (a) = {a}")
    print(f"       Bob's Secret (b) = {b}")

    # 3. Public Values Calculation
    print("\n--- STEP 3: CALCULATING PUBLIC VALUES ---")

    # Alice's Public Value: A = g^a mod p
    A = pow(g, a, p)
    print(f"[Alice] Formula: A = g^a mod p")
    print(f"        A = {g}^{a} mod {p}")
    print(f"        Alice's Public Value (A) = {A}")

    # Bob's Public Value: B = g^b mod p
    B = pow(g, b, p)
    print(f"[Bob]   Formula: B = g^b mod p")
    print(f"        B = {g}^{b} mod {p}")
    print(f"        Bob's Public Value (B) = {B}")

    # 4. Exchange
    print("\n--- STEP 4: EXCHANGING VALUES ---")
    print(f"       Alice sends (A={A}) to Bob")
    print(f"       Bob sends (B={B}) to Alice")

    # 5. Shared Secret Calculation
    print("\n--- STEP 5: CALCULATING SHARED SECRET KEY ---")

    # Alice calculates: K = B^a mod p
    key_alice = pow(B, a, p)
    print(f"[Alice] Formula: K = B^a mod p")
    print(f"        K = {B}^{a} mod {p}")
    print(f"        Alice's Calculated Key = {key_alice}")

    # Bob calculates: K = A^b mod p
    key_bob = pow(A, b, p)
    print(f"[Bob]   Formula: K = A^b mod p")
    print(f"        K = {A}^{b} mod {p}")
    print(f"        Bob's Calculated Key = {key_bob}")

    # 6. Verification
    print("\n" + "="*60)
    print("                  FINAL VERIFICATION")
    print("="*60)
    print(f"Alice's Key: {key_alice}")
    print(f"Bob's Key:   {key_bob}")

    if key_alice == key_bob:
        print("\nSUCCESS: Both keys match! A secure channel can now be established.")
        print(f"Shared Secret Key is: {key_alice}")
    else:
        print("\nERROR: Keys do not match. Check your calculations or parameters.")
    print("="*60)

diffie_hellman()
