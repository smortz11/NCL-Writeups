# Rail Fence Cipher Walkthrough
Once again, we are given an encoded string. We are also given the following hint:

```bash
Our analysts have obtained encrypted messages. We saw hand-written notes that indicated the keys as being "3" and "5". See if you can crack them.
```

---
# Q1 - 15 Points
#### Cair eruSA-0org sgaeudrpesr K-II98.ue cn seYQ3

This string does not appear to follow any conventional, easy patterns we see in encodings. However, armed with our hint at the start, a number for each question, we can deduct that this may be a rail fence cipher (the room name also hints this).

We can use [CyberChef](https://cyberchef.org) with the `Rail Fence Cipher Decode` recipe. Along with this recipe, we can provide a key and an offset. When we use the kef `3`, as suggested in the intro, we get the following string:

```bash
Courage is grace under pressure SKY-AIQI-9380.
```
#### Answer:
`SKY-AIQI-9380

# Q2 - 15 Points

#### F daS-eefn n KZ3eheadty.YI8lta oiwy-Q0. r aI2

Same string type as above. Let's now try the key `5`:

```bash
Feel the fear and do it anyway. SKY-IQIZ-3802.
```

#### Answer:
`SKY-IQIZ-3802`

---
# Conclusion

Unfortunately, with encoded strings, some of the steps we take may feel arbitrary. However, there is a process you can follow to best equip yourself to find an answer. This flowchart will be detailed at the conclusion of the Cryptography rooms.