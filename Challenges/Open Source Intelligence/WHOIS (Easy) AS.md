# Utilizing whois Walkthrough
Whois is a Linux command that returns information on a domain name. It can serve as a cornerstone of reconnaissance and OSINT.

All of the below question pertain to the `cityinthe.cloud` domain.

---
# Q1 - 10 Points
#### Who is the registrar of this domain?

Run the following command:

```bash
whois cityinthe.cloud
```

Output (truncated):

```bash
Domain Name: cityinthe.cloud
Registry Domain ID: D15CD1AC4DEB54207A5048A69B9FC0558-ARI
Registrar WHOIS Server: whois.dynadot.com
Registrar URL: www.dynadot.com
Updated Date: 2025-02-16T22:19:22.070Z
Creation Date: 2016-02-16T18:23:14.904Z
Registry Expiry Date: 2027-02-16T18:23:14.904Z
Registrar: Dynadot, LLC
Registrar IANA ID: 472
Registrar Abuse Contact Email: info@dynadot.com
Registrar Abuse Contact Phone: +1.6502620100
Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
Name Server: ns-515.awsdns-00.net
Name Server: ns-399.awsdns-49.com
Name Server: ns-1390.awsdns-45.org
Name Server: ns-1749.awsdns-26.co.uk
DNSSEC: unsigned
URL of the ICANN RDDS Inaccuracy Complaint Form: https://icann.org/wicf

```

#### Answer:
`Dynadot, LLC`

# Q2 - 10 Points

#### On what day was this domain first registered?

Use the above output
#### Answer:
`2016-02-16T18:23:14.904Z`

# Q3 - 10 Points

#### What is this domain's registry domain ID?

Use the above output

#### Answer:
`D15CD1AC4DEB54207A5048A69B9FC0558-ARI`

# Q4 - 10 Points

#### What is the Top-Level Domain (TLD) of this domain?

The TLD is the furthest-right portion of a URL. Here, we have a domain of `cityinthe.cloud`. The TLD here is `cloud`.

#### Answer:
`cloud`

# Q5 - 10 Points

#### What organization manages the TLD used by cityinthe.cloud?

We can find a list of organizations that manage TLD's using the [Internet Assigned Numbers Authority (IANA)](https://www.iana.org/domains/root/db).  Here, we can locate `.cloud`, and  find this TLD's organization manager.

#### Answer:
`ARUBA PEC S.p.A.`

---
# Conclusion

Whois is a Linux tool that allows us to view several facts about a given domain, such as it's creation date, name servers, registrar, and potentially other information if set by the domain owner. It can serve a valuable role in OSINT and reconnaissance.