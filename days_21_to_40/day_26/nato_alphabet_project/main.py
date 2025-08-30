import pandas

# import csv and prepare letter: word dictionary
nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = { row.letter: row.code for (index, row) in nato_alphabet_df.iterrows() }
# print(nato_alphabet_df)
# print(nato_alphabet_dict)

# read user input
word = input("Enter a word (no spaces): ").upper()

# iterate through the word entered by the user and prepare result list
result = [nato_alphabet_dict[letter] for letter in word]
print(result)
