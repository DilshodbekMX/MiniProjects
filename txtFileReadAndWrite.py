# Txt file read
with open("data/dont_touch.txt", 'r') as txt_file:
    lines = txt_file.readlines()
# Append every line o the list called file_list
    file_list = [line for line in lines]
# Txt file create and write the data in file_list
with open("data/new_file.txt", 'w') as new_file:
    for line in file_list:
        new_file.write(line)
