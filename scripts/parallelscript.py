file = open("../app/NachRiddles/app/database/parasha.json", "r")

read = file.read()
read2 = read.rstrip()
read3 = read.replace('\n',' ').replace('111','{ "parasha":"').replace('222','" },')
print (read3,"check")