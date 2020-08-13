#!/usr/bin/env python
import os

clear = lambda: os.system('clear')

heros =[0,0,0,0]
questions = [
"What is your preferred profession \n 1.Entrepreneur\n 2.Journalist\n 3.Scientist\n 4.Photographer\n", 
"Which color do you prefer more \n 1.Black\n 2.Blue\n 3.Green\n 4.Red\n", 
"What is your preffered method of transportation\n 1.Car\n 2.Flight\n 3.Walking\n 4.Something more acrobatic\n", 
"Who is your ideal nemesis\n 1.Insane but brilliant\n 2.The smartest man alive\n 3.Genius with Psionic powers\n 4.Super strength and endurance\n", 
"Which of these is your favorite creature\n 1.Bat\n 2.Bird\n 3.Mouse\n 4.Spider\n" ]

def main():
    for string in questions :
        while(True):
            ans = input(string)
            clear()
            if(ans > 0 and ans < 5):
                heros[(ans-1)] = heros[(ans-1)]+1
                break
    index = heros.index(max(heros))
    if index == 0:
        print("You are Batman\n")
    elif index == 1:
        print("You are Superman\n")
    elif index == 2:
        print("You are the Incredible Hulk\n")
    else:
        print("You are Spiderman\n")

main()

