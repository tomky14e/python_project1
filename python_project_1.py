"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Matějíček
email: tomas.matejicek@hotmail.com
discord: tomas_38052

"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

number_of_texts = len(TEXTS)
line_separator = '-' * 40
special_characters = ",.-!/()%ˇ´"

registered_users = {
    'bob' : '123', 
    'ann' : 'pass123', 
    'mike' : 'password123', 
    'liz' : 'pass123'
}

user_name = input('User name: ')
user_password = input('Password: ')

if not (
    user_name in registered_users.keys() \
    and registered_users.get(user_name) == user_password
    ):
    print('Unregistered user, terminating the program..')
else:
    print(
        line_separator,
        f'Welcome to the app, {user_name.capitalize()}!', 
        f'We have {number_of_texts} texts to be analyzed.',
        line_separator,
        sep="\n"
    )

    chosen_text = (
        input(f'Enter a number btw. 1 and {number_of_texts} to select: '))

    print(line_separator)

    if not (
        chosen_text.isnumeric() \
        and int(chosen_text) in range(1, number_of_texts + 1)
        ):
        print(f'Invalid selection "{chosen_text}", terminating the program..')
    else:
        words_clean = [
        word.strip(special_characters)
        for word in TEXTS[int(chosen_text) - 1].split()
        ]
        words = {   
            "words": 
                len(words_clean),
            "words_title": 
                sum(1 for word in words_clean if word.istitle()),
            "words_upper": 
                sum(1 for word in words_clean if word.isupper()),
            "words_lower": 
                sum(1 for word in words_clean if word.islower()),
            "words_numeric": 
                sum(1 for word in words_clean if word.isnumeric()),
            "words_numeric_sum": 
                sum(int(word) for word in words_clean if word.isnumeric())
        }

        words_len = {
            len(word):
            sum(1 for occurrence in words_clean 
            if len(occurrence) == len(word))
            for word in words_clean
        }

        print(
            f'There are {words["words"]} words in the selected text.',
            f'There are {words["words_title"]} titlecase words.',
            f'There are {words["words_upper"]} uppercase words.',
            f'There are {words["words_lower"]} lowercase words.',
            f'There are {words["words_numeric"]} numeric strings.',
            f'The sum of all the numbers {words["words_numeric_sum"]}.',
            line_separator,
            sep="\n"
        )

        print(
            f'LEN |{"OCCURRENCES".center(max(words_len.values()) + 2)}| NR.',
            line_separator,
            sep="\n"
        )
        
        for length in sorted(words_len):
            print(
                f'{str(length).ljust(3)}',
                f'|{("*" * words_len[length]).ljust(max(words_len.values()) + 2)}|',
                f'{words_len[length]}'
            )

    
    
    
    
    
    
    



    # words = {
#     "words": 0,
#     "words_title": 0,
#     "words_upper": 0,
#     "words_lower": 0,
#     "words_numeric": 0,
#     "words_numeric_sum": 0
# }

    # for word in words_clean:
    #         words["words"] += 1
    #         if word.istitle():
    #             words["words_title"] += 1
    #         elif word.isupper():
    #             words["words_upper"] += 1
    #         elif word.islower():
    #             words["words_lower"] += 1
    #         elif word.isnumeric():
    #             words["words_numeric"] += 1
    #             words["words_numeric_sum"] += int(word)