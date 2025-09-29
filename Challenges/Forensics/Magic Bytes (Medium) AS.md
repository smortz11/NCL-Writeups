# File Headers Walkthrough
Magic bytes are the leading hex values of a file that identify the type of file that it is. These are documented online, on a site like [this](https://en.wikipedia.org/wiki/List_of_file_signatures). There are a few steps and tools we need to take to solve this problem. We are given a file of type `.jpeg` and need to restore it to it's *original* file type. The headers have been messed with. Let's use [CyberChef](https://cyberchef.org/) to analyze.

---
# Q1 - 25 Points
#### What is the original file type?

Download the file and navigate to its download location in a command line. Next, we can run the following command to view its hex contents:

```bash
xxd flag.jpeg | head
```

When running this, we can see the individual bytes (two hex characters) next to eachother as well as some translation to the right. In the right side, we can see some strings like IHDR. 

If we google IHDR, we can see references to PNG images. This is likely the original file type.
#### Answer:
`.png`

---
# Q2 - 75 Points
#### What is the flag?

We know that we have a file being identified as a `.jpeg` and it needs to be identified as a `.png`. Within CyberChef, let's import our file as input. Afterwards, we can use the recipe `To Hex` so that we can copy it and work with it. (I copied the output of `To Hex` and pasted it back in the top)

Now, if we go to the wiki and search for either `.jpeg` or the first few bytes of our file, we will see the following header for `.jpeg` files:

```bash
FF D8 FF E0 00 10 4A 46 49 46 00 01
```

Note our header in the hex dump in CyberChef:

```bash
ff d8 ff e0 00 10 4a 46 49 46 00 0d
```

All is the same here except for the last byte, which is a tad odd actually. I'm unsure if that matters.

Let's replace this hex with the first twelve bytes of a `.png` file. The wiki only has the first eight bytes, so we must use a temporary `.png` file to grab the bytes from. If we use the `xxd` command on a `.png`, we can grab them and concatenate them onto our hexdump in CyberChef. 

The `.png` hex should be:

```bash
89 50 4e 47 0d 0a 1a 0a 00 00 00 0d
```

If we then add the `From Hex` recipe to CyberChef, we can download our binary as a `.png` file. If we do this, we can now open the image, which contains the flag.
#### Answer:
`SKY-DSFG-5792`

---
# Conclusion

We got to work with some hex in magic numbers. Fun! Onto the next challenge!