# Certificates Walkthrough
In this room, we need to be able to access the certificate of the website we are on (NCL's site, of course). This is different for other browsers, but for FireFox users, do the following:

Press the Lock Icon in the URL -> Connection Secure -> More Information -> View Certificate

---
# Q1 - 15 Points
#### Who is the issuer for Cyber Skyline's SSL certificate?

We can search for the field `Issuer`, where we can find the answer.
#### Answer:
`Sectigo Limited`

---
# Q2 - 15 Points
#### How many bits long is the SSL key?

On the same page, we can search for the field `key size`
#### Answer:
`2048`

---
# Q3 - 15 Points
#### How many certificates are in the certificate chain?

For this question, we need to download the link found in the same page, `PEM (chain`. Upon opening this file, we see three large entries
#### Answer:
`3`

---
# Conclusion

Another room testing our ability to find information. This room concludes the OSINT challenges!