def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    letters_dict = get_letters_dict(file_contents)
    print_letters_dict(letters_dict)


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

    letters_dict = dict(sorted(letters_dict.items(), key=lambda item: item[0]))
    return letters_dict
    
def print_letters_dict(letters_dict):
    for key,value in letters_dict.items():
        print(f"The '{key}' character was found {value} times")

if __name__ == '__main__':
    main()