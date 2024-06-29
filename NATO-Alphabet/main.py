import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
encoded_word = [nato_alphabet[letter] for letter in word]
print(encoded_word)
