# DNS Walkthrough
In this room, we are asked about different types of DNS records. If we were checking the DNS records of an actual site, we would use the `nslookup` tool, but since we are just looking at general record types, I used [this](https://en.wikipedia.org/wiki/List_of_DNS_record_types) site.

---
# Q1 - 10 Points
#### What type of DNS record holds the DNSSEC public signing key?

On the site, lets `Ctrl + F` for `DNSSEC`. We see several records, but remember, they must have something to do with cryptography/keys. We can find the following:

|   |   |   |   |   |
|---|---|---|---|---|
|[DNSKEY](https://en.wikipedia.org/wiki/DNSKEY "DNSKEY")|48|RFC 4034|DNS Key record|The key record used in [DNSSEC](https://en.wikipedia.org/wiki/DNSSEC "DNSSEC"). Uses the same format as the KEY record.|
#### Answer:
`DNSKEY`

---
# Q2 - 10 Points
#### What type of DNS record is used to map hostnames to IPv6 addresses?

|   |   |   |   |   |
|---|---|---|---|---|
|AAAA|28|RFC 3596[[2]](https://en.wikipedia.org/wiki/List_of_DNS_record_types#cite_note-2)|[IPv6](https://en.wikipedia.org/wiki/IPv6 "IPv6") address record|Returns a 128-bit [IPv6](https://en.wikipedia.org/wiki/IPv6 "IPv6") address, most commonly used to map [hostnames](https://en.wikipedia.org/wiki/Hostname "Hostname") to an IP address of the host.|
#### Answer:
`AAAA`

---
# Q3 - 10 Points
#### What type of DNS record is used to delegate a DNS zone?

|   |   |   |   |   |
|---|---|---|---|---|
|NS|2|[RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035#page-12)[[1]](https://en.wikipedia.org/wiki/List_of_DNS_record_types#cite_note-RFC1035_page-12-1)|Name server record|Delegates a [DNS zone](https://en.wikipedia.org/wiki/DNS_zone "DNS zone") to use the given [authoritative name servers](https://en.wikipedia.org/wiki/Authoritative_name_server "Authoritative name server")|
#### Answer:
`NS`

---
# Conclusion

Again, this room is more of an exercise on the ability to find and parse information. While some records are more obvious than others, there is not always a 100% way to locate an answer. We must think (sometimes).