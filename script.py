# -*- coding: utf-8 -*-
import nltk
import re
from num2words import num2words
import mishkal.tashkeel
from PersianG2p import Persian_g2p_converter

vocalizer = mishkal.tashkeel.TashkeelClass()

file = open("tweets.txt",encoding="utf8") 

data = file.read()

def remove_emoji(string):
    emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


nltk_tokanize = nltk.sent_tokenize(data)

numbers = ['0','1','2','3','4','5','6','7','8','9']


for sent in nltk_tokanize:
    # normalization 
      print(sent)
      temp = sent.strip()
      temp = remove_emoji(temp)
      for num in numbers:
          if num in temp:
              temp=re.sub(num ,num2words(int(num),lang='ar'),temp)
      print("[tweet after normalize]")
      print(temp)
      tweet_tashkeel =vocalizer.tashkeel(temp)
      print("[tweet after add diacritics]")
      print(tweet_tashkeel)
      print("[converted tweet from grapheme to phoneme]")
      print(Persian_g2p_converter().transliterate(tweet_tashkeel , secret = True))
      print("____________________________________________________________________")
      
