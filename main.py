import sys
from stats import num_words
from stats import count_chars
from stats import sort_chars

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]

	text = get_book_text(book_path)
	word_count = num_words(text)
	char_count = count_chars(text)
	
	sorted_chars = sort_chars(char_count)
	print_report(book_path, word_count, sorted_chars)

def get_book_text(path):
        with open(path) as f:  
                return f.read()
	
def print_report(book_path, word_count, sorted_chars):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")

	for char_dict in sorted_chars:
		char = char_dict["char"]
		count = char_dict["count"]

		if char.isalpha():
			print(f"{char}: {count}")

	print("============= END ===============")


main()
