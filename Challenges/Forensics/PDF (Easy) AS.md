# PDF Forensics Walkthrough
In this challenge, we are given a .pdf and are asked several questions about it. We can use a pdf tool for forensics such as `exiftool`

---
# Q1 - 15 Points
#### What is the name of the program that exported this PDF file?

If we run the following command, we can search for information:

```bash
exiftool api.pdf
```
#### Answer:
`Adobe Photoshop CC 2019`

---
# Q2 - 15 Points
#### What PDF version is this file?

This can be seen in the above output.
#### Answer:
`1.7`

---
# Q3 - 20 Points
#### What software was used to redact the file and insert a watermark?

For this, we cannot find any information with `exiftool`. We can, however, use a pdf editor to remove the boxes around the watermark. I used LibreOffice Draw in order to move the boxes and see the solution.
#### Answer:
`PDFTRON`

---
# Q4 - 50 Points
#### What is the flag?

With the following command, we can search the file for hidden data containing a word in the flag:

```bash
exiftool api.pdf | grep -i "sky"
```

Here, `-i` specifies case insensitive. We can see the flag.
#### Answer:
`SKY-PDRD-2390`

---
# Conclusion

A short pdf analysis lab. We have used `exiftool` before. It is a nice tool for analyzing metadata in images. Onto the next challenge!