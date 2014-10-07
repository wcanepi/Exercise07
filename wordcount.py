# Opens file assigns words to list.
def read_file(filename):
    
    word = []

    f = open(filename)
    for line in f:
        entry = line.strip().split(' ')
        word.extend(entry)
    print word

#Count the letters in each word in our word list.
def letter_count():
    pass

# Assign word list and letter count list to a dictionary.
def dictionary():
    pass

# Prints dictionary of words and the letter count.
def print_dictionary(story):
    pass    

def main():
    read_file('short.txt')

if __name__ == "__main__":
    main()
