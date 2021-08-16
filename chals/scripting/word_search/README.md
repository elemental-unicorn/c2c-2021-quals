# Word Search

## Description
How quickly can you do a wordsearch?

```bash
nc word-search.ctf.fifthdoma.in 4243
```

## Solve
### Version 1 - Actually solving the puzzle
This challenge was solved by using some code from `https://github.com/robbiebarrat/word-search/blob/master/wordsearch.py` and modifying it to find the word end locations based on length of the word and direction of find. 

```bash
python3 solve.py
```

### Version 2 - Pure bruteforce the grid 
Thanks to `ZylonAU` for this method solve
```bash
python3 solve_2.py
```

## Flag
```
FLAG{fastest_word_finder_in_the_west}
```
