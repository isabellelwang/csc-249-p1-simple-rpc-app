data = "ASCENDING 1 4 13 54 521 52 3 5 32"
number_list = data.split(" ")
number_list = [item.lower() for item in number_list]


if "ascending" in number_list: 
    number_list.remove("ascending")
    number_list.sort(key=int)
    data = str(number_list)
    print(type(data))
