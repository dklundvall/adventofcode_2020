import os

CUR_DIR_ABS_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_NAME = '03_input.txt'
INPUT_FILE_PATH = os.path.join(CUR_DIR_ABS_PATH, INPUT_FILE_NAME) 
SLOPES = [(1,1), (1,3), (1,5), (1,7), (2,1)]

def find_trees(row_step, col_step, map):
    width = len(map[0]) - 1
    height = len(map)
    row = 0
    col = 0
    trees = 0

    while row + 1 < height:
        col += col_step
        row += row_step
        if map[row][col%width] == '#':
            trees += 1
    return trees

if __name__ == '__main__':    
    with open(INPUT_FILE_PATH, 'r') as input_file:
        map = []
        for line in input_file:
            map.append(line)
        input_file.close()
    answer = 1
    for slope in SLOPES:
        answer *= find_trees(*slope, map)
    print(answer)
