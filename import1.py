import csv;
data = ['abc',"'aa"]
f = open("my.csv","w",newline="");
w = csv.writer(f);
for data1 in data:
    w.writerows(data1);
f.close()