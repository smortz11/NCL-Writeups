# Navigating Git Walkthrough
In this room, we are given a git repository that we need to navigate and check through. Let's get started. Navigate to your desired directory of work and run the following command to get started:

```bash
git clone https://gitlab.com/cybergit4823/my-awesome-flag-project.git
```

Note: We won't always answer questions in the order presented. In this example, I found flag3 before anything else!

---
# Q1 - 10 Points
#### What is the display name of the author of this git project??

We can see this after navigating to the web URL.
#### Answer:
`Cyber Cyber`

---
# Q2 - 10 Points
#### What is the short commit hash (first 8 characters) of the initial commit?

Instead of using our cloned repository, I also navigated to the website shown above before any questions were answered. Here, if we navigate to `History`, we can see the initial commit along with it's eight character short hash.
#### Answer:
`f9714edd`

---
# Q3 - 15 Points
#### What is flag #1?

Inside of the cloned directory, if we look at the file `README.md`, with the following command, we can see the flag:

```bash
cat README.md
```
#### Answer:
`SKY-HSNO-2303`

---
# Q4 - 15 Points
#### What is flag #2?

While in the web GUI for the repository, when I looked at the branches tab, there was a branch containing the second flag.
#### Answer:
`SKY-OZNW-3730

---
# Q5 - 15 Points
#### What is flag #3?

After using `cd` to navigate inside of the cloned directory,  I ran `ls` to see what was in it, and found the flag. We can obtain it with the following command:

```bash
cat flag3.txt
```
#### Answer:
`SKY-CCXL-4067`

---
# Q6 - 15 Points
#### What is flag #4?

While answering Q2 (in the web GUI for the repository), in the `History` tab, we see a commit that mentions removing/adding `flag4`. If we click on this we can see the change, as well as the flag.
#### Answer:
``SKY-IRRK-9672``

---
# Q7 - 20 Points
#### What is flag #5?

This is the most random of them all.

I stumbled upon flag five when clicking around in the web GUI. I found the latest commit (shown at the top of the main repository page), and pressed the three dots next to it, which toggles the commit comment.

Flag 5 can be seen in this comment.
#### Answer:
`SKY-DKIT-9801`

---
# Conclusion

For this challenge, cloning the repository was not required at all. But, going in, we could not assume that. Be resilient in your searches and cover all bases!