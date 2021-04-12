'''
Write a Python program to remove all the lines that contain the character 'a' in a text file (Content.txt)
and write it to another file(Newfile.txt).
'''

# Method 1 (Only copies lines with a to another file. does not delete lines with a)
oldfile = open('content.txt')
lines = oldfile.readlines()
newopen = open('newfile.txt', 'w')
#print(lines)

for line in lines:
    if 'a' in line:
        #print(line)
        newopen.write(line)
newopen.close()
oldfile.close()
print("Contents copied over to newfile.txt")




# method 2 (Deletes the lines containing a)
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
