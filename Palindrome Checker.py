import re # Import module for regular expressions

def is_palindrome(phrase):
    # Remove non-alphanumeric characters and convert to lower case
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    # Reverse the 'forwards string'
    backwards = forwards[::-1]
    # Check if the forward and backwards strings are equal
    return forwards == backwards


if __name__ == '__main__':
    # Test the 'is_palindrome' function
    print(is_palindrome('Hello world'))
    print(is_palindrome('level'))