import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

# Read the 'count' file into an array of tuples
word_dict = {}
with open('counts') as file:
    word_counts_array = file.readlines()

word_counts = {}
for line in word_counts_array:
    word, count = line.split('\t')
    word = word.strip('"')
    count = int(count.strip('\n'))
    word_counts[word] = count

# A sorted array of tuples, eg [('the', 4501), ('is', 3414)]:
sorted_dict = sorted(word_counts.iteritems(), key=itemgetter(1), reverse=True)
words = []
counts = []
for pair in sorted_dict:
    word, count = pair
    words.append(word)
    counts.append(count)

# Now make a frequency chart:
n_words = 25
left_sides = np.arange(0.75, n_words+0.75)
top_words_counts = counts[:n_words]
plt.bar(left_sides, top_words_counts, width=0.5)
plt.xticks(left_sides+0.25, words[:n_words], va='center')
plt.title("Frequency of words in Jane Austen's Pride and Prejudice")
plt.show()
