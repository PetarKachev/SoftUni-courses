kids = list(map(str, input().split(" ")))
circle = int(input())
first_circle = circle

while len(kids) > 1:
    circle -= 1
    if circle == 0:
        removed_kid = kids.pop(0)
        print(f"Removed {removed_kid}")
        circle = first_circle
    else:
        first_kid = kids.pop(0)
        kids.append(first_kid)
print(f"Last is {kids[0]}")