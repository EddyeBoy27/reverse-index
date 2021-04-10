import os
from file_management import doc_reader, exist_word


def reverse_index(dir_path):
    # files_arr = sorted(os.listdir(dir_path), key=lambda x: x[:-1])
    files_arr = ['0']
    words_list_global = dict()
    words_list_set = set()
    words_list = list()
    reverse_index = dict()
    # words_set_index = set()
    words_dict_index = dict()
    # words_ids = dict()
    counter = 0
    for doc in files_arr:
        doc_read = doc_reader(f"./dataset/{doc}", doc)
        # for word in doc_read:
        #     if not word in words_list_global:
        #         words_list_global[word] = counter
        #         counter += 1
    # for doc in files_arr:
    #     for word in words_list_global:
    #         verify_word = exist_word(f"./dataset/{doc}", word)
    #         if verify_word:
    #             if not words_list_global[word] in reverse_index:
    #                 reverse_index[words_list_global[word]] = list(doc)
    #             else:
    #                 reverse_index[words_list_global[word]].append(doc)
    # print(reverse_index)
    # for index, array in enumerate(words_list):
    #     if array[0] in words_list:
    #         words_list[index] = [array]
    #         words_dict_index[word] = doc_read[word]
    #     for word in doc_read:
    #         if ((word in words_dict_index) & (doc_read[word] == words_dict_index[word])):
    #             words_list_set.add((doc_read[word], [doc]))
    # print(words_list_set)
    # print(words_dict_index)
            # words_list_set.add(word)
    # print(words_list_set)
            # words_list.add(word)
            # counter += 1
            # if not word in words_dict_index:
            #     words_dict_index[word] = counter
            #     words_list_set.add((word, counter, doc))
            #     counter += 1
        # print(words_set)
    # for word in words_dict_index:
    #     print(words_dict_index[word])
    #     for value in words_dict_index.values():
    #         if not value in words_ids.values():
    #             words_ids[value] = list()
    #         words_ids[value].append(doc)
    # print(words_ids)
    # print(words_dict_index)


reverse_index('./dataset/')
