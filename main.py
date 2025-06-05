from stats import get_letters_dict, get_num_words
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    address = sys.argv[1]
    with open(address) as f:
        file_contents = f.read().split()
    num = get_num_words(file_contents)
    letters_dict = get_letters_dict(file_contents)
    
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {address}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    print_letters_dict(letters_dict)
    
def print_letters_dict(letters_dict):
    for key,value in letters_dict.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    main()