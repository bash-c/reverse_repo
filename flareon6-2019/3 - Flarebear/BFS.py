
queue = []
track = {}

track[(0, 0, 0)] = ''
queue.append((0, 0, 0))

while len(queue):
    now = queue[0]
    mass, happy, clean = now

    queue = queue[1: ]
    path = track[now]

    if mass == 72 and happy == 30 and clean == 0:
        print(path)
        exit(0)
    
    next = (mass - 2, happy + 4, clean - 1)
    if not next in track:
        track[next] = path + ' play'
        queue.append(next)

    next = (mass, happy - 1, clean + 6)
    if not next in track:
        track[next] = path + ' clean'
        queue.append(next)

    next = (mass + 10, happy + 2, clean - 1)
    if not next in track:
        track[next] = path + ' feed'
        queue.append(next)