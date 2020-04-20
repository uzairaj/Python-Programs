'''

Input: a list of words 
Return: the lower case letter that appears most frequently, total number of occurrences of a letter in the words in 𝚠𝚘𝚛𝚍_𝚕𝚒𝚜𝚝.
In the case of ties, return the earliest letter in alphabetical order

 
'''

def count_letters(word_list):

    alphabets_list = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in alphabets_list:
        letter_count[letter] = 0
        
    # enter code here
    for word in word_list:
        letters = list(word)
        for letter in letters:
            if letter in alphabets_list:
                letter_count[letter] += 1
        

#   print(letter_count)

    letter_total_count = 0
    letter_value = ''

    for key, value in letter_count.items():
        if letter_count[key] > letter_total_count:
            letter_total_count = value
            letter_value = key
     
    print(letter_value, letter_total_count)
    return letter_value, letter_total_count       

sentence = "Hope you are doing well. I would like to request you to forward this email to the student body of IBA kindly."
word_list = sentence.split(" ")
print(word_list)
print(count_letters(word_list))
