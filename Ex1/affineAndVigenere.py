# ================= Affine Cipher  =================
def modInverse(a):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return None

def affineEncrypt(t, a, b):
    res = ""
    print(f"\n--- Encryption Steps (a={a}, b={b}) ---")
    for c in t:
        p = ord(c) - 65
        cipher_idx = ((a * p) + b) % 26
        cipher_char = chr(cipher_idx + 65)
        print(f"Letter: {c} ({p}) -> (({a}*{p})+{b})%26 = {cipher_idx} -> {cipher_char}")
        res += cipher_char
    return res

def affineDecrypt(t, a, b):
    inv = modInverse(a)
    if inv is None: return "Invalid key"
    res = ""
    print(f"\n--- Decryption Steps (inv={inv}, b={b}) ---")
    for c in t:
        c_idx = ord(c) - 65
        plain_idx = (inv * (c_idx - b)) % 26
        plain_char = chr(plain_idx + 65)
        print(f"Cipher: {c} ({c_idx}) -> {inv}*({c_idx}-{b})%26 = {plain_idx} -> {plain_char}")
        res += plain_char
    return res

# ================= Vigenere Cipher =================
def vigEncrypt(t, k):
    r = ""
    print(f"\n--- Encryption Steps (Key={k}) ---")
    for j, c in enumerate(t):
        key_char = k[j % len(k)]
        # Formula logic: (P + K) % 26
        c_idx = (ord(c) + ord(key_char) - 130) % 26
        res_char = chr(c_idx + 65)
        print(f"Text: {c} + Key: {key_char} -> ({ord(c)-65} + {ord(key_char)-65})%26 = {c_idx} -> {res_char}")
        r += res_char
    return r

def vigDecrypt(t, k):
    r = ""
    print(f"\n--- Decryption Steps (Key={k}) ---")
    for j, c in enumerate(t):
        key_char = k[j % len(k)]
        # Formula logic: (C - K + 26) % 26
        p_idx = (ord(c) - ord(key_char) + 26) % 26
        res_char = chr(p_idx + 65)
        print(f"Cipher: {c} - Key: {key_char} -> ({ord(c)-65} - {ord(key_char)-65} + 26)%26 = {p_idx} -> {res_char}")
        r += res_char
    return r

# ================= Main Program =================
def main():
    print("--- Detailed Cipher Tool ---")
    choice = input("1. Affine / 2. Vigenere: ")

    if choice == '1':
        text = input("Message (UPPERCASE): ").upper().replace(" ", "")
        a = int(input("Key a: "))
        b = int(input("Key b: "))
        enc = affineEncrypt(text, a, b)
        print(f"\nFinal Encrypted: {enc}")
        dec = affineDecrypt(enc, a, b)
        print(f"Final Decrypted: {dec}")

    elif choice == '2':
        text = input("Message (UPPERCASE): ").upper().replace(" ", "")
        key = input("Key (UPPERCASE): ").upper()
        enc = vigEncrypt(text, key)
        print(f"\nFinal Encrypted: {enc}")
        dec = vigDecrypt(enc, key)
        print(f"Final Decrypted: {dec}")

if __name__ == "__main__":
    main()
