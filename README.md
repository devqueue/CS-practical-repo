# CS-practical-repo

with open("content.txt", "r+") as file:
    lines_with_a =[]
    lines = file.readlines()
    for line in lines:
        for ch in line:
            if ch=="a":
                lines_with_a.append(line)
    lines_wo_a = list(set(lines).difference(lines_with_a))
    line_with_aa = list(set(lines_with_a))
    file.seek(0)
    file.writelines(lines_wo_a)
    file.truncate()

with open("newfile.txt", "w") as f:
    f.writelines(line_with_aa)
