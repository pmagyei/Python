favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(F"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title() # value of the name is the key
        print(f"\t{name.title()}, I see you love {language}")

    if 'erin' not in favourite_languages.keys():
        print("Erin, please take your poll!\n")


# for name in friends:
#     language = favourite_languages[name].title()
#     print(f"\t{name.title()}, I see you love {language}")

for name in sorted(favourite_languages.keys()):
    print(f"\t{name.title()}, thank you for taking the poll.")