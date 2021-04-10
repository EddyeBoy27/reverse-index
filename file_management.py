def doc_reader(path_file, doc):
    words_dict = dict()
    counter = 0
    with open(path_file, 'rb') as text_doc:
        text_lines = text_doc.read().split()
        for line in text_lines:
            word_decoded = line.decode('cp437').lower()
            if not word_decoded == '':
                words_dict[word_decoded] = counter
                counter += 1
    return words_dict


def exist_word(path_file, word):
    with open(path_file, 'rb') as text_doc:
        text_list = list()
        text_lines = text_doc.read().split()
        for word in text_lines:
            text_lines.append(word)
        print(text_list)
        # for line in text_lines.split(b" "):
        #     line2 = line.split()
        #     line3 = line.split(b'\n')
        #     for wordl in line3:
        #         word_decoded = wordl.decode('cp437').lower()
        #         if ((not word_decoded == '') and (word_decoded == word)):
        #             return True