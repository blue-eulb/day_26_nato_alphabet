import pandas

phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for item, row in phonetic_data.iterrows()}



while True:
    user_word = input("Choose a word: ").replace(" ","").upper()
    list_letters = [letter.upper() for letter in user_word]
    try:
        result = [phonetic_dict[letter] for letter in list_letters]
    except KeyError:
        print("The program only accept letters.")
    else:
        print(result)
