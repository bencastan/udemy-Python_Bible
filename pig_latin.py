# Ask user for sentence
original = input("Enter a sentence to convert to Pig Latin:").strip().lower()
# Split sentence into words
words = original.split()
# Loop through words and convert to pig latin
new_words = []
vowels = "aeiou"
for word in words:
    # If it starts with a  vowel, just add yay
    if word[0] in vowels:
        word = word + "yay"
        new_words.append(word)
    else:
        # Otherwise move the first consonant cluster to the end and add ay
        vowel_pos = 0
        for letter in word:
            if letter not in vowels:
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
# Stick words back into sentence
output = " ".join(new_words)
# Output the sentence
print(output)