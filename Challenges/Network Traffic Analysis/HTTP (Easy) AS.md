# Analyzing HTTP Traffic Walkthrough
Yet another .pcap file, but this time, with emphasis on HTTP. HTTP is not encrypted and can be viewed in packet captures without any sort of decryption. Go ahead and download the file and load up Wireshark! The capture should be 40 packets.

---
# Q1 - 20 Points
#### What Linux tool was used to execute a file download?

Let's get started! For a tad of background (important for future networking courses), there are two types of ports, TCP and UDP. Without going into specifics, most traffic is over TCP if it is communication. UDP is lighter weight, but less secure in the sense that it does not know if the packet was delivered. 

Looking at the info in this .pcap, there are a few things to note. Packets 1-3 contain a sequence `SYN, SYN ACK, ACK`. This is a three-way handshake that occurs over TCP connections (HTTP is TCP 80). We can also see two numbers in the `Info` column, a random one, and 80. 80 is the server and the other number is the client. HTTP is offered by servers over port 80.

With this little background, we can skip the first three packets, as they contain no information about user interaction. We are drawn to packet 4, however, as the `Info` column contains the phrase `GET`. If we look in this packet, the User-Agent (kinda like the thing/person that invokes the request) is `Wget`. This is a Linux utility that is used to download files.
#### Answer:
`wget`

---
# Q2 - 20 Points
#### What is the name of the web server software that handled the request?

After skimming packets 5-35, it looked to be more of file transfer, nothing denoting what server we were dealing with. Packet 36 stuck out to me as it was different/the end to the data transfer. If we inspect this package, we can see the HTTP server that offered this file, denoted by `Server: nginx/0.8.53`
#### Answer:
`nginx/0.8.53`

---
# Q3 - 20 Points
#### What IP address initiated request?

From the small explanation in Q1, or intuition, it makes sense for the user to be the first person to initiate conversation with a server. (How weird would it be if users were constantly asked by servers if they wanted to download files?...). We can look at the first packet in the `Source` column.
#### Answer:
`192.168.1.140`

---
# Q4 - 20 Points
#### What is the IP address of the server?

This is just the destination of the previous question.
#### Answer:
`174.143.213.184`

---
# Q5 - 20 Points
#### What is the md5sum of the file downloaded?

In order to calculate the md5sum of a file, we need the file. How can we do that you may ask? Easy enough:

File -> Export Objects -> HTTP

From here, we can select the file to download. Once we download it and navigate to it's download directory, we can run the following command:

```bash
md5sum <filename>
```

Where `<filename>` is the name of the file you downloaded.
#### Answer:
`966007c476e0c200fba8b28b250a6379`

---
# Conclusion

Short, simple, and to the point. This room gave us more familiarity with Wireshark as well as introduced the way to extract objects that were communicated over the .pcap. Onto the next challenge!