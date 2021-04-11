def doc_reader(path_file, doc):
    words_list = list()
    with open(path_file, 'rb') as text_doc:
        text_lines = text_doc.read().split()
        for line in text_lines:
            word_decoded = line.decode('cp437')
            if not word_decoded == '':
                words_list.append(word_decoded)
    return words_list