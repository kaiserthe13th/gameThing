# -*- coding: utf-8 -*
import random
from sys import platform

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if platform != ("linux" or "linux2"):
    #exit()
    print("The game may not work properly in your operating system.\n\n")

print('An Python Game made to run on Ubuntu Terminal by '+ bcolors.WARNING + 'kaiserthe13th\n\n' + bcolors.ENDC)
print('When you are given choices type the number of the choice')


name = raw_input("What is your name?\n" + bcolors.OKCYAN + '\n\n' + bcolors.FAIL +'>>' + bcolors.ENDC)
print("~Okay! Nice to meet you "+name+".\n\n")

rockPaperScissors = ['rock', 'paper', 'scissors']

def rockPaper():
    RPS = input(bcolors.OKGREEN + '\n1)rock 2)paper 3)scissors\n\n' + bcolors.ENDC)
    comRPS = random.choice(rockPaperScissors)
    if (RPS == 1 and comRPS == 'rock') or (RPS == 2 and comRPS == 'paper') or (RPS == 3 and comRPS == 'scissors'):
        again = input("It's a draw. Can we play once again?"+ bcolors.OKGREEN + "1)no i dont wanna 2)let's play again\n" + bcolors.FAIL + '\n\n>>' + bcolors.ENDC)
        if again <= 1:
            print("Uh, I wanted to play. But it seems this is goodbye.")
            action()
        elif again == 2:
            rockPaper()
    elif (RPS == 1 and comRPS == 'scissors') or (RPS == 2 and comRPS == 'rock') or (RPS == 3 and comRPS == 'paper'):
        again = input("Uhh.. I lost. I will win next time so play with me again, ~please!" + bcolors.OKGREEN + "1)no i dont wanna 2)let's play again\n" + bcolors.FAIL + '\n\n>>' + bcolors.ENDC)
        if again <= 1:
            print("Uh, I wanted to play. But it seems this is goodbye.")
            action()
        elif again == 2:
            rockPaper()
    elif (RPS == 1 and comRPS == 'paper') or (RPS == 2 and comRPS == 'scissors') or (RPS == 3 and comRPS == 'rock'):
        again = input("Kukuku, I won. I'll let you play again!" + bcolors.OKGREEN + "1)no i dont wanna 2)let's play again\n" + bcolors.FAIL + '\n\n>>' + bcolors.ENDC)
        if again <= 1:
            print("Uh, I wanted to play. But it seems this is goodbye.")
            action()
        elif again == 2:
            rockPaper()

funFacts = [
'Sunlight takes about 8.3 minutes to reach the Earth from the surface of the Sun. A photon starting at the centre of the sun and changing direction every time it encounters a charged particle would take between 10 000 and 170 000 years to get to the surface.',
"Cerf proposed the bet and challenged that Dr. Seuss would not be able to write an entertaining children's book using only 50 different words. Dr. Seuss took the bet and won. The result was a little book called Green Eggsand Ham.", "The Hunchback of Notre-Dame (French: Notre-Dame de Paris) is a French Romantic/Gothic novel by Victor Hugo published in 1831. The title refers to the Notre Dame Cathedral in Paris, on which the story is centered.",
"Number 4 is considered an unlucky number in Chinese because it is nearly homophonous to the word 'death' (pinyin si). Due to that, many numbered product lines skip the '4': e.g., Nokia cell phones (there is no series beginning with a 4), Palm PDAs, Canon PowerShot G's series...", "'The Statue of Liberty Enlightening the World' was a gift of friendship from the people of France to the United States and is recognized as a universal symbol of freedom and democracy. The Statue of Liberty was dedicated on October 28, 1886. It was designated as a National Monument in 1924.",
"Bette Nesmith Graham. Bette Claire Graham (March 23, 1924 – May 12, 1980) was an American typist, commercial artist, and the inventor of Liquid Paper. She was also the mother of musician and producer Michael Nesmith of The Monkees.",
"Honey bees do not have sensory organs that can pick up sounds that we can hear.",
"On December 23 1924, the first successful living-related kidney transplant was led by Dr. Joseph Murray and Dr. David Hume at Brigham Hospital in Boston. A kidney was transplanted from Ronald Herrick into his identical twin, Richard.",
"A falling person will reach terminal velocity after about 12 seconds, falling some 450 m (about 1,500 ft) in that time. That person will not then fall any faster, so it makes no difference what distance they fall if it is more than 1,500 ft - they will still reach the ground at the same speed."
]

def funFact():
    if len(funFacts) > 0:
        factVar = random.choice(funFacts)
        print(factVar)
        funFacts.remove(factVar)
        again = input("Do you want more?" + bcolors.OKGREEN + "1)nah 2)I want more" + bcolors.FAIL + '\n\n>>' + bcolors.ENDC)
        if again <= 1:
            print("Okay, ~bye!")
            action()
        elif again == 2:
            if len(funFacts) > 0:
                print("I can do it anytime. No problem!")
                funFact()
            else:
                print("But I've already told you all I know.")
                exitFact = input("Will you go back to actions?" + bcolors.OKGREEN + "1)End Session 2)Go to actions" + bcolors.FAIL + '\n\n>>' + bcolors.ENDC)
                if exitFact <= 1:
                    exit()
                elif exitFact == 2:
                    action()
    else:
        print("You already know everything I can tell you.")
        action()

def aGame():
    print("Hello " + name)

def action():
    choiceIntro = input("Now, what shall we do? What do you think " + name + "?\n" + bcolors.OKGREEN + "1)idk 2)let's play a game 3)Za Warudo 4)Fun Facts" + bcolors.FAIL + '\n\n>>' + bcolors.ENDC)
    if choiceIntro <= 1:
        print("Hello World")
        exit()
    elif choiceIntro == 2:
        print("Let's play rock paper scissors")
        rockPaper()
    elif choiceIntro == 3:
        print("You expected Za Warudo but it was me " + bcolors.WARNING + 'Dio\n\n' + bcolors.ENDC)
        action()
    elif choiceIntro == 4:
        if len(funFacts) > 0:
            print("Let me teach you something.\n")
        funFact()
    elif choiceIntro == 5:
        yesno = input("Would you like to play a game with me?"+bcolors.OKGREEN+"1)Yup 2)No thanks"+bcolors.ENDC)
        if yesno <= 1:
            aGame()
        if yesno == 2:
            action()

action()
