# Ghosts in the Website

## Description
deepnoobdev created his portfolio as a static website using a famous platform. Can you delve into its secrets?

## Solve
Searching archive.org (internet archive) shows up results for deepnoobdev

- `https://archive.org/index.php`
- `https://archive.org/search.php?query=deepnoobdev`
- `https://archive.org/details/bg_20210319`
- `https://ia801803.us.archive.org/30/items/bg_20210319/index.html`

The last item has a secret in it. Running it through rot13 you get the flag
```bash
echo SYNT{qps1o469s5nno296369sq8sp0978nr0s} | tr 'a-z' 'n-za-m' | tr 'A-Z' 'N-ZA-M'
```

## Flag
```
FLAG{dcf1b469f5aab296369fd8fc0978ae0f}
```
