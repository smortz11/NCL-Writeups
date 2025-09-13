# atbash Walkthrough
This room gives us, yet another, encoded string. The string we are given contains spaces, and appears to be some sort of character mapping. Let's look at our options, and use [CyberChef](https://cyberchef.org).

---
# Q1 - 25 Points
#### hzuvob lyerlfh xzev

As mentioned above, this is likely some sort of character mapping. I initially attempted to use CyberChef to do a rotation cipher (a Caesar Cipher) by rotating each letter of the alphabet.

Honestly, the name of the room should have been a large enough clue. In CyberChef, I typed in the word `bash` in hopes of finding an encoding scheme to decode our string.

As it turns out, there exists an `atbash` cipher, which allows us to perfectly decode our string.
#### Answer:
`safely obvious cave`

---
# Conclusion

If you couldn't tell by now, CyberChef is going to be our best friend when working with encoded strings. It as an extremely versatile tool that will aid us greatly!