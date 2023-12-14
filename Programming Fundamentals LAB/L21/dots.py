from collections import deque
def largest_region(grid):
    rows = len(grid)
    cols = len(grid[0])
    q = deque()
    area = 0
    ans = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ".":
                ans = 0
                q.append((i, j))
                grid[i][j] = -1
                while len(q) > 0:
                    t = q.popleft()
                    ans += 1
                    x, y = t[0], t[1]

                    if x + 1 < rows:
                        if grid[x + 1][y] == ".":
                            q.append((x + 1, y))
                            grid[x + 1][y] = - 1

                    if x - 1 >= 0:
                        if grid[x - 1][y] == ".":
                            q.append((x - 1, y))
                            grid[x - 1][y] = - 1

                    if y + 1 < cols:
                        if grid[x][y + 1] == ".":
                            q.append((x,y + 1))
                            grid[x][y + 1] = -1

                    if y - 1 >= 0:
                        if grid[x][y - 1] == ".":
                            q.append((x, y - 1))
                            grid[x][y - 1] = -1

                area = max(area, ans)
    return area
def main():
    n = int(input())
    grid = [list(input().split()) for _ in range(n)]
    result = largest_region(grid)
    return result
print(main())