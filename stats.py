import sys

def get_letters_dict(file_contents, num):
    count = 0
    letters_dict = {}
    for word in file_contents:
        count += 1
        show_progress(count, num)
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

def show_progress(count, num):
    length = 20
    if num <= 0:
        sys.stdout.write("file contains no text")
        return
    percentage = count / num * 100
    filled = int(count / num * length)
    prev_fill = int((count-1) / num * length)
    if filled == prev_fill and filled != 0:
        return
    else:
        if percentage > 100:
            bar = length * "⏹ "
            percentage = 100
        else :
            bar = filled * "⏹ " + (length - filled) * "▪ "
        sys.stdout.write(f"\rProgress : {bar} {percentage:.1f}% done")
        sys.stdout.flush()

def get_num_words(file_contents):
    num = 0
    for word in file_contents:
        num += 1
    return num