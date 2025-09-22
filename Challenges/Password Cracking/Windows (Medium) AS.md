# Intro to NTLM Walkthrough
Have you ever heard of Ophcrack? Me either! Let's hope you have several gigabytes of free storage, because you're going to need *all* of it :)

We can assume that the hashes given to us are NTLM hashes. This is like the signature Windows hash. The colon in the hashes also help us identify them as such, separating NT:LM. 

With tools like john, you can try to crack NT or LM hashes. However, for my run, I decided to use Ophcrack, a tool that is more specifically designed for tackling this hash format. The tool came pre-installed on my own device, so I only had to download the `tables`, which is kinda like the equivalent of a wordlist. Let's also go ahead and compile our hashes into a file, ie, `windows_hashes.txt`. The tables can be installed [here](https://ophcrack.sourceforge.io/tables.php). See the 17.0GB one? That's the one I got (the free small and free fast will do the job though)

---
# Q1 - 10 Points
#### 21259DD63B980471AAD3B435B51404EE:1E43E37B818AB5EDB066EB58CCDC1823

Let's get started with Ophcrack. Run this command:

```bash
ophcrack -f windows_hashes.txt -t ~/Wordlists/ophcrack_xp_tables/xp_free_fast/
```

This will open the Ophcrack GUI, load in our hashes correctly, and load the one table we specified. After opening, there are a few things we need to do:
1. Install other tables if we need them
	1. Tables -> Install
2. Crack

After some time, we will see all of our passwords. Submit the ones under the right column (NT Password)
#### Answer:
`starf0x`

---
# Q2 - 10 Points
#### 11CB3F697332AE4C4A3B108F3FA6CB6D:13B29964CC2480B4EF454C59562E675C

#### Answer:
`P@ssword`

---
# Q3 - 10 Points
#### 65711C079DC4CD3CC2265B23734E0DAC:47F747C5190DC0F0B921AA4A07F06285

#### Answer:
`footba11`

---
# Q4 - 10 Points
#### FBBDA33FC12E83FB0C240E84A183686E:DDE9DC6E34E2E6E11EF9E51C6B27ED96

#### Answer:
`1trustno1`

---
# Q5 - 10 Points
#### 21C4E7C2EFE8E8D1C00B70065ED76AA7:A7A0F9AFD4A78F531A1CF4C42E531BBF

#### Answer:
`ectoplasm32`

---
# Q6 - 10 Points
#### E85B4B634711A266AAD3B435B51404EE:FD134459FE4D3A6DB4034C4E52403F16

#### Answer:
`"=Cxu&L`

---
# Q7 - 10 Points
#### BA756FB317B622DBAAD3B435B51404EE:C8405270B10B13AE8A24612BB853567A

#### Answer:
`yhM^GK7`

---
# Q8 - 10 Points
#### 199C926FA387EAB7AAD3B435B51404EE:F196F77BF8BB15781BA8364C649C5FD4

#### Answer:
`58?-<C6`

---
# Q9 - 10 Points
#### FE4AACAAAD7D986AAAD3B435B51404EE:3928E16F614E2316CA51C336FA5B3011

#### Answer:
`$xEn@=y`

---
# Q10 - 10 Points
#### 3613F7EC15407F56AAD3B435B51404EE:C82E164316183AA3AF3EA6BAA642A237

#### Answer:
`^B7e3D;`

---
# Conclusion

Enjoy the huge tables file. Remember to use Ophcrack for NTLM hashes, ie, Windows hashes!