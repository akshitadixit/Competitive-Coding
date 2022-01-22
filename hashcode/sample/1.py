with open('input.txt', 'r') as f:
    t = int(f.readline())
    likes = set()
    dislikes = set()

    while t > 0:
        t -= 1
        choice = f.readline().split()[1:]
        avoid = f.readline().split()[1:]
        for x in avoid:
            if x in likes:
                likes.remove(x)

            dislikes.add(x)

        for x in choice:
            if x in dislikes and x in likes:
                likes.remove(x)
            else:
                likes.add(x)

with open('output.txt', 'w') as f:
    f.write(str(len(likes))+' '+' '.join(list(likes)))


with open('input.txt', 'r') as f:
    t = int(f.readline())
    likes = {}
    dislikes = {}

    while t > 0:
        t -= 1
        choice = f.readline().split()[1:]
        avoid = f.readline().split()[1:]
        for x in avoid:
            if x in likes:
                likes[x] -= 1

            if x not in dislikes:
                dislikes[x] = 1
            else:
                dislikes[x] += 1

        for x in choice:
            if x in dislikes and x in likes:
                likes[x] -= 1

            if x not in likes:
                likes[x] = 1
            else:
                likes[x] += 1

with open('output1.txt', 'w') as f:
    s = [x for x in likes if likes[x] > 0]
    f.write(str(len(s))+' '+' '.join(s))
