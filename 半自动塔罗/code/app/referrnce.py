
def reference(target_word):
    with open("./data/explain.txt", 'r',encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if target_word in line:
                if i + 1 < len(lines):
                    print(lines[i + 1].strip())
                else:
                    print("文件损坏")
