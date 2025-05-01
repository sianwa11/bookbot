def get_num_words(str):
  return len(str.split())

def count_chars(book_text):
  char_count = {}

  for text in book_text:
    char = text.lower()
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1

  return char_count

def sort_on(dict):
  return dict["num"]

def sort_dict(char_dict):
  char_list = []
  for key, value in char_dict.items():
    if not key.isalpha():
      continue
    char_list.append({"char": key, "num": value})

  char_list.sort(reverse=True,key=sort_on)
  return char_list
