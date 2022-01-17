import numpy as np
from typing import Dict, Tuple
from collections import defaultdict
  

class Game():
    def __init__(self, p1_start: int, p2_start: int, end_condition: int, die) -> None:
        self.p1_start = p1_start - 1
        self.p2_start = p2_start - 1
        self.current_player = 1
        self.end_condition = end_condition   
        self.game_over = False
        self.die = die

        self.active_states = defaultdict(int)
        self.active_states[(self.p1_start,self.p2_start,0,0)] += 1
        self.winning_states = defaultdict(int)


    def step(self) -> None:
        self.update_all()
        self.flip()

    def update_all(self) -> None:
        is_done = True
        new_active_states = defaultdict(int)

        for location, count in self.active_states.items():
            if location[2] >= self.end_condition or location[3] >= self.end_condition:
                self.winning_states[location] += count
                continue
            else:    
                is_done = False                
                new_active_states = self.update_individual(location, count, new_active_states)     
                           
        self.game_over = is_done
        self.active_states = new_active_states


    def update_individual(self, loc: Tuple[int], count: int, new_state: dict) -> dict:
        for moves_forward, mult_factor in self.die.get_roll().items():
            if self.current_player == 1:
                new_position = (loc[0] + moves_forward)%10
                new_score = loc[2] + new_position + 1
                new_state[new_position, loc[1], new_score, loc[3]] += count * mult_factor
                
            elif self.current_player == 2:
                new_position = (loc[1] + moves_forward)%10
                new_score = loc[3] + new_position + 1
                new_state[loc[0], new_position, loc[2], new_score] += count * mult_factor
        
        return new_state

    def flip(self):
        if self.current_player == 1: self.current_player = 2
        elif self.current_player == 2: self.current_player = 1
