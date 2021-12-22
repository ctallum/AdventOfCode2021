data = readmatrix('input.csv');
%% Part 1

count = 0;
length(data)

for i = 2:length(data)
    previous = data(i-1);
    current = data(i);
    if current > previous
        count = count + 1;
    end
end
count

%% part 2

count = 0;
length(data);

for i = 4:length(data)
    previous = mean([data(i-1), data(i-2), data(i-3)]);
    current = mean([data(i), data(i-1), data(i-2)]);
    if current > previous
        count = count + 1;
    end
end
count