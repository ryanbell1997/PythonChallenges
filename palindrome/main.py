
def check_for_palindrome(input):
    userWord = input.lower()
    reversedWord = userWord [::-1]
    if userWord == reversedWord:
        return "Yes, your word is a palindrome"
    else:
        return "Your word is NOT a palindrome"

def main():
    print("Enter a word, any word")
    user_word = input(">>> ")
    print(check_for_palindrome(user_word))

main()