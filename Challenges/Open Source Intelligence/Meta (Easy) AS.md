# Image Metadata Extraction Walkthrough
This walkthrough demonstrates how to extract metadata from an image using `exiftool`. Metadata includes useful information such as when the image was created, camera details, exposure settings, dimensions, and GPS coordinates. Each question below corresponds to a specific piece of metadata we can extract.

The image for this challenge is located in /Images/Open Source Intelligence/Meta.jpg
# Q1 - 10 points
#### When was the image created? Round down to the nearest minute.

Run the following command:

```bash
exiftool Meta.jpg
```

In the output, locate the `Create Date` field:

```bash
Create Date                     : 2015:05:15 02:14:22
```

Note: This is different from the file modification date, which can change if the file is copied or edited. `Create Date` represents when the photo was originally captured.
#### Answer:
`2015-05-15 02:14`

# Q2 - 10 Points

#### What are the dimensions of the image? (ex: 800x600)

Look for `Image Width` and `Image Height` in the output:

```bash
Image Width                     : 1024
Image Height                    : 768
```

Combine them as `Width x Height`.
#### Answer:
`1024x768`

# Q3 - 10 Points

#### What is the make of the camera that took that picture?

Check the `Make` field:

```bash
Make                            : Apple
```

#### Answer:
`Apple`

# Q4 - 10 Points

#### What is the model of the camera that took the picture?

Check the `Camera Model Name` field:

```bash
Camera Model Name               : Apple iPhone 5
```

#### Answer:
`Apple iPhone 5`

# Q5 - 10 Points

#### What is the exposure time for the picture? (ex: 1/200)

Check the `Exposure Time` field:

```bash
Exposure Time                   : 1/640
```

#### Answer:
`1/640`
# Q6 - 20 Points

#### What are the GPS coordinates where was the picture taken? (Any standard format is acceptable)

Locate the `GPS Position` field:

```bash
GPS Position                    : 39 deg 52' 30.00" N, 20 deg 0' 36.00" E
```

#### Answer
`39 deg 52' 30.00" N, 20 deg 0' 36.00" E`

---
# Conclusion

This is an easy starting challenge. Moving forward, having access to a Linux terminal is most likely necessary. A dedicated machine is nice, but a VM will do. In this challenge, we used `exiftool`, a tool used to view metadata in images.