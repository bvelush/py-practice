# google coding interview: https://youtu.be/4tYoVx0QoN0
# problem statement: delete all islands from map. Island is defined as adjacent 1's 
# (up, right, down, left) that don't touch the perimeter. 

f = [ # field (n, m)
    #0  1  2  3  4  5  6  7  8  9 <-- n
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1], # 0 <-- m
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0], # 1
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0], # 2
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 0], # 3
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0], # 4
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1], # 5
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1]  # 6
]

def nextBorder(f):
    n = len(f[0])
    m = len(f)
    for i in range(0, n):
        yield (0, i)
    for i in range(1, m):
        yield (i, n-1)
    for i in range(n-2, 0, -1):
        yield (m-1, i)
    for i in range(m-1, 0, -1):
        yield (i, 0)

def buildVisitedMap(f):
    ret_val = []
    for r in range(len(f)):
        ret_val.append([False for _ in range(len(f[0]))])
    return ret_val

def genNeighboors(f, visited, r, c): # return neighboors that are land (1), not visited and are in correct range (0..n-1, 0..m-1)
    neighboors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for (offset_r, offset_c) in neighboors:
        ret_r = r + offset_r
        ret_c = c + offset_c
        if ret_r >= 0 and ret_r < len(f):
            if ret_c >= 0 and ret_c < len(f[0]):
                if not visited[ret_r][ret_c]:
                    if f[ret_r][ret_c] == 1:
                        yield (ret_r, ret_c)

def visitLand(f, visited, r, c): # BFS visit all adjacent 1's that are not yet visited
    if f[r][c] == 1 and not visited[r][c]:
        visited[r][c] = True
        queue = list(genNeighboors(f, visited, r, c))
        while len(queue) > 0:
            curr_r, curr_c = queue.pop(0)
            visited[curr_r][curr_c] = True
            queue.extend(list(genNeighboors(f, visited, curr_r, curr_c)))

def visitMainland(f):
    visited = buildVisitedMap(f)
    for (curr_r, curr_c) in nextBorder(f):
        visitLand(f, visited, curr_r, curr_c)
    return visited

aa = list(nextBorder(f))
print(aa)

for (r, c) in nextBorder(f):
    print(f'({r}, {c}) => {f[r][c]}')

visited = buildVisitedMap(f)
print(len(visited))
print(len(visited[0]))

print(list(genNeighboors(f, visited, 0, 0)))
print(list(genNeighboors(f, visited, 1, 1)))
print(list(genNeighboors(f, visited, 0, 9)))
print(list(genNeighboors(f, visited, 6, 0)))
print(list(genNeighboors(f, visited, 6, 9)))
visited[1][2] = True
print(list(genNeighboors(f, visited, 1, 1)))
visited[2][1] = True
print(list(genNeighboors(f, visited, 1, 1)))
visited[1][0] = True
print(list(genNeighboors(f, visited, 1, 1)))
visited[0][1] = True
print(list(genNeighboors(f, visited, 1, 1)))

# solution assembled together
visited = visitMainland(f)
print(visited)
for r in range(len(visited)):
    s = []
    for c in range(len(visited[0])):
        if visited[r][c]:
            s.append(1)
        else:
            s.append(0)
    print(s)

        

