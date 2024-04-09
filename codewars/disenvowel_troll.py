'''
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
'''

def disemvowel(string_):
    resp = ""
    string_list = [i for i in string_]    
    for i in string_list:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U": continue
        else: resp += i
    return resp

'''
Best practices:

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
'''
