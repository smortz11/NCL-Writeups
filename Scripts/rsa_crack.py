from math import gcd

# Inputs
n = int(input("Enter the modulus (N): "))
e = int(input("Enter the public exponent (e): "))
c_blocks = input("Enter the ciphertext blocks, separated by spaces: ").split()

# Factor n
def factor_n(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i, n // i
    return None, None

p, q = factor_n(n)
if not p or not q:
    print("Failed to factor n. Try a more advanced factoring method.")
    exit()

print(f"Factors found: p={p}, q={q}")

# Compute phi
phi = (p-1)*(q-1)

# Modular inverse
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q*x0, x0
    return x1 + m0 if x1 < 0 else x1

d = modinv(e, phi)
print(f"Private key d={d}")

# Decrypt each block
plaintext = ""
for c_str in c_blocks:
    c = int(c_str)
    if c >= n:
        print(f"Warning: block {c} >= n. Skipping...")
        continue
    m = pow(c, d, n)
    # Convert number to character (assuming ASCII)
    plaintext += chr(m)

print(f"Decrypted message: {plaintext}")