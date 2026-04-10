# S-DES Tables
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IPI = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]
S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

def permute(bits, table):
    return [bits[i - 1] for i in table]

def shift(bits):
    return bits[1:] + [bits[0]]

def generate_keys(key_10bit):
    bits = permute(key_10bit, P10)
    L, R = bits[:5], bits[5:]
    L, R = shift(L), shift(R)
    k1 = permute(L + R, P8)
    L, R = shift(shift(L)), shift(shift(R))
    k2 = permute(L + R, P8)
    return k1, k2

def f_k(bits, key):
    L, R = bits[:4], bits[4:]
    ep = permute(R, EP)
    xor_res = [ep[i] ^ key[i] for i in range(8)]
    row0 = int(f"{xor_res[0]}{xor_res[3]}", 2)
    col0 = int(f"{xor_res[1]}{xor_res[2]}", 2)
    row1 = int(f"{xor_res[4]}{xor_res[7]}", 2)
    col1 = int(f"{xor_res[5]}{xor_res[6]}", 2)
    sbox_out = [int(x) for x in list(f"{S0[row0][col0]:02b}{S1[row1][col1]:02b}")]
    return [permute(sbox_out, P4)[i] ^ L[i] for i in range(4)] + R

def sdes_process(byte_val, key_10bit, decrypt=False):
    bits = [int(x) for x in f"{byte_val:08b}"]
    k1, k2 = generate_keys(key_10bit)
    bits = permute(bits, IP)
    bits = f_k(bits, k2 if decrypt else k1)
    bits = bits[4:] + bits[:4]
    bits = f_k(bits, k1 if decrypt else k2)
    return int("".join(map(str, permute(bits, IPI))), 2)

# Main Execution
choice = input("S-DES: Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
key_bin = [int(x) for x in input("Enter 10-bit binary key: ")]

if choice == 'E':
    msg_bin = int(input("Enter 8-bit binary message: "), 2)
    res = sdes_process(msg_bin, key_bin, False)
    print(f"Result (Ciphertext): {res:08b}")
elif choice == 'D':
    cipher_bin = int(input("Enter 8-bit binary ciphertext: "), 2)
    res = sdes_process(cipher_bin, key_bin, True)
    print(f"Result (Plaintext): {res:08b}")
