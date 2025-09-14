# Morse Code Walkthrough
In yet another cryptography challenge, we are given a string consisting of dots, dashes, and slashes. This is morse code, and can be decoded with [CyberChef](https://cyberchef.org).

---
# Q1 - 25 Points
#### - .... . / ... . -.-. .-. . - / --- ..-. / --. . - - .. -. --. / .- .... . .- -.. / .. ... / --. . - - .. -. --. / ... - .- .-. - . -.. / ... -.- -.-- / -.. -.- ...- -... / ----. ---.. .---- -....

A method of communication consisting of dots and dashes is known as morse code. The slashes in this case denote a new word (I think). Regardless, we can decode the string using the `From Morse Code` recipe in CyberChef.

```bash
THESECRETOFGETTINGAHEADISGETTINGSTARTEDSKYDKVB9816
```

We may inherently paste the entire string as the issue, but if we look closer, we can see a flag at the end!
#### Answer:
`SKYDKVB9816`

---
# Conclusion

If you ever come across an encoded string that you are unsure of it's format, there are tools online that can attempt to determine the type of encoded string that was passed. Try [DCode](https://www.dcode.fr/cipher-identifier).