def parse_input():
    with open('input/2.txt', 'r') as f:
        raw = f.read().split('\n')[:-1]
    splitter = lambda x: x.split(' ')
    return list(map(splitter, raw))

def win_points(opp, you):
    # Win
    wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    if wins[opp] == you:
        return 6
    # Tie
    if ord(you) - ord('X') == ord(opp) - ord('A'):
        return 3
    # Lose
    return 0

def play_points(you):
    return 1 + ord(you) - ord('X')

def get_score(opps, yous):
    return sum([win_points(opp, you) + play_points(you) for opp, you in zip(opps, yous)])

def part1():
    rounds = parse_input()
    opps = [round[0] for round in rounds]
    yous = [round[1] for round in rounds]
    return get_score(opps, yous)

def part2():
    rounds = parse_input()
    opps = [round[0] for round in rounds]
    outcomes = [round[1] for round in rounds]
    wins = {chr(start + ord('A')): chr((start + 1) % 3 + ord('X')) for start in range(3)}
    ties = {chr(start + ord('A')): chr(start % 3 + ord('X')) for start in range(3)}
    loses = {chr(start + ord('A')): chr((start - 1) % 3 + ord('X')) for start in range(3)}
    yous = []
    for opp, outcome in zip(opps, outcomes):
        if outcome == 'X':
            yous.append(loses[opp])
        elif outcome == 'Y':
            yous.append(ties[opp])
        else:
            yous.append(wins[opp])
    return get_score(opps, yous)

print(part1())
print(part2())
