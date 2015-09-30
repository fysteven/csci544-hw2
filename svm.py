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
        elif first_word == 'SPAM':
            output_line = '+1 ' + words[1]
        elif first_word == 'HAM':
            output_line = '-1 ' + words[1]
        elif first_word == 'POSITIVE':
            output_line = '+1 ' + words[1]
        elif first_word == 'NEGATIVE':
            output_line = '-1 ' + words[1]
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

    all_the_lines = ''

    for line in original_data:
        all_the_lines += '+1 ' + line

    file_to_write = open(file_name + '.svm.test', 'w')
    file_to_write.write(all_the_lines)

    return


def feature_add_one(file_name):
    original_data = open(file_name, 'r')
    all_the_lines = ''
    for line in original_data:
        words = line.split()
        output_line = ''
        output_line += words[0] + ' '
        for i in range(1, len(words)):
            pair = words[i].split(':')
            feature = pair[0]
            output_line += str(int(feature) + 1) + ':' + pair[1] + ' '
        output_line += '\n'
        all_the_lines += output_line

    file_to_write = open(file_name + '.added', 'w')
    file_to_write.write(all_the_lines)
    return


def convert_back_output_format(file_name, mode):
    file = open(file_name, 'r')
    positive = ''
    negative = ''
    if mode == 'positive':
        positive = 'POSITIVE'
        negative = 'NEGATIVE'
    elif mode == 'spam':
        positive = 'SPAM'
        negative = 'HAM'

    output = ''
    for line in file:
        words = line.split()
        if float(words[0]) < 0:
            output += negative + '\n'
        elif float(words[0]) > 0:
            output += positive + '\n'

    file_to_write = open(file_name + '.svm.out', 'w')
    file_to_write.write(output)

    return


def main():
    print('SVM-Light toolkit')
    print('1 TRAININGFILE - convert training data to svm format')
    print('2 TESTFILE - convert test data to svm format')
    print('3 FILE - add one on the feature')
    print('4 FILE positive/spam - convert the output file to original format')
    if len(sys.argv) == 3:
        if sys.argv[1] == '1':
            convert_training_data(sys.argv[2])
        elif sys.argv[1] == '2':
            convert_test_data(sys.argv[2])
        elif sys.argv[1] == '3':
            feature_add_one(sys.argv[2])
    elif len(sys.argv) == 4:
        if sys.argv[1] == '4':
            convert_back_output_format(sys.argv[2], sys.argv[3])
    return


main()
