# nest a list inside a dictionary any
favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'], 
    'edward': ['ruby', 'go'], 
    'phil' : ['python'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n {name.title()}'s favorite languages is: ")
    else:
        print(f"\n {name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t {language.title()}")
