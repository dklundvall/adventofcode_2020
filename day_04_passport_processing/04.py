import os
import re

CUR_DIR_ABS_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_NAME = '04_input.txt'
INPUT_FILE_PATH = os.path.join(CUR_DIR_ABS_PATH, INPUT_FILE_NAME)

REQUIRED_KEYS = {'byr': lambda x: 1920 <= int(x) <= 2002, 
                 'iyr': lambda x: 2010 <= int(x) <= 2020, 
                 'eyr': lambda x: 2020 <= int(x) <= 2030, 
                 'hgt': lambda x: check_height(str(x)), 
                 'hcl': lambda x: re.search('^#[0-9a-fA-F]{6}$', x) != None, 
                 'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 
                 'pid': lambda x: re.search('^[0-9]{9}$', x) != None
                }

def check_height(height):
    if(re.search('^([0-9]+(cm|in))$', height) is None):
        return False
    strlen = len(height)
    num = height[:strlen-2]
    if height[strlen-2:] == 'cm':
        return 150 <= int(num) <=193
    return 59 <= int(num) <= 76

def find_valid_passports(passport_data):
    valid_passports = 0
    passport = {}

    for line in passport_data:
        line = line.strip()

        ''' Finished parsing passport? '''
        if not line: 
            valid = True
            for key in REQUIRED_KEYS:
                if key not in passport or not REQUIRED_KEYS[key](passport[key]):
                    valid = False
            if valid:
                valid_passports += 1
            passport = {}
        else:
            fields = line.split(' ')
            for field in fields:
                key, value = field.split(':')
                passport[key] = value 
    
    return valid_passports
        
if __name__ == '__main__':
    with open(INPUT_FILE_PATH, 'r') as file:
        data = []
        for line in file:
            data.append(line)
        file.close()

    ans = find_valid_passports(data)
    print(ans)
    