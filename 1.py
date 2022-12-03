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
print(m)

# second part

f = open("input", "r")
ls = f.readlines()
c = 0
m = []
for l in ls:
    if l.strip() == "":
         m.append(c)
         c = 0
         continue
    c += int(l.strip())
print(sum(sorted(m, reverse=True)[:3]))
