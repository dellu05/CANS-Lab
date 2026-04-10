def playfair(t, k, enc):
    #change J to I
    k = k.upper().replace("J", "I")
    # Spaces remove ,change J to I
    t_clean = t.upper().replace("J", "I").replace(" ", "")

    # 5x5 Matrix (Key Square)
    s = ""
    m = []
    for c in (k + "ABCDEFGHIKLMNOPQRSTUVWXYZ"):
        if c not in s:
            s += c
            m.append(c)

    # Matrix display
    print("\n--- Playfair Matrix (5x5) ---")
    for i in range(0, 25, 5):
        print("  ".join(m[i:i+5]))

    # Text-a pairs-aa pirkkanum (Padding with 'X')
    pairs = []
    i = 0
    while i < len(t_clean):
        a = t_clean[i]
        if i + 1 < len(t_clean):
            if t_clean[i] == t_clean[i+1]:
                b = "X"
                i += 1
            else:
                b = t_clean[i+1]
                i += 2
        else:
            b = "X"
            i += 1
        pairs.append(a + b)

    r = ""
    d = 1 if enc else 4  # Encrypt: +1, Decrypt: +4 (Same as -1 mod 5)

    print(f"\n--- {'Encryption' if enc else 'Decryption'} Steps ---")
    for p in pairs:
        a, b = p[0], p[1]
        i1, i2 = m.index(a), m.index(b)
        r1, c1 = i1 // 5, i1 % 5
        r2, c2 = i2 // 5, i2 % 5

        if r1 == r2: # Same Row
            res = m[r1 * 5 + (c1 + d) % 5] + m[r2 * 5 + (c2 + d) % 5]
        elif c1 == c2: # Same Column
            res = m[((r1 + d) % 5) * 5 + c1] + m[((r2 + d) % 5) * 5 + c2]
        else: # different
            res = m[r1 * 5 + c2] + m[r2 * 5 + c1]

        print(f"Pair: {a}{b} -> {res}")
        r += res
    return r

def main():
    print("\n--- Playfair Cipher Tool ---")
    text = input("Enter Message: ")
    key = input("Enter Key: ")
    mode = input("Choose (1: Encrypt / 2: Decrypt): ")

    if mode == '1':
        result = playfair(text, key, True)
        print(f"\nFinal Encrypted Text: {result}")
    elif mode == '2':
        result = playfair(text, key, False)
        print(f"\nFinal Decrypted Text: {result}")
        final_msg = result.replace("X", "")
        print(f"Cleaned Message: {final_msg}")
    else:
        print("Invalid Choice!")

if __name__ == "__main__":
    main()
