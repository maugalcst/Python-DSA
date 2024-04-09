'''
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
'''

def solution(string):
    sol = ""
    string_list = [i for i in string]
    string_list.reverse()

    for letter in string_list:
        sol += letter
    return sol

solution("word")

'''
Mejore práctica: 

def solution(str):
  return str[::-1]

'''
