#!/usr/bin/env python3
import fileinput
from googletrans import Translator

f = fileinput.input()

word = f.readline().split(" ")
translator = Translator()


def connect_character(character_index):
    text_list = []
    for start, end in character_index:
        text = [k for k in word[start:end]]
        text_list.append([" ".join(text)])
    return text_list


title_index, url_index = [], [0]
begin_index, end_index = [], []
for count, i in enumerate(word):
    if(i[-4:] == "doi:"):
        title_index.append(count-1)
    elif(i[-9:] == "Abstract:"):
        begin_index.append(count+1)
    elif(i == "keywords:"):
        end_index.append(count)
    elif("http:" in i):
        url_index.append(count+1)

title_index = list(zip(url_index, title_index))
abstract_index = list(zip(begin_index, end_index))

titles = connect_character(title_index)
abstracts = connect_character(abstract_index)

for title, abst in list(zip(titles, abstracts)):
    print("Title: "+title[0], "\n")
    print("Abst: "+abst[0], "\n")
    print("JP_Abst:" +
          translator.translate(abst[0], dest="ja").text, "\n"*5)
