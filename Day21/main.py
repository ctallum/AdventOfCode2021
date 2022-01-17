from game import *
from dies import *

with open('input.txt') as f:
    data = [int(a.strip()[-1]) for a in f.readlines()]

p1_spot = data[0]
p2_spot = data[1]

# part 1
die = DeterministicDie()
game = Game(p1_start=p1_spot, p2_start=p2_spot, end_condition=1000, die=die)

while not game.game_over:
    game.step()

winning_state = list(game.winning_states.keys())[0]

die_rolls = die.times_rolled
losing_score = min(winning_state[2], winning_state[3])

p1_answer = die_rolls * losing_score

print(f'(Solution to part 1: {p1_answer}')


# part 2
die = QuantumDie()
game = Game(p1_start=p1_spot, p2_start=p2_spot, end_condition=21, die=die)

while not game.game_over:
    game.step()

winning_states = game.winning_states

p1_wins = 0
p2_wins = 0

for state, count in winning_states.items():
    if state[2] > state[3]:
        p1_wins += count
    elif state[3] > state[2]:
        p2_wins += count


print(f'Solution to part 2: {max(p1_wins, p2_wins)}')
