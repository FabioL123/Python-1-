
def is_palindrome(text):
    # Convert the text to lowercase and remove spaces
    cleaned = text.replace(" ", "").lower()

    # Check if the cleaned text is the same forwards and backwards
    return cleaned == cleaned[::-1]

# Example usage:
word = input("Enter a word or phrase: ")

if is_palindrome(word):
    print("It IS a palindrome!")
else:
    print("It is NOT a palindrome.")