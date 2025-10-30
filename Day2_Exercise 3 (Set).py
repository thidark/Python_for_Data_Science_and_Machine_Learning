# Finding Unique Words

sentence="The quick brown fox jumps over the lazy dog"
word_set=[]

split_sent=sentence.split(" ")
for word in split_sent:
    word_set.append(word)

unique_words=set(word_set)

for word in unique_words:
    print(word)


