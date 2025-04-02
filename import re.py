import re

def to_pig_latin(word):
    vowels = "AEIOUaeiou"
    if word[0] in vowels:
        return word + "-yay"
    
    match = re.match(r"[^AEIOUaeiou]+", word)
    if match:
        consonant_cluster = match.group()
        return word[len(consonant_cluster):] + "-" + consonant_cluster + "ay"
    
    return word

