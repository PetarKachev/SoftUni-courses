n = int(input())
maze = [list(input()) for _ in range(n)]
flag = False
spaces = []
steps = 0
steps_old = -1

k_idx = 0
for i in range(n):
    if 'k' in maze[i]:
        k_idx = [i, maze[i].index('k')]

maze[k_idx[0]][k_idx[1]] = ' '

visited = [[k_idx[0], k_idx[1]]]


def find_space(k, ma):
    s_u = []
    s_r = []
    s_d = []
    s_l = []
    if k[0] != 0 and ma[k[0] - 1][k[1]] == ' ':
        s_u += [k[0] - 1, k[1]]
    if k[1] < (len(ma[k[0]]) - 1) and ma[k[0]][k[1] + 1] == ' ':
        s_r += [k[0], k[1] + 1]
    if k[0] < (len(ma) - 1) and ma[k[0] + 1][k[1]] == ' ':
        s_d += [k[0] + 1, k[1]]
    if k[1] != 0 and ma[k[0]][k[1] - 1] == ' ':
        s_l += [k[0], k[1] - 1]
    return [s_u, s_r, s_d, s_l]


def move(k, s, v, ma, m):
    for i in range(len(s)):
        if s[i] not in v and bool(s[i]):
            k = s[i]
            v.append(s[i])
            m += 1
            return k, v, m

        elif all(i in v for i in list(filter(lambda x: bool(x), s))):
            ma[k[0]][k[1]] = '@'
            k = v[-2]
            del v[-1]

            m -= 1
            return k, v, m


while k_idx[0] <= (n - 1):
    if k_idx[1] == 0 or k_idx[1] == len(maze[0]) - 1 or k_idx[0] == 0 or k_idx[0] == n - 1:
        steps_old = max(steps, steps_old)

    spaces = find_space(k_idx, maze)
    if not sum((lambda x: bool(x))(x) for x in spaces) and k_idx[0] < (n - 1) and steps_old == -1:
        print("Kate cannot get out")
        flag = True
        break

    elif not sum((lambda x: bool(x))(x) for x in spaces) and steps_old != -1:
        steps = steps_old
        break

    k_idx, visited, steps = move(k_idx, spaces, visited, maze, steps)

if not flag:
    print(f"Kate got out in {max(steps, steps_old) + 1} moves")