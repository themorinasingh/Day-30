
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


word = input("Enter a word: ").upper()

try:
    output_list = [phonetic_dict[letter] for letter in word]

except:
    print("Sorry, only letters in the alphabet please.")

else:
    print(output_list)
