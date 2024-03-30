import random


def choose_word_from_file(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
    return random.choice(words).strip().lower()


def main():
    filename = 'words.txt'

    word = choose_word_from_file(filename)
    print(word)
    display_word = []
    for letter in word:
        display_word += "_"
    print(display_word)

    game_over = False
    while not game_over:
        guess = input("Guess a letter ").lower()
        letter_found = False

        for position in range(len(word)):
            letter = word[position]
            if letter == guess:
                display_word[position] = letter
                letter_found = True

        print(display_word)

        if not letter_found:
            print(f"The letter '{guess.upper()}' is not in the word.")

        if "_" not in display_word:
            print("Congratulations!!!! You won.")
            game_over = True


if __name__ == "__main__":
    main()
