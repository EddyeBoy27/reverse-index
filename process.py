import os
from file_management import doc_reader


def reverse_index():
    files_arr = sorted(os.listdir('./dataset/'), key=lambda x: x[:-1])
    words_list = set()
    words_dict_index = dict()
    counter = 0
    for doc in files_arr:
        words_ids = dict()
        words_set = doc_reader(f"./dataset/{doc}")
        for word in words_set:
            if not word in words_dict_index:
                words_dict_index[word] = counter
                counter += 1
        for value in words_dict_index.values():
            if not value in words_ids.values():
                words_ids[value] = list()
        print(words_ids)
            # words_ids[value].append(doc)
        # print(words_ids)
    # print(words_dict_index)


reverse_index()