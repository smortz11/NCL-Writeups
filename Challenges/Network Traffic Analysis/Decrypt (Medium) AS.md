# The S in HTTPS Walkthrough
In this challenge, we are given a .pcap that has captured HTTPS traffic. This, over HTTP, is encrypted. In order to bypass this, we need to decrypt the traffic. Luckily, we are given a text file containing some secrets.

Go ahead and download both files. Open up the .pcapng in Wireshark. There should be 28 packets.

Now, we need to import our decryption keys. Follow this stream:

Edit -> Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename Browse -> Select file

---
# Q1 - 25 Points
#### What Cipher Suite was chosen by the secure socket server?

I had no idea what this was prior. I followed the stream from the start, ignoring our three-way TCP handshake. Then, I went packet by packet looking for mention of a `Cipher Suite` in the TLS portion of the packet. I found a list of cipher suites in packet 4.

I assumed that the server would choose one soon, and upon looking on frame 6, we can see the answer.
#### Answer:
`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`

---
# Q2 - 25 Points
#### What is the domain covered by the SSL key?

This is essentially asking for the website that was covered by this key. This is information that we can find in the `certificate` that is exchanged. Look through the packets for hints towards a certificate.

In the `Info` column, we can actually see the word mentioned in packet 6. If we open this up, we can look for the section labeled `Handshake Protocol: Certificate`

If we:

right click -> show packet bytes

We can see references to the domain.
#### Answer:
`tomsvacations.com`

---
# Q3 - 50 Points
#### What is the flag transferred over HTTPS?

With TLS now decrypted, we can easily see a request in the `Info` column for `flag.txt`. The next packet contains it's contents in plaintext (bottom-right)
#### Answer:
`SKY-LADN-1435`

---
# Conclusion

A more in-depth look at .pcap analysis. This time, we decrypted traffic and learned how to import our decryption keys.