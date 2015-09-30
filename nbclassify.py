import sys
import os


__author__ = 'Frank'


def open_model_file(file_name):
    file = open(file_name, 'r')

    positive_count = 0
    negative_count = 0
    neutral_count = 0
    total_count = 0

    words_in_positive = 0
    words_in_negative = 0
    words_in_total = 0

    tokens_in_positive_count = {}
    tokens_in_negative_count = {}

    for line in file:
        words = line.split()
        first_word = words[0]
        if first_word == 'positive_count':
            positive_count = int(words[1])

        elif first_word == 'negative_count':
            negative_count = int(words[1])

        elif first_word == 'neutral_count':
            neutral_count = int(words[1])

        elif first_word == 'total_count':
            total_count = int(words[1])

        elif first_word == 'words_in_positive':
            words_in_positive = int(words[1])

        elif first_word == 'words_in_negative':
            words_in_negative = int(words[1])

        elif first_word == 'words_in_total':
            words_in_total = int(words[1])

        elif first_word == 'positive':
            feature = int(words[1])
            value = int(words[2])
            if feature not in tokens_in_positive_count:
                tokens_in_positive_count[feature] = value
            else:
                print('something wrong with the model')

        elif first_word == 'negative':
            feature = int(words[1])
            value = int(words[2])
            if feature not in tokens_in_negative_count:
                tokens_in_negative_count[feature] = value

    return positive_count, negative_count, neutral_count, total_count, words_in_positive, words_in_negative, \
        words_in_total, tokens_in_positive_count, tokens_in_negative_count


def naive_bayes_classify(feature_value, positive_count, negative_count, neutral_count, total_count, words_in_positive, \
                         words_in_negative, words_in_total, tokens_in_positive_count, tokens_in_negative_count):
    p_positive = positive_count / total_count
    p_negative = negative_count / total_count

    p_message_positive = 1
    p_message_negative = 1

    for key in feature_value:
        if key not in tokens_in_positive_count:
            p_message_positive *= (1 / (words_in_positive + words_in_total)) ** feature_value[key]
        else:
            p_message_positive *= ((tokens_in_positive_count[key] + 1) / (words_in_positive + words_in_total) ** feature_value[key])

        if key not in tokens_in_negative_count:
            p_message_negative *= (1 / (words_in_negative + words_in_total)) ** feature_value[key]
        else:
            p_message_negative *= ((tokens_in_negative_count[key] + 1) / (words_in_negative + words_in_total) ** feature_value[key])

    p_positive_message = (p_positive * p_message_positive) / (p_positive * p_message_positive + p_negative * p_message_negative)

    return p_positive_message


def function1(model_file_name, test_file_name):

    positive_count, negative_count, neutral_count, total_count, words_in_positive, words_in_negative, words_in_total, \
        tokens_in_positive_count, tokens_in_negative_count = open_model_file(model_file_name)

    output = ''

    test_file = open(test_file_name, 'r')
    for line in test_file:
        words = line.split()
        feature_value = {}
        for word in words:
            pair = word.split(':')
            feature = int(pair[0])
            value = int(pair[1])
            if feature not in feature_value:
                feature_value[feature] = value
            else:
                print('something wrong happened')

        output += naive_bayes_classify(feature_value, positive_count, negative_count, neutral_count, total_count, \
            words_in_positive, words_in_negative, words_in_total, tokens_in_positive_count, tokens_in_negative_count)

        output += '\n'

    output_file = open(test_file_name + '.out', 'w')
    output_file.write(output)
    return


def main():
    if len(sys.argv) != 3:
        print('Please run this program in the following manner:')
        print('python3 nbclassify.py MODELFILE TESTFILE')
    else:
        function1(sys.argv[1], sys.argv[2])
    return

main()
