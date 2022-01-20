import tensorflow as tf

imdb = tf.keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(
    num_words=10000)

#print(max([max(sequence) for sequence in train_data]))

word_index = imdb.get_word_index()
print(type(word_index.items()))

reverse_word_index = dict(
    [(value, key) for (key, value) in word_index.items()])

print(train_data)
decoded_review = ' '.join(
    [reverse_word_index.get(i - 3, '?') for i in train_data[1]])

print(decoded_review)