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


def translate_phrase(phrase):
    language = detect_language(phrase)
    words = phrase.split()
    
    if language == "English":
        translated_words = [to_pig_latin(word) for word in words]
        print("English detected. Translating to Pig Latin.")
    else:
        translated_words = [from_pig_latin(word) for word in words]
        print("Pig Latin detected. Translating to English.")
    
    return " ".join(translated_words)


def main():
    while True:
        phrase = input("Please enter a phrase to be translated:\n")
        translation = translate_phrase(phrase)
        print("Translation:", translation)
        
        again = input("Would you like to translate again? (Y/N)\n").strip().lower()
        if again != 'y':
            print("Goodbye.")
            break

if __name__ == "__main__":
     main()

