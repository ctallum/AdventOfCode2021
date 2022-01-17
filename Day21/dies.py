from typing import List, Dict
import itertools
from collections import defaultdict


class DeterministicDie():
    def __init__(self):
        self.value = 0
        self.times_rolled = 0

    def single_roll(self) -> int:
        self.times_rolled += 1
        self.value += 1
        if self.value == 101:
            self.value = 1
        return self.value

    def get_roll(self) -> Dict[int, int]:
        roll_sum = 0
        for _ in range(3):
            roll_sum += self.single_roll()
        return {roll_sum: 1}


class QuantumDie():
    def __init__(self):
        pass

    @staticmethod
    def get_roll() -> Dict[int, int]:
        '''
        Return a dictionary that contains all the possible roll sums and how many of of
        those possible rolls are possible.
        '''
        possible_roll_count = defaultdict(int)

        for roll in itertools.product(range(1, 4), repeat=3):
            die_options = [int(a) for a in roll]
            possible_roll_count[(sum(die_options))] += 1

        return possible_roll_count
