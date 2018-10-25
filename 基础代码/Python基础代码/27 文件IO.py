
with open("test.txt", "wt") as f:
    f.write("该文本会写入到文件中\n看到我了吧！")

# Read a file
with open("test.txt", "rt") as f:
    text = f.read()

print(text)