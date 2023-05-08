from string import punctuation

with open("files/text.txt", "r") as file:
    text = file.readlines()

with open("files/output.txt", "w") as file:
    for i in range(len(text)):
        line = text[i].replace("\n", "")
        letters = 0
        punctuations = 0
        for char in line:
            if char.isalpha():
                letters += 1
            elif char in punctuation:
                punctuations += 1

        file.write(f"Line {i+1}: {line} ({letters})({punctuations})\n")
