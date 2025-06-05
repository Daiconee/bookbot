def get_letters_dict(file_contents):
    letters_dict = {}
    for word in file_contents:
        ls = list(word)
        for letter in ls:
            letter = letter.lower()
            if (letter.isalpha()):
                if letter not in letters_dict:
                    letters_dict[letter] = 1
                else:
                    letters_dict[letter] += 1

    letters_dict = dict(sorted(letters_dict.items(), key=lambda item: item[1], reverse=True))
    return letters_dict

def get_num_words(file_contents):
    num = 0
    for word in file_contents:
        num += 1
    return num