# Opens file assigns words to list.
def read_file(filename):
    d = {}
    word = []

    f = open(filename)
    for line in f:
        entry = line.strip().split(' ')
        word.extend(entry)
    print word

# Assign word list as keys with no value to a dictionary.
    d[word] = None
    print d



    


#Count the letters in each word in our word list.
def letter_count():
    pass

# Prints dictionary of words and the letter count.
def print_dictionary(story):
    pass    

def main():
    read_file('short.txt')

if __name__ == "__main__":
    main()
