# done directly in REPL
f = open("input", "r")
ls = f.readlines()
m = 0
c = 0
for l in ls:
    if l.strip() == "":
          m = max(m, c)
          c = 0
          continue
    c += int(l.strip())
