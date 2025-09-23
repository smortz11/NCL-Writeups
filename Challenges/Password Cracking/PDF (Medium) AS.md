# Cracking Protected PDF's Walkthrough
PDFs that are "protected" via password can also be cracked! There are a slew of addons with John (funnily named Jumbo John) that allows us to extract hashes from a PDF. We will use this addon along with John to get access to the PDF!

---
# Q1 - 25 Points
#### What is the password used to encrypt the pdf?

When working with PDFs, we have a small order of operations:
1. Extract the hash from the .pdf
2. Crack the hash!

We can extract the hash from the .pdf using `pdf2john`:

```bash
pdf2john encrypted.pdf > pdf_hash.txt
```

Here, we create a text file containing the hash to use with john. We can start cracking with john using the following:

```bash
john --format=pdf --forks=6 --wordlist=rockyou.txt pdf_hash.txt
```

Here, we tell John the format, our wordlist (usually default to rockyou), a hash, and a new argument. The `--forks` argument allows us to allot more CPU computational power to the process. 

NOTE: This hash took ~20 minutes to crack on my laptop. In the real world, we would be using a desktop with a GPU along with hashcat. However, since most people will be on laptops, John is about our best option.

After about twenty minutes, we can see John spit out the password:
#### Answer:
`keanereeves2008'

---
# Q2 - 25 Points
#### What is the flag in the PDF?

Simple open the .pdf with the password we found in the last step!
#### Answer:
`SKY-KANU-5902'

---
# Conclusion

This was a short introduction to some of the functionality offered by Jumbo John. I will advise that if you run into any of these challenges, that you install the tools necessary so that you have them during the games!