# Strings and Steganography Walkthrough
Steganography is the practice of hiding information in other mediums of data, such as storing passwords in an image. In this room, we are given an image that is mentioned to hold a secret message. To find this message, we are going to use the `strings` tool.

---
# Q1 - 35 Points
#### What is the hidden flag in the image?

Once we navigate to the directory in which the picture is downloaded, we are in a position that allows us to use the `strings` tool. Example usage:

```bash
strings -a steg1.jpg
```

You may notice the `-a` flag. In this case, it is almost like outputting with verbosity, making sure that we do not skip any embedded strings.

The output of this command is very long. Moving forward, we can pursue two avenues to find our secret code:
1. Skimming - search through the strings manually for a potential password. This is a strong option if we do not know the password format.
2. grep - Since we know the password is likely a flag (Of the form SKY-...), we can use grep to search for this string. We can do this with the following command:

```bash
strings -a steg1.jpg | grep "SKY"
```

This will return a flag if it exists in the image.
#### Answer:
`SKY-TVJI-2063`

---
# Conclusion

A short conclusion if necessary