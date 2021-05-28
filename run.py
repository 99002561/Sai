import difflib

my_file = open("file1.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

my_file = open("file2.txt", "r")
content = my_file.read()
content_list1 = content.split("\n")
my_file.close()

lines1 = content_list
lines2 = content_list1

diff = difflib.unified_diff(lines1, lines2, lineterm='', n=0)
lines = list(diff)[2:]

added = [line[1:] for line in lines if line[0] == '+']
removed = [line[1:] for line in lines if line[0] == '-']

print('additions:')
for line in added:
    print(line)
print()

print('Deletions:')
for line in removed:
    print(line)
print()
