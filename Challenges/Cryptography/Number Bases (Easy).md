# Password Decoding Walkthrough
This walkthrough demonstrates how to identify and decode different types of encoded passwords. We will examine each example, determine its encoding format, and decode it step by step using [CyberChef](https://cyberchef.org/)

---
# Q1 - 5 Points
#### 0x73636f7270696f6e

1. We notice the string starts with `0x`. In computing, a `0x` prefix **always indicates a hexadecimal (base 16) encoded string.
2. To decode:
	- Use CyberChef and apply the recipe `From Hex`.
	- Input the string with OR without the `0x` prefix.
#### Answer:
`scorpion`

# Q2 - 5 Points

#### c2NyaWJibGU=

1. We notice the string ends with `=`. This is a **common padding character in Base64 encoding**, although not all Base64 strings have it.
2. The presence of letters beyond `A-F` tells us this is **not hexadecimal**.
3. To decode:
	- Use CyberChef with the recipe `From Base64`.

#### Answer:
`scribble`

# Q3 - 5 Points

#### 01110011 01100101 01100011 01110101 01110010 01100101 01101100 01111001

1. This string only contains `0`s and `1`s, so we can immediately identify it as **binary encoding.
2. To decode:
	- Use CyberChef with the recipe `From Binary`.
#### Answer:
`securely`

# Q4 - 10 Points

#### 01100010 01000111 00111001 01110011 01100010 01000111 01101100 01110111 01100010 00110011 01000001 00111101

1. At first glance, this is **binary code**. Decoding it with CyberChef `From Binary` produces another encoded string:

```bash
bG9sbGlwb3A=
```

2. This new string ends with `=` and contains characters outside `0-9` and `A-F`, so we recognize it as **Base64.
3. Apply the `From Base64` recipe in CyberChef to decode the final password.

#### Answer:
`lollipop`

---

# Conclusion
This walkthrough shows how to:
- Identify encoding formats using simple visual cues: `0x` -> hex, `=` -> Base64, `0`/`1` -> binary
- Decode strings using CyberChef recipes
- Recognize layered encodings

Following these steps allows for systematic decoding of passwords or other encoded data.