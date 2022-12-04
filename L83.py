#Kaylen Nyhuis and Emily Rusch
def count_character(x,y):
    total = 0
    index = 0
    while index >= 0:
        index = index +1
        for ch in x:
            if ch == y:
                total = total + 1
        if index == 1:
            break
    print(total)
count_character("bonobos", "o")
