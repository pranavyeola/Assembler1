f = open('symbolT.txt')
rows=[]
 # use readline() to read the first line
line = f.readline()
while line:
  if line.rstrip():
      #print(line)
      rows.append(line.split())
       # use realine() to read next line
  line = f.readline()
f.close()
#print(rows)

for i in range(len(rows)):
    if i<len(rows):
        k=4+len(rows[i][4:-2])
        for j in range(5,k):
            rows[i][4]+=" "+rows[i][j]
        del rows[i][5:k]

l=len(rows)
for i in range(len(rows)):
    #print(i)
    if i<len(rows):
        if (len(rows[i]))==1:
            rows[i-1][4]+=" "+rows[i][0]
            del rows[i]

        #print(rows[i])
for i in range(len(rows)):
    print(rows[i])

#for i in range(len(rows)):
#         if rows[i][2]=="Data":
#             if i==1:
#                 lc=0
#             else:
#                 lc=int(rows[i-1][1])+int(rows[i-1][5])
#                    rows[i][1]=lc
#             print(rows[i])
#             continue
print()
print()
rows1=[]
j=0
d=0
flag=0
for i in range(len(rows)):
    flag=0
    if(rows[i][2]=="Data"):
        if d==0:
            lc=0
            rows[i].insert(0,rows[i][0])
        else:
            #print(rows1[d-1])
            lc=int(rows1[d-1][2])+int(rows1[d-1][6])
            for j in range(len(rows1)):
                if rows1[j][0]==rows[i][0]:
                    flag=1
                    rows[i].insert(0,("new"+rows[i][0]))
            if flag==0:
                rows[i].insert(0,rows[i][0])
        rows[i][2]=lc
        rows1.append(rows[i])
        d+=1
    else:
        continue
d=0
flag=0
for i in range(len(rows)):
    if(rows[i][2]=="Bss"):
        if d==0:
            lc=0
            rows[i].insert(0,rows[i][0])
        else:
            lc=int(rows1[d-1][2])+int(rows1[d-1][6])
            for j in range(len(rows1)):
                if rows1[j][0]==rows[i][0]:
                    flag=1
                    rows[i][0].insert(0,("new"+rows[i][0]))
            if flag==0:
                rows[i].insert(0,rows[i][0])
        rows[i][2]=lc
        rows1.append(rows[i])
        d+=1
    else:
        continue
d=0
flag=0
for i in range(len(rows)):
    if(rows[i][2]=="Text"):
        if d==0:
            lc=0
            rows[i].insert(0,rows[i][0])
        else:
            lc=int(rows1[d-1][2])+int(rows1[d-1][6])
            for j in range(len(rows1)):
                if rows1[j][0]==rows[i][0]:
                    flag=1
                    rows[i][0].insert(0,("new"+rows[i][0]))
            if flag==0:
                rows[i].insert(0,rows[i][0])
        if int(rows[i][2])<lc:
            rows[i][2]=lc
        rows1.append(rows[i])
    else:
        continue

for i in range(len(rows1)):
    print(rows1[i])
