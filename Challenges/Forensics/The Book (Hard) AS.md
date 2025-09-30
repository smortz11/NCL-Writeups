# Memory Dumps Walkthrough
In this challenge, we are given a memory dump as a xz archive. We need the raw `.mem` file to start our analysis. Let's get started.

---
# Q1 - 5 Points
#### What operating system was this dump taken from?

Once we download the file, we need to create the raw file with the following command:

```bash
xz -d memdump.mem.xz
```

This creates a file `memdump.mem` in the current working directory. If we run `file memdump.mem`, we can see that it is related to a Windows OS. Since the answer may want the version, this will not suffice.

We are going to use Volatility 3. It may not come pre-installed. I'm not going to detail the install process. Just get it downloaded and working :)

After installing, we can use the following command (knowing that it is Windows) and grab some information:

```bash
python vol.py -f /path/to/memdump windows.info
```

This will tell us the NtSystemRoot (C:\Windows) as well as the PE MajorOperatingSystemVersin (10)
#### Answer:
`Windows 10`

---
# Q2 - 5 Points
#### What is the name of the computer?

NOTE: At any point, we can run the following to see what plugins we have available:

```bash
python vol.py -h
```

I know that the computer name is stored in the registry, so I ran the following command:

```bash
python vol.py -f /path/memdump windows.registry.hivelist
```

Here, we can see an entry for `\REGISTRY\MACHINE\SYSTEM` along with a corresponding memory offset of `0xc00154a3e000`. I then ran the following command:

```bash
python vol.py -f ~/Documents/Notes/NCL\ Writeups/Attachments/Forensics/memdump.mem windows.registry.printkey --offset 0xc00154a3e000 --key "ControlSet001\\Control\\ComputerName\\ComputerName"
```

Output:

```bash
Volatility 3 Framework 2.27.0
Progress:  100.00		PDB scanning finished                        
Last Write Time	Hive Offset	Type	Key	Name	Data	Volatile

2023-10-31 03:45:05.000000 UTC	0xc00154a3e000	REG_SZ	\REGISTRY\MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ComputerName	(Default)	mnmsrvc	False
2023-10-31 03:45:05.000000 UTC	0xc00154a3e000	REG_SZ	\REGISTRY\MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ComputerName	ComputerName	DESKTOP-OT97GG3	False
```

The string followed by key is the extended location for the name of the key. This is just information within the registry, which you can find online.

At any point, while I will not detail it, after the main Volatility argument, ie `windows.registry`, we can append `-h` afterwards and see more information per command. This is how I crafted the command.
#### Answer:
`DESKTOP-OT97GG3`

---
# Q3 - 10 Points
#### What is the name of the user that was logged in?

After running some `-h` commands, I determined the following would yield results: 

```bash
python vol.py -f /memdump.mem windows.sessions.Sessions
```

This actually returns the desktop name as well. Neat!
#### Answer:
`liber8hacker`

---
# Q4 - 10 Points
#### What is the full filepath and file of the file in interest?

I may be doing this wrong, but here is my process for solving:

Let's check which processes are running. This may give us some insight.

```bash
python vol.py -f memdump.mem windows.pslist.PsList
```

This outputs a large number of processes that were running when the memdump was taken. Some of them are not normal for Windows processes:

```
3544	2596	FTK Imager.exe	0xe0003e097840	21	-	1	False	2023-10-31 05:09:24.000000 UTC	N/A	Disabled

3768	2596	DB Browser for	0xe0003fb2c380	11	-	1	True	2023-10-31 05:05:28.000000 UTC	N/A	Disabled

2596	2564	explorer.exe	0xe0003e805080	42	-	1	False	2023-10-31 05:05:21.000000 UTC	N/A	Disabled
```

PID 2596 spawned both FTK imager and DB browser. Since FTK is for forensic analysis, I'm going to assume that it is not the one we need. 

Then I ran the following command to obtain more information about the process:

```bash
python vol.py -f memdump.mem windows.cmdline.CmdLine --pid 3768
```

