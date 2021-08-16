# Happy of Sad

## Description
This is a curious case of cats holding secrets

## Solve 
Extracting the zip archive provides 2 folders with ~50 images in each.
```bash
unzip 06b6ebc4-612a-4fa8-8cfb-e98067b5bb00
...
```

We then aim to remove duplicate files in the directories
```bash
fdupes -rdN ./
# listing removed files
```
Completing a `binwalk` on the directory shows that sad has an embedded file in the image. We run `binwalk` again with the extract option on the sad directory
```bash
binwalk sad/* -e 

Scan Time:     2021-08-11 19:24:37
Target File:   /srv/datastore/workspace/ctfs/c2c-quals/happy_or_sad/sad/id16.JPG
MD5 Checksum:  03149a35903f5bcf4ae8f5ae8b24361f
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
65644         0x1006C         Zip archive data, at least v2.0 to extract, compressed size: 383, uncompressed size: 547, name: password.txt
66163         0x10273         End of Zip archive, footer length: 22


Scan Time:     2021-08-11 19:24:37
Target File:   /srv/datastore/workspace/ctfs/c2c-quals/happy_or_sad/sad/id47.JPG
MD5 Checksum:  35eb3e1bcd53ffd95c4989e2ca55a853
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
```

One of the files extracted was a password. Using that password we brute force steghide on the images in happy to get the flag.

```bash
for f in happy/*.jpg; do for x in $(cat ./sad/_id16.JPG.extracted/password.txt ); do steghide extract -sf ${f} -p ${x} -xf - 2>/dev/null | tee -a flat.out ; done ; done


PSUEDO FLAG
PSUEDO FLAG
..snip...
PSUEDO FLAG
FLAG{78b024dfe63b7078e91d049d204f0a57}
PSUEDO FLAG
PSUEDO FLAG
..snip...
```

## Flag
```
FLAG{78b024dfe63b7078e91d049d204f0a57}
```
