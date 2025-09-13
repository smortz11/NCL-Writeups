# ROT13 Walkthrough
This room presents us with another type of obfuscated information. We are asked to find the true meaning behind it.

---
# Q1 - 10 Points
#### iveghny ynxr

Based on knowledge of our previous rooms, let us do some thinking here:

Base64? No - Base64 does not contain space characters.
Binary? No - We have digits other than 0's and 1's
Hex? No - We have characters greater that 0-9 A-F.

This is a type of encoding that is known as a Caesar Cipher, in this particular case, a ROT13 cipher. ROT13 is a Caesar Cipher, but not all Caesar Ciphers are ROT13. Let me explain.

A Caesar Cipher maps letters of the alphabet to different letters by rotating them around. Lets say that we rotate letters three times. We can transform the string `abcd` to `defg`.

ROT13 is the most popular type of Caesar Cipher. Using [CyberChef](https://cyberchef.org/), we can use the ROT13 recipe to undo this encoded string.
#### Answer:
`virtual lake`

---
# Conclusion

In encoded strings, spaces are uncommon. For this reason, we should likely assume that it is a character mapping of sorts. It just so happens that ROT13 is the most common type of character mapping.

There are several ciphers that map each letter to a random one, not by shifting, or rotating, the alphabet a certain number of letters. In English, there are still ways to decode them by using frequency analysis, but that is out of the scope of this challenge.