data = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().replace(" | ", " ").split(" ")
        line = [set(section) for section in line]
        data.append(line)

answer = 0
for signal in data:
    
    solve_list = [0 for i in range(14)]

    for idx,unknown_bit in enumerate(signal):
        if len(unknown_bit) == 2:
            solve_list[idx] = "1"
            one_digit = unknown_bit
        if len(unknown_bit) == 4:
            solve_list[idx] = "4"
            four_digit = unknown_bit
        if len(unknown_bit) == 3:
            solve_list[idx] = "7"
        if len(unknown_bit) == 7:
            solve_list[idx] = "8"
    
    for idx,unknown_digit in enumerate(signal):
        if len(unknown_digit) == 5:
            if len(unknown_digit.intersection(one_digit)) == 2:
                solve_list[idx] = "3"
            elif len(unknown_digit.intersection(four_digit)) == 3:
                solve_list[idx] = "5"
            else:
                solve_list[idx] = "2"
        if len(unknown_digit) == 6:
            if len(unknown_digit.intersection(one_digit)) == 1:
                solve_list[idx] = "6"
            elif len(unknown_digit.intersection(four_digit)) == 4:
                solve_list[idx] = "9"
            else:
                solve_list[idx] = "0"

    output_digit = int("".join(solve_list[9:13]))

    answer += output_digit

print(answer)