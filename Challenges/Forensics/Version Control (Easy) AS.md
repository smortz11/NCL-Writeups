# Git as Version Control Walkthrough
In this room, we are given a .zip file that inflates into a what was a git backup. We will unzip this file and analyze its contents.

Before we begin, lets unzip the file using the following command:

```bash
unzip git_backup.zip
```

```bash
ls
git_backup git_backup.zip
```

```bash
rm git_backup.zip
```

```bash
cd git_backup
```

We can now begin our forensics.

---
# Q1 - 10 Points
#### What is the email address of the employee who was compromised?

Let's first check the README:

```bash
cat README.md
This repo is for storing important information
```

Let's try to check what else is in the directory:

```bash
ls
README.md
```

It appears that there are no other contents in this .zip file. However, there are many file types that are blocked from being seen with just `ls`. We can view all hidden files with `ls -a`

```bash
ls -a
. .. .git README.md
```

It is important to note that the directory `.` represents the current working directory and `..` represents the directory a level above the current directory. The directory `.git` suggests that we can use `git` commands to inspect some data here. Let's try the following:

```bash
git log
```

This command will give us a list of the commits made in the git repository, which comes with an email address!
#### Answer:
`gpeterson@mpd.hacknet.cityinthe.cloud`


# Q2 - 20 Points

#### Each employee is assigned a flag. What is the flag that was compromised?

From our previous command, we can see output of the form:

```bash
commit f28a0c2e4ef9bdc2cd6e780abdbd8695485c7083 (HEAD -> master)
Author: Greg Peterson <gpeterson@mpd.hacknet.cityinthe.cloud>
Date:   Sun Feb 12 23:25:59 2017 -0500

    Oops wasn't supposed to commit that

```

Here, we can see a hash following the commit command. This hash is like a unique identifier for this particular commit. We can copy this hash and paste it into the command `git show <hash>`

```bash
git show f28a0c2e4ef9bdc2cd6e780abdbd8695485c7083
```

We can iterate through each of the hashes for the given commits (there should be 3), and we can scan for a flag. Recall that all NCL flags are in the format `SKY-AAAA-NNNN`, where A is a letter and N is a number.
#### Answer:
`SKY-LRHX-4910`

# Q3 - 15 Points

#### Greg thinks that he may have had additional account credentials that were compromised. What's the name of the service provider for that other compromised account?

Following more git commands, we can check to see if there exist any other branches with possible data. We have exhausted the commits on the main branch already. We can find a new branch and switch using the following commands:

```bash
git branch
*master next
```

```bash
git checkout next
```

Now, if we run the `ls` command to see if anything has changed, we will see a new `passwords.txt` file. Let's check it's output:

```bash
cat passwords.txt
Facebook: waffles85
```
#### Answer:
`Facebook`

# Q4 - 15 Points

#### What was the password on that compromised account?

We know the answer from the above output.

#### Answer:
waffles85

---
# Conclusion

Comparatively, this room felt kinda random. The important part here is to recognize that we had a git repository to work with and knew some of the basic inner workings of git. Apart from this, we, as investigators, just have to poke around. The steps detailed here are not going to work in every instance.