# Password Manipulation Walkthrough
We are, once again, given five different hashes. Running hashID, we can likely assume them to be md5 once again (these are common).  I visited [this](https://pokemondb.net/tools/text-list) link to generate a list of all the pokemon names (also located in `/Attachments/Password Cracking/pokemon_wordlists.txt`)

---
# Q1 - 20 Points
#### a532443f3e04a9e00295a8cd2a75e080

I began with the following command:

```bash
john --format=raw-md5 --wordlist=pokemon_wordlists.txt pokemon_hashes.txt
```

This returned nothing. The hashes are not *just* pokemon names. There is some, what we call, salt added to the passwords. There is a default option with John that adds common password variants to each attempt that can be called via `--rules`

This is the new command:

```bash
john --format=raw-md5 --rules --wordlist=pokemon_wordlists.txt pokemon_hashes.txt
```

As it turns out, our first command didn't work because the wordlist was titlecase and the passwords were lowercase. Still an important tool to know! We can view the cracked hashes with the command:

```bash
john --show --format=md5-sum pokemon_hashes.txt
```

We have all passwords for the next four questions as well.
#### Answer:
`golduck`

---
# Q2 - 20 Points
#### 54c10b9736b70e75c6e505f340b6e2f1

#### Answer:
`basculin`

---
# Q3 - 20 Points
#### b8a24794813a47521b4be55747e0665a

#### Answer:
`rotom`

---
# Q4 - 20 Points
#### 83b020b0a7b3c353e1c11b1647b53cda

#### Answer:
`celebi`

---
# Q5 - 20 Points
#### 999cae1e22fe69d89d6f56e3050f18cb

#### Answer:
`goldeen`

---
# Conclusion

This challenge introduced us to the `--rules` option in John. This is a super strong tool and will be helpful for many challenges (probably).