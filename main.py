

with open('./books/frankenstein.txt') as f:
	print("Begin Report of book")
	file_contents = f.read()
	split_file = file_contents.split()
	word_count = len(split_file)
	print(f"{word_count} words found in the document")

	dictionary = {}

	for word in split_file:
		word = word.lower()
		word = list(word)
		for letter in word:
			if letter.isalpha():
				if letter in dictionary:
					dictionary[letter] += 1
				else:
					dictionary[letter] = 1
	
	# print(dictionary)
	list = []

	for word in dictionary:
		list.append({"letter": word, "num": dictionary[word]})
		# print(word)
  
	
	def sort_on(dict):
		return dict["num"]

	list.sort(reverse=True, key=sort_on)

	for item in list:
		# print(item)
		print(f"The {item['letter']} character was found {item['num']} times")

	# print(len(split_file))