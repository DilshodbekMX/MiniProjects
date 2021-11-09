# First and main txt file
with open("data/dont_touch.txt", 'r') as f:
    all_words = [ line for line in f.readlines()]
print(len(all_words))
# Second txt file for comparing to the first for getting unique words from the first
with open('data/new.txt', "r") as f:
    comparing_words = [line for line in f.readlines()]
# unique.txt file for collecting unique words
f = open('unique.txt', 'a')
# same.txt file for collecting the same words
ff = open('same.txt', 'a')

for i in all_words:
    if i not in comparing_words:
        f.write(i)
        print(f'{i} is unique word')
    else:
        ff.write(i)
        print(f'{i} is same word')