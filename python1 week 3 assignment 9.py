# Ask the user to enter a single character
char = input("Enter a single character: ").lower()

# Check if the character is a vowel or consonant
if char in ['a', 'e', 'i', 'o', 'u']:
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.") 