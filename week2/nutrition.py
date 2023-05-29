def main():
    # Create a dictionary to store the nutrition information for fruits
    fruits = {
        'apple': 130,
        'Avocado': 50,
        'banana': 110,
        'cantaloupe': 50,
        'grapes': 90,
        'grapefruit': 60,
        'honeydew': 50,
        'Kiwifruit': 90,
        'lemon': 15,
        'lime': 20,
        'nectarine': 60,
        'orange': 80,
        'Sweet Cherries': 100,
        'peach': 60,
        'pear': 100,
        'pineapple': 50,
        'plum': 70,
        'strawberries': 50,
        'watermelon': 80
    }

    # Prompt the user for a fruit
    fruit=input("Item: ")

    # Check if the fruit is in the dictionary and output the number of calories
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")


if __name__ == "__main__":
    main()
