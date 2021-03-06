def frequency_words (word_file, out_file):
	texts = [word for line in open(word_file, 'r') for word in line.split()]
	dictionary = corpora.Dictionary(texts)	
	dictionary.save('dictionary.txt')
	corpus = [dictionary.doc2bow(text) for text in texts]
	with open(out_file, 'w') as file:
		for items in corpus:
			file.write(item)
			if item == ')],':
				file.write('\n')
	
