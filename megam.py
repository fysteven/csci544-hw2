import sys


__author__ = 'Frank'


def convert_training_data_to_megam_format(file_name):
    file = open(file_name, 'r')

    all_the_lines = ''
    output_line = ''
    for line in file:
        output_line = line.replace(':', ' ')
        words = output_line.split(' ', 1)
        first_word = words[0]
        if first_word == 'SPAM':
            output_line = '1 ' + words[1]
        elif first_word == 'HAM':
            output_line = '0 ' + words[1]
        elif first_word == 'POSITIVE':
            output_line = '1 ' + words[1]
        elif first_word == 'NEGATIVE':
            output_line = '0 ' + words[1]
        elif int(first_word) >= 7:
            output_line = '1 ' + words[1]
        elif int(first_word) <= 4:
            output_line = '0 ' + words[1]
        elif first_word == '1':
            pass
        elif first_word == '0':
            pass

        all_the_lines += output_line

    output_file = open(file_name + '.megam.model', 'w')
    output_file.write(all_the_lines)
    return


def invent_labels_for_test_data(test_data):
    # file = open(file_name, 'r')

    all_the_lines = ''
    output_line = ''
    for line in test_data:
        output_line = '0 ' + line
        all_the_lines += output_line

    return all_the_lines


def replace_delimiter(all_the_lines):
    output_data = ''
    for line in all_the_lines:
        output_data += line.replace(':', ' ')
    return output_data


def convert_test_data(file_name):
    file = open(file_name, 'r')
    labeled_data = invent_labels_for_test_data(file)
    data2 = replace_delimiter(labeled_data)

    file_to_write = open(file_name + '.megam.intermediate', 'w')
    file_to_write.write(data2)
    return


def main():
    print('MegaM toolkit')
    print('1 TRAININGFILE - convert training data to MegaM format')
    print('2 TESTFILE - convert test data to MegaM format')
    print('')
    if len(sys.argv) == 3:
        if sys.argv[1] == '1':
            convert_training_data_to_megam_format(sys.argv[2])
        elif sys.argv[1] == '2':
            convert_test_data(sys.argv[2])
    return

main()

