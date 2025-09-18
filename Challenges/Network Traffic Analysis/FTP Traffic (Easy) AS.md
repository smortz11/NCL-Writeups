# More Wireshark Walkthrough
Go ahead and download the specified .pcap file and open it up in Wireshark! There should be 97 packets in this .pcap.

---
# Q1 - 10 Points
#### What was the first username:password combination attempt made to log in to the server? (e.g. `user:password`)

Thankfully, we can easily see server responses in the `Info` column, further right of the main screen. Here, we can see a username and password submitted in packets 2 and 4, respectively.
#### Answer:
`user1:cyberskyline`

---
# Q2 - 10 Points
#### What software is the FTP server running? (Include name and version)

We can actually see this in the `Info` column of the first packet. Make sure to submit the entire thing!
#### Answer:
`FileZilla Server 0.9.53 beta`

---
# Q3 - 10 Points
#### What is the first username:password combination that allows for successful authentication? (e.g. `user:password`)

Since we can easily see the usernames and passwords used, as well as if the credentials are incorrect in the `Info` column, we can just skim until we see a username and password combination that does not fail. We can see is in packets 9 and 11.
#### Answer:
`user1:metropolis`

---
# Q4 - 10 Points
#### What is the first command the user executes on the ftp server?

Well, we know that, sequentially, this has to come after the previous login. Again, since the .pcap is small, let's just skim.

The info for packet 13 looks interesting, consisting of an array of numbers. If we click on this packet, we can see data under the FTP section of the packet. This gives aus a simple `Command: LIST`.
#### Answer:
`LIST`

---
# Q5 - 15 Points
#### What file is deleted from the ftp server?

In the previous question, you may have noticed that while we identified the command in packet 13, it is actually listed in the `Info` column in packet 15. Since we assume that the command can show up in this column, let's skim the `Info` column once again to find a command that might reference delete.

In packet 19, the `Info` column discloses our answer.
#### Answer:
`bank.cap`

---
# Q6 - 15 Points
#### What file is uploaded to the ftp server?

The next command we see after the delete command is one called `STOR`. This is likely referencing store, the act of saving/uploading a file? 

We can verify by looking at the following packets, where we can see the file being uploaded packet by packet.
#### Answer:
`compcodes.zip`

---
# Q7 - 15 Points
#### What is the filesize (in bytes) of the uploaded file?

There are two ways to solve this problem.

At first glance, it is easy to notice that the file transfer spans packets 25-44. We can either sum the value of bytes shown in the `Info` column, OR, we can look at the command from the user `STOR compcodes.zip` (packet 23) and look inside of the FTP portion of the packet. Here, we can see the pair `Command response bytes: 28183`
#### Answer:
`28183`

---
# Q8 - 15 Points
#### What file does the anonymous user download?

Follow the packet. We can eventually see a logon for the `anonymous` user. They attempt to download many files, but are told that they cannot be found. If we scroll until we see a block of FTP-DATA packets, we can look back and see what file is being downloaded (via `RETR` in packet 69)
#### Answer:
`compcodes.zip`

---
# Conclusion

We love to see .pcap's that we can read down. Fortunately, FTP logs by themselves are not bad at all! However, when we start adding encryption as well as multiple simultaneous conversations, things tend to become a tad more convoluted.