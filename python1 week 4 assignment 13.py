import string

# Prompt the user to enter a word or phrase
text = input("Enter a word or phrase: ")

# Remove spaces, punctuation, and convert to lowercase
translator = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(translator).replace(" ", "").lower()

# Check if the string is a palindrome
if cleaned_text == cleaned_text[::-1]:
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")