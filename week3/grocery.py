grocery_list = []

while True:
    try:
        item = input()
        grocery_list.append(item.lower())
    except EOFError:
        break

counted_items = {}

for item in grocery_list:
    if item in counted_items:
        counted_items[item] += 1
    else:
        counted_items[item] = 1

sorted_items = list(counted_items.keys())
sorted_items.sort()

for item in sorted_items:
    count = counted_items[item]
    print(f"{count} {item.upper()}")