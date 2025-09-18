# Apparently We Need to Know Bytes Walkthrough
This challenge is not really packet analysis. I mean, it *is*, but the task is moreso converting bits to bytes and reading graphs. There are no .pcap's here. We have two charts. Buckle up and hope you paid attention in Computer Structures.


| Offset | 0        | 1        | 2        | 3        |
| ------ | -------- | -------- | -------- | -------- |
| 0      | 01000101 | 00000000 | 00000000 | 00111100 |
| 4      | 10101001 | 10011010 | 01000000 | 00000000 |
| 8      | 01000000 | 00000110 | 01001111 | 10010011 |
| 12     | 11000000 | 10101000 | 10000000 | 10000000 |
| 16     | 10011111 | 11001011 | 01100000 | 10011010 |

![[bigasstable.png]]

Note: a byte consists of eight bits. In the top table, these are bytes (not bits, aka, 8 characters). Since the large table is 0-31 *bits* wide, this is equal to two bytes.

---
# Q1 - 20 Points
#### What is the header checksum in hexadecimal representation?

In the larger table, the header checksum starts in the third row, third byte. Each row is four bytes (0-31 bits). 

The header checksum is also two bytes long. So bytes 10-11 are the ones we need (we start counting at 0).

This gives us the binary 01001111 10010011. Convert this to hex via a binary -> hex converter.
#### Answer:
`4F93`

---
# Q2 - 20 Points
#### What is the TTL of the packet?

Third row, first byte: 01000000. Convert to hex:
#### Answer:
`40`

---
# Q3 - 30 Points
#### What is the source IP address?

Fourth row, four bytes: 11000000 10101000 10000000 10000000. Convert each one to decimal to get our IP.
#### Answer:
`192.168.128.128`

---
# Q4 - 30 Points
#### What is the destination IP address?

Fifth row, four bytes: 10011111 11001011 01100000 10011010. Same as above.
#### Answer:
`159.203.96.154`

---
# Conclusion

A network traffic analysis challenge without the network traffic analysis! Hooray! Easy challenge.