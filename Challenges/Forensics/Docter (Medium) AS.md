# File Analysis Walkthrough
We are given a `.docx` file that we need to analyze. Let's get going!

---
# Q1 - 20 Points
#### What is the name of the hidden file containing the flag?

We've got some work to do. Let's start by just looking at the file. We can see four different images in the file, each one is from the Spooky Scary Skeletons video. Neat throwback.

Now, let's use binwalk to extract hidden files that may be contained from within the `.docx`:

```bash
binwalk -e SuperAwesomeDoc.docx
```

This will create a directory `_SuperAwesomeDoc.docx.extracted` that we can look around. There will be a lot of data. In the future, you will not always inherently know where to look (I didn't!), but we must analyze everything. For brevity, I skip straight to the solution. 

Inside of the directory, I grepped each file I could find for "SKY" to no avail. I then navigated into the `word` directory.

Again, I grepped each file for "SKY" to no avail. Then I navigated into `media`.

Inside `media`, we see five images. I ran binwalk on each of them to look at potentially hidden data. `image0.png` contains a `.zlib`. I then analyzed this for many minutes to no avail.

Wait... we see... five images? Not four?

Uh.

If we navigate to this folder in file explorer, we can see that one of the images is the flag. Neat. I was looking too deep.
#### Answer:
`image0.png`

---
# Q2 - 80 Points
#### What is the flag?

If you got the above, you got this too. Cheers!
#### Answer:
`SKY-RATL-8439`

---
# Conclusion

Hey, not bad! Forensics on images doesn't seem too bad when we have binwalk at our disposal. Sometimes, the answer isn't as complex as it may sound. Onto the hard challenge!