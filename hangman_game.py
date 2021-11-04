import random
import os



def read_data(filepath="./files/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
        return words


def run():
    data = read_data(filepath="./files/data.txt")
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    lifes = 7
    
    while True:
        os.system("clear")
        print("¡Adivina la palabra!")
        print("Tienes: " + str(lifes) + " vidas")
        if lifes == 7: #Here starts the art
            print('''
 +----+
 |    |
      |
      |
      |
      |
=========''')
        elif lifes == 6:
            print('''
 +----+
 |    |
 O    |
      |
      |
      |
=========''')
        elif lifes == 5:
            print('''
 +----+
 |    |
 O    |
 |    |
      |
      |
=========''')
        elif lifes == 4:
            print('''
 +----+
 |    |
 O    |
/|    |
      |
      |
=========''')
        elif lifes == 3:
            print('''
 +----+
 |    |
 O    |
/|\   |
      |
      |
=========''')
        elif lifes == 2:
            print('''
 +----+
 |    |
 O    |
/|\   |
/     |
      |
=========''')
        elif lifes == 1:
            print('''
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
=========''')
        elif lifes == 0:
            print('''
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
    =====''')


        for element in chosen_word_list_underscores:
            print(element + "", end="")
        print("\n")

        try:
            letter = input("Ingresa una letra: ").strip().upper()
            assert letter.isalpha(), input("Solo puedes ingresar letras")
            assert len(letter) == 1, input("Solo puedes ingresar una letra")
        except AssertionError as e:
            print(e)
            continue

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        else:
            lifes -= 1
            if lifes == -1:
                os.system("clear")

                lose = input("Acabas de perder")
                break            

        if "_" not in chosen_word_list_underscores:
            os.system("clear")
            print("¡Ganaste la palabra era!", chosen_word)
            print('''
 +----+
      |
      |
\O/   |
 |    |
/ \   |
=========''')
            break


if __name__ == '__main__':
    run()