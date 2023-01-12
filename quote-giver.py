import random



file = open('quotes.txt', 'r')
Lines = file.readlines()
line = [random.choice(Lines)]
print(line[0])