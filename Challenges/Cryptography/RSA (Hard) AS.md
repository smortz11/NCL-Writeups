# Cracking Encryption Walkthrough
RSA is the gold standard of encryption. It uses very large prime numbers in order to generate keys and encrypt text. However, if we have some of the numbers (as those provided to us in the intro), we can reverse engineer it and decrypt our message. 

---
# Q1 - 15 Points
#### What is the value of p (the smaller prime)?

```bash
n = 1079
e = 43
c = 996 894 379 631 894 82 379 852 631 677 677 194 893
```

This is the hint given to us starting the room.

There are a few numbers we need to understand. Unfortunately, RSA is a tad math heavy. It is much easier to write a script to automate this for us. There is a script, `rsa_crack.py`, which is found in `/Scripts`. Download the script onto your system, navigate to its directory and run the following command:

```bash
python3 rsa_crack.py
```

The script will ask you for a few values and crack it!

![[RSA_CRACK.png]]
#### Answer:
`13`

# Q2 - 15 Points

#### What is the value of q (the larger prime)

This is shown in the above output.

#### Answer:
`83`

# Q3 - 25 Points

#### What is the plaintext of the encrypted message?

This is also shown above.

#### Answer:
`SKY-KRYG-5530`

---
# Conclusion

RSA cracking is difficult by hand. Then again, it is probably for the best that a used encryption algorithm is secure. The script I created should help enormously. Please do feel free to use it!