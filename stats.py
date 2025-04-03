def num_words(whole_text):
	words = whole_text.split()
	word_count = len(words)
	return word_count

def count_chars(whole_text):
	char_counts = {}
	for char in whole_text.lower():
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts

def sort_chars(char_count):
	chars_list = []
	for char, count in char_count.items():
		chars_list.append({"char": char, "count": count})

	def sort_on(dict):
		return dict["count"]

	chars_list.sort(reverse = True, key = sort_on)
	return chars_list
