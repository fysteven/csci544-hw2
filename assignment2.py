import sys
import os

__author__ = 'Frank'


def convert_sentiment_training_data_into_model(file):
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    total_lines = 0

    training_data = ""
    for line in file:
        total_lines += 1

        words = line.split()
        first_word = words[0]

        if int(first_word) >= 7:
            positive_count += 1
        elif int(first_word) <= 4:
            negative_count += 1
        else:
            neutral_count += 1

        training_data += line

    output = "positive_count " + str(positive_count)
    output += "\nnegative_count " + str(negative_count)
    output += "\nneutral_count " + str(neutral_count)
    output += "\ntotal_count " + str(total_lines)
    output += "\n"

    print("The number of positive reviews is: ", positive_count)
    print("The number of negative reviews is: ", negative_count)
    print("The number of neutral reviews is:  ", neutral_count)
    print("Total lines in this document are: ", total_lines)

    output += training_data

    # print(output)

    return output


def convert_training_file_into_model(file):
    spam_count = 0
    ham_count = 0
    total_lines = 0

    training_data = ''

    for line in file:
        total_lines += 1

        words = line.split()
        first_word = words[0]

        if first_word == '+1':
            spam_count += 1
        elif first_word == '-1':
            ham_count += 1
        else:
            pass
        training_data += line

    output = ''
    output += 'spam_count ' + str(spam_count) + '\n'
    output += 'ham_count ' + str(ham_count) + '\n'
    output += 'total_count ' + str(total_lines) + '\n'
    output += '\n'

    output += training_data

    return output


def probability(a, sum):
    return a / sum


def probability(message, given, file):
    number_of_words_in_spam = 0
    number_of_words_in_not_spam = 0
    for line in file:
        words = line.split()
        first_word = words[0]
        if int(first_word) >= 7:
            pass

        elif int(first_word) <= 4:
            pass
        else:
            pass


def naive_bayes_probability(positive, negative, line, probability_of_p, probability_of_np, file):

    return 1 / (1 + probability_of_np / probability_of_p * probability(line, negative, file) / probability(line, positive, file))


def naive_bayes(message_list, model):
    positive = 0
    negative = 0
    neutral = 0
    tokens_count_in_positive = [0] * len(message_list)
    tokens_count_in_negative = [0] * len(message_list)
    tokens_count_in_neutral = [0] * len(message_list)

    for line in model:
        words = line.split()
        if int(words[0]) >= 7:
            positive_temp, tokens_times_in_positive_temp = count_words_with_tokens(line, message_list)
            positive += positive_temp
            tokens_count_in_positive += tokens_times_in_positive_temp
        elif int(words[0]) <= 4:
            negative_temp, tokens_times_in_negative_temp = count_words_with_tokens(line, message_list)
            negative += negative_temp
            tokens_count_in_negative += tokens_times_in_negative_temp
        else:
            neutral_temp , tokens_times_in_neutral_temp = count_words_with_tokens(line, message_list)
            neutral += neutral_temp
            tokens_count_in_neutral += tokens_times_in_neutral_temp

    return


def count_words_in_line(line):
    words = line.split()
    count = 0
    for i in range(1, len(words)):
        print(words[i])
        word = words[i]
        pair = word.split(":")
        # word_id = pair[0]
        word_times = pair[1]
        count += int(word_times)
    return count


def count_words(line, token):
    words = line.split()
    total_count_in_line = 0
    token_count = 0
    for i in range(1, len(words)):
        word = words[i]
        pair = word.split(":")
        if pair[0] is token:
            token_count = int(pair[1])

        word_times = pair[1]
        total_count_in_line += int(word_times)
    return total_count_in_line, token_count


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


def list_files(path):
    # returns a list of names (with extension, without full path) of all files
    # in folder path
    files = []
    for name in os.listdir(path):
        # if os.path.isfile(os.path.join(path, name)):
        # if .DS_Store file exists, which is generated by Mac OS, don't append this on the list
        if name == '.DS_Store':
            pass
        else:
            files.append(path + name)
    return files


def list_all_the_files():
    all_ham_files = []
    all_spam_files = []
    base_directory = "./emails_input/"
    all_ham_files += list_files(base_directory + "enron1/ham/")
    all_ham_files += list_files(base_directory + "enron2/ham/")
    all_ham_files += list_files(base_directory + "enron4/ham/")
    all_ham_files += list_files(base_directory + "enron5/ham/")

    all_spam_files += list_files(base_directory + "enron1/spam/")
    all_spam_files += list_files(base_directory + "enron2/spam/")
    all_spam_files += list_files(base_directory + "enron4/spam/")
    all_spam_files += list_files(base_directory + "enron5/spam/")

    print(len(all_ham_files), len(all_spam_files))

    return all_ham_files, all_spam_files


