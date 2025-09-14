# Identifying a Vigenere Cipher Walkthrough
In this room, we are given an encoded string (who could've guessed) and a string key that was found along with the ciphertext. The name of the room, `French`, also give a hint to the cipher we will be using.

Vigenere is a French word that takes a string key to encode/decode. This can be completed using [CyberChef](https://cyberchef.org).

---
# Q1 - 25 Points
#### Y ln xkv lubj swlzqvkht, A vmzb pjk bbua we ddgs ILQ-GQYU-8026

In the intro to the room, we are also given the string `qizkwcgqbs`. Anytime we see an encoded string along with another string, we should immediately assume it is a vigenere cipher. Using the `Vigenere Decode` recipe in CyberChef, we can plug in our ciphertext and key:

```bash
I do not fear computers, I fear the lack of them SKY-QIZK-8026
```
#### Answer:
`SKY-QIZK-8026`