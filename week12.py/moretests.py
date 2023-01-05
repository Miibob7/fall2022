def items(list, prefix):
    for item in list:
        if item.startswith(prefix):
            yield item

list = ("orange", "green", "blue")
for item in items(list, "g"):
    print(item)