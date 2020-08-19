#imports
import sqlite3
import os

#Init
#DB FORMAT: {fd: (File 'f' or directory 'd'), filename: (Filename duh), path: (path)}
#ex: {"fd":"f","filename":""
#may add more later
conn = sqlite3.connect('tiny_BETA.db')
files = []
counter = 0
#creates cursor
c = conn.cursor()
#create table
c.execute('''CREATE TABLE files
             (fd text, filename text, path text)''')

#Indexes disks:

for (dirpath, dirnames, filenames) in os.walk('C:'):
    #progress "bar"
    counter = counter + 1
    if counter == 500:
        counter = 0
        print(".", end='')
        
    for f in filenames:
        files.append(("f", f, os.path.join(dirpath, f)))
    
    for d in dirnames:
        files.append(("d", d, os.path.join(dirpath, d)))

print("C drive indexed!")
  
for (dirpath, dirnames, filenames) in os.walk('D:'):
    #progress "bar"
    counter = counter + 1
    if counter == 500:
        counter = 0
        print(".", end='')
        
    for f in filenames:
        files.append(("f", f, os.path.join(dirpath, f)))
        
    for d in dirnames:
        files.append(("d", d, os.path.join(dirpath, d)))
        
print("D drive indexed!")

c.executemany('INSERT INTO files VALUES (?,?,?)', files)
conn.commit()

print("DB saved! Press enter to see files!")
#print(files)
c.close()

