import os

directory = input()
extensions = {}
result = []

for file in os.listdir(directory):
    if os.path.isfile(file):
        extension = file.split(".")[-1]

        if extension not in extensions:
            extensions[extension] = []

        extensions[extension].append(file)
    elif os.path.isdir(file):
        for s_file in os.listdir(f"{directory}/{file}"):
            sub_file = os.path.join(directory, file, s_file)
            if os.path.isfile(sub_file):
                extension = sub_file.split(".")[-1]

                if extension not in extensions:
                    extensions[extension] = []

                extensions[extension].append(s_file)

for extension, files in sorted(extensions.items()):
    result.append(f".{extension}")
    for file in sorted(files):
        result.append(f"- - - {file}")

with open("files/report.txt", "w") as file:
    file.write("\n".join(result))