for i in range(0, 10):
    spaces = ''
    for j in range(0, 10 - i - 1):
        spaces = spaces + ' '
    stars = ''
    for j in range(0, i * 2 + 1):
        stars = stars + '*'
    print(spaces + stars)






