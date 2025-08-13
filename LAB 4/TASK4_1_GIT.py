def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

# Example usage
string = input("Enter a string: ")
print("Number of vowels in a given string:", count_vowels(string))