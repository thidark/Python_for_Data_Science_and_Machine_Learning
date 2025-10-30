def count_words(filename):
    # Open and read the file
    with open(filename, 'r') as file:
        text = file.read()

    
    text = text.lower()   
    words = text.split()


    # Create a dictionary to store word counts
    word_counts = {}

    # Count each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts



result = count_words("text.txt")
print(result)
