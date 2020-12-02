import os

CUR_DIR_ABS_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_NAME = 'passwords.txt'
INPUT_FILE_PATH = os.path.join(CUR_DIR_ABS_PATH, INPUT_FILE_NAME) 

print(INPUT_FILE_PATH)

with open(INPUT_FILE_PATH, 'r') as password_file:
    invalid_passwords = 0
    for line in password_file:
        space_split = line.split(' ')
        min, max = space_split[0].split('-')
        min = int(min)
        max = int(max)

        letter = space_split[1].replace(':', '')
        occurrence_of_letter = space_split[2].count(letter)

        if (occurrence_of_letter > max) or (occurrence_of_letter < min):
            invalid_passwords += 1
            print(line)

    password_file.close()
    print(invalid_passwords)
