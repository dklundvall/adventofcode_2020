import os

CUR_DIR_ABS_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_NAME = 'puzzle_input.txt'
INPUT_FILE_PATH = os.path.join(CUR_DIR_ABS_PATH, INPUT_FILE_NAME) 

'''
Finds and returns the numbers creating a specified sum,
from a list of integers.
'''
def find_numbers_of_sum(sum, list):
    # See if sum of any two numbers in the list is 2020 
    for idx1, num1 in enumerate(list):
        for idx2, num2 in enumerate(list):
            if idx1 == idx2:
                break
            for idx3, num3 in enumerate(list):
                if idx1 == idx2 or idx1 == idx3:
                    break
                elif (num1 + num2 + num3) == sum:
                    return num1, num2, num3
                    
if __name__ == '__main__':
    # Populate list with lines from file
    with open(INPUT_FILE_PATH, 'r') as input_file:
        input_list = []
        for idx, line in enumerate(input_file):
            input_list.append(int(line))
        input_file.close()

        num1, num2, num3 = find_numbers_of_sum(2020, input_list)
        product = (num1*num2*num3)
        print('%d * %d * %d = %d' % (num1, num2, num3, product))

