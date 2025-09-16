# SQL Walkthrough
Structured Query Language (SQL) is a language used to interface with relational databases. It's syntax may feel a tad uncommon at first, but it is not too unusual to grasp and understand. In this room, we are give an sqlite database, which is a type of SQL database. We can use the same commands on it that we could with an SQL database.

Each command I use will be explained at least once, but make sure you understand how/why they work. For now, go ahead and download the file and navigate to its download location. Finally, we can begin interfacing with the database by running the following command:

```bash
sqlite3 browser.sqlite
```

---
# Q1 - 10 Points
#### What did the user search for on craigslist?

We can first interface with this database using a few commands. First of all, we must understand that a database is a series of tables, essentially like an excel sheet. Databases are made of several of these excel sheets.

| Command              | Output                                                                               |
| -------------------- | ------------------------------------------------------------------------------------ |
| .tables              | All of the tables contained within the database                                      |
| .schema <table_name> | Outputs how the table is formatted, essentially the name of the columns it possesses |

Output of `.tables`:

```bash
sqlite> .tables
moz_anno_attributes  moz_favicons         moz_items_annos    
moz_annos            moz_historyvisits    moz_keywords       
moz_bookmarks        moz_hosts            moz_places         
moz_bookmarks_roots  moz_inputhistory  
```

There are a few takeaways here. 

Yes, this did look like dispair and garbage to me at first as well. So no worries about that! But if we look at the tables, they are all prefaced with `moz`, short for Mozilla, a.k.a. FireFox.

There is documentation for this online. As it turns out, we can access the URL's accessed using the table `moz_places`.

Output of `.schema moz_places`:

```bash
sqlite> .schema moz_places
CREATE TABLE moz_places (   id INTEGER PRIMARY KEY, url LONGVARCHAR, title LONGVARCHAR, rev_host LONGVARCHAR, visit_count INTEGER DEFAULT 0, hidden INTEGER DEFAULT 0 NOT NULL, typed INTEGER DEFAULT 0 NOT NULL, favicon_id INTEGER, frecency INTEGER DEFAULT -1 NOT NULL, last_visit_date INTEGER , guid TEXT, foreign_count INTEGER DEFAULT 0 NOT NULL);
CREATE INDEX moz_places_faviconindex ON moz_places (favicon_id);
CREATE INDEX moz_places_hostindex ON moz_places (rev_host);
CREATE INDEX moz_places_visitcount ON moz_places (visit_count);
CREATE INDEX moz_places_frecencyindex ON moz_places (frecency);
CREATE INDEX moz_places_lastvisitdateindex ON moz_places (last_visit_date);
CREATE UNIQUE INDEX moz_places_url_uniqueindex ON moz_places (url);
CREATE UNIQUE INDEX moz_places_guid_uniqueindex ON moz_places (guid);
```

We can see the columns in this table. The one that interests us the most is the url, as from there, we may gain insight into search terms. I used the following command:

```sqlite
SELECT * FROM moz_places WHERE url LIKE "%craigslist%";
```

1. SELECT * FROM moz_places -> Select everything in this table
2. WHERE -> an exception clause. We only grab everything fitting the following criteria
3. url LIKE "%craigslist%"; -> The URL contains the string "craigslist". Note the `%` . These are like wildcards and are needed.

The result is the set of URLs accessed that contain "craigslist". Among these, we can see the following line:

`http://baltimore.craigslist.org/search/sss?sort=rel&query=bitcoin|baltimore for sale "bitcoin" - craigslist|gro.tsilsgiarc.eromitlab.|1|0|0|6|100|1443892381725656|q4v23qBFq_il|0`

What follows the `query` in the URL?
#### Answer:
`bitcoin`

---
# Q2 - 10 Points
#### What was the current price of bitcoin when the user was browsing?

I do not know where to find this immediately, so let's do some work! Let's first determine which tables shown in `.tables`:

| Table Name      | Has Contents |
| --------------- | ------------ |
| anno_attributes | yes          |
| annos           | no           |
| bookmarks       | yes          |
| bookmarks_roots | yes          |
| favicons        | yes          |
| history_visits  | yes          |
| hosts           | yes          |
| inputhistory    | no           |
| items_annos     | yes          |
| keywords        | no           |
| places          | yes          |
Okay, Imma be so real. I just looked at every single table. I figured that the most probable table would be `places` and skimmed it. I found the following in the text:

```bash
craigslist: baltimore jobs, apartments, personals, for sale, services, community, and events
baltimore for sale "bitcoin" - craigslist

($239.5) Bitstamp - buy and sell bitcoins
Bitcoin Mining Hardware 3TH


Buy and Sell Bitcoin - Coinbase
Coinbase - Your Hosted Bitcoin Wallet

```
#### Answer:
`$239.5`

---
# Q3 - 10 Points
#### What Bitcoin exchange did the user log in to?

This sounds like something that can be found in the URL:

```bash
SELECT url FROM moz_places;
```

We get several lines here, but we can see the following:
`https://www.coinbase.com/accounts`
#### Answer:
`coinbase`

---
# Q4 - 15 Points
#### What is the email that was used to log into the exchange?

Here, I would like to use `grep`. However, grep is not available in the SQL interface. I exited the interface with `Ctrl + C` and used the following command:

```bash
sqlite3 browser.sqlite "SELECT * FROM moz_places;" | grep "@"
```

Notice how our SQL query is now in quotes. This is because we are not using the SQL interface. We get two lines of output, which contains our answer.
#### Answer:
`b1gbird@gmail.com`

---
# Q5 - 15 Points
#### What was the ID of the Bitcoin transaction that the user looked at?

I started this question with the assumption that we would be able to find the ID as part of a URL. I used the following command in the SQL interface:

```sql
SELECT url FROM moz_places;
```

This outputs several lines. After reading through them, you can get an idea of what the user was doing (craigslist -> coinbase login of sorts -> gmail -> coinbase login -> reddit ...)

I scrolled through until I found the lines:

```bash
290|https://blockchain.info/search/5274cfba585a4b5681527a37f95c76340428916bb7480cef6c545f0a28dcd2d7||ofni.niahckcolb.|1|1|0||100|1443893741538123|-j1Ds3wpzbga|0
291|http://blockchain.info/tx/5274cfba585a4b5681527a37f95c76340428916bb7480cef6c545f0a28dcd2d7||ofni.niahckcolb.|1|0|0||100|1443893741542257|03HGGdEFeu-n|0
292|https://blockchain.info/tx/5274cfba585a4b5681527a37f95c76340428916bb7480cef6c545f0a28dcd2d7|Bitcoin Transaction 5274cfba585a4b5681527a37f95c76340428916bb7480cef6c545f0a28dcd2d7|ofni.niah
```
#### Answer:
`5274cfba585a4b5681527a37f95c76340428916bb7480cef6c545f0a28dcd2d7`

---
# Q6 - 20 Points
#### What was the total BTC of all the inputs of the Bitcoin transaction?

Since we have the transaction ID above, we can find this information by pasting the transaction ID into a site like [this](https://www.blockchain.com/en/). Once we do, we must be careful to select the value *before* the fee, which is shown in advanced details.
#### Answer:
`0.22616302 BTC`

---
# Q7 - 20 Points
#### Which bitcoin address received the majority of the Bitcoin in the transaction?

This can also be seen in the previous site.
#### Answer:
`18z6bTFjxkXCmhfp8YBetR2wgmoVjXGJZz`

---
# Conclusion

This challenge is definitely harder than the typical CLI ninja moves. Just stay resilient.