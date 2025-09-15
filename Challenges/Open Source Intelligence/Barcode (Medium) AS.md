# Analyzing Barcodes Walkthrough
In this challenge, we are only given an image of a barcode. Thankfully, there exist tools that we can use in order to analyze and decode it!

We need to install `zbar-tools`, which can be done with the following command:

```bash
sudo apt install zbar-tools
```

---
# Q1 - 10 Points
#### What format does the barcode use?

We can use the above tool after downloading and navigating to our image:

```bash
zbarimg Barcode.gif
```

This command gives us the following output:

```bash
CODE-39:SKY-UZLU-5635
scanned 1 barcode symbols from 1 images in 0.03 seconds
```
#### Answer:
`CODE-39`

# Q2 - 15 Points

#### What is the flag hidden in the barcode?

This is shown in the above output.
#### Answer:
`SKY-UZLU-5635`

---
# Conclusion

This room is more gimmicky than hands-on. We can simply use the above tool to analyze barcodes. We can do the same with qr codes!