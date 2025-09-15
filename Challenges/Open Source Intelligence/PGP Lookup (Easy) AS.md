# PGP Walkthrough
PGP is a method of encrypting communications. It stands for `Pretty Good Privacy`. The way this works includes a public and private key. Each individual must store their private key, while they must publish the public key.

Senders will encrypt messages with the public key, and that message can only be decrypted with the private key.

---
# Q1 - 15 Points
#### What is the key fingerprint for security@cpanel.net?

We can find information related to these keys with https://keyserver.ubuntu.com/. Here, we can type in `security@cpanel.net`. The key fingerprint is the top string that follows the `rsa4096/`
#### Answer:
`ded38747ceefc789fdc3a6154cf279c5c0424907

---
# Q2 - 15 Points
#### What email address is associated with the key fingerprint `7A39A56B73D1E097D57435CFCDE2DE1DCB2077F2`?

We can use the same site, but this time, search for the fingerprint shown above.

Searching for this key fingerprint gives us the email address that we need for this question.
#### Answer:
`hx@liber8tion.cityinthe.cloud`

---
# Q3 - 15 Points
#### On what date does the above key expire (in UTC)?

Since we already have the page for the key in-question pulled up, we can already see the expiration. We can also assume that the latest date shown is likely the expiration date.
#### Answer:
`2050-12-26T20:36:17Z`