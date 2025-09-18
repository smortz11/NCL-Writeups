# Analyzing a Car? Walkthrough
We have another .pcap that resembles the CAN bus of a vehicle. We are also given a code snippet for insight:

```c
int speed_id = 589;
int speed_pos = 3;
struct canfd_frame frame;

while (PollEvent(&event) != 0) {
    read_data(&event, &frame);
    if (frame.can_id == speed_id) {
        double speed = frame->data[speed_pos] << 8;
        speed += frame->data[speed_pos + 1];
        speed = speed / 100;
        speed = speed * 0.6213751;
        update_speed(speed);
    }
}
```

Remember Wireshark? Remember how nice it was? WE ARE USING TSHARK BABYYYY GOODBYE GUI ELEMENTS, HELLLOOOO CLI.

---
# Q1 - 25 Points
#### How many unique CAN Bus IDs are present in this capture?

Before using TShark, I recommend looking at Wireshark, or both honestly. Scrolling through the .pcap in Wireshark, we can see the CAN Bus IDs in the `Info` column. If we click the title name, it will sort it, but it will not tell us how many unique ones there are. Navigate to the directory the .pcap is downloaded in on a terminal and run the following command:

```bash
tshark -r Candump.pcap -T fields -e can.id | sort -n | uniq | nl
```

1. `-r Candump.pcap` -> specifies the file to read
2. `-T fields` -> specifies we are limiting input by fields
3. `-e can.id` -> specifies the field we are cutting
4. `sort -n | uniq | nl` -> compresses output and gives a total number of unique entries
#### Answer:
`36`

---
# Q2 - 25 Points
#### How many speed update messages are present in this capture?

From the code snippet at the top, we know that the can.id for the speed event is `589`. Let's use Tshark again and look at how many `589` messages we have.

```bash
tshark -r Candump.pcap -T fields -e can.id | sort -n | uniq -c
```

(How did we get can.id? scroll down to the big word The Note. I explain there.)

Output:

```bash
	273 57
    415 149
    414 307
    414 310
    414 314
    415 319
    415 323
    414 344
    414 353
    415 356
    414 358
    415 380
    415 387
      8 392
    415 398
    414 401
    207 420
    206 426
    206 432
    207 463
    206 464
    207 476
    104 542
    352 589
    104 660
     40 773
     42 777
     42 800
     42 804
     41 819
     42 892
     14 1029
     14 1036
     14 1064
     14 1108
      4 1441

```
#### Answer:
`352`

---
# Q3 - 50 Points
#### What is the maximum speed, in mph, that this vehicle reached in the capture? (round to the nearest hundredth)

Strap in, cupcake. This is not gonna be awesome. We are gonna reference the C code a ton, so I will repaste it here:

```c
int speed_id = 589;
int speed_pos = 3;
struct canfd_frame frame;

while (PollEvent(&event) != 0) {
    read_data(&event, &frame);
    if (frame.can_id == speed_id) {
        double speed = frame->data[speed_pos] << 8;
        speed += frame->data[speed_pos + 1];
        speed = speed / 100;
        speed = speed * 0.6213751;
        update_speed(speed);
    }
}
```

Let's look at the `if` statement.

`if (frame.can_id == speed_id) {` -> If the can.id is 589, the id for speed

`double speed = frame->data[speed_pos] << 8;` -> Go to the data at speed_pos (This is three). We are now looking at the fourth byte (we start counting at zero). Take in 8 bits, or 2 hex characters.

`speed += frame->data[speed_pos + 1];` -> move to the next byte and take it in. Add this as the second digit of the speed. So now, speed is two digits. We don't actually sum these numbers, we append this one to the end of the previous one.

The rest of the code *probably* converts this number to mph. 

So, now we know that the fourth and fifth bytes (index 3 and 4) are both our speed bytes.

We will use a tool, Tshark, to extract this data from the .pcap. Recall, our can.id must be 589, then we want the fourth and fifth bytes. Once we have these, we can calculate which is the highest.

# The Note
Important to note now. Remember earlier when we used can.id as a field? Where did this field come from? In Wireshark, we can click elements in the bottom-left pane of something we want to capture. It will pop up it's filter name in the bottom. Test it out!

The hex data is contained within `data.data`.

```bash
tshark -r Candump.pcap -Y "can.id == 589" -T fields -e data.data > can.txt
```

This command adds all of the hex values for the specified can.id to a text file so we can script the final answer.

```bash
cat hex_values.txt | while read hex; do
    last4=${hex: -4}; high=${last4:0:2}; low=${last4:2:2}; speed=$(( (16#$high << 8) + 16#$low )); echo "scale=2; $speed/100*0.6213751" | bc
done | sort -nr | head -1
```

This command, for each hex value, cuts off the final four digits, assigns a high and low, and calculates the speed out of it. Then, it sorts numerically, and returns only the top number: 20.1325532 -> 20.13

#### Answer:
`20.13`

---
# Conclusion

Solving this was a confidence booster LOL. Welcome to Tshark. It sucks, I know. But, if we have to *script* with data inside of a .pcap, it may be the best way to move forward.