data = readtable('input.csv');

commands = table2array(data(:,1));
distances = table2array(data(:,2));

%% Part 1
position = 0;
depth = 0;

for i = 1:length(commands)
    new_command = commands{i};
    new_dist = distances(i);
    
    if strcmp(new_command,'down')
        depth = depth + new_dist;
    end
    if strcmp(new_command,'up')
        depth = depth - new_dist;
    end
    if strcmp(new_command,'forward')
        position = position + new_dist;
    end
end

depth*position

%% Part 2

position = 0;
depth = 0;
aim = 0;

for i = 1:length(commands)
    new_command = commands{i};
    X = distances(i);
    
    if strcmp(new_command,'down')
        aim = aim + X;
    end
    
    if strcmp(new_command,'up')
        aim = aim - X;
    end
    
    if strcmp(new_command,'forward')
        position = position + X;
        depth = depth + (aim*X);
    end
end

answer = depth*position