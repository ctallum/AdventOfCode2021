import ast
import math
import copy

class Number():
    def __init__(self, value: list) -> None:
        self.value = value
        self.value = self.reduce()
        self.magnitude = self.eval()

    def reduce(self) -> list:
        while True:
            old_explode_value = copy.deepcopy(self.value)
            self.explode()
            if old_explode_value == self.value:
                old_split_value = copy.deepcopy(self.value)
                self.split()
                if old_split_value == self.value:
                    return self.value
                self.reduce()
    
    def eval(self) -> int:
        return self.recursively_eval(self.value)
    
    @classmethod
    def recursively_eval(cls,fish_num: list) -> int:
        weight = [3, 2]
        count = 0
        for idx,num in enumerate(fish_num):
            if isinstance(num,list):
                count += weight[idx] * cls.recursively_eval(num)
            else:
                count += weight[idx] * num
        return count
        
    def explode(self):
        fish_num = str(self.value)
        fish_num = fish_num.replace('[','[#').replace(',','#,#').replace(']','#]').replace('# ','#').split('#')
        open_bracket_count = 0
        for idx,char in enumerate(fish_num):
            if char == "[":
                open_bracket_count += 1
            if char == "]":
                open_bracket_count -= 1
            if open_bracket_count == 5:
                left_num = fish_num[idx + 1]
                right_num = fish_num[idx+3]
                for left_idx, char in enumerate(fish_num[idx::-1]):
                    if char.isnumeric():
                        first_left = fish_num[idx - left_idx]
                        fish_num[idx - left_idx] = str(int(first_left) + int(left_num))
                        break
                for right_idx,char in enumerate(fish_num[idx + 4:]):
                    if char.isnumeric():
                        first_right = fish_num[idx + 4 + right_idx]
                        fish_num[idx + 4 + right_idx] = str(int(first_right) + int(right_num))
                        break
                fish_num[idx:idx+5] = ['0']
                break
        self.value = ast.literal_eval(''.join(fish_num))

    def split(self) -> None:
        self.value, _ = self.recursively_split(self.value)

    @classmethod
    def recursively_split(cls,fish_num: list) -> list:
        done = False
        for idx, num in enumerate(fish_num):
            if isinstance(num,list):
                fish_num[idx], done = cls.recursively_split(num)
                if done: break
            else:
                if num > 9:
                    fish_num[idx] = [math.floor(num/2),math.ceil(num/2)]
                    return fish_num, True
        return fish_num, done
