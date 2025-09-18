# Telnet Analysis Walkthrough
You know the drill. We have a telnet .pcap file. Download it and open it in Wireshark! There should be 113 packets.

---
# Q1 - 10 Points
#### What is the username that was used to log in?

Let's get started. We can see our three-way TCP handshake at the beginning. Ignore this. 

Start scrolling through the packets with the `Telnet` data section open. We are looking for some sort of login query.

I found it in packet 15. If we continue scrolling, we can get the username key by key. Packets 17-27
#### Answer:
`test`

---
# Q2 - 10 Points
#### What is the password that was used to log in?

We can expect this to follow the username prompt. Let's continue scrolling.

Packtet 32, indeed. contains a password prompt. We can expect the user input to be letter by letter again.
#### Answer:
`capture`

---
# Q3 - 20 Points
#### What command was executed once the user was authenticated?

After signing in, we see a prompt of `$`, this is common on CLI's. Let's scroll to get the first command used.
#### Answer:
`uname`

---
# Q4 - 20 Points
#### In what year was this capture created?

Continuing our scroll, we can see a lot of data in packet 81. This contains the year!
It also contains the CPU architecture, the answer to Q6.
#### Answer:
`2011`

---
# Q5 - 20 Points
#### What is the hostname of the machine that was logged in to?

This is also shown in Q4
#### Answer:
`cm4116`

---
# Q6 - 20 Points
#### What CPU architecture does the remote machine use?

This is shown in packet 81, Q5.
#### Answer:
`armv4tl`

---
# Conclusion

A short conclusion if necessary