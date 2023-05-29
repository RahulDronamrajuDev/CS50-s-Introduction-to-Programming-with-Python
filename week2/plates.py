def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if plate starts with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check if numbers are used only at the end of the plate and that the first number used is not '0'
    first_digit_index = -1
    for i in range(len(s)):
        if s[i].isdigit():
            first_digit_index = i
            break
    if first_digit_index != -1:
        for i in range(first_digit_index + 1, len(s)):
            if not s[i].isdigit():
                return False
        if s[first_digit_index] == '0':
            return False

    # Check if no periods, spaces, or punctuation marks are used in the plate
    for c in s:
        if not c.isalnum():
            return False

    return True



main()