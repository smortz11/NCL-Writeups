# Port Scanning Walkthrough
This room serves as an introduction to port scanning, namely through perhaps the most iconic "hacking" tool, nmap. Nmap allows us to scan an IP address, or host name, for open ports on the target system. We can also perform ping sweeps to determine which IP addresses exist within a subnet.

nmap is a very large and complex tool that is easy to learn but hard to master. Let's get started!

---
# Q1 - 15 Points
#### What is the lowest open TCP port on the system?

Since we need to know what ports are open, we are going to use nmap, of course. We can scan the given domain with the following command:

```bash
sudo nmap ports.cityinthe.cloud
```

Note: The keyword `sudo` runs the following command with higher privileges. This allows us to perform a SYN scan over a TCP connect scan. The work behind this is not important at the moment.

We get the following output:

```bash
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-09-12 21:33 EDT
Nmap scan report for ports.cityinthe.cloud (34.199.237.244)
Host is up (0.045s latency).
rDNS record for 34.199.237.244: ec2-34-199-237-244.compute-1.amazonaws.com
Not shown: 996 filtered tcp ports (no-response)
PORT      STATE SERVICE
7/tcp     open  echo
13/tcp    open  daytime
37/tcp    open  time
16080/tcp open  osxwebadmin

Nmap done: 1 IP address (1 host up) scanned in 11.57 seconds

```
#### Answer:
`7`

# Q2 - 15 Points

#### What is the second lowest open TCP port on the system?

We can see the answer in the above output.
#### Answer:
`13`

# Q3 - 15 Points

#### What is the third lowest open TCP port on the system?

We can see the answer in the above output.
#### Answer:
`37`

# Q4 - 20 Points

#### What is the lowest open UDP port on the system?

Notice: In this question, we are asked for the *UDP* ports, not *TCP*. We can conduct a scan of the UDP ports by appending the flag `-sU` to our `nmap` command as follows:

```bash
sudo nmap -sU ports.cityinthe.cloud
```

Output:

```bash
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-09-12 21:44 EDT
Nmap scan report for ports.cityinthe.cloud (34.199.237.244)
Host is up (0.046s latency).
rDNS record for 34.199.237.244: ec2-34-199-237-244.compute-1.amazonaws.com
Not shown: 999 open|filtered udp ports (no-response)
PORT  STATE SERVICE
7/udp open  echo

```
#### Answer:
`7`

# Q5 - 20 Points

#### What software is being run on TCP port 16080?

In order to determine a software type running on a port, we must run what is known as a version scan. This can be done by appending `-sV` to the nmap command:

```bash
sudo nmap -sV ports.cityinthe.cloud
```

Output:

```bash
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-09-12 21:48 EDT
Nmap scan report for ports.cityinthe.cloud (34.199.237.244)
Host is up (0.039s latency).
rDNS record for 34.199.237.244: ec2-34-199-237-244.compute-1.amazonaws.com
Not shown: 996 filtered tcp ports (no-response)
PORT      STATE SERVICE VERSION
7/tcp     open  echo
13/tcp    open  daytime
37/tcp    open  time    (32 bits)
16080/tcp open  http    nginx 1.10.3 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.50 seconds
```

#### Answer:
`nginx`

---
# Conclusion

Nmap is an awesome tool that is the standard for port scanning. Though it may seem basic at first, there are many applications it has in reconaissance, penetration testing, and other tasks, such as hardening networks.