import sys


__author__ = 'Frank'


def check_positive(word):
    if word == '+1':
        return True
    elif word == '-1':
        return False
    elif word == 'POSITIVE':
        return True
    elif word == 'NEGATIVE':
        return False
    elif word == 'SPAM':
        return True
    elif word == 'HAM':
        return False
    elif int(word) >= 7:
        return True
    elif int(word) <= 4:
        return False
    else:
        print('Something wrong in the first word of a line')
        return False


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
        words = line.split(' ', 1)
        if ':' in words[0]:
            all_the_lines += '0 ' + line
        else:
            if check_positive(words[0]):
                all_the_lines += '1 ' + words[1]
            else:
                all_the_lines += '0 ' + words[1]

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

    file_to_write = open(file_name + '.megam.training', 'w')
    file_to_write.write(data2)
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
    print('MegaM toolkit')
    print('1 TRAININGFILE - convert training data to MegaM format')
    print('2 TESTFILE - convert test data to MegaM format')
    print('3 FILE positive/spam - convert the output file to original format')

    print('')
    if len(sys.argv) == 3:
        if sys.argv[1] == '1':
            convert_training_data_to_megam_format(sys.argv[2])
        elif sys.argv[1] == '2':
            convert_test_data(sys.argv[2])
    elif len(sys.argv) == 4:
        if sys.argv[1] == '3':
            convert_back_output_format(sys.argv[2], sys.argv[3])
    return

main()

