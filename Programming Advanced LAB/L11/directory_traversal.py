import os

def save_extensions(dirname):
    for filename in os.listdir(dirname):
        file = os.path.join(dirname, filename)

        if os.path.isfile(file):
            extension = file.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(filename)
            extensions[extension] = sorted(extensions[extension])

        elif os.path.isdir(file):
            save_extensions(file)

dir_name = input()
extensions = {}
save_extensions(dir_name)
sorted_dict = dict(sorted(extensions.items(), key=lambda kvp: kvp[0]))

for key, value in sorted_dict.items():
    print(f".{key}")
    for current_value in value:
        print(f'- - - {current_value}')