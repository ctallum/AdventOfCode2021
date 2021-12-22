clc
clearvars
data = readmatrix("input.csv");
new_data = zeros(length(data),12);

for i = 1:length(data)
    convert_array = str2double(regexp(num2str(data(i)),'\d','match'));
    new_data(i,end-length(convert_array)+1:end) = convert_array;
end

data = new_data

%% Part 1

gamma = zeros(1,12);
epsilon = zeros(1,12);

for col = 1:12
    avg_val = mean(data(:,col));
    if avg_val > .5
        gamma(col) = 1;
        epsilon(col) = 0;
    end
    if avg_val < .5
        gamma(col) = 0;
        epsilon(col) = 1;
    end
end
gamma = array2number(gamma);
epsilon = array2number(epsilon);
gamma*epsilon

%% Part 2
oxygen_array = data;
co2_array = data;

for row = 1:12
    if size(oxygen_array,1) > 1
        avg_val = mean(oxygen_array(:,row));
        if avg_val < .5
            oxygen_array = oxygen_array(oxygen_array(:,row) == 0,:);
        
        else
            oxygen_array = oxygen_array(oxygen_array(:,row) == 1,:);
        end
    end
end

for row = 1:12
    if size(co2_array,1) > 1
        avg_val = mean(co2_array(:,row));
        if avg_val < .5
            co2_array = co2_array(co2_array(:,row) == 1,:);
        
        else
            co2_array = co2_array(co2_array(:,row) == 0,:);
        end
    end
end

oxygen_rating = array2number(oxygen_array);
co2_rating = array2number(co2_array);
oxygen_rating*co2_rating
%% Functions
function num = array2number(array)
    num = 0;
    for i = 1:length(array)
        num = num + array(13-i)*2^(i-1);
    end
end