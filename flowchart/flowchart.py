#!/usr/bin/env python3

def main():
    while True:
        ans = input("Is it broke\n")
        if ans.lower() == "yes":
            mwi()
            break
        elif ans.lower() == "no":
            final("good")
            break
        else:
            print("That's not a yes or no answer")


def mwi():
    while True:
        ans = input("Did you mess with it?\n")
        if ans.lower() == "yes":
            trouble()
            break
        elif ans.lower() == "no":
            final("good")
            break
        else:
            print("That's not a yes or no answer")


def trouble():
    while True:
        ans = input("Will you get in trouble?\n")
        if ans.lower() == "yes":
            blame()
            break
        elif ans.lower() == "no":
            final("good")
            break
        else:
            print("That's not a yes or no answer")


def blame():
    while True:
        ans = input("Can you blame someone else?\n")
        if ans.lower() == "yes":
            work()
            break
        elif ans.lower() == "no":
            fix()
            break
        else:
            print("That's not a yes or no answer")


def work():
    while True:
        ans = input("Did it work?\n")
        if ans.lower() == "yes":
            final("good")
            break
        elif ans.lower() == "no":
            final("bad")
            break
        else:
            print("That's not a yes or no answer")


def fix():
    while True:
        ans = input("Can you get someone else to fix it?\n")
        if ans.lower() == "yes":
            final("good")
            break
        elif ans.lower() == "no":
            hide()
            break
        else:
            print("That's not a yes or no answer")


def hide():
    while True:
        ans = input("Can you hide it?\n")
        if ans.lower() == "yes":
            work()
            break
        elif ans.lower() == "no":
            self_fix()
            break
        else:
            print("That's not a yes or no answer")


def self_fix():
    while True:
        ans = input("Can you fix it?\n")
        if ans.lower() == "yes":
            work()
            break
        elif ans.lower == "no":
            final("bad")
            break
        else:
            print("That's not a yes or no answer")


def final(ans):
    print("You're screwed" if ans == "bad" else "Then theres no problem")


main()

