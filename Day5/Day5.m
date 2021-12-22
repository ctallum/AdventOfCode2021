clc
clearvars

data = readmatrix('input.csv');

%% Part 1
field = zeros(990,990);

for row = 1:size(data,1)
    vals = data(row,:);
    vals = data(row,:);
    x1 = vals(:,1);
    y1 = vals(:,2);
    x2 = vals(:,3);
    y2 = vals(:,4);
    
    % horizontal lines
    if x1 == x2
        y1 = min(vals(:,2),vals(:,4));
        y2 = max(vals(:,2),vals(:,4));
        field(y1+1:y2+1,x1+1) = field(y1+1:y2+1,x1+1) + 1;
    % vertical lines
    elseif y1 == y2
        x1 = min(vals(:,1),vals(:,3));
        x2 = max(vals(:,1),vals(:,3));   
        field(y1+1,x1+1:x2+1) = field(y1+1,x1+1:x2+1) + 1;
    end
end

mask = field~=0;
field(mask) = field(mask) - 1;

pt1_answer = nnz(field)

%% Part 2
field = zeros(990,990);

for row = 1:size(data,1)
    vals = data(row,:);
    x1 = vals(:,1);
    y1 = vals(:,2);
    x2 = vals(:,3);
    y2 = vals(:,4);
    
    % horizontal lines
    if x1 == x2
        y1 = min(vals(:,2),vals(:,4));
        y2 = max(vals(:,2),vals(:,4));
        field(y1+1:y2+1,x1+1) = field(y1+1:y2+1,x1+1) + 1;
    % vertical lines
    elseif y1 == y2
        x1 = min(vals(:,1),vals(:,3));
        x2 = max(vals(:,1),vals(:,3));   
        field(y1+1,x1+1:x2+1) = field(y1+1,x1+1:x2+1) + 1;
    % pos diagonal lines
    elseif (y2-y1)/(x2-x1) > 0
        for i = 1:abs(x2-x1)+1
            field(min(y1,y2)+i,min(x1,x2)+i) = field(min(y1,y2)+i,min(x1,x2)+i) + 1;
        end
    % neg niagonal line
    elseif (y2-y1)/(x2-x1) < 0
        for i = 1:abs(x2-x1)+1
            field(max(y1,y2)-i+2,min(x1,x2)+i) = field(max(y1,y2)-i+2,min(x1,x2)+i) + 1;
        end
    end
end

% mask to find all digits above 2
mask = field~=0;
field(mask) = field(mask) - 1;

% find all non zero elements
pt2_answer = nnz(field)