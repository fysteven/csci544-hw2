import os
import sys

__author__ = 'Frank'


def count_words_with_tokens(line, tokens):
    words = line.split()
    total_count_in_line = 0
    tokens_count = [0] * len(tokens)

    for i in range(1, len(words)):
        word = words[i]
        pair = word.split(":")
        word_times = pair[1]
        total_count_in_line += int(word_times)

        for j in range(0, len(tokens)):
            if pair[0] is tokens[j]:
                temp = int(pair[1])
                tokens_count[j] = temp

    return total_count_in_line, tokens_count


def convert_training_data_into_model(file):
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    total_lines = 0

    words_in_positive = 0
    words_in_negative = 0
    words_in_total = 0

    tokens_in_positive_count = {}
    tokens_in_negative_count = {}

    training_data = ""
    for line in file:
        total_lines += 1

        words = line.split()
        first_word = words[0]

        if int(first_word) >= 7:
            positive_count += 1
            for i in range(1, len(words)):
                pair = words[i].split(':')
                feature = int(pair[0])
                value = int(pair[1])
                words_in_positive += value
                words_in_total += value
                if feature not in tokens_in_positive_count:
                    tokens_in_positive_count[feature] = value
                else:
                    tokens_in_positive_count[feature] += value

        elif int(first_word) <= 4:
            negative_count += 1
            for i in range(1, len(words)):
                pair = words[i].split(':')
                feature = int(pair[0])
                value = int(pair[1])
                words_in_negative += value
                words_in_total += value
                if feature not in tokens_in_negative_count:
                    tokens_in_negative_count[feature] = value
                else:
                    tokens_in_negative_count[feature] += value
        else:
            neutral_count += 1

        training_data += line

    output = ''
    output += "positive_count " + str(positive_count) + '\n'
    output += "negative_count " + str(negative_count) + '\n'
    output += "neutral_count " + str(neutral_count) + '\n'
    output += "total_count " + str(total_lines) + '\n'

    output += 'words_in_positive ' + str(words_in_positive) + '\n'
    output += 'words_in_negative ' + str(words_in_negative) + '\n'
    output += 'words_in_total ' + str(words_in_total) + '\n'

    # for i in range(0, len(tokens_in_positive_count)):
    #     feature = str(i)
    #     output += feature
    #     if feature in tokens_in_positive_count:
    #         output += ' ' + str(tokens_in_positive_count[feature])
    #     if feature in tokens_in_negative_count:
    #         output += ' ' + str(tokens_in_negative_count[feature])
    #     output += '    \n'

    for i in sorted(tokens_in_positive_count.keys()):
        output += 'positive ' + str(i) + ' ' + str(tokens_in_positive_count[i]) + '\n'

    for i in sorted(tokens_in_negative_count.keys()):
        output += 'negative ' + str(i) + ' ' + str(tokens_in_negative_count[i]) + '\n'

    return output


def generate_sentiment_model(input_file, output_file):
    # file = open('labeledBow.feat', 'r')
    file = open(input_file, 'r')
    content = convert_training_data_into_model(file)
    # file_to_write = open('sentiment.nb.model', 'w')
    file_to_write = open(output_file, 'w')
    file_to_write.write(content)
    return


def main():
    print("Current script file is: ", sys.argv[0])
    if len(sys.argv) != 3:
        print('Please run this program in the following manner:')
        print('python3 nblearn.py TRAININGFILE MODELFILE')
    else:
        if sys.argv[1] == sys.argv[2]:
            print('TRAININGFILE and MODELFILE cannot be the same one.')
        else:
            generate_sentiment_model(sys.argv[1], sys.argv[2])
    return


main()