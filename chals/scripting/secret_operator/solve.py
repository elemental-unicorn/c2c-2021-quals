
x = 0
s = ""
while True:
    x+=1
    s += str(x)
    if len(s) >= 190:
        print(f'flag{{{x}}}')
        break
    

