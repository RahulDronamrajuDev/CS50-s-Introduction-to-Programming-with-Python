def main():
    while True:
        fraction = input("Enter a fraction (X/Y): ")
        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            if x <= y and y != 0:
                break
        except (ValueError, ZeroDivisionError):
            pass

    fuel_percentage = round(x / y * 100)
    if fuel_percentage <= 1:
        print("E")
    elif fuel_percentage >= 99:
        print("F")
    else:
        print(f"{fuel_percentage}%")

if __name__ == "__main__":
    main()
