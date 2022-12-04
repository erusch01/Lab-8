#Kaylen Nyhuis and Emily Rusch
def total_length(list):
    total = 0
    for x in list:
        length = len(x)
        total = length + total
    print(total)
total_length(["Queen", "Rules"])
total_length([])
total_length(["balloons"])
total_length(["",'',"",''])


s = "Tenochtitlan"
index = 0
while index < len(s):
    index += 1
    print(s[:index])
