from stats import word_count, string_count,sort_dictionary,helper_function_name
import sys

def get_book_text (file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = word_count(text)
    character_dictionary = string_count(text)
    sort_text = sort_dictionary(character_dictionary)
    #print(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_text:
        char = item["char"]
        if char.isalpha():
            count = item["num"]
            print(f"{char}: {count}")
    print("============= END ===============")

    #print(text)


main()
