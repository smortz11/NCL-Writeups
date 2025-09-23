# Masking with a Custom Wordlist Walkthrough
In this challenge, we are told that it appears that these hashes are base off of Law and Order: SVU episodes and end in two digits. We will need to construct our own wordlist and use some of the masking techniques we learned back in the [[Mask (Medium) AS]] challenge. Let's get started!

---
# Q1 - 20 Points
#### 6475c851b56004eb96ab1404252c3a34

These are probably MD5 hashes (judging by the others used in NCL and the short length), but double checking will never hurt (using the hashID script!). It turns out to, indeed, be MD5.

Next, let's compile a list of the episodes. There exists a wordlist online that another person has compiled for this same NCL challenge, but in the individual game, that would be cheating, so I will be using [this](https://epguides.com/lawandordersvu/) site. We will copy it's contents into a file and use the `cut` command to separate the fields by the space character, and put that into a file.

```bash
cat SVU_dirty.txt | grep -v "Season" | cut -f4- | awk 'NF' > SVU_clean.txt
```

Going through this command, we first output the contents of this "dirty" file to the screen. We use `grep -v "Season"` to return all lines without that word. The following `cut` command returns the fourth field to us (the title), and `awk 'NF'` cleans the input. We can now take this good wordlist and write it to a new file.

Now, let's take our hashes and compile them into a file. Then we will run the following command with john:

```bash
john --format=raw-md5 --wordlist=SVU_clean.txt --mask='?w?d?d' SVU_hashes.txt
```

This cracks zero hashes. Any guess? We should add the argument `--rules`. This will try different capitalization patterns as well!

```bash
john --format=raw-md5 --wordlist=SVU_clean.txt --rules --mask='?w?d?d' SVU_hashes.txt
```

This line cracks all five hashes. We can view them with the following:

```bash
john --show --format=raw-md5 SVU_hashes.txt
```

#### Answer:
`hooked37`

---
# Q2 - 20 Points
#### abe6591e06aafc3cf1b0783b120f685e

#### Answer:
`manhunt74`

---
# Q3 - 20 Points
#### 1e1612db8bdeebc7e8d56f8f30b39456

#### Answer:
`philadelphia53`

---
# Q4 - 20 Points
#### 3dd9dd0e352df4433aadf2273e269287

#### Answer:
`resilience05`

---
# Q5 - 20 Points
#### 08038f679de74982bfb9bac43d46271a

#### Answer:
`unorthodox12`

---
# Conclusion

This was a fun challenge that combined the `--rules` and `--mask` options with John. We constructed our own wordlist using unsanitized online input. Onto the next challenge!