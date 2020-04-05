import glob
import os
import re

datapath_input = os.path.join('..','files','input')
datapath_output = os.path.join('..','files','num_foreign_words')

text_of_all_files = [open(f, encoding='utf-8') for f in glob.glob(os.path.join(datapath_input, '*.txt'))]

for single_file_text in text_of_all_files:
    file_name = single_file_text.name.split(os.sep)[-1]
    output_file_path = os.path.join(datapath_output, file_name)
    output_file = open(output_file_path, 'w', encoding='utf-8')
    for line in single_file_text:
        line = line.strip()
        array_words = re.split(r'[;:,\-\s]', line)
        list_numbers = list()
        list_words = list(filter(None, array_words))
        for num, word in enumerate(list_words):
            regular = re.compile('[a-zA-Z]+')
            results = regular.findall(word)
            if results:
                list_numbers.append(str(num))
        output_file.write(','.join(list_numbers))
        output_file.write('\n')
    output_file.close()
    single_file_text.close()






