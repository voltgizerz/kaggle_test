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
with open('./output.csv', 'a', newline='') as f:  # INSER DATA OUTPUT
    writer = csv.writer(f)
    writer.writerow(["index", "groups_found"])

i = 0
x = 0
index = 0
storeFound = []  # SAVES LIST GROUP FOUNDED
categoryFound = []
for fullspam in range(len(dataSpam)-1):
    fullstring = dataSpam[index+1][1].lower()
    x = 0
    storeFound = []
    categoryFound = []
    count = 0
    for fullcategory in dataCat:
        i = 0
        splitCat = dataCat[x][1].split(', ')
        for category in splitCat:
            if splitCat[i] in fullstring:
                simpan = dataCat[x][0]
                categoryFound.insert(count, splitCat[i])
                storeFound.insert(count, int(simpan))
            else:
                pass
            i += 1
            count += 1
        x += 1
        #DO FILTER

    listDel = [] #STORE GROUP SUBSTRINGS WANT TO DELETED
    h = 0
    for cat in categoryFound:
        for j in range(len(categoryFound)-1):
            if (cat in categoryFound[j] or categoryFound[j] in cat) and len(cat) <= len(categoryFound[j]):
                pass
            elif (cat in categoryFound[j] or categoryFound[j] in cat) and len(cat) > len(categoryFound[j]):
                listDel.insert(j, int(j))
            elif categoryFound[j] not in cat or cat not in categoryFound[j] :
                pass
            h += 1
    # CONVERT LISTDEL DELETE DATA MULTIPLE
    listDel = list(dict.fromkeys(listDel))
    #print(listDel)
    #DO POP storeFound
    for i in range(len(listDel)-1):
        storeFound.pop(listDel[i])
        categoryFound.pop(listDel[i])

    # CONVERT TO DICT FILTER SAME GROUPS
    print("Index : ", index, " | Group : ", list(dict.fromkeys(storeFound)))
    print("Nama Category : ", categoryFound)
    #print("\n")
    with open('./output.csv', 'a', newline='') as f:  # INSER DATA OUTPUT
        writer = csv.writer(f, dialect='excel', encoding='utf_8_sig')
        writer.writerow([index, list(dict.fromkeys(storeFound))])
    index += 1

print("SUCCESSFULLY OUTPUTED : ", index, "DATA! ")
# TO DO FIX ALL SUBSTRING
