# Trapdoor

## Description
What is the local infected computer's domain name where the backdoor call to the C2 is fivu4vjamve5vfrt5uwsruf0212eu1.appsync-api.us-west-2.avsvmcloud.com

Flag will be in the format FLAG{domain.name}


## Solve 
Using a github publically hosted script `https://github.com/RedDrip7/SunBurst_DGA_Decode/raw/main/decode.py`
```bash
echo fivu4vjamve5vfrt5uwsruf0212eu1 | python2 decode.py                                                      1 ⨯
fivu4vjamve5vfrt5uwsruf0212eu1,favreau.local
```

## Flag 
```
flag{favreau.local}
``` 
