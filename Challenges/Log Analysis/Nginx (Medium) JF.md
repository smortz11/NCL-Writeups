# Nginx Log Analysis Walkthrough
Analyze an nginx access log and answer questions about what happened.

Download the log file and open it with 'open "access_(8).log"'

![A picture of the log file mentioned above open ith its contents.](https://github.com/smortz11/NCL-Writeups/blob/main/Attachments/Log%20Analysis/Nginx1.png)

---
# Q1 - 10 Points
#### How many different IP addresses reached the server?

Do the command:

```bash
cat 'access_(8).log' | cut -d " " -f 1 | sort | uniq | wc -l
```

This is saying that we need to concatenate the files contents while only using the first line and breaking off everything after the delimeter (space).
Then we are sorting them numerically while only accounting for unique IP's. Finally, we get a printout of actually how many there are.

#### Answer:
`47`

# Q2 - 10 Points
#### How many requests yielded a 200 status?

Run:

```bash
cat 'access_(8).log' | grep " 200 " | wc -l
```

We are looking for 200 status so we need to search for 200. It is important to know that we see that 200 codes always have a space behind them.
We get to use this to our advantage so we can grep for a space quoted behind the 200. Then we just get to wordcount the amount of lines for our answer.

#### Answer:
`19`

# Q3 - 10 Points
#### How many requests yielded a 400 status?

Try:

```bash
cat 'access_(8).log' | grep " 400 " | wc -l
```

Nothing too different happening on this one. Simply query for a 400 instead of a 200.

#### Answer:
`38`

# Q4 - 10 Points
#### What IP address rang at the doorbell?

This one probably makes no sense to you, don't worry, it made no sense to me either. So when I set out to do this one I started grepping related things.
I started off with "doorbell" then "door bell" then "door", nothing...

That is until I tried it with just "bell"

Until I ran:

```bash
cat 'access_(8).log' | grep "bell""
```

Well we actually get a result from this command when ran.

![A picture of the log file mentioned above open ith its contents.](https://github.com/smortz11/NCL-Writeups/blob/main/Attachments/Log%20Analysis/Nginx2.png)

Looking at the IP address associated with this log we can get the answer for this question.

#### Answer:
`186.64.69.141`

## OTHER QUESTIONS UNDER CONSTRUCTION

---
# Conclusion

A short conclusion if necessary
