favorite_languages = {
    'jen' : 'python', 
    'sarah' : 'c', 
    'edward': 'ruby', 
    'phil' : 'python',
}

#print(f"Sarah favorite language is {favorite_languages['sarah'].title()}.")

for name, language in sorted(favorite_languages.items()):       #alfabetical order
    print(f"{name.title()}'s favorite language is {language.title()}.")