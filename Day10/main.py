# import data

with open('input.txt') as f:
    data = f.readlines()
    for idx,line in enumerate(data):
        data[idx] = list(line.strip())
    

def clean_list(char_list: list) -> list:
    temp_list = char_list
    pair = {'(':')','[':']','{':'}','<':'>'}
    start_chars = ['(','[','{','<']
    done = False
    while not done:
        done = True
        for idx,char in enumerate(temp_list):
            if idx == len(temp_list)-1:
                break
            else:
                if char in start_chars and pair[char] == temp_list[idx+1]:
                    done = False
                    del temp_list[idx:idx+2]
    return temp_list

def part1(data):
    score = 0
    end_chars = [')',']','}','>']
    point_value = {')': 3,']': 57,'}': 1197,'>': 25137}
    for line in data:
        for char in clean_list(line):
            if char in end_chars:
                score += point_value[char]
                break
    return score

def part2(data):
    # find all incomplete lines
    incompletes = []
    end_chars = set([')',']','}','>'])
    for line in data:
        set_line = set(clean_list(line))
        if not set_line.intersection(end_chars):
            incompletes.append(line)
    
    # complete all incomplete lines
    completions = []
    pair = {'(':')','[':']','{':'}','<':'>'}
    for line in incompletes:
        completion_line = []
        for char in reversed(line):
            completion_line.append(pair[char])
        completions.append(completion_line)
    
    # score all incomplete lines
    all_scores = []
    point_value = {')': 1,']': 2,'}': 3,'>': 4}
    for line in completions:
        score = 0
        for char in line:
            score *= 5
            score += point_value[char]
        all_scores.append(score)

    # find middle of sorted scores
    all_scores = sorted(all_scores)    
    middle_index = int((len(all_scores) - 1)/2)
    return(all_scores[middle_index])

print(f'Solution to Part1: {part1(data)}')
print(f'Solution to Part1: {part2(data)}')