Output: `3768	DB Browser for	"C:\Program Files (x86)\DB Browser for SQLite\DB Browser for SQLite.exe" `

Now we can look and search for SQLite or some sort of database confirmed. The user had this process open. Let's investigate the handles spawned from this process:

```bash
python vol.py -f memdump.mem windows.handles.Handles --pid 3768
```

Here, we can see different categories (events, threads, files, section, ...). Let's enter the same command but this time, append `| grep -i "file"`

Output:

```bash
3768ressDB Browser for	0xe0003fb248f0an0x14 finFile	0x100020	\Device\HarddiskVolume2\Windows
3768	DB Browser for	0xc001564bdd60	0x1c	Key	0x9	MACHINE\SOFTWARE\MICROSOFT\WINDOWS NT\CURRENTVERSION\IMAGE FILE EXECUTION OPTIONS
3768	DB Browser for	0xe0003f65a5a0	0x28	File	0x100020	\Device\HarddiskVolume2\Program Files (x86)\DB Browser for SQLite
3768	DB Browser for	0xe0003fb1d6a0	0x30	File	0x100020	\Device\HarddiskVolume2\Windows\WinSxS\x86_microsoft.windows.common-controls_6595b64144ccf1df_5.82.10240.16384_none_49c02355cf03478c
3768	DB Browser for	0xe0003e8e3c70	0xa8	File	0x100003	\Device\KsecDD
3768	DB Browser for	0xe0003fb265c0	0xb4	File	0x100001	\Device\CNG
3768	DB Browser for	0xe0003fb2d970	0x1bc	File	0x120089	\Device\DeviceApi\CMApi
3768	DB Browser for	0xe0003fbf4ae0	0x214	File	0x120089	\Device\HarddiskVolume2\Windows\SysWOW64\en-US\KernelBase.dll.mui
3768	DB Browser for	0xe0003f399220	0x254	File	0x100080	\Device\Nsi
3768	DB Browser for	0xe0003f861960	0x3a8	File	0x12019f	\Device\HarddiskVolume2\Users\liber8hacker\Desktop\black_book.db-journal
3768	DB Browser for	0xe0003eaa52d0	0x3c8	File	0x120089	\Device\HarddiskVolume2\Windows\SysWOW64\en-US\user32.dll.mui
```

One of these isn't a .dll and looks like it could be suspicious.
#### Answer:
`\Device\HarddiskVolume2\Users\liber8hacker\Desktop\black_book.db-journal`

---
# Q5 - 30 Points
#### What is the real name of "cloud"?

What.

I'm going to guess this is referencing the suspicious file we mentioned. We should try to find it in the memdump and extract it I guess. Since the file above is the journal, we need to find the actual database. 

Okay. Future me here. This one had me in the *weeds*. Like, bad. I'm not going to torture myself by typing each and every command.

What did I do? I ran this command to find the possible offsets for the file mentioned above:

```bash
python vol.py -f memdump.mem windows.filescan.FileScan | grep -i "black_book"
```

With these virtual addresses, I used:

```bash
python vol.py -f memdump.mem -o temp_databases/ windows.dumpfiles.DumpFiles --virtaddr <addr>
```

Then, I copied the .dat file into a .db file, and used SQL to analyze, ie, `.tables` and some `SELECT * FROM <table_name>`

I ran the above select command on both tables in the .db in order  to find the alias and name. Cloud corresponded to the following.
#### Answer:
`gloria hampton`

---
# Q6 - 40 Points
#### What is the password of the currently logged in user?

I ran the following:

```bash
python vol.py -f memdump.mem windows.registry.hashdump.Hashdump
```

Here, we are given the hashes of each user on the system. We are interested in the following though:

```bash
liber8hacker	1001	aad3b435b51404eeaad3b435b51404ee	214a7d83f1c36a5f7071137d7c6e5ae6
```

The fourth field is the NTLM hash that we need to crack. Since this isn't the password cracking module, I did not expect the hash to be difficult. I pasted it into [Crackstation](https://crackstation.net/) and got the answer.
#### Answer:
`avatar2`

---
# Conclusion

This was the worst experience of my life.