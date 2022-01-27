/!\ READ ME /!\

This code translates french sentences in lists and nxm matrix with a tokenizer and a stemmer,
both in a different code.

- "assets" contains "stopwords" in json, words that are not useful in a sentence
- "tokenizer" contains a tokenizer algorithm that selects useful words and gives back 3 arguments:
	- a list of all words
	- an iteration matrix 
	- words by sentences

- "stemmer" contains a stemmer algorithm that reduces words lenght with french language characteristics in order to get their root.
It returns the same list that tokenizer gave before but with shorter words.