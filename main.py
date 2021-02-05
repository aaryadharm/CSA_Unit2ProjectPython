import pygame
import random

pygame.init()

from pygame.locals import *
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Hangman Game")
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 30) #initializes the font used throughout the game
startx=100 #is a starting x coordinate which allows the entire game to move together if we wanted to shift everything
starty=100 #is a starting y coordinate which allows the entire game to move together if we wanted to shift everything
thickness=5 #is a variable that determines the thickness that every line in the hangman will be
randomWords = ['csa','coding','java','method','python','class','variable','hangman'] #list of random words that the hangman game can choose between
guess = '' #creates a blank string for for guess
used_letters = '' #creates a blank string for used letters
stopGame = False #keeps game running
letterCount = 0 #is the variable that checks if the letter count is equal to the length of the string
part_num = 1 #is the variable that determines which next body part to add to the hangman
word = random.choice(randomWords) #chooses a random word from the randomWords list
win = 0 #determines whether the user won or not

def setUp(startx, starty, thickness):
  '''This function makes the hanging drawing'''
  pygame.draw.rect(screen, (255, 255, 255), (startx - 50,starty + 200,150,thickness), 0)
  pygame.draw.rect(screen, (255, 255, 255), (startx,starty,thickness,200), 0)
  pygame.draw.rect(screen, (255, 255, 255), (startx,starty,60,thickness), 0)
  pygame.draw.rect(screen, (255, 255, 255), (startx + 55,starty,thickness,20), 0)

def displayBlanks (numBlanks):
  '''This function makes the appropriate number of blanks according to the number of letters in the word'''
  for i in range(numBlanks):
    pygame.draw.rect(screen, (255, 255, 255), (startx - 50 + (75*i),starty + 300,50,thickness), 0)

def addPart(partNumber):
  '''This Function adds a part to the hangman and is called when the user guesses a wrong letter'''
  global stopGame
  if (partNumber==1):
    pygame.draw.circle(screen, (255, 255, 255), (startx+57, starty + 45), 25, 0)
  elif (partNumber==2):
    pygame.draw.rect(screen, (255,255,255), (startx+55, starty+70, thickness, 75))
  elif (partNumber==3):
    pygame.draw.rect(screen, (255,255,255), (startx+30, starty+100, 55, thickness))
  elif (partNumber==4):
    pygame.draw.line(screen, (255,255,255), (startx+58, starty+143), (startx+30, starty+170), thickness)
  elif (partNumber==5):
    pygame.draw.line(screen, (255,255,255), (startx+55, starty+143), (startx+83, starty+170), thickness)
  else:
    stopGame = True

def attempt(guess):
  '''Checks if the letter is in the word. If it isn't then it will add a part to the hangman game'''
  global part_num
  global used_letters
  isIn = False
  count = 0
  index = 0
  correctLetter = ''
  if (guess not in used_letters):
    '''only runs if the user has not already tried that letter'''
    used_letters += guess + ", " 
    for letter in word: 
      '''iterates through each letter in the word and causes different actions to occur if the letter is the same as guess or not'''
      if guess is letter:
        isIn = True
        index = count
        correctLetter = letter
        displayLetter(correctLetter, index)
      count+=1
    if (not isIn):
      '''checks if any letter was guessed correctly, if not, then a body part is added'''
      addPart(part_num)
      part_num += 1
  displayUsedLetters(used_letters)
  
def displayLetter(letter,index):
  '''Displays letters onto the blanks if they are correct'''
  global letterCount
  newLetter = myfont.render(letter , False, (255,255,255))
  screen.blit(newLetter, (startx - 110 +(75*(index+1)), starty + 260))
  letterCount+=1
  

def displayUsedLetters(used_letters):
  '''Displays letters so user knows what letters were already tried'''
  usedLetter = myfont.render(used_letters , False, (255,255,255))
  screen.blit(usedLetter, (startx + 200, starty + 100))


def check(guess):
  '''Checks if a letter is typed and displays it onto the screen'''
  if event.type == pygame.KEYDOWN:
    guess = event.unicode
  if len(guess) == 1:
    attempt(guess)

while True:
  for event in pygame.event.get():
    setUp(startx, starty, thickness)
    displayBlanks(len(word))
    instructions = myfont.render('enter a letter', False, (255,255,255))
    screen.blit(instructions, (startx + 150, starty - 50))
    used_letter = myfont.render('used letters:', False, (255,255,255))
    screen.blit(used_letter, (startx + 200, starty + 50))
    
    if (not stopGame):
      '''checks if the number of correct letters is equal to the length of the word'''
      check(guess)
      if(letterCount == len(word)):
        '''makes the user win and stops the game'''
        win = 1
        stopGame = True
    else:
      '''stops the game by displaying text that they either won or lost'''
      pygame.draw.rect(screen, (1,1,1), (startx+110, starty-50, 400, 300))
      if (win == 1):
        winningText = myfont.render('Congrats You Won', False, (255,255,255))
        screen.blit(winningText, (startx + 200, starty + 100))
      else:
        losingText = myfont.render('You Lose', False, (255,255,255))
        screen.blit(losingText, (startx + 200, starty + 100))

  pygame.display.update()
  
