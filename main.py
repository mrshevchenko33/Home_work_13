import string

my_string = input('Enter your letters: ')
my_lst = my_string.split('-')

if '-' not in my_string:
    print('- is missing!')
elif my_lst[0] and my_lst[1] in string.ascii_letters:
    start_letter = string.ascii_letters.index(my_lst[0])
    end_letter = string.ascii_letters.index(my_lst[1])
    result = string.ascii_letters[start_letter:end_letter + 1]
    print(result)
else:
    print('Unknow symbol')