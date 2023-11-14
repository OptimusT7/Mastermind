import random

TORANGE = "\033[1;30;33m"
TYELLOW = "\033[1;33m"
TGREEN = '\33[1;92m'
TNOEFFECT = "\033[0m"
TBLACK = '\33[30m'
TWHITE = '\33[97m'
TBLACKBG = '\33[40m'
TWHITEBG = '\33[107m'

loop = 'y'
guess = ""
all_pegs = [
    "R",
    "O",
    "Y",
    "G",
    "B",
    "P",
    "S",
    "L",
    "M",
    "C",
    "V",
    "T",
]
all_colours = [
    "(R)ed",
    "(O)range",
    "(Y)ellow",
    "(G)reen",
    "(B)lue",
    "(P)urple",
    "(S)ilver",
    "(L)ime",
    "(M)agenta",
    "(C)yan",
    "(V)iolet",
    "(T)urquoise",
]


def split(word):
    global char
    return [char for char in word]


print(f"{TGREEN}Welcome to MASTERMIND!{TNOEFFECT}")

while loop == 'y':
    pegs_list = []
    colours = []
    pegs_num = input(
        "\nHow many pegs did you want to be selected? There will be 2 more possible colours. "
        "(Standard: 4, Min: 2, Max: 10): "
    )
    while not pegs_num.isdigit() or int(pegs_num) not in range(2, 11):
        pegs_num = input(
            "Please enter a whole number between 2 and 10 (inclusive of)\n\n"
            "How many pegs did you want to be selected? (Standard: 4, Min: 2, Max: 10): "
        )

    pegs_num = int(pegs_num)
    max_guesses = (int(pegs_num) * 3) - 2

    for x in range(0, pegs_num + 2):
        pegs_list.append(all_pegs[x])
        colours.append(all_colours[x])

    pegs = "".join(pegs_list)
    colours = ", ".join(colours)

    print(
        f"\nI will select {pegs_num} coloured pegs from the following colours:\n{colours}\n"
        f"\nBut you only have {max_guesses} guesses."
        f"\nIf you can't guess the pegs in {max_guesses} guesses, then I win!\n\n"
        "Ready? Then let's go..."
    )

    guess_num = 0
    guesses = 0

    solution_pegs = random.choices(pegs, k=int(pegs_num))
    solution = "".join(solution_pegs)

    print("\nOK, I've chosen my colours. What's your guess?", end="")
    # print(f"Solution: {solution}")
    while guesses < max_guesses:
        guess_num += 1

        successful = False
        while not successful:
            if guess_num == max_guesses:
                guess = input(f"\n{guess_num} - Last Guess! > ").upper().strip()
            else:
                guess = input(f"\n{guess_num}> ").upper().strip()
            successful = True
            if guess == "" or len(guess) != pegs_num:
                successful = False
            for char in guess:
                if char not in pegs_list:
                    successful = False
            if not successful:
                example = "".join(random.choices(pegs_list, k=int(pegs_num)))
                print(f"{TYELLOW}Please only use the characters '{pegs}' (Not Case Sensitive)\n{TNOEFFECT}"
                      f"Example guess: {example} ({pegs_num} Pegs Needed)")

        guesses += 1
        results = [guess + " ="]

        temp_guess = split(guess)
        temp_solution = split(solution)

        for x in range(pegs_num):
            if temp_solution[x] == temp_guess[x]:
                results.append(" " + TBLACKBG + "  " + TNOEFFECT)
                temp_guess[x] = "*"
                temp_solution[x] = "#"

        for x in range(pegs_num):
            if (temp_guess[x] in temp_solution) and (
                    temp_guess[x] not in temp_solution[x]
            ):
                results.append(" " + TWHITEBG + "  " + TNOEFFECT)
                solution_x = temp_solution.index(temp_guess[x])
                temp_solution[solution_x] = "#"
                temp_guess[x] = "*"

        print(*results, sep="")

        if guess == solution:
            if guesses == 1:
                print(f"{TGREEN}\nOutstanding! You got it first try!{TNOEFFECT}")
            else:
                print(
                    f"{TGREEN}\nWell done! You got it. It took you {guesses} guesses.{TNOEFFECT}"
                )

            break

        if guesses == max_guesses and guess != solution:
            print(f"{TORANGE}You lost! The solution was {solution}{TNOEFFECT}")

    play_again = input("\nPlay Again? (Y or N)\n> ")
    while not play_again.isalpha() or (
            play_again != "Y"
            and play_again != "N"
            and play_again != "y"
            and play_again != "n"
    ):
        play_again = input("Please enter Y or N\n\nPlay Again? (Y or N)\n> ")
    if play_again == "n" or play_again == "N":
        loop = 0
