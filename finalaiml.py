import random
import easygui

def choose_team():
    teams = ["RCB", "MI", "DC", "KKR", "PBKS", "SRH", "RR", "CSK", "LSG", "GT"]
    return random.choice(teams)

def display_team(team, guessed_letters):
    display = ""
    for letter in team:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    easygui.msgbox("Welcome to the IPL Team Abbreviation Guessing Game!", "IPL Game")
    score = 0
    attempts_per_game = 6
    total_teams = 10

    while True:
        team = choose_team()
        guessed_letters = []
        attempts = attempts_per_game

        while attempts > 0:
            message = "The abbreviation has {} letters: {}\n\nGuess a letter:".format(len(team), display_team(team, guessed_letters))
            guess = easygui.enterbox(message, "IPL Game").upper()

            if len(guess) != 1 or not guess.isalpha() or guess not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                easygui.msgbox("Please enter a single letter.", "IPL Game")
                continue

            if guess in guessed_letters:
                easygui.msgbox("You've already guessed that letter.", "IPL Game")
                continue

            guessed_letters.append(guess)

            if guess in team:
                easygui.msgbox("Correct!", "IPL Game")
                if "_" not in display_team(team, guessed_letters):
                    score += 1
                    easygui.msgbox("Your score: {}".format(score), "IPL Game")
                    break
            else:
                attempts -= 1
                easygui.msgbox("Incorrect!\nYou have {} attempts left.".format(attempts), "IPL Game")

        if score == total_teams:
            easygui.msgbox("Congratulations! You've guessed all abbreviations correctly!", "IPL Game")
            break

        play_again = easygui.buttonbox("Do you want to play again?", "IPL Game", choices=["Yes", "No"])
        if play_again == "No":
            break

if __name__ == "__main__":
    main()
