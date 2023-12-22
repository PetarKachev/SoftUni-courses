title = input()
content = input()
command = input()

print(f'<h1>')
print(f'    {title}')
print(f'</h1>')
print(f'<article>')
print(f'    {content}')
print(f'</article>')

while command != "end of comments":
    print('<div>')
    print(f'    {command}')
    print('</div>')
    command = input()