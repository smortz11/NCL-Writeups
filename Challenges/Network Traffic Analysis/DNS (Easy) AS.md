# Analyzing PCAPs Walkthrough
In this room, we are given a .pcap file (short for packet capture). It is a file format that aggregates network traffic for viewing. The room itself offers a simplified view of analyzing the packet, but I will be using Wireshark, a popular GUI .pcap analysis tool.

Thankfully, this .pcap only contains 9 packets. There will be times when we are analyzing thousands of packets within one file!

---
# Q1 - 20 Points
#### What is the type of the DNS query requested?

Within Wireshark, we can see the following:

![[DNS.png]]

If we select one of our DNS packets (denoted by the DNS protocol in the protocol column), we can open up the menu on the bottom left. Here, we can see a file system of sorts regarding information about this packet. 

Since we need information about the type of DNS query, let's see if we can poke around and find it.

Domain Name System -> Queries

Here, we can see the following line:
`etas.com: type AXFR, class IN`
#### Answer:
`AXFR`

# Q2 - 20 Points
#### What domain was requested?

We can see this in the above answer.
#### Answer:
`etas.com`

# Q3 - 20 Points
#### How many items were in the response?

Remember how we had only two DNS packets? One if them is a query, and the other is a response. Here, we will be looking at the response.

Again, after opening the Domain Name System portion of this packet's data, we can see another "folder" named `Answers`.

![[DNS2.png]]
#### Answer:
`4`

# Q4 - 20 Points
#### What is the TTL for all of the DNS records? (note that this is the TTL for the DNS record, not the IP packet.)

This question requires us to dig around a little more. We already know which packet we are dealing with, so let's poke around through the "subfolders" found under `Domain Name System`.

Each answer that the DNS server sent actually has it's own TTL. We can view it by clicking on any of the folders found in the above question.
#### Answer:
`3600`

# Q5 - 20 Points
#### What is the IP address for the "welcome" subdomain?

In question three, we can already see a response containing a domain name with subdomain "welcome". Upon expanding this "folder", we can see the IP address that the DNS server responded.
#### Answer:
`1.1.1.1`

---
# Conclusion

I would highly recommend using your own tools for projects in the NCL playground. They are helpful tools to have at the ready. There are many .pcap tools available (tcpdump, tshark), but Wireshark is most definitely the best for beginners.