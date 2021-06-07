# strings
string = "example"
empty_string = ""

# print(string[3])

# integers
7
#floats
7.7
# booleans
True 
False

# List
languages = ['python', 'javascript', 'html', 'css']
empty_list = []

# access items in list index
# print(languages[2])

# # accessing items outside of possible values will throw an IndexError
# print(languages[10])

# # access items from end of list from negative index
# print(languages[-1])

# # access a range of items in a list
# print(languages[1:3])

# #search a list for a specific item index number
# print(languages.index("html"))

index = 0
while index < len(languages):
    print(f"No, {languages[index]} is the best language!")
    index += 1

for lang in languages:
    print("No, " + lang + "is the best language")
