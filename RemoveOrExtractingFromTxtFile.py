with open('data/new_file.txt', "r") as f:
    lines = f.readlines()
with open('data/new_file.txt', "w") as f:
    for line in lines:
        # Extract words have upper and lower cases
        mixed_case = not line.islower() and not line.isupper()
        # Remove newline characters from the txt file.
        remove_newLine = line.rsplit('\n')
        # replace ' ' space with ',' comma
        replace_element = line.replace(' ', ',')
        if not mixed_case:
            f.write(line)
        else:
            print(line)