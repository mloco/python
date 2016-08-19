import fileinput
f = open('dropAdds.txt', 'w')

for i in range(1,100000):
   f.write(format(i,'032x'))
   f.write('\n')