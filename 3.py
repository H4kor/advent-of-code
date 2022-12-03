#part 1

rs = open("input", "r").readlines()

score = 0
for r in rs:
    s = len(r)
    c1 = set(r[:s//2])
    c2 = set(r[s//2:])
    conflict = c1.intersection(c2)
    conflict = list(conflict)[0]
    if ord(conflict) < 97:
        score += ord(conflict) - ord('A') + 27
    else:
        score += ord(conflict) - ord('a') + 1

print(score)

# part 2

rs = open("input", "r").readlines()

score = 0
for i in range(0, len(rs), 3):
    r1 = set(rs[i].strip())
    r2 = set(rs[i+1].strip())
    r3 = set(rs[i+2].strip())
    badge = r1.intersection(r2).intersection(r3)
    badge = list(badge)[0]
    if ord(badge) < 97:
        score += ord(badge) - ord('A') + 27
    else:
        score += ord(badge) - ord('a') + 1

print(score)