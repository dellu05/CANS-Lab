import random

# ================= Miller-Rabin =================
def modPow_steps(a, d, n):
    r = 1
    base = a % n
    print(f"      [Calculation: {a}^{d} mod {n}]")
    while d > 0:
        if d & 1: r = (r * base) % n
        base = (base * base) % n
        d >>= 1
    print(f"      Initial Result (x) = {r}")
    return r

def millerTest_steps(n, a):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    print(f"\n   Testing Witness a = {a}")
    print(f"   Step 1: n-1 ({n-1}) = {d} * 2^{s}")

    x = modPow_steps(a, d, n)
    if x == 1 or x == n - 1:
        print(f"   Step 2: x is {x} (1 or n-1). Pass!")
        return True

    temp_d = d
    step_count = 1
    while temp_d != n - 1:
        prev_x = x
        x = (x * x) % n
        temp_d *= 2
        print(f"      Square {step_count}: {prev_x}^2 mod {n} = {x}")
        if x == n - 1:
            print(f"      Found n-1 ({n-1})! Pass!")
            return True
        if x == 1:
            return False
        step_count += 1
    return False

def testPrime_steps(n):
    if n < 2: return "Composite"
    if n == 2 or n == 3: return "Probably Prime"

    for i in range(5):
        a = random.randint(2, n - 2)
        if not millerTest_steps(n, a):
            return "\nFinal Result: Composite"
    return "\nFinal Result: Probably Prime"

# ================= GCD =================
def calculateGCD(a, b):
    print(f"\n--- Euclidean Algorithm Steps ---")
    print(f"{'Step':<5} | {'Equation':<25} | {'Rem'}")
    print("-" * 42)
    step = 1
    while b:
        q, r = a // b, a % b
        print(f"{step:<5} | {a:^3} = ({q:^2} * {b:^3}) + {r:^3} | {r}")
        a, b = b, r
        step += 1
    print(f"GCD (Euclidean) = {a}")
    return a

def calculateNormalGCD(a, b):
    print(f"\n--- Normal GCD (Factor Method) ---")
    factors_a = [i for i in range(1, a + 1) if a % i == 0]
    print(f"Factors of {a}: {factors_a}")
    factors_b = [i for i in range(1, b + 1) if b % i == 0]
    print(f"Factors of {b}: {factors_b}")
    common = [i for i in factors_a if i in factors_b]
    print(f"Common Factors: {common}")
    g = max(common)
    print(f"Greatest Common Factor (GCD) = {g}")
    return g

def main():
    print("\n--- Math & Primality Tool ---")
    print("1. Miller-Rabin Primality Test")
    print("2. GCD Calculation (Both Methods)")
    choice = input("Option: ")

    if choice == '1':
        n_val = int(input("Enter number: "))
        print(testPrime_steps(n_val))
    elif choice == '2':
        num1 = int(input("Enter number A: "))
        num2 = int(input("Enter number B: "))
        calculateGCD(num1, num2)
        calculateNormalGCD(num1, num2)

if __name__ == "__main__":
    main()
