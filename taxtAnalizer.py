text = input('Please enter a block of text for analysis:\n ')


def remove_punctuation(text):
    punctuation = ".,?!:;'(){}[]\/"
    for char in punctuation:
        text = text.replace(char, "")
    return text


total_characters = len(text)
total_words = len(text.split())
total_sentences = text.count('.')+ text.count('!')+ text.count('?')

word_frequency = {}
word_list = remove_punctuation(text).lower().split()
for word in word_list:
    if not word in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

most_frequent_word = max(word_frequency, key=word_frequency.get)

lengths = [len(word) for word in word_list]
average_word_length = sum(lengths)/len(lengths)

average_sentence_length = total_words/total_sentences



print('Analysis complete! Results: ')
print('-'*25)
print(f'Total characters: {total_characters}')
print(f'Total words: {total_words}')
print(f'Total sentences: {total_sentences}')
print(f"Most frequent word: '{most_frequent_word}' (used {word_frequency[most_frequent_word]} times)")
print(f'Average word length: {average_word_length:.2f}')
print(f'Average sentence length: {average_sentence_length:.2f}')