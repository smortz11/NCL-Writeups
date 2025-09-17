# Navigating URL from a Server Walkthrough
In this challenge, we are once again given a server: `metadata.services.cityinthe.cloud:1338`. Once again, I attempted to telnet in, but after being accepted, any input would terminate the session. However, upon using `telnet` to gain access, I also discovered that it is an `HTTP` server. So, let's simply navigate to the above URL.

Upon doing so, we will see a screen with the word `latest`. If we append this to the URL like so:
`http://metadata.services.cityinthe.cloud:1338/latest`, we find that we can crawl around the site. We will do this to answer the following questions.

---
# Q1 - 10 Points
#### What availability zone is this instance hosted in?

From the main URL, `http://metadata.services.cityinthe.cloud:1338/latest/meta-data`, I navigated to `placement`. I do not inherently know this. But, in my head, I made the association that the place in which it is hosted may correlate with an availability zone. I was correct. If we navigate into `placement`, we see `availability-zone`, which when navigated to, gives us the answer.
#### Answer:
`us-west-2a`

---
# Q2 - 10 Points
#### What is the security credentials role named?

From `http://metadata.services.cityinthe.cloud:1338/latest/meta-data/`, I navigated to IAM, which stands for Identity and Access Management (likely to hold credentials). From here, if we follow down the chain, we see an extension for `security-credentials`, where we only have one entry:
#### Answer:
`liber8-role`

---
# Q3 - 15 Points
#### What is the instance type being used?

I found this answer first. By crawling around the site, I eventually navigated to `http://metadata.services.cityinthe.cloud:1338/latest/meta-data/`. Here, we can see a directory for `instance-type`. We can navigate to this and grab the answer for this question.
#### Answer:
`c6g.16xlarge`

---
# Q4 - 20 Points
#### What is the operating system name and version number?

For this one, I did some research. I originally thought that `kernel-id` would give insight, but I was wrong. However, the `ami-id` can! Once navigating to it, I copied it and pasted it [here](https://amilookup.com/). This gives us information about the cloud server:

```bash
VirtualizationType

hvm

Description

Canonical, Ubuntu, 16.04 LTS, arm64 xenial image build on 2021-09-28

Hypervisor

xen

ImageOwnerAlias

amazon

EnaSupport

true

SriovNetSupport

simple

ImageId

ami-08305dd8ab642ad8c

State

available
```
#### Answer:
`Ubuntu 16.04 LTS`

---
# Q5 - 45 Points
#### What is the flag?

This could literally be anywhere. Time to get looking!

After following all the way down `/latest/dynamic`, I do not believe the flag to be there. I am even decoding base64 strings I see just in case they are being sneaky!

Navigating to `/user-data` downloads a file with the contents:

```bash
1234,john,reboot,true
```

Our flag is probably in `meta-data`.

From `meta-data`:
1. not in `tags`
2. not in `services`

Okay. Not writing over this. This is a stupid approach. I just wrote a script to recurse into each subdirectory and grep it for a flag. This script is in attachments and is called `check_meta.sh`. If you run that and then grep it's output for `Potential`, you will get the line that contains the flag.

This one took a while.
#### Answer:
`SKY-AWSM-1570`

---
# Conclusion

I had no idea how any of this worked. What is most important, if you are following along, is that you can get the answers *without* just following a guide. During the games, research and internet sources are free game. Knowing how the stuff works speeds you up, which is an extremely important factor, but you are not expected to know anything.

You are, however, expected to know how to get to it. 

Cheers!