def read_vocab_file():
    file_name = 'enron.vocab'
    file = open(file_name, 'r', encoding="latin1")

    tokens = [' ']

    for line in file:
        words = line.split()
        tokens.append(words[0])
    return tokens


def read_vocab_file2():
    file_name = 'enron.vocab'
    file = open(file_name, 'r', encoding='latin1')
    vocabs = {}

    count = 1
    for line in file:
        words = line.split()
        vocabs[words[0].lower()] = count
        count += 1

    return vocabs


def transform_file_into_project_data_format(file_name, category, vocab):
    file = open(file_name, 'r', encoding='latin1')

    output = ''
    output += category + ' '

    word_dictionary = {}
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower()
            if word not in word_dictionary:
                word_dictionary[word] = 1
            else:
                word_dictionary[word] += 1

    # print(word_dictionary)

    for i in range(1, len(vocab)):
        token = vocab[i].lower()
        if token in word_dictionary:
            output += str(i) + ':' + str(word_dictionary[token]) + ' '
    # print(output)
    return output


def transform_file_into_project_data_format2(file_name, category, vocabs):
    file = open(file_name, 'r', encoding='latin1')

    output = ''
    if category == '':
        pass
    else:
        output += category + ' '

    word_dictionary = {}
    result_dictionary = {}
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower()
            if word not in word_dictionary:
                word_dictionary[word] = 1
            else:
                word_dictionary[word] += 1

    for key in word_dictionary.keys():
        if key in vocabs:
            result_dictionary[int(vocabs[key])] = int(word_dictionary[key])
        else:
            print('A word is not in the vocabulary')

    for key in sorted(result_dictionary.keys()):
        output += str(key) + ':' + str(result_dictionary[key]) + ' '

    output += '\n'
    return output


def generate_email_training_file():
    all_ham_files, all_spam_files = list_all_the_files()

    vocab_list = read_vocab_file()
    print(len(vocab_list), vocab_list[0], vocab_list[1], vocab_list[159211])

    file_to_write = open('email_training_file', 'w')

    output_data = ''
    count = 0
    for file in all_spam_files:
        a_line = transform_file_into_project_data_format(file, '+1', vocab_list)
        output_data += a_line + '\n'
        print(count)
        count += 1
    for file in all_ham_files:
        a_line = transform_file_into_project_data_format(file, '-1', vocab_list)
        output_data += a_line + '\n'
        print(count)
        count += 1

    file_to_write.write(output_data)
    return


def generate_spam_model():
    file = open('email_training_file', 'r')
    model_file_content = convert_training_file_into_model(file)
    model_file = open('spam.nb.model', 'w')
    model_file.write(model_file_content)
    return


def generate_sentiment_model():
    file = open('labeledBow.feat', 'r')
    content = convert_sentiment_training_data_into_model(file)
    file_to_write = open('sentiment.nb.model', 'w')
    file_to_write.write(content)
    return


def generate_spam_test_data():
    base_directory = './spam_or_ham_test/'
    email_test_files = list_files(base_directory)
    # print(email_test_files)
    vocabs = read_vocab_file2()

    output_data = ''
    count = 0
    for file in email_test_files:
        a_line = transform_file_into_project_data_format2(file, '', vocabs)
        output_data += a_line
        print(count)
        count += 1

    file_to_write = open('email_test_file', 'w')
    file_to_write.write(output_data)
    return


def main():
    print("Current script file is: ", sys.argv[0])
    print('How to use this program?')
    print('Run this program with parameter: (one at a time)')
    print('1 - ')
    print('2 - convert email test files into Project Data format without labels')
    line = "9 0:9 1:1 2:4 3:4 4:6 5:4"
    print(count_words(line, "3"))
    tokens = ["3", "4", "6"]
    print(count_words_with_tokens(line, tokens))

    if len(sys.argv) == 2:
        print("The input path in the first argument is: ", sys.argv[1])
        # print("The output path in the second argument is: ", sys.argv[2])



        all_spam_files = []
        all_ham_files = []
    # generate_sentiment_model()
        if sys.argv[1] == '2':
            generate_spam_test_data()

    # vocabs = read_vocab_file2()
    # print(vocabs)
    return


main()
