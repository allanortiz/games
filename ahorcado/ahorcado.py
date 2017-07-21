# -*- coding: utf-8 -*-
import random, os

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        raise "No se puede limpiar la pantalla"
        print  "<-No se pudo borrar la pantalla->"

def random_line(fname = 'palabras.txt'):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def print_board(hidden_word, tries):
    clear_screen()

    print '  EL AHORCADO'
    print IMAGES[tries]
    print ''
    print hidden_word
    print '--- * --- * --- * --- * --- * --- '
    print ''
    print 'Quedan {} intentos.'.format(7 - tries)
    print ''

def run():
    word = random_line()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        print_board(hidden_word, tries)
        current_letter = str(raw_input('Escribe una letra:'))
        letter_indexes = []

        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                print_board(hidden_word, tries)
                print ""
                print '¡Perdiste! La palabra correcta era: {}'.format(word)
                break
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

            try:
                hidden_word.index('-')
            except ValueError:
                print ""
                print '¡Felicidades! Ganaste. La palabra es: {}'.format(word)
                break

    print ''

    if str(raw_input('¿Volver a jugar?:')) == 'si':
        run()


if __name__ == '__main__':
    print 'El AHORCADO'
    run()
