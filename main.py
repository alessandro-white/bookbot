from stats import get_num_of_words
from stats import get_chars
from stats import sort_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    word_count = get_num_of_words(book_path)
    char_dict = get_chars(book_path)
    sort_dict2 = sort_dict(char_dict)
    print_report(book_path, word_count, sort_dict2)
    
def print_report(book_path, word_count, sort_dict2):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sort_dict2:
        if not char["char"].isalpha():
            continue
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
        


main()