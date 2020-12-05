import os
import re

CUR_DIR_ABS_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_NAME = '05_input.txt'
INPUT_FILE_PATH = os.path.join(CUR_DIR_ABS_PATH, INPUT_FILE_NAME)
ROW_IDX = 7


def get_row(string):
    row_spec = line[:ROW_IDX]
    row_lower = 0
    row_upper = 127
    if re.search('^[(F|B)]{7}$', row_spec) is None:
        return None
    for i in range(ROW_IDX):
        if row_spec[i] == 'F':
            row_upper -= int(((row_upper-row_lower)/2)+0.5)
        else:
            row_lower += int(((row_upper-row_lower)/2)+0.5)
    return row_upper

def get_column(string):
    col_spec = line[ROW_IDX:]
    col_lower = 0
    col_upper = 7
    if re.search('^[(R|L)]{3}$', col_spec) is None:
        return None
    for i in range(3):
        if col_spec[i] == 'L':
            col_upper -= int(((col_upper-col_lower)/2)+0.5)
        else:
            col_lower += int(((col_upper-col_lower)/2)+0.5)
    return col_upper

def find_seat(seats):
    max_id = 0
    ids = [] 
    for s in seats:
        ids.append(int(s['id']))
        if s['id'] > max_id:
            max_id = s['id']
    ids = sorted(ids)

    for i in range(1, len(ids)):
        if ids[i+1] != (ids[i] + 1) and ids[i+1] == (ids[i] + 2):
            return ids[i] + 1

with open(INPUT_FILE_PATH, 'r') as file:
    data = []
    seats = []
    for line in file:
       data.append(line.strip()) 
    for line in data:
        if line:
            seat = {}
            row = get_row(line)
            col = get_column(line)
            if row is not None and col is not None:
                seat['row'] = row
                seat['col'] = col
                seat['id'] = row*8+col
            seats.append(seat)
    seat = find_seat(seats)
    print(seat)



