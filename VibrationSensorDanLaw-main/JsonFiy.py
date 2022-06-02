file = open('jsonData.txt')
data = file.readlines()

file.close()

listOfStr = []
for v in data:
    listOfStr.append(v.strip())
    
listOfInt = [i+1 for i in range(len(data))]

zipbObj = zip(listOfInt,listOfStr )
# Create a dictionary from zip object
d = dict(zipbObj)
print(d)