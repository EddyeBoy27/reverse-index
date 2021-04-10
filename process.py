import os
from file_management import doc_reader


def reverse_index(dir_path):
    files_arr = sorted(os.listdir(dir_path), key=lambda x: x[:-1])
    words_list_dict = dict()
    words_list_set = set()
    # words_set_index = set()
    words_dict_index = dict()
    # words_ids = dict()
    counter = 0
    for doc in files_arr:
        words_set = doc_reader(f"./dataset/{doc}")
        for word in words_set:
            # words_list.add(word)
            # counter += 1
            if not word in words_dict_index:
                words_dict_index[word] = counter
                counter += 1
    for word in words_dict_index:
        print(words_dict_index[word])
    #     for value in words_dict_index.values():
    #         if not value in words_ids.values():
    #             words_ids[value] = list()
    #         words_ids[value].append(doc)
    # print(words_ids)
    # print(words_dict_index)


reverse_index('./dataset/')
