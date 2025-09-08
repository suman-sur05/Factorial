# Take input from the user
text = input("Enter a word or phrase: ")

# Remove spaces and convert to lowercase for comparison
cleaned_text = text.replace(" ", "").lower()

# Check if the cleaned text is equal to its reverse
if cleaned_text == cleaned_text[::-1]:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")
