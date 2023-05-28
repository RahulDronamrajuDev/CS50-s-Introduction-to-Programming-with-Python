word = input("Enter the string: ")
print("Input: " + word)

vowels = "aeiouAEIOU"
new_word = ""

for c in word:
    if c not in vowels:
        new_word += c

print("Output: " + new_word)