# Analyzing Random Server Walkthrough
All we are given is a "strange server" at `net-track.services.cityinte.cloud:8090`.

At first, I tried to `ssh` into it with no luck. Then, I tried `telnet`, which worked. I do not know why this is, but we roll with it. `telnet` is essentially a deprecated version of `ssh`. To get started, lets run the command:

```bash
telnet net-track.services.cityinthe.cloud 8090
```

---
# Q1 - 25 Points
#### What is the name and version of the software?

Now connected to the server, lets try to run `ls`. This gives us the output:

```bash
Use help to get a list of supported commands
```

`help` it is!

```bash
Here is a list of commands
version
list
get
help
```

The `version` command will probably answer this question.
#### Answer:
`RadicalShell v9`

---
# Q2 - 25 Points
#### What is the flag?

Our command arsenal is listed above. Let's do some recon and try the `list` command;

```bash
records
secret
notes
schedule
contacts
```

Hm. `secret` sounds interesting. Let's use the command:

```bash
get secret
```

This gives us a flag.
#### Answer:
`SKY-NCAT-3071`

---
# Q3 - 50 Points
#### What is the size of the largest file in bytes?

For each file that is output from `list`, lets use `get` with it and count which is larger. Note that on these systems, each character position is a byte.

```bash
get records
No records so far
get secret
SKY-NCAT-3071
get notes
TODO: take flag off server
get schedule
Completely free and busy when convenient
get contacts
Mom : REDACTED, Dad : REDACTED
```

Of these, schedule has the most characters. Let's count them (including spaces):

#### Answer:
`40`

---
# Conclusion

An... interesting room. Being honest, I don't know why the title is a play on the tool `netcat`. I also do not know why `ssh` didn't work. However, once we got inside, it was quite straightforward. Onto the next one!