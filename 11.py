List = ["Orange", "Apple", "Pear"]

for element in List:
    unique_letters = set(element)  # Get unique letters using a set
    count_unique = len(unique_letters)  # Count the number of unique letters
    print(f"The count of unique letters in '{element}' is: {count_unique}")
