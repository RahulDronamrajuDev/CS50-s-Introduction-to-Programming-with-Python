#take the user's input
word = input("Enter a variable name in camel case: ")
print(f"camelCase: {word}")
snake_case = ""
#iterate through each charcter in word
for c in word:
    if c.isupper():
        snake_case += "_" + c.lower()
    else:
        snake_case += c.lower()

print(f"snake_case: {snake_case}")