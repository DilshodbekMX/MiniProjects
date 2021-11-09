f_l = []
with open("data/dont_touch.txt", 'r') as f:
    for line in f.readlines():
        f_l.append(line)
with open("data/SortedFile", "w") as g:
    for line in sorted(f_l):
        g.write(line)