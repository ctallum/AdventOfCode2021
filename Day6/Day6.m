data = readmatrix('input.csv');
states = zeros(1,9);

[GC,GR] = groupcounts(data');
states(GR + 1) = GC;

for day = 1:256
    new_fish = states(1);
    states(1:8) = states(2:9);
    states(9) = new_fish;
    states(7) = states(7) + new_fish;
end

answer = sum(states)