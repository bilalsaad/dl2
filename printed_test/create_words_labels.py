
words = 'words.txt'
words = open(words, 'r')
out = open('words_and_labels.txt', 'w')
count = 0
for line in words:
    out.write(line.rstrip()  + " " + str(count) + '\n')
    count += 1

words.close()
out.close()


