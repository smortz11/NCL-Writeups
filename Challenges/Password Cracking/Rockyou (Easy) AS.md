# Password Cracking Walkthrough
This walkthrough demonstrates how to crack MD5-hashed passwords using **John the Ripper** and the popular **rockyou** wordlist The hashes we are working with are the same type that were used in the RockYou breach. We will also reference [hashID](https://github.com/psypanda/hashID.git) for identifying hash types.

All hashes were compiled into a single file called `temp_hashes.txt`. The workflow involves using John the Ripper to attempt cracking each hash against the wordlist.

---

## Setup
1. Download the rockyou wordlist: [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
2. Identify hash types (optional here, but probably required later) using hashID
```bash
python3 hashid.py temp_hashes.txt
```
3. Run John the Ripper with the rockyou wordlist:
```bash
john --wordlist=rockyou.txt --format=raw-md5 temp_hashes.txt
```
4. View cracked passwords in the original hash order:
```bash
john --show --format=raw-md5 temp_hashes.txt
```

---
# Q1 - 20 Points

#### 68a96446a5afb4ab69a2d15091771e39

#### Answer:
`emilybffl`

# Q2 - 20 Points

#### ec5f0b1826389df8622133014e88afde

#### Answer:
`ryjd1982`

# Q3 - 20 Points

#### 32e5f63b189b78dccf0b97ac41f0d228

#### Answer:
`joybird1`

# Q4 - 20 Points

#### 2233287f476ba63323e60addca1f6b64

#### Answer:
`kirkles`

# Q5 - 20 Points

#### 6539bbb84fe2de2628fc5e4f2a31f23a

#### Answer:
`ddmack`