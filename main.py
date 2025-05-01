import sys
from stats import get_num_words,count_chars,sort_dict

if len(sys.argv) < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

BOOK_FILE_PATH = sys.argv[1]

def get_book_text(filepath):
  file_contents = ''
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def print_receipt(sorted_list, num_words):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {BOOK_FILE_PATH}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")

  for pair in sorted_list:
    char = pair["char"] 
    num = pair["num"]

    print(f"{char}: {num}")

  print("============= END ===============")
  pass




def main():
  book_text = get_book_text(BOOK_FILE_PATH)

  num_words = get_num_words(book_text)
  char_count = count_chars(book_text)

  # print(f"{num_words} words found in the document")
  # print(char_count)

  sorted_list = sort_dict(char_count)
  print_receipt(sorted_list, num_words)


main()