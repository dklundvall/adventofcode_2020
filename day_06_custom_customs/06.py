'''
Uses Python set() intersection function, to get the
intersection of a groups answer
'''

import os
import re

CUR_DIR_ABS_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_NAME = '06_input.txt'
INPUT_FILE_PATH = os.path.join(CUR_DIR_ABS_PATH, INPUT_FILE_NAME)

with open(INPUT_FILE_PATH, 'r') as file:
    ans = 0
    g_intersect = set()
    line_ans = set()
    group_idx = 0
    ''' Loop through all the lines in the file '''
    for line in file:
        line = line.strip()

        ''' New group '''
        if not line:
            ans += len(g_intersect)
            line_ans.clear()
            group_idx = 0
        else:
            for letter in line:
                line_ans.add(letter)
            if group_idx == 0:
                g_intersect = line_ans.copy()
            else:
                g_intersect = g_intersect.intersection(line_ans)
            group_idx += 1
            line_ans.clear()
    file.close()
    print(ans)
