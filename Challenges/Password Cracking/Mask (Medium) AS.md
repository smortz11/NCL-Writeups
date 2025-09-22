# Cracking Somewhat-known Passwords Walkthrough
In this challenge, we are given several hashes that are in the format `SKY-HQNT-` followed by four digits. We can take this knowledge and craft a command that appends four digits to the end of this string, and hash it, comparing them.

We can first run the `hashID.py` script on the hashes to identify their hash type. Though the script gives a lot of potential options, it is most likely MD5, which is quite common with password cracking.

Let's go ahead and copy each of the hashes into a file to work with. They will be located in `/Attachments/Password Cracking/mask_hashes.txt`

---
# Q1 - 20 Points
#### 71b816fe0b7b763d889ecc227eab400a

Since all of the passwords are of the same format, we can crack them all similarly. We can do this with the `--mask` option in John. Let's dissect the following command:

```bash
john --format=raw-md5 --mask='SKY-HQNT-?d?d?d?d' mask_hashes.txt
```

- `john` - command for John the Ripper, a hash cracking tool.
- `--format=raw-md5` - specifies the format of the hashes. 
	- We can find the name of the hash format by using `john --list=formats`, then grepping, (Ex. `john --list=formats | grep md5)
- `--mask='SKY-HQNT-?d?d?d?d'` - specifies the format of the password. The ?d signifies a digit
- `mask_hashes.txt` - the file containing the hashes

John will then crack the passwords. We can view the cracked hashes with the following command:

```bash
john --show --format=raw-md5 mask_hashes.txt
```

This will give us the hashes in sequential order, answering all following questions.
#### Answer:
`SKY-HQNT-8765`

---
# Q2 - 20 Points
#### 674291170dffcf620bda2a604a6820ea

#### Answer:
`SKY-HQNT-7659`

---
# Q3 - 20 Points
#### 06f03267f31077d2c4b5c728472070ae

#### Answer:
`SKY-HQNT-6598`

---
# Q4 - 20 Points
#### d866f4b3b34b598375149fb7661113ab

#### Answer:
`SKY-HQNT-5981`

---
# Q5 - 20 Points
#### d9053951a8d1c15254b46ec9fc974a6b

#### Answer:
`SKY-HQNT-9816`

---
# Conclusion

Another password cracking room, but this time, we are given the format of the password. This is important because specific flags like the ones here are likely not contained within any wordlists (ie rockyou.txt).