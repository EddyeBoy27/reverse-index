def doc_reader(path_file):
    text_splited_bytes = set()
    with open(path_file, 'rb') as text_doc:
        text_lines = text_doc.read()
        for line in text_lines.split(b" "):
            line2 = line.split()
            line3 = line.split(b'\n')
            for word in line3:
                word_decoded = word.decode('cp437')
                if not word_decoded == '':
                    text_splited_bytes.add(word_decoded)
    return text_splited_bytes