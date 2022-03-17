## Make a program which will counts the words frequency (the count) of a given text

s1= ('''apple and banana one apple one banana
a red apple and a green apple''')

s2=s1.strip() # изчистване на шпации
print(s2)
words_list=s2.split() # list of words
print(words_list)
set_words_list=set(words_list) # set от tuple --> изчистване на дублирани думи
# print(set_words_list)
dict_word={} # деклариране на празен dictionary

for word in set_words_list: # формиране на dictionary с key = words, value =0
    dict_word[word]=0

for word in words_list:  # промяна на dictionary  --> key = words, value = броя на думите
    dict_word[word]  +=1

for k,v in dict_word.items():
    # print(f"|{k}|{v}|")    # необходимо форматиране за подравняване в таблица!!!
    print("|%10s|%10d|" % (k,v) )