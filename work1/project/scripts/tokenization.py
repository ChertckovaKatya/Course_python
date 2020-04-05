import glob
import os
import re

datapath_input = os.path.join('..', 'files', 'input')
datapath_output = os.path.join('..', 'files', 'token_output')

text_of_all_files = [open(f, encoding='utf-8') for f in glob.glob(os.path.join(datapath_input, '*.txt'))]

for single_file_text in text_of_all_files:
    file_name = single_file_text.name.split(os.sep)[-1]
    output_file_path = os.path.join(datapath_output, file_name)
    output_file = open(output_file_path, 'w', encoding='utf-8')
    for line in single_file_text:
        line = line.strip()
        array_words = re.split(r'\s', line)
        list_words = list(filter(None, array_words))
        for word in list_words:
            first_reg = re.compile(r'([0-9А-Яа-яa-zA-Z»][.,;][«А-Яа-яa-zA-Z0-9]?)')

            second_reg = re.compile(r'([А-Яа-яa-zA-Z»][.,;][«А-Яа-яa-zA-Z0-9])')
            third_reg = re.compile(r'([А-Яа-яa-zA-Z]\d|\d[А-Яа-яa-zA-Z])')
            fourth_reg = re.compile(r'([а-яa-z][А-ЯA-Z])')
            fifth_reg = re.compile(r'(["«\'][0-9А-Яа-я]+[.,;:][А-Яа-я]+["»\'])')
            sixth_reg = re.compile(r'[А-Яа-я]{1,3}[-]\w{2}[А-Я]{1,3}')
            seven_reg = re.compile(r'[0-9a-zA-Z]+.ru')
            eighth_reg = re.compile(r'[#][\w\s]+')

            result_first_reg = first_reg.findall(word)
            result_second_reg = second_reg.findall(word)
            result_third_reg = third_reg.findall(word)
            result_fourth_reg = fourth_reg.findall(word)
            result_fifth_reg = fifth_reg.findall(word)
            result_sixth_reg = sixth_reg.findall(word)
            result_seven_reg = seven_reg.findall(word)
            result_eighth_reg = eighth_reg.findall(word)

            value_result_fifth_reg = ''
            value_result_sixth_reg = ''
            value_result_seven_reg = ''
            value_result_eighth_reg = ''

            if result_fifth_reg:
                value_result_fifth_reg = result_fifth_reg[0]
            if result_sixth_reg:
                value_result_sixth_reg = result_sixth_reg[0]
            if result_seven_reg:
                value_result_seven_reg = result_seven_reg[0]
            if result_eighth_reg:
                value_result_eighth_reg = result_eighth_reg[0]

            if result_first_reg:
                for result in result_first_reg:
                    if value_result_fifth_reg.find(result) == -1 and value_result_seven_reg.find(result) == -1\
                            and value_result_eighth_reg.find(result) == -1:
                        difference = len(result)
                        start = word.find(result)
                        end = word.find(result) + difference
                        if start and end:
                            if difference == 3:
                                word = word[0:start+1] + ' ' + word[start + 1:end - 1] + ' ' + word[end - 1:len(word)]
                            else:
                                word = word[0:start + 1] + ' ' + word[end - 1:len(word)]
            if result_second_reg:
                for result in result_second_reg:
                    if value_result_fifth_reg.find(result) == -1 and value_result_seven_reg.find(result) == -1\
                            and value_result_eighth_reg.find(result) == -1:
                        difference = len(result)
                        start_second_reg = word.find(result)
                        end_second_reg = word.find(result) + difference
                        if not start_second_reg == -1:
                            if difference == 3:
                                word = word[0:start_second_reg+1] + ' ' + word[start_second_reg + 1:end_second_reg - 1] + ' ' + word[end_second_reg - 1:len(word)]
                            else:
                                word = word[0:start_second_reg + 1] + ' ' + word[end_second_reg - 1:len(word)]
            if result_third_reg:
                for result in result_third_reg:
                    if value_result_sixth_reg.find(result) == -1 and value_result_eighth_reg.find(result) == -1:
                        difference = len(result)
                        start_third_reg = word.find(result)
                        end_third_reg = word.find(result) + difference
                        if not start_third_reg == -1:
                            word = word[0:start_third_reg + 1] + ' ' + word[end_third_reg - 1:len(word)]

            if result_fourth_reg:
                for result in result_fourth_reg:
                    if value_result_sixth_reg.find(result) == -1 and value_result_eighth_reg.find(result) == -1:
                        difference = len(result)
                        start_fourth_reg = word.find(result)
                        end_fourth_reg = word.find(result) + difference
                        if start_fourth_reg and end_fourth_reg:
                            word = word[0:start_fourth_reg + 1] + ' ' + word[end_fourth_reg - 1:len(word)]
            output_file.write(word + ' ')

    output_file.close()
    single_file_text.close()
