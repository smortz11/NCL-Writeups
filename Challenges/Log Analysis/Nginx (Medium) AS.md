# More CLI Analysis Walkthrough
In this challenge, we are given an Nginx access log. We will be using our CLI ninja skills. Let's get started!

---
# Q1 - 10 Points
#### How many different IP addresses reached the server?

I used the command:

```bash
cat access.log | cut -d' ' -f1 | sort | uniq | sort | nl
```

Instead of explaining per command, I will explain that we are parsing the log by ' ', and selecting the first field, the IP address. We then filter to get only unique ones and number them.
#### Answer:
`47`

---
# Q2 - 10 Points
#### How many requests yielded a 200 status?

I used the command:

```bash
cat access.log | grep " 200 " | nl
```
#### Answer:
`19`

---
# Q3 - 10 Points
#### How many requests yielded a 400 status?

Same command as before, but we change the number:

```bash
cat access.log | grep " 400 " | nl
```
#### Answer:
`38`

---
# Q4 - 10 Points
#### What IP address rang at the doorbell?

For this one, I wasn't quite sure what it was asking, but I used the following command:

```bash
cat access.log | grep -i "bell"
```

NOTE: the `-i` flag for grep means case-insensitive.
#### Answer:
`186.64.69.141`

---
# Q5 - 10 Points
#### What version of the Googlebot visited the website?

I used the command:

```bash
cat access.log | grep -i "bot"
```

We return lines that say `Googlebot/2.1`
#### Answer:
`2.1`

---
# Q6 - 10 Points
#### Which IP address attempted to exploit the shellshock vulnerability?

The shellshock vulnerability has a signature payload of sorts that looks like this: `() { :; }`. Yes, I had to google this, that's okay.

I grepped for the first part and found it:

```bash
cat access.log | grep "()"
```
#### Answer:
`61.161.130.241`

---
# Q7 - 10 Points
#### What was the most popular version of Firefox used for browsing the website?

For this, we have to use some RegEx (AHHHHHHHHHHH)

I used this command:

```bash
cat access.log | grep -o "Firefox/[0-9.]\+" | sort | uniq -c
```

This RegEx searches for the string Firefox, and only returns that along with the following version number (hence the -o flag for grep)
#### Answer:
`31.0`

---
# Q8 - 10 Points
#### What is the most common HTTP method used?

I used the following command.

```bash
cat access.log | cut -d'"' -f2 | cut -d' ' -f1 | sort | uniq -c | sort
```

We cut by the first `"` character. Then, we can cut by the space character to separate by the HTTP methods. We sort, uniq it, and find the answer.
#### Answer:
`GET`

---
# Q9 - 10 Points
#### What is the second most common HTTP method used?

We can see this in the same command, just the second highest number.
#### Answer:
`CONNECT`

---
# Q10 - 10 Points
#### How many requests were for \x04\x01\x00P\xC6\xCE\x0Eu0\x00?

I used the command:

```bash
cat access.log | grep -F "\x04\x01\x00P\xC6\xCE\x0Eu0\x00" | nl
```

The only notable thing here is the `-F` flag for grep. This means we search the plain string and do no regex. Otherwise, the `\` will cause issues.
#### Answer:
`6`

---
# Conclusion

This was another fun room to test our CLI ninja skills. Onto the next one!