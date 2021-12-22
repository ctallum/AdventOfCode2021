clc
clearvars

data = readmatrix('input.csv');
fold_order = [1 0 1 0 1 0 1 0 1 0 0 0];
folds = [655 447 327 223 163 111 81 55 40 27 13 6];

max_x = max(data(:,1))+1;
max_y = max(data(:,2))+1;

paper = zeros(max_y,max_x);

for row = 1:length(data)
    x = data(row,1);
    y = data(row,2);
    paper(y+1,x+1) = 1;
end

for i = 1:length(fold_order)
    fold = folds(i);
    if fold_order(i) == 0
        fold_side = paper(fold+1:end,:);
        fold_side = flip(fold_side);
        paper(fold-size(fold_side,1)+2:fold+1,:) = paper(fold-size(fold_side,1)+2:fold+1,:) + fold_side;
        paper = paper(1:fold,:);
    end
    if fold_order(i) == 1
        fold_side = paper(:,fold+1:end);
        fold_side = flip(fold_side,2);
        paper(:,fold-size(fold_side,2)+2:fold+1) = paper(:,fold-size(fold_side,2)+2:fold+1) + fold_side;
        paper = paper(:,1:fold);
    end
end

code = ~(paper > 0);

imshow(code)