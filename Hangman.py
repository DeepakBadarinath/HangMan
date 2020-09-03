# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:28:44 2020

@author: deepa
"""

import random
from random import randint
import numpy as np

from bs4 import BeautifulSoup
import requests
def setup_game(word,auto=True,blank_letters=[],blank_indices=[],blank_percent=0.8):
    if(auto==True):
        word_new=word.replace(" ", "")
        #print(word_new)
        length=len(word_new)
        #print(length)
        no_dash_letters=int(length*blank_percent)
        #print(no_dash_letters)
        #list_word_new=list(word_n)
        sampled_letters=random.sample(list(word_new),no_dash_letters)
        #print(sampled_letters)
        final_word=list(word)
        for letter in sampled_letters:
            if letter in word:
                occurences = [i for i in range(len(word)) if word.startswith(letter, i)]
                posn = random.choice(occurences)
                final_word[posn]='_'
            else:
                print("ERRROR NOOB")
                return
        finale="".join(final_word)
        #print(final_word)
        print(finale)
        #print(list(finale))
        return finale
    



def front_end_player(dashed_word,actual_word,no_guesses=6):
    attempts=no_guesses
    guessed_letters=[]
    dashed_word=list(dashed_word)
    while attempts>0:
        print("Remaining word is-: ")
        print("".join(dashed_word))
        print("No of attempts remaining ", attempts)
        print("Guessed letters are")
        print(guessed_letters)
        guess=input("Please guess a letter Player: ")
        if(guess=='end'):
            return
        while guess in guessed_letters:
            print("You have guessed this already, guess again")
            guess=input("Please guess a letter Player: ")
        guessed_letters.append(guess)
        if guess in actual_word:
            occurences = [i for i in range(len(actual_word)) if actual_word.startswith(guess, i)]
            occurences=np.array(occurences)
            #print(occurences)
            for blank in occurences:
                #print("dashed word ", blank," position was ",dashed_word[int(blank)])
                dashed_word[int(blank)]=guess
            print("Correct guess!")
            print("Word now is")
            print("".join(dashed_word))
            if("".join(dashed_word)==actual_word):
                print("You win! The answer is")
                print(actual_word)
                return
        else:
            print("Wrong!")
            attempts=attempts-1
            print("No of attempts remaining ",attempts)
            if attempts == 0:
                print("You Lose!")
                print("Answer is")
                print(actual_word)
                return
            



def get_top_imdb_movie():
    source=requests.get('https://www.imdb.com/chart/top/').text
    soup=BeautifulSoup(source,'lxml')
    inner_movietags=soup.select('td.titleColumn a')
    random_number=randint(0,249)
    #print(random_number)
    return inner_movietags[random_number].text


def get_trending_movie():
    source=requests.get('https://www.imdb.com/chart/moviemeter/').text
    soup=BeautifulSoup(source,'lxml')
    inner_movietags=soup.select('td.titleColumn a')
    random_number=randint(0,99)
    #print(random_number)
    return inner_movietags[random_number].text

def Play():
    print("Welcome Player")
    actual_word=get_top_imdb_movie()
    print("A Top Imdb movie has been selected")
    dashed_word=setup_game(actual_word)
    front_end_player(dashed_word,actual_word)

Play()



"""Skills learnt-:
    String Manipulation
    Data Scraping
    GitHub Repository"""

"""Things to improve on:
    Add songs
    """

    
    
    
    
    
    
    
    
    
    