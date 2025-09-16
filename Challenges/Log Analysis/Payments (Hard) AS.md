# XML Logs Walkthrough
Download the log and navigate to it, you know the drill by now. Lemme tell you; this log is *dense*. Like, an absolute *unit*.

Being an XML log though, we can understand it better by using an XML visualizer like [this](https://codebeautify.org/xmlviewer) one.

---
# Q1 - 15 Points
#### How many transactions are contained in the log?

After visualizing one of the XML responses, I found a field named `transactionid`. I decided that by grepping for this term, I would find the number of transactions.

```bash
cat payments.log | grep -i "transactionid" | nl
```
#### Answer:
`192`

---
# Q2 - 40 Points
#### What is the transaction ID of the largest purchase made in the log?

Things now become difficult. We must do several things. Upon inspection of the file, we will see headers notating requests and responses.

I'm not even gonna fake this. This took me like an hour by itself. This one *sucked*.

Like I mentioned above, there are requests and responses. As we will find out, the order amount is in the request and the transaction id is in the response. Let's first find out what our largest purchase is:

```bash
cat payments.log | grep -oE 'OrderTotal currencyID="USD">[0-9]+(\.[0-9]+)?' | cut -d'>' -f2 | sort -n
```

This will give us a largest amount of `998.6`. But when we grep this, we cannot find a transaction id...

That is because it is in the following response!

I used the following command to find the chronological next response:

```bash
cat payments.log | grep -A6 "998.6"
```

Here, we can see a transaction id.

#### Answer:
`3a4da8c8-6934-4655-9ec5-335ab4540a2b`

---
# Q3 - 45 Points
#### Which state made the greatest number of purchases?

We can filter for these states with the following command:

```bash
cat payments.log | grep -oE "StateOrProvince>[A-Z]{1,3}" | cut -d'>' -f2 | sort | uniq -c | sort -n
```
#### Answer:
`MA`

---
# Conclusion

This one was hard for me, most of the time was spent actually understanding the log. Once I understood the format of the requests and responses, things became much easier!