# Part 1

moves = open("input", "r").readlines()

results = {
    "X": { # Rock
        "A": 1 + 3, # Rock
        "B": 1 + 0, # Paper
        "C": 1 + 6, # Scissors
    },
    "Y": { # Paper
        "A": 2 + 6, # Rock
        "B": 2 + 3, # Paper
        "C": 2 + 0, # Scissors
    },
    "Z": { # Scissors
        "A": 3 + 0, # Rock
        "B": 3 + 6, # Paper
        "C": 3 + 3, # Scissors
    }
}

score = 0
for move in moves:
    parts = move.strip().split(" ")
    theirs = parts[0]
    mine = parts[1]
    score += results[mine][theirs]

print(score)

# Part 2

moves = open("input", "r").readlines()

results = {
    "A": { # Rock
        "X": 0 + 3, # lose
        "Y": 3 + 1, # draw
        "Z": 6 + 2, # win
    },
    "B": { # Paper
        "X": 0 + 1, # lose
        "Y": 3 + 2, # draw
        "Z": 6 + 3, # win
    },
    "C": { # Scissors
        "X": 0 + 2, # lose
        "Y": 3 + 3, # draw
        "Z": 6 + 1, # win
    },
}

score = 0
for move in moves:
    parts = move.strip().split(" ")
    theirs = parts[0]
    mine = parts[1]
    score += results[theirs][mine]

print(score)