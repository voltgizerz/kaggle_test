import csv
import os
# OPEN LIST CATEGORY CSV
with open('./list.csv', 'r') as f:
    reader = csv.reader(f)
    dataCat = list(reader)
print("==========================")
print("~~~~~~~~~Data Category")
print("==========================")
print(dataCat[3][1])
splitCat = dataCat[3][1].split(', ')
print(splitCat)

# OPEN SPAM CSV
with open('./spam.csv', 'r', encoding="utf8") as f:
    reader = csv.reader(f)
    dataSpam = list(reader)
print("==========================")
print("~~~~~~~~~Data Spam")
print("==========================")
print(dataSpam[1])
print(dataSpam[1][1])

os.remove('./output.csv')
with open('./output.csv', 'a', newline='') as f: # INSER DATA OUTPUT
    writer = csv.writer(f)
    writer.writerow(["index","groups_found"])
    
i = 0 
x = 0
j = 0 
storeFound = [] #SAVES LIST GROUP FOUNDED
for fullspam in dataSpam:
    fullstring = dataSpam[j+1][1].lower()
    x = 0
    storeFound = []
    count = 0
    for fullcategory in dataCat:
        i = 0
        splitCat = dataCat[x][1].split(', ')
        for category in splitCat:
            if splitCat[i] in fullstring:
                simpan = dataCat[x][0]
                storeFound.insert(count, int(simpan))
            else:
                pass
            i += 1
            count += 1
        x += 1
    print("Index : ", j," - Group : ", list(dict.fromkeys(storeFound)))
    with open('./output.csv', 'a', newline='') as f: # INSER DATA OUTPUT
        writer = csv.writer(f)
        writer.writerow([j,list(dict.fromkeys(storeFound))])
    j += 1

# TO DO FIX ALL SUBSTRING  
