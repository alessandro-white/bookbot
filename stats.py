import sys
def get_num_of_words(book_path):
    num_words = 0
    with open(book_path) as f:
        file_contents = f.read()
        list_words = file_contents.split()

        for i in list_words:
            num_words +=1
        
        return(num_words)


def get_chars(book_path):
    num_of_chars = dict()
    with open(book_path) as f:
        file_contents = f.read()
        chars = list(file_contents.lower())
        for i in chars:
            if i in num_of_chars:
                num_of_chars[i] += 1
            else:
                num_of_chars[i] = 1
    return num_of_chars

def sort_on(d):
    return d["num"]


def sort_dict(char_dict):
    sort_list = []
    for i in char_dict:
        sort_list.append({"char": i, "num": char_dict[i]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list


    