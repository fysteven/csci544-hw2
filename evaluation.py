import sys


__author__ = 'Frank'


def compare_result(actual, predicted):
    pass


def convert_actual_result_into_uniform_format(actual_list):
    result_list = []

    for i in range(0, len(actual_list)):
        if actual_list[i] == '+1':
            result_list.append('+1')
        elif actual_list[i] == '-1':
            result_list.append('-1')
        elif actual_list[i] == 'POSITIVE':
            result_list.append('+1')
        elif actual_list[i] == 'NEGATIVE':
            result_list.append('-1')
        elif actual_list[i] == 'SPAM':
            result_list.append('+1')
        elif actual_list[i] == 'HAM':
            result_list.append('-1')
        elif int(actual_list[i]) >= 7:
            result_list.append('+1')
        elif int(actual_list[i]) <= 4:
            result_list.append('-1')
    return result_list


def evaluate(actual_file, predicted_file):
    actual_result = open(actual_file, 'r')
    predicted_result = open(predicted_file, 'r')

    actual_list = []
    predicted_list = []

    positive_in_actual = 0
    negative_in_actual = 0

    for line in actual_result:
        words = line.split()
        actual_list.append(words[0])

    # convert actual_list to uniform format +1 or -1
    actual_list = convert_actual_result_into_uniform_format(actual_list)

    for line in predicted_result:
        words = line.split()
        predicted_list.append(words[0])

    predicted_list = convert_actual_result_into_uniform_format(predicted_list)

    total_in_actual = len(actual_list)
    total_in_predicted = len(predicted_list)

    for i in range(0, len(actual_list)):
        if actual_list[i] == '+1':
            positive_in_actual += 1
        elif actual_list[i] == '-1':
            negative_in_actual += 1

    precision_positive_count = 0
    precision_negative_count = 0

    positive_in_predicted = 0
    negative_in_predicted = 0

    for i in range(0, len(predicted_list)):
        if predicted_list[i] == actual_list[i]:
            if actual_list[i] == '+1':
                precision_positive_count += 1
            if actual_list[i] == '-1':
                precision_negative_count += 1
        if predicted_list[i] == '+1':
            positive_in_predicted += 1
        elif predicted_list[i] == '-1':
            negative_in_predicted += 1

    precision_positive = precision_positive_count / positive_in_predicted
    precision_negative = precision_negative_count / negative_in_predicted

    recall_positive = precision_positive_count / positive_in_actual
    recall_negative = precision_negative_count / negative_in_predicted

    f_one_score_positive = 2 * precision_positive * recall_positive / (precision_positive + recall_positive)
    f_one_score_negative = 2 * precision_negative * recall_negative / (precision_negative + recall_negative)

    return precision_positive, recall_positive, f_one_score_positive, \
           precision_negative, recall_negative, f_one_score_negative


def main():
    print('Evaluation of the results.')
    print('Please use this program like this:')
    print('python3 evaluation.py ACTUAL PREDICTED')
    print()
    if len(sys.argv) == 3:
        if sys.argv[1] == sys.argv[2]:
            print('Actual file and predicted file cannot be the same file.')
        else:
            precision_positive, recall_positive, f_one_score_positive, \
                precision_negative, recall_negative, f_one_score_negative = evaluate(sys.argv[1], sys.argv[2])

            print('precision of positive: ', precision_positive)
            print('recall of positive: ', recall_positive)
            print('F1 score of positive: ', f_one_score_positive)

            print()

            print('precision of negative: ', precision_negative)
            print('recall of negative: ', recall_negative)
            print('F1 score of negative: ', f_one_score_negative)

main()
