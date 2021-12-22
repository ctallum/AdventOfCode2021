% Setup
clc,
clearvars
data = readmatrix('input.csv');
%% Part 1

goal = data(1)*ones(size(data));
dif = goal - data;
goal = goal - median(dif);
dif = goal - data;

answer1 = sum(abs(dif))
%% Part 2

min_val = min(data);
max_val = max(data);

results = zeros(size(data));

f = @(x) abs(x).*(abs(x)+1)/2;

for i = min_val:max_val
    dif = f(i*ones(size(data)) - data);
    results(i+1) = sum(abs(dif));
end

answer2 = min(results)