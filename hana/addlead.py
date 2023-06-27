import sys
import os

if not os.path.exists('fragments'):
    os.mkdir('fragments')

lines=open(sys.argv[1],'r').readlines()
fh=open('fragments/' + sys.argv[1],'w',encoding='utf-8')

print(sys.argv[1])

fh.write(lines[0])
fh.write(lines[1])
fh.write(lines[2])
fh.write(lines[3])
fh.write(lines[4])
fh.write(lines[5])
fh.write("\n")
fh.write("[.lead]\n")
fh.write("Placeholder\n")

for x in range(6,len(lines)):
    fh.write(lines[x])

fh.close()
