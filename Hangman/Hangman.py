# Problem Set 2, hangman.py
# Name: Eve Bogdanova
# Collaborators: only me
# Time spent: 7-10 hours

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing; assumes all letters are lowercase
  letters_guessed: list (of letters), which letters have been guessed so far;
  assumes that all letters are lowercase
  returns: boolean, True if all the letters of secret_word are in letters_guessed;
  False otherwise
  '''
  secret_word_letters = list(secret_word)
  result = [True for x in secret_word_letters if x in letters_guessed]
  if len(result) == len(secret_word_letters):
      return True
  else:
      return False


def get_guessed_word(secret_word, letters_guessed):
  '''
secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
  '''
  word = ["_" for x in secret_word]
  for let in letters_guessed:
    if let in secret_word:
      index = [i for i,ch in enumerate(secret_word) if ch==let]
      for i in index:
        word[i]=let
  return ' '.join(word)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in letters_guessed:
        if let in letters:
            letters.remove(let)
        else:
            pass   
    return ' '.join(letters)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!\nI am thinking of a word that is',f'{ len(secret_word) }','letters long\nYou have 3 warnings left.')
    import time
    guesses = 6
    warnings = 3
    got_letters = []
    used_letters = []
    while guesses > 0:
        print('\n--------------------------\nYou have',guesses,'guesses left.\nAvailable letters: ', get_available_letters(used_letters))
        print(draw_hangman(guesses))
        inp = input('Please, guess a letter: ')
        letter = inp.lower()
        if letter.isalpha() == True and len(letter) == 1:
          if letter in secret_word:
            if letter in used_letters:
              warnings-=1
              print('Oops! You have already guessed that letter.\nYou have',warnings,'warnings left: ',get_guessed_word(secret_word,got_letters))
              continue
            else:
              got_letters.append(letter)
              used_letters.append(letter)
              if is_word_guessed(secret_word, got_letters) == False:
                print('Good guess: ',get_guessed_word(secret_word,got_letters))
                continue
              else:
                score = guesses*len(got_letters)
                print('Good guess: ',get_guessed_word(secret_word,got_letters))
                print('\n--------------------------\nCongratulations, you won! Your total score for this game is: ',score) 
                time.sleep(20)
                break
          elif letter not in secret_word and letter in used_letters:
            if warnings==0:
              guesses = guesses-1
              print('Oops! You\'ve already guessed that letter.\nYou have no warnings left so you lose one guess: ',get_guessed_word(secret_word,got_letters))
            else:
              warnings-=1
              print('Oops! You have already guessed that letter.\nYou have',warnings,'warnings left: ',get_guessed_word(secret_word,got_letters))
            continue
          else:  
            used_letters.append(letter)
            vowels = ['a','e','i','o','u']
            if letter in vowels:
              guesses-=2
            else:
              guesses-=1
            print('Oops! That letter is not in my word: ',get_guessed_word(secret_word,got_letters))
            continue  
        else:
          if warnings<0:
            guesses = guesses-1
            print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess: ',get_guessed_word(secret_word,got_letters))
          else:
            warnings = warnings-1  
            print('Oops! That is not a valid letter. You have',warnings,'warnings left: ',get_guessed_word(secret_word,got_letters))
    if guesses==0:
      print(draw_hangman(guesses))
      print('\nSorry, you ran out of guesses. The word was else: ',secret_word,'\nThe window game will be closed in 20 seconds')
      time.sleep(20)   

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ','')
    if len(my_word)==len(other_word):
      space = [i for i,ch in enumerate(my_word) if ch=='_']
      compare = list(map(lambda x,y: x==y,my_word,other_word))
      compare = list(filter(lambda x: x==True,compare))
      if len(compare)==len(other_word)-len(space):
        return True
      else:
        return False
    else:
      return False  

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for word in wordlist:
      if match_with_gaps(my_word, word)==True:
        matches.append(word)
    return ' '.join(matches)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!\nI am thinking of a word that is',f'{ len(secret_word) }','letters long\nYou have 3 warnings left.')
    import time
    guesses = 6
    warnings = 3
    got_letters = []
    used_letters = []
    while guesses > 0:
        print('\n--------------------------\nYou have',guesses,'guesses left.\nAvailable letters: ', get_available_letters(used_letters))
        print(draw_hangman(guesses))
        inp = input('Please, guess a letter: ')
        letter = inp.lower()
        if letter.isalpha() == True and len(letter) == 1:
          if letter in secret_word:
            if letter in used_letters:
              warnings-=1
              print('Oops! You have already guessed that letter.\nYou have',warnings,'warnings left: ',get_guessed_word(secret_word,got_letters))
              continue
            else:
              got_letters.append(letter)
              used_letters.append(letter)
              if is_word_guessed(secret_word, got_letters) == False:
                print('Good guess: ',get_guessed_word(secret_word,got_letters))
                continue
              else:
                score = guesses*len(got_letters)
                print('Good guess: ',get_guessed_word(secret_word,got_letters))
                print('\n--------------------------\nCongratulations, you won! Your total score for this game is: ',score) 
                time.sleep(20)
                break
          elif letter not in secret_word and letter in used_letters:
            if warnings==0:
              guesses = guesses-1
              print('Oops! You\'ve already guessed that letter.\nYou have no warnings left so you lose one guess: ',get_guessed_word(secret_word,got_letters))
            else:
              warnings-=1
              print('Oops! You have already guessed that letter.\nYou have',warnings,'warnings left: ',get_guessed_word(secret_word,got_letters))
            continue
          else:  
            used_letters.append(letter)
            vowels = ['a','e','i','o','u']
            if letter in vowels:
              guesses-=2
            else:
              guesses-=1
            print('Oops! That letter is not in my word: ',get_guessed_word(secret_word,got_letters))
            continue  
        else:
          if letter == '*':
            print('Possible word matches are: ',show_possible_matches(get_guessed_word(secret_word,got_letters)))
            continue
          else:
            if warnings<0:
              guesses = guesses-1
              print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess: ',get_guessed_word(secret_word,got_letters))
            else:
              warnings = warnings-1  
              print('Oops! That is not a valid letter. You have',warnings,'warnings left: ',get_guessed_word(secret_word,got_letters))
    if guesses==0:
      print(draw_hangman(guesses))
      print('\nSorry, you ran out of guesses. The word was else: ',secret_word,'\nThe window game will be closed in 20 seconds')
      time.sleep(20)   


def draw_hangman(n):
  if n == 5:
    print(

    ' ║ '
    '\n ║ '
    '\n ║ '
    '\n ║ '
    '\n ║ '
    '\n ║ '  
    '\n ║'
    )
  elif n == 4:    
    print(
    ' ╔════════'
    '\n ║ '
    '\n ║ '
    '\n ║ '
    '\n ║ '
    '\n ║ '
    '\n ║ '  
    '\n ║'
    )
  elif n ==3:
    print(

    ' ╔════════'
    '\n ║      |'
    '\n ║      |'
    '\n ║ '
    '\n ║ '
    '\n ║ '
    '\n ║ '  
    '\n ║'
    )
  elif n == 2:  
    print(

    ' ╔════════'
    '\n ║      |'
    '\n ║      |'
    '\n ║      O'
    '\n ║     / \\'
    '\n ║'
    '\n ║'  
    '\n ║'
    )
  elif n == 1:  
    print(

    ' ╔════════'
    '\n ║      |'
    '\n ║      |'
    '\n ║      O'
    '\n ║     /H\\'
    '\n ║ '
    '\n ║ '  
    '\n ║'
    )
  elif n == 0:
    print(

    ' ╔════════'
    '\n ║      |'
    '\n ║      |'
    '\n ║      O'
    '\n ║     /H\\'
    '\n ║      |'
    '\n ║     /"\\'  
    '\n ║'
    )
  else:
    pass
  return ''

if __name__ == "__main__":
    inp = input('\nChoose game mode (R for regular hangman and H for hangman with hints): ')
    start = inp.upper()
    if start == 'R':
      secret_word = choose_word(wordlist)
      hangman(secret_word)
    elif start == 'H':
      secret_word = choose_word(wordlist)
      hangman_with_hints(secret_word)
    else:
      import time
      print('\nSee you next time!')
      time.sleep(5)
