### **Step 1: Look for obvious clues**

- Are there spaces? → Could be **Atbash**, **ROT13**, or **Caesar Cipher**
    
- Dots, dashes, and slashes? → **Morse Code**
    
- Starts with `0x` → **Hexadecimal**
    
- Ends with `=` → **Base64**
    
- Only `0`s and `1`s → **Binary**
    
- Numbers given for key → **Rail Fence Cipher**
    
- Key string provided → **Vigenere Cipher**
    
- Image given → **Steganography**
    
- Large primes/numbers given → **RSA Encryption**
    

---

### **Step 2: Choose the correct decoding method**

1. **Character Mapping Ciphers**
    
    - **Atbash** → Use `Atbash Decode`
        
    - **ROT13 / Caesar Cipher** → Use `ROT13` or `Caesar Decode` with appropriate shift
        
2. **Morse Code**
    
    - Convert using `From Morse Code`
        
3. **Rail Fence Cipher**
    
    - Use `Rail Fence Decode` with key number (and offset if given)
        
4. **Vigenere Cipher**
    
    - Use `Vigenere Decode` with provided key
        
5. **Password Encodings**
    
    - Hex (`0x...`) → `From Hex`
        
    - Base64 (`...=`) → `From Base64`
        
    - Binary → `From Binary`
        
    - Layered encoding → Decode step by step (e.g., binary → Base64 → plaintext)
        
6. **Steganography**
    
    - Use `strings -a <file>`
        
    - Optional: `grep` to search for known patterns (`SKY-`)
        
7. **RSA Encryption**
    
    - Use `rsa_crack.py` script
        
    - Provide n, e, c to get p, q, plaintext
        

---

### **Step 3: Tools**

- [CyberChef](https://cyberchef.org) → Most ciphers and encoding types
    
- [DCode](https://www.dcode.fr/cipher-identifier) → To identify unknown ciphers
    
- **Strings / Grep** → For images and steganography
    
- **Python Scripts** → For heavy cryptography like RSA