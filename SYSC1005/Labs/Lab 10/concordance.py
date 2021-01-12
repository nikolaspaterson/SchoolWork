import string
def build_concordance(filename):
    """ (str) -> dict of str, list pairs
    
    Return a dictionary in which the keys are the words in the
    specified file. The value associated with each key is a list
    containing the line numbers of all the lines in which each word
    occurs.
    
    >>> concordance = build_concordance('sons_of_martha.txt')
    """
    word_dict = {}
    infile = open(filename, "r")
    line_num = 0
    
    for line in infile:
        line_num = line_num + 1
        for word in line.strip(string.punctuation).lower().split():

            if word not in word_dict:
                word_dict[word] = []
                
            if line_num not in word_dict[word]:
                word_dict[word].append(line_num)

    return word_dict

if __name__ == '__main__':
    print(build_concordance('two_cities.txt'))
    print(build_concordance('sons_of_martha.txt'))
    
  