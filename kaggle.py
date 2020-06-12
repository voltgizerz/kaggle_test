import csv
import os
import re

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
            maxLen = len(fullstring)
            if splitCat[i] in fullstring:
                indices = [m.start() for m in re.finditer(splitCat[i], fullstring)]
                b = 0
                for double in range(len(indices)):
                    start_position = indices[b]
                    length = len(splitCat[i])
                    # CHECKING SUBSTRINNG
                    if fullstring[start_position-1:start_position] == ' ' and fullstring[start_position+length:start_position+length+1] == ' ' or start_position == 0 and fullstring[start_position+length:start_position+length+1] == ' ' or start_position+length == maxLen and fullstring[start_position-1: start_position] == ' ':
                        # check if roups already in list store
                        if splitCat[i] not in categoryFound:
                            simpan = dataCat[x][0]
                            categoryFound.insert(count, splitCat[i])
                            storeFound.insert(count, int(simpan))
                        else:
                            pass
                    elif  fullstring[start_position-1:start_position].isalpha() == False and fullstring[start_position+length:start_position+length+1] == ' ' or fullstring[start_position-1:start_position] == ' ' and fullstring[start_position+length:start_position+length+1].isalpha() == False or fullstring[start_position-1:start_position].isalpha() == False and fullstring[start_position+length:start_position+length+1].isalpha() == False or start_position == 0 and fullstring[start_position+length:start_position+length+1].isalpha() == False or start_position+length == maxLen and fullstring[start_position-1: start_position].isalpha() == False:
                        # check if roups already in list store
                        if splitCat[i] not in categoryFound:
                            simpan = dataCat[x][0]
                            categoryFound.insert(count, splitCat[i])
                            storeFound.insert(count, int(simpan))
                        else:
                            pass
                    else:
                        pass
                    b += 1
            else:
                pass
            i += 1
            count += 1
        x += 1
        # DO FILTER

    listDel = []  # STORE GROUP SUBSTRINGS WANT TO DELETED
    h = 0
    for cat in categoryFound:
        for j in range(len(categoryFound)):
            if (cat in categoryFound[j] or categoryFound[j] in cat) and len(cat) == len(categoryFound[j]):
                pass
            elif (cat in categoryFound[j]) and len(cat) < len(categoryFound[j]):
                pass
            elif (categoryFound[j] in cat) and len(cat) < len(categoryFound[j]):
                listDel.insert(j, int(j))
            elif (cat in categoryFound[j] or categoryFound[j] in cat) and len(cat) > len(categoryFound[j]):
                listDel.insert(j, int(j))
            elif categoryFound[j] not in cat or cat not in categoryFound[j]:
                pass
            h += 1
    # CONVERT LISTDEL DELETE DATA MULTIPLE
    listDel = list(dict.fromkeys(listDel))
    # print(listDel)
    # DO POP storeFound

    for i in range(len(listDel)):
        # -1 all the value in dellist
        for i in range(len(listDel)):
            listDel[i] = listDel[i]-1
        storeFound.pop(listDel[i]-1)
        categoryFound.pop(listDel[i]-1)

    # CONVERT TO DICT FILTER SAME GROUPS
    print("Index : ", index, " | Group : ", list(dict.fromkeys(storeFound)))
    #print("Name Category : ", categoryFound)
    # print("\n")
    with open('./output.csv', 'a', newline='') as f:  # INSER DATA OUTPUT
        writer = csv.writer(f)
        writer.writerow([index, list(dict.fromkeys(storeFound))])
    index += 1

print("SUCCESSFULLY OUTPUTED : ", index, "DATA! ")
# TO DO FIX ALL SUBSTRING
