import csv
len_c=0
with open('sample.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row[' browsername'], row['version'])
        len_c+=1
print(len_c)

for i in range(len_c):
    print('Hi')
