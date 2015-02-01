def read_words (word_file, out_file):
    stoplist = set('for a of the and to in'.split())
    texts = [word for line in open(word_file, 'r') for word in line.split() if word not in stoplist]
    with open(out_file, 'w') as file:
        for item in texts:
            file.write(item)
            file.write('\t')
            if(item == '##'):
             file.write('\n')

