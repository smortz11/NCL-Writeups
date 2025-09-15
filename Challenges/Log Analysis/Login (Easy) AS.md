# CLI Searching Walkthrough
In this challenge,  we will be manipulating a file in order to gain information from it. We should go ahead and download the file and navigate to it's directory.

The following are some commands that we will need for the challenge.

| Command      | Output                                                                                                            |
| ------------ | ----------------------------------------------------------------------------------------------------------------- |
| `cat <file>` | Outputs the contents of the file                                                                                  |
| nl           | Appends a number to each line, useful for counting lines                                                          |
| `cut -f<n>`  | Splits a line by delimiters and returns the nth field                                                             |
| sort         | Alphabetically sorts the lines                                                                                    |
| uniq -c      | Only returns uniq names along with their number of occurrences (LINES MUST BE SORTED BEFORE WE USE THIS COMMAND!) |



---
# Q1 - 5 Points
#### How many total login attempts were made in this log?

Let's formulate a command using the top chart to find how many lines are in the file:

```bash
cat login.log | nl
```

We can see 6063 lines.
#### Answer:
`6063`

---
# Q2 - 15 Points
#### How many unique usernames appear in this log?

Let's formulate a command using the top chart to find how many uniq users there are:

```bash
cat login.log | cut -f3 | sort | uniq | nl
```

We can see 1879 lines. NOTE: We must sort the lines before we use `uniq`
#### Answer:
`1879`

---
# Q3 - 15 Points
#### What is the username with the most login attempts?

Let's formulate a command to cut the usernames, sort them, and use `uniq -c`

```bash
cat login.log | cut -f3 | sort | uniq -c | sort -n
```

In this variant, we cut the usernames, sort them, and find the count of each username. After this, notice that we sort the output again with the flag `-n`. This allows us to sort numerically, which is the occurrences that we are looking for.
#### Answer:
`ntory`

---
# Q4 - 20 Points
#### How many attempts were made for the username with the most login attempts?

This can be found using the last command as well, it is the numerical value next to the username.
#### Answer:
`124`

---
# Q5 - 20 Points
#### What is the date with the most login attempts?

We know that we want the first field in the file. However, when we cut by just the first field, we get the following output:

`2011-03-31 23:59:31`

We do not want to include the time. For this reason, we can actually cut this again, but this time, separated by a space (denoted ' '). We must select the first field of this cut.

Finally, we have just the dates. We can sort them, find the unique entries, then sort them again:

```bash
cat login.log | cut -f1 | cut -d ' ' -f1 | sort | uniq -c | sort -n
```
#### Answer:
`2011-03-23`

---
# Q6 - 20 Points
#### What is the username that had logins from the most unique IP addresses?

I am not claiming to have the best answer here, but an answer that I can walk through. Here is the command:

```bash
cat login.log | cut -f2,3 | sort | uniq | cut -f2 | sort | uniq -c | sort -n
```

Phew. Let's take this one bite at a time:
1. cat login.log -> we get all of the file contents
2. cut -f2,3 -> we retrieve the columns of the IP followed by username
3. sort -> sorts the file, putting duplicate entries together
4. uniq -> takes all duplicate lines and removes them. We are now left with unique IP and username combinations
5. cut -f2 -> retrieves the usernames
6. sort -> sorts the usernames
7. uniq -c -> Counts the occurrence of each username
8. sort -n -> finds the largest number of each username

You will not inherently type this command in one go. Instead, we run commands incrementally. We test each step of the way to confirm that we are doing what we need to do. This is not the only solution, but it is one that works.
#### Answer:
`wlfla0190`

---
# Conclusion

CLI skills are a tad difficult to grasp, but once you do, your versatility skyrockets. The commands introduced here are integral for log parsing and will help you in your Linux adventures.