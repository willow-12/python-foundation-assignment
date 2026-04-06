# Program to count vowels in a string

text = input("Enter a word or sentence: ")

vowels = "aeiou"
count = 0

for char in text:
    if char.lower() in vowels:
        count += 1

print("Number of vowels:", count)
