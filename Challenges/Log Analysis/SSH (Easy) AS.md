# SSH Log Analysis Walkthrough
In this challenge, we are given a terminal window with 274 content lines of ssh logs. We will scroll through the terminal to correlate solutions to the following questions. If preferred, we can download the file.

---
# Q1 - 10 Points
#### What is the hostname of the ssh server that was compromised?

Scrolling to the top of the log, we can see the following line:

`Oct 11 10:12:00 myraptor sshd[29459]: Server listening on 0.0.0.0 port 22.`

Here, we can come to the conclusion that the server is starting on port 22, which is for ssh. For that reason, we can understand that the hostname for the ssh server is `myraptor`.
#### Answer:
`myraptor`

# Q2 - 15 Points

#### What was the first IP address to attack the server?

Looking through the first few lines of the log, we can see the following:

```bash
Oct 11 10:12:24 myraptor sshd[29463]: Connection from 169.139.243.218 port 57273
Oct 11 10:12:25 myraptor sshd[29465]: Failed password for harvey from 169.139.243.218 port 57273 ssh2
Oct 11 10:12:25 myraptor sshd[29467]: Received disconnect from 169.139.243.218: Bye Bye
Oct 11 10:12:27 myraptor sshd[29469]: Connection from 169.139.243.218 port 57274
Oct 11 10:12:28 myraptor sshd[29471]: Failed password for harvey from 169.139.243.218 port 57274 ssh2
Oct 11 10:12:28 myraptor sshd[29473]: Failed password for harvey from 169.139.243.218 port 57274 ssh2
Oct 11 10:12:28 myraptor sshd[29475]: Received disconnect from 169.139.243.218: 11: Bye Bye
```

We can see failed passwords for the user `harvey` multiple times from the IP address `169.139.243.218`. We can interpret this as brute force attempts on the user.

#### Answer:
`169.139.243.218`

# Q3 - 15 Points

#### What was the second IP address to attack the server?

Below the previous attack, we can see the following line:

```bash
Oct 11 10:13:03 myraptor sshd[29477]: Connection from 56.13.188.38 port 55319
Oct 11 10:13:04 myraptor sshd[29479]: Failed password for harvey from 56.13.188.38 port 55319 ssh2
Oct 11 10:13:04 myraptor sshd[29481]: Received disconnect from 56.13.188.38: Bye Bye

```
#### Answer:
`56.13.188.38`

# Q4 - 15 Points

#### What was the third IP address to attack the server?

Again, starting where we left off, we can scan for anomalous behavior.

```bash
Oct 11 10:13:15 myraptor sshd[29483]: Connection from 30.167.206.91 port 55320
Oct 11 10:13:16 myraptor sshd[29485]: Failed password for harvey from 30.167.206.91 port 55320 ssh2
Oct 11 10:13:16 myraptor sshd[29487]: Received disconnect from 30.167.206.91: Bye Bye
Oct 11 10:13:18 myraptor sshd[29489]: Connection from 30.167.206.91 port 55321
Oct 11 10:13:18 myraptor sshd[29491]: Failed password for harvey from 30.167.206.91 port 55321 ssh2
Oct 11 10:13:18 myraptor sshd[29493]: Received disconnect from 30.167.206.91: Bye Bye

```

#### Answer:
`30.167.206.91`

# Q5 - 20 Points

#### Which user was targeted in the attack?

We can see this in the above logs.

#### Answer:
`harvey`

# Q6 - 25 Points

#### From which IP address was the attacker able to successfully log in?

We can either skim the log or use `grep` to aid in our seaches. I used the following command:

```bash
cat auth.log | grep -v "Failed" | grep "password"
```

This snippet concatenates (cat) the output of auth.log into a text format, passes it into the next function with `|`, calls `grep -v`, which returns all inputs that do NOT contain the word `Failed`, then passes it into normal `grep`, which returns any line that says `password`.

Output:
`Oct 11 10:36:59 myraptor sshd[30003]: Accepted password for harvey from 30.167.206.91 port 55326 ssh2
`
#### Answer:
`30.167.206.91`

---
# Conclusion

This challenge had us skimming a log output. Having fundamental Linux commands down is very important for this task, as well as moving forward. Knowing commands such as `cd`, `ls`, `pwd`, `cat`, `grep`, `head`, etc., will help very much.