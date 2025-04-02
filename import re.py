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

def from_pig_latin(word):
    if "-" in word:
        parts = word.split("-")
        if parts[1].endswith("ay"):
            return parts[1][:-2] + parts[0]
        return parts[0]  # Handling cases like vowel-starting words
    return word

def detect_language(phrase):
    words = phrase.split()
    if all("-" in word and (word.endswith("ay") or word.endswith("yay")) for word in words):
        return "Pig Latin"
    return "English"