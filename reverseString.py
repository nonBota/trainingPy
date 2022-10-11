def solution(x):
    return x[::-1]

mytxt = solution ("world")
myt = solution ("word")

prints = [mytxt, myt]

fraseCompleta = ''

for word in prints:
    fraseCompleta += word
    
print(fraseCompleta)