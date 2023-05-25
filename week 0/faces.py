# faces.py

def convert(text):
    # Replace :) with 
    text = text.replace(":)", "🙂")

    # Replace :( with 
    text = text.replace(":(", "🙁")

    # Return the converted text
    return text

def main():
    # Prompt the user for input
    user_input = input("Enter some text: ")

    # Convert the input
    output = convert(user_input)

    # Print the output
    print(output)


main()
