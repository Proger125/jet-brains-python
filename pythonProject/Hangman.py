import random

if __name__ == '__main__':
    wons = 0
    losts = 0
    print("H A N G M A N  # 8 attempts")
    while True:
        command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if command == "play":
            attempts = 8
            words = ("python", "java", "swift", "javascript")
            random_word = words[random.randint(0, len(words) - 1)]
            word = list("-" * len(random_word))
            used_letters = set()
            while attempts >= 0:
                is_contains = False
                print("".join(word))
                letter = input("Input a letter:")
                if len(letter) != 1:
                    print("Please, input a single letter.")
                    continue
                if not letter.isalpha() or letter.upper() == letter:
                    print("Please, enter a lowercase letter from the English alphabet.")
                    continue
                for i in range(len(word)):
                    if letter == random_word[i]:
                        if letter in used_letters:
                            print("You've already guessed this letter.")
                        else:
                            word[i] = letter
                        is_contains = True
                if not is_contains:
                    attempts -= 1
                    if letter in used_letters:
                        print("You've already guessed this letter.")
                    else:
                        print("That letter doesn't appear in the word.  #{} attempts".format(attempts))
                used_letters.add(letter)
                print()
                if attempts == 0:
                    losts += 1
                    print("You lost!")
                    break
                if "-" not in word:
                    wons += 1
                    print("".join(word))
                    print("You guessed the word {}!".format("".join(word)))
                    print("You survived!")
                    break
        elif command == "results":
            print("You won: {} times".format(wons))
            print("You lost: {} times".format(losts))
        else:
            break
