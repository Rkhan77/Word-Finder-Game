import random
import string
import json
import enchant

def select_letters():
    letter_weights = (9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1)
    chosen_letters = random.choices(string.ascii_uppercase, weights=letter_weights, k=9)
    return chosen_letters

def display_letters(letters):
    print(" | ".join(letters[0] + letters[1] + letters[2]).center(42))
    print("---------".center(42))
    print(" | ".join(letters[3] + letters[4] + letters[5]).center(42))
    print("---------".center(42))
    print(" | ".join(letters[6] + letters[7] + letters[8]).center(42))

def validate_word(word, letters):
    C_letters = letters.copy()
    for letters in word:
        if letters not in C_letters:
            return False
        C_letters.remove(letters)
    return True

if __name__ == '__main__':
    score = 0
    used_words = []
    letters = select_letters()
    user_input = None
    hard_mode = False
    print("Welcome to word find\nCome up with as many word as possible.")
    while True:
        choice = input('Do You Wish To Play [E]asy mode or [H]ard mode?\n:> ').strip().upper()
        if choice == 'H':
            print('Hard Mode Selected! Entering an invalid word will end the game')
            hard_mode = True
            break

        elif choice == 'E':
            print('Easy Mode Selected!')
            break

        else:
            print('Invalid input. Please Select a Mode! \n')

    while user_input != 'E':
        print(f"Score: {score}  Your letters are:")
        display_letters(letters)
        user_input = input("Enter a word, [s]huffle letters, [l]ist words, or [e]nd game: ").upper()

        if user_input == "E":
            print("Ending game…")
            break

        elif user_input == 'S':
            print("Shuffle letters")
            random.shuffle(letters)

        elif user_input == "L":
            if len(used_words) == 0:
                print("You have not yet entered any words.")
                continue
            else:
                used_words.sort()
                print("Previously entered words:")
                for word in used_words:
                    print("  - " + word)

        elif len(user_input) < 3 or user_input == int:
            print("you have not yet entered any words")
            continue

        elif user_input in used_words:
            print("The word has been previously used. Try another word.")
            continue

        elif not validate_word(user_input, letters):
            print("Invalid characters used!")
            if hard_mode is True:
                print('Game Over')
                break

        else:
            d = enchant.Dict("en_US")
            correct_word = d.check(user_input)
            scrabble_score = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
                              'k': 5,
                              'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
                              'v': 8,
                              'w': 4, 'x': 8, 'y': 4, 'z': 10}

            if correct_word is True:
                total = 0
                for chars in user_input.lower():
                    points = int(scrabble_score.get(chars))
                    total += points
                score += total
                print(f'{user_input} is accepted. - {total} points awarded. your score is now {score}')
                used_words.append(user_input)

            if correct_word is False and hard_mode is True:
                print('Game Over')
                break

        if score >= 50:
            try:
                jsonFile = open("logs.txt", "r")
                jsonData = json.load(jsonFile)
                jsonFile.close()
            except:
                jsonData = []

            jsonData.append({"letters": letters, "words": used_words, "score": score})

            jsonFile = open("logs.txt", "w")
            json.dump(jsonData, jsonFile)
            jsonFile.close()

    print("Your final score was " + str(score))
    print("Thank you for playing!")

# if __name__ == '__main__':
# main()
