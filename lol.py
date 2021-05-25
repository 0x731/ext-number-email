import re

nigga = input(">>> File : ")


no = '(?:\+[1-9]\d{0,2}[- ]?)[1-9][0-9]{9}'
f2 = open('emails.txt','w+')
f3 = open('num.txt','w+')


for line in open(nigga, encoding="utf8"):
    out = re.findall(no,line)
    for i in out :
        f3.write(i + '\n')




for file in open(nigga, encoding="utf8"):
    match = re.findall(r'[\w\.-]+@[\w\.-]+', file)
    for i in match:
        f2.write(i + '\n')
print("Done!")
