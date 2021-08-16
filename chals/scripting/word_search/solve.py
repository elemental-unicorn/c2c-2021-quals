
from pwn import *
import sys 

# get noise 
c = remote("word-search.ctf.fifthdoma.in",4243)
c.recvline()

# get words 
l = ""
words = []
ws = {}
while True:
    l = c.recvline().decode().rstrip()
    if l[0] == " ":
        break
    words.append(l)
    ws[l]={}
    ws[l]['start']=[0,0]
    ws[l]['end']=[0,0]
print(ws)

# get grid
grid = []
for x in range(15):
    grid.append( c.recvline().decode().rstrip().split()[1:] )

puzzle = '\n'.join([''.join(l) for l in grid] )
solutions = words
print(puzzle)

# Just formats the puzzle into a more computer-readable text
wordgrid = puzzle.replace(' ','')

# Computers start counting at zero, so...
length = wordgrid.index('\n')+1


characters = [(letter, divmod(index, length))
            for  index, letter in enumerate (wordgrid)]

wordlines = {}
# These next lines just  directions so you can tell which direction the word is going
directions = {'going downwards':0, 'going downwards and left diagonally':-1, 'going downwards and right diagonally':1}

for word_direction, directions in directions.items():
    wordlines[word_direction] = []
    for x in range(length):
        for i in range(x, len(characters), length + directions):
            wordlines[word_direction].append(characters[i])
        wordlines[word_direction].append('\n')

# Nice neat way of doing reversed directions.
wordlines['going right'] = characters
wordlines['going left'] = [i for i in reversed(characters)]
wordlines['going upwards'] = [i for i in reversed(wordlines['going downwards'])]
wordlines['going upwards and left diagonally'] = [i for i in reversed(wordlines['going downwards and right diagonally'])]
wordlines['going upwards and right diagonally'] = [i for i in reversed(wordlines['going downwards and left diagonally'])]

#print( c.recvline() )
def printitout(direction, tuple, lines):
    ww = words
    print("Keep in mind, rows are horizontal and columns are vertical.\n")
    for direction, tuple in lines.items():
        string = ''.join([i[0] for i in tuple])
        for word in solutions:
            #print(word)
            if word in string:
                coordinates = tuple[string.index(word)][1]
                #print( word, 'is at row', coordinates[0], 'and column', coordinates[1], direction + ".")
                end = getEnd(coordinates[0], coordinates[1], direction,len(word)-1) 
                #print( coordinates[0], coordinates[1], " -> ", end[0], end[1] )
                ws[word]['start']=[ coordinates[0], coordinates[1] ]
                ws[word]['end']=[end[0],end[1]]

def getEnd(x,y,d,l):
    if d == 'going right':
        return x, y+l
    elif d == 'going left':
        return x, y-l
    elif d == 'going upwards':
        return x-l,y
    elif d == 'going downwards':
        return x+l,y
    elif d == 'going upwards and left diagonally':
        return x-l,y-l
    elif d == 'going upwards and right diagonally':
        return x-l,y+l
    elif d == 'going downwards and left diagonally':
        return x+l,y-l
    elif d == 'going downwards and right diagonally':
        return x+l,y+l
    else:
        return 0,0

printitout(word_direction, tuple, wordlines)

def rec(n=False):
    if n:
        return c.recvline().decode().rstrip()
    return c.recvline().decode()

def checkFlag(f):
    if f[:5] == 'FLAG{':
        print(f)
        return True

for x in range(len(words)+1):
    while True:
        t = rec(n=True)
        if checkFlag(t):
            sys.exit()
            break
        #print(t)
        if t[:6] == 'Input ':
            break
    start = "{}\n".format( ', '.join( [ str(i) for i in ws[words[x]]['start'] ]) )
    end = "{}\n".format( ', '.join( [ str(i) for i in ws[words[x]]['end'] ]) )
    print("Word: %s | Start: %s | End: %s" % (words[x],start.rstrip(),end.rstrip()) )
    c.send( start.encode() ) 
    rec()
    #print('End: ', end)
    c.send( end.encode() )
    #c.send(', '.join( ws[words[x]]['end']).encode() + b'\n')
    lastLine = rec(n=True)
    print("Response:",lastLine)
    time.sleep(0.2)




          



