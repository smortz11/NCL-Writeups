# Navigating HTTP Headers Walkthrough
HTTP headers are present through any HTTP traffic. They exist between the start line of the packet and the actual packet data. They serve almost as information about the packet or sender to the server that will receive it. A list of all of the common HTTP headers can be found [here](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields).

Note: As an OSINT room, we are less likely to inherently know the information, but are expected to know how to find it. While these headers are common and do not hurt to be known, they can be found online through documentation.

---
# Q1 - 10 Points
#### What HTTP request header is used to denote what URI linked to the resource being requested?

"This is the address of the previous web page from which a link to the currently requested page was followed."
#### Answer:
`Referer`

# Q2 - 10 Points
#### What HTTP request header is used to identify the client software that made the HTTP request?

This is a common HTTP header that is especially helpful in log analysis. It can be used to determine malicious actors! Again, this section is less about inherently knowing answers, and rather, knowing how to find them (that is indeed OSINT).

"In [computing](https://en.wikipedia.org/wiki/Computing "Computing"), the **User-Agent header** is an [HTTP](https://en.wikipedia.org/wiki/HTTP "HTTP") header intended to identify the [user agent](https://en.wikipedia.org/wiki/User_agent "User agent") responsible for making a given HTTP request"
#### Answer:
`User-Agent`

# Q3 - 10 Points
#### What HTTP request header is used to identify the acceptable content types that can be returned?

"[Media type(s)](https://en.wikipedia.org/wiki/Media_type "Media type") that is/are acceptable for the response. See [Content negotiation](https://en.wikipedia.org/wiki/Content_negotiation "Content negotiation")."
#### Answer:
`Accept`

---
# Conclusion

A short conclusion if necessary