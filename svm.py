import os
import sys

__author__ = 'Frank'


def convert_training_data(file_name):
    original_data = open(file_name, 'r')

    all_the_lines = ''
    output_line = ''
    for line in original_data:
        words = line.split(' ', 1)
        first_word = words[0]
        if first_word == '+1':
            output_line = line
        elif first_word == '-1':
            output_line = line
        elif int(first_word) >= 7:
            output_line = '+1 ' + words[1]
        elif int(first_word) <= 4:
            output_line = '-1 ' + words[1]
        else:
            print('the first word is something else')

        all_the_lines += output_line

    output_file = open(file_name + '.svm.model', 'w')
    output_file.write(all_the_lines)

    return


def convert_test_data(file_name):
    original_data = open(file_name, 'r')

    output_line = ''
    all_the_lines = ''
    for line in original_data:
        all_the_lines += '+1 ' + line

    file_to_write = open(file_name + 'svm.intermediate', 'w')
    file_to_write.write(all_the_lines)

    return


def main():
    print('SVM-Light toolkit')
    print('1 TRAININGFILE - convert training data to svm format')
    print('2 TESTFILE - convert test data to svm format')
    if len(sys.argv) == 3:
        if sys.argv[1] == '1':
            convert_training_data(sys.argv[2])
        elif sys.argv[1] == '2':
            convert_test_data(sys.argv[2])
    return


main()
