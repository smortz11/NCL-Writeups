# I Have Never Heard of Squid Walkthrough
In this room, we have proxy logs. I have never heard of Squid and I am fearful.

---
# Q1 - 10 Points
#### In what year was this log saved?

Within a squid log, the first value is the UNIX timestamp. We can copy this and decode it with the following command:

```bash
date -d @1286536309
```

Output:

```bash
Fri Oct  8 07:11:49 AM EDT 2010
```
#### Answer:
`2010`

---
# Q2 - 10 Points
#### How many milliseconds did the fastest request take?

In a squid log, the second value is the response time in ms. We can filter these then sort them:

```bash
cat squid_access.log | grep -oE "[0-9]{1,9} ([0-9]{1,3}\.){3}[0-9]{1,3}" | cut -d' ' -f1 | sort -n
```

This answer is... interesting. There is a variable amount of space between the first value and second value, so we cannot easily cut it.

Instead, I grep for a numerical value between one and nine digits in length followed by an IP address. This will give us output in the format `<ms> <ip>`. Then we can cut by the space character, select the first field, and sort it.
#### Answer:
`5`

---
# Q3 - 10 Points
#### The question in question

Same as the above command.
#### Answer:
`41762`

---
# Q4 - 10 Points
#### How many different IP addresses did the proxy service in this log?

This is the command I used:

```bash
cat squid_access.log | grep -oE " ([0-9]{1,3}\.){3}[0-9]{1,3}" | sort | uniq -c | nl
```

This command is worse than the others, so lets diagnose. This separates the IP address with regex. We use the `-oE` flag with grep to allow extended regex as well as matching only the text we input. There is a space at the beginning so we do not claim the server IP with it.

Finally, we sort and such to count only the unique IPs
#### Answer:
`4`

---
# Q5 - 15 Points
#### How many GET requests were made?

I used the command:

```bash
cat squid_access.log | grep "GET" | nl
```
#### Answer:
`35`

---
# Q6 - 15 Points
#### How many POST requests were made?

I used the command:

```bash
cat squid_access.log | grep "POST" | nl
```
#### Answer:
`78`

---
# Q7 - 10 Points
#### What company created the antivirus used on the host at 192.168.0.224?

Do a  command:

```bash
cat squid_access.log | grep "192.168.0.224"
```

Here, we can see references to a popular antivirus, Norton. This is not what it is asking for (I tried twice, RIP accuracy :(  ). It wants the creator.
#### Answer:
`Symantec`

---
# Q8 - 20 Points
#### The question in question

I simply grepped for `norton`

```bash
cat squid_access.log | grep -i "norton"
```

Here, we can find a URL that contains the word update. Neat!
#### Answer:
`http://liveupdate.symantecliveupdate.com/streaming/norton$202009$20streaming$20virus$20definitions_1.0_symalllanguages_livetri.zip`

---
# Conclusion

A short conclusion if necessary