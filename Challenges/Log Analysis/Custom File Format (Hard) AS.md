# How to Write a Parser Walkthrough
Don't do this.

In the real game, there will be different requirements. I have a script for solving this in `/Scripts`

---
# Q1 - 10 Points
#### What is the hostname of the server?

My script  will output this in the terminal where it is ran.
#### Answer:
`sky-server-711`

---
# Q2 - 10 Points
#### What is the plaintext flag in the log file?

My script will output this in the terminal. It is base64 encoded, however. We must decode it using a tool like CyberChef.
#### Answer:
`What is the plaintext flag in the log file?`

---
# Q3 - 10 Points
#### On what date was the file created (in UTC)?

This is included in the terminal output of the script.
#### Answer:
`2018-03-03 05:00:00`

---
# Q4 - 10 Points
#### How many entries are in the log file?

I also have this included in the terminal output.
#### Answer:
`162`

---
# Q5 - 10 Points
#### How many total transferred bytes were recorded in the log?

We now can use the `.csv` that my script creates. Plug it into Excel and use a summation on the column including the bytes transferred.
#### Answer:
`811167`

---
# Q6 - 10 Points
#### How many unique IP addresses (both senders and receivers) are recorded?

In the Excel sheet, we can use `=COUNTA(UNIQUE(VSTACK(A2:A163, B2:B163)))` to find the number of unique values in the two columns
#### Answer:
`13`
`

---
# Q7 - 10 Points
#### Which IP address sent the most amount of data?

This is shown in the terminal of my script
#### Answer:
`229.212.21.212`

---
# Q8 - 10 Points
#### How many total bytes were sent by the above IP address that sent the most amount of data?

Also shown in the script.
#### Answer:
`145048`

---
# Q9 - 20 Points
#### What was the busiest day (day with the most bytes transferred)?

In the script.
#### Answer:
`2018-03-23`

---
# Conclusion

I hated this and I want to cry.