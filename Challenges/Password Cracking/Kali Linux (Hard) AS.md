# Cracking Linux Walkthrough
In this challenge, we are given the `/etc/shadow` of a Kali machine, which contains this format:

```bash
username:password:lastchg:min:max:warn:inactive:expire:reserved
```

Upon inspection of the file, we can see that many of the services have a password of `*`, which means that we could not crack it with just this file. This is not the case for every service/user though! Let's get started.

---
# Q1 - 10 Points
#### What is the username of the only user account with a password?

We can either skim the file or we can use the CLI to use cut and search for the entry. I used the following commands:

```bash
cat kali_hash.txt | cut -d':' -f2 | grep -v "*" | grep -v "!"
```

And then, we can grep the file for this output, which gives us the user account.

Output:
```bash
hollie:$y$j9T$/WzixhAsn8sdXhCquYzh01$KZlio78LilItobsx/17ecFf1e2SbsduhP1sZEWuHrL4:18934:0:99999:7:::
```

#### Answer:
`hollie`

---
# Q2 - 10 Points
#### On what date was the user's password last changed?

From the intro, we know that this is the third field. This is UNIX time, which we can convert using the following command:

```bash
date -d "1970-01-01 +18934 days"
```

The 1970-01-01 is the UNIX epoch, and the field in the hash is the days since the epoch.
#### Answer:
`2021-11-03`

---
# Q3 - 10 Points
#### What is the salt used to secure the user's password?

Salt is an arbitrary text added to the end of a password before the hash to make it more difficult to brute force. Within the password hash, we can see multiple `$` signs. These actually delimit more fields in this format:

```bash
$id$salt$hash
```

NOTE: The salt can contain the `$` symbol. Therefore, the salt is everything between the second $ and the last $.
#### Answer:
`j9T$/WzixhAsn8sdXhCquYzh01`

---
# Q4 - 10 Points
#### What is the hash digest of the user's password?

This is just the last field from above.

NOTE: Don't include anything past the colon though, that is a different field!
#### Answer:
`KZlio78LilItobsx/17ecFf1e2SbsduhP1sZEWuHrL4`

---
# Q5 - 30 Points
#### What is the plaintext password of the user's password?

For this, you need a machine that natively supports yescrypt. That means Linux, which you should already have of course.

After we add the entire hash to the file (including username and such), we can run the following command:

```bash
john hash.txt --format=crypt
```

NOTE: we can, indeed, use rockyou, but this is faster since the hash takes longer to compute (and was given as a hint just in case).
#### Answer:
`hollie03`

---
# Conclusion

Up to Q5, this was a nice challenge! I hated it. I somehow repeatedly put the hash in wrong for Q5, causing me to spin up a brand new VM to prove I wasn't crazy (I was).