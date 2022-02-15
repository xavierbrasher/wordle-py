from random import randint

words = []
prev_responce = ""

def readWords():
    with open("words.txt", "r") as f:
        words_with_endline_statement = f.readlines()
        for i in range(len(words_with_endline_statement)):
            tmp = ""
            for j in range(len(words_with_endline_statement[i])):
                if words_with_endline_statement[i][j] == "\n":
                    break
                tmp += words_with_endline_statement[i][j]
            words.append(tmp)
        words.sort()

def wordToBlank(str):
    tmp = ""
    for i in range(len(str)):
        tmp += "⬛"
    return tmp

def spacedOut(str):
    tmp = ""
    for i in range(len(str)):
        if i == len(str):
            tmp += str[i]
        else:
            tmp += " " + str[i] + " "
    return tmp
        

def GetColors(word:str, guess:str = "EMPTYGUESS"):
    if guess == "EMPTYGUESS":
        prev_responce = "⬛ ⬛ ⬛ ⬛ ⬛"
        return prev_responce
    elif word == guess:
        return spacedOut(guess) + "\n" + "🟩 🟩 🟩 🟩 🟩 "
    else:
        check_for_greens = ""
        for i in range(0,5):
            if word[i] == guess[i]:
                check_for_greens += "🟩 "
            else:
                check_for_greens += "⬛ "
        prev_responce = spacedOut(guess) + "\n" + check_for_greens
        return prev_responce

def playAgain():
    if input("Would you like to play again? (y/n)").lower() == "y":
        main()
    else:
        print("Goodbye :)")


def main():
    guesses = 6
    #word = words[randint(0, len(words) - 1)]
    word = "their"
    won = False
    print(word)
    wordUnder = GetColors(word)

    while guesses > 0 and not won: 
        print("Guesses Left:", str(guesses))
        print(wordUnder)
        guess = input("Enter your guess:")
        if guess == word:
            won = True
            print(GetColors(word, guess))
        elif len(guess) != 5:
            print("Enter a 5 digit word")
        elif not words.__contains__(guess): 
            print("Enter a valid word")
        else:
            wordUnder = GetColors(word, guess)
            guesses -= 1
    if not won:
        print("Damn you lost. The word was", word)
    else:
        print("Good job :)")

if __name__ == "__main__":
    readWords()
    main()