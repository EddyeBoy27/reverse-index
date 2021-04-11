import os
from file_management import doc_reader


def reverse_index(dir_path):
    files_arr = sorted(os.listdir(dir_path), key=lambda x: x[:-1])
    words_list_global = dict()
    counter = 0
    for doc in files_arr:
        doc_read = doc_reader(f"./dataset/{doc}", doc)
        for word in doc_read:
            if not word in words_list_global:
                words_list_global[word] = list()
                words_list_global[word].append(counter)
                words_list_global[word].append([])
                words_list_global[word][1].append(doc)
            if ((word in words_list_global) and (not doc in words_list_global[word][1])): 
                words_list_global[word][1].append(doc)
            counter += 1
    return words_list_global


print(reverse_index('./dataset/'))
