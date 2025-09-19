# Walkthrough
lorem ipsum

---
# Q1 - 5 Points
#### What is the IP address of the server?

We know that the initialization between the client and server starts with a 4-byte integer. Therefore, if we search for `tcp.len == 4`, we will get our first communication, which yields Q1, Q2, and Q3.
#### Answer:
`10.1.0.20`

---
# Q2 - 5 Points
#### What is the IP address of the client?

Found along with previous question.
#### Answer:
`10.1.0.217`

---
# Q3 - 10 Points
#### What port is the server listening on?

This is found in the same packet as Q1 and Q2.
#### Answer:
`60123`

---
# Q4 - 10 Points
#### What is the magic 2-byte ID in decimal representation?

This is a hard challenge. From here, this is what I did:

Remember that first message with a data length of four? Do this:

Right Click -> Follow -> TCP Stream

This will isolate all the traffic we need. I then constructed the following table:


| Packet # | Flow             | Size (bytes) | Data (if plausible) |
| -------- | ---------------- | ------------ | ------------------- |
| 5518     | Client -> Server | 4            | 00000005            |
| 5522     | Client -> Server | 2            | 0417                |
| 5528     | Server -> Client | 4            | 000000a0            |
| 5545     | Client -> Server | 416          |                     |
| 5547     | Server -> Client | 32           |                     |
| 5549     | Server -> Client | 128          |                     |

We see our 2-byte message in the table above. Let's use CyberChef to convert from hex to decimal.
#### Answer:
`1047`

---
# Q5 - 10 Points
#### How many encrypt requests were made by the client?

Shown in the above table, packet 5518. The data, when converted to decimal, is 5.
#### Answer:
`5`

---
# Q6 - 10 Points
#### What is the length of the first encrypt request (in bytes)?

We know there are 5 encrypt requests in packet 5545. Think: packet 5528 is from the server, telling use how large the final encrypt response is going to be. The hex converts to 160, which is `32 x 5`. Each encrypted response should be 32 bytes long.

Packets 5547 and 5549 sum to 160, which is the end of the exchange. So, logically, 5545 must be all of the encrypt requests. We know that each encrypt request is prefaced with a 2-byte check and a 4-byte len. Looking at the hex in this packet, we can separate it into all of its individual requests by delimiting by the first six bytes (12 hex chars), usually starting with a string of 0. These are pasted below and will probably be referenced again.

```hex
00000058546b4e4d4c555a4b513063744d54597a4d69424f51307774526b7044527930784e6a4d794945354454433147536b4e484c5445324d7a4967546b4e4d4c555a4b513063744d54597a4d69424f0a51307774526b70445279300417

00000048784e6a4d794945354454433147536b4e484c5445324d7a4967546b4e4d4c555a4b513063744d54597a4d69424f51307774526b7044527930784e6a4d79494535440a54433147536b0417

0000006b4e484c5445324d7a4967546b4e4d4c555a4b513063744d54597a4d69424f51307774526b7044527930784e6a4d794945354454433147536b4e484c5445324d7a4967546b4e4d0a4c555a4b513063744d54597a4d69424f51307774526b7044527930784e6a4d79494535440417

0000005754433147536b4e484c5445324d7a4967546b4e4d4c555a4b513063744d54597a4d69424f513077740a526b7044527930784e6a4d794945354454433147536b4e484c5445324d7a4967546b4e4d4c555a4b513063744d540417

00000022597a4d69424f51307774526b7044527930784e6a4d7949453544544331470a536b4e
```

Now, we can look at the top encrypt request. Remember our check sent in packet 5522? For some reason, it is at the end of these encrypt requests (the 0417 hex). It's not in the last one. Odd! (I thought I just didn't see the check in the first request, but i just don't see it! Correct me here if you see otherwise...)

The length is the first four bytes (8 characters) of each request. Let's decode it.
#### Answer:
`88`

---
# Q7 - 10 Points
#### What is the length of the second encrypt request (in bytes)?

Do the above, but for the second.
#### Answer:
`72`

---
# Q8 - 10 Points
#### How large is an individual encrypt hash (in bytes)?

We talked about this at the top of Q6
#### Answer:
`32`

---
# Q9 - 10 Points
#### What was the encrypt response, in hexadecimal representation, for the first request? (e.g. 123456789ABCDEF)

This is 32 bytes of data, which is in packet 5547.
#### Answer:
`b8c97b08e198fa9ff79a3a9c1f0109b18687b7a1a3ff1772c29b4dc86753d711`

---
# Q10 - 10 Points
#### What was the encrypt response, in hexadecimal representation, for the second request?

This answer is contained within packet 5549. Recall that each response is 32 bytes. Take those bytes!
#### Answer:
`8817153ae81d94b5d6c745e63d1df31d5d02bd3b030b820c3c038654fdca619c`

---
# Q11 - 10 Points
#### What is the hidden flag being sent over the protocol?

We have 5 encrypt requests and 5 encrypt responses. Let's take this data and try to find something. Remember to take off everything but the data bytes.

Doing so with the first request yields (From hex -> from base64):
`NCL-FJCG-1632`

Let's try the other requests. Flags should start with `SKY`

Request 4: `NCL-FJCG-1632`
#### Answer:
`NCL-FJCG-1632`

---
# Conclusion

They lied about the flag format. Very upsetting.

If you made it this far, congrats! This was a hard one!