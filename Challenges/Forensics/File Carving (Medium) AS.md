# Photo Analysis Walkthrough
In this challenge, we are given a file and need to analyze it. Initially, I am going to use `exiftool`, but we may need to pivot to more tools later in the analysis.

---
# Q1 - 10 Points
#### This file initially looks like something green, what's the file format of this green file?

Run the following command:

```bash
exiftool green_file
```

This will give us a large amount of information, and towards the top, we can see the file type.

#### Answer:
`png`

---
# Q2 - 25 Points
#### How many files can be extracted from the binary blob?

Unfortunately, `exiftool` cannot solve this for us. Instead, we will be using a tool named `binwalk`. We can execute at below:

```bash
binwalk -e green_file
```

The `-e` flag here tells us to create a folder to store some extracted data.

After running the command, we can see the following output:

```bash
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 63 x 36, 8-bit/color RGBA, non-interlaced
3243          0xCAB           gzip compressed data, from Unix, last modified: 2017-02-14 05:32:27
3605          0xE15           PNG image, 24 x 24, 8-bit/color RGBA, non-interlaced
3818          0xEEA           PNG image, 24 x 24, 8-bit/color RGBA, non-interlaced
4040          0xFC8           PNG image, 24 x 24, 8-bit/color RGBA, non-interlaced
4264          0x10A8          PNG image, 24 x 24, 8-bit/color RGBA, non-interlaced
```

This is five files and a gzip archive, for a total of six files.
#### Answer:
`6`

---
# Q3 - 50 Points
#### What is the hidden flag in the file?

Let's analyze the gzipped data. `cd` into the new directory and use the following command to see the contents of the file:

```bash
cat CAB
```

We can see the flag in the output.
#### Answer:
`SKY-RWCI-4291`

---
# Conclusion

This challenge introduced us to a new tool, `binwalk`. With it, we can extract files from binary files based off of the magic numbers (essentially file headers) that are contained from within it.