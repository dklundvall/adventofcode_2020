import os

CUR_DIR_ABS_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_NAME = 'passwords.txt'
INPUT_FILE_PATH = os.path.join(CUR_DIR_ABS_PATH, INPUT_FILE_NAME) 

print(INPUT_FILE_PATH)

with open(INPUT_FILE_PATH, 'r') as password_file:
    valid_passwords = 0
    for line in password_file:
        space_split = line.split(' ')
        idx1, idx2 = space_split[0].split('-')
        idx1 = int(idx1)
        idx2 = int(idx2)
        password = space_split[2]

        letter = space_split[1].replace(':', '')
        occurrence_of_letter = password.count(letter)

        if ((password[idx1 - 1] == letter) and (password[idx2 - 1] != letter)) or \
            ((password[idx1 - 1] != letter) and (password[idx2 - 1] == letter)):
            valid_passwords += 1
            print(password[idx1 - 1], password[idx2 - 1])
            print(line)

    password_file.close()
    print(valid_passwords)

