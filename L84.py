#Kaylen Nyhuis and Emily Rusch
def until_dot(x):
    index = 0
    s = x
    while index < len(s)  and s[index] != ".":
        index += 1
    print(s[:index])

until_dot("Hi. Hope you have a great day")
