class Node:
    def __init__(self, name=None,address=None,section=None,type=None,value=None,size=0,Defined="U"):
        self.name=name
        self.address=address
        self.section=section
        self.type=type
        self.value=value
        self.size=size
        self.Defined=Defined
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def AtEnd(self, a,b,c,d,e,f,g):
        NewNode = Node(a,b,c,d,e,f,g)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.name,printval.address,printval.section,printval.type,printval.value,printval.size,printval.Defined)
            printval = printval.nextval





Filenm=input("Enter  Assembly file name :")
f = open(Filenm,"r")
line = f.readline()
print(line)
line.rstrip()
if "section .data" in line:
    line = f.readline()
    line.rstrip()
    j=0
    while "section. txt" not in line and "section .bss" not in line:
        if j==0:
            address=00000000
        if line!="\n":
            w=line.split()

            for i in range(len(w)):
                #print(i,end=" ")
                if i==0:
                    symbi=w[i]

                    print("symbi= ",symbi)
                elif w[i]=="dd":
                    c=len(w)-1-i
                    c=c*4
                    size=c
                    print("dds= ",size)
                elif w[i]=="db":
                    c=0
                    k=w[(i+1):len(w)]

                    count=0
                    for d in k:
                        print("d=",d)
                        m=d.split('"')
                        print(m)
                        print("len(m)=",len(m))
                        l=len(m)
                        for p in range(len(m)):
                            if m[p]==""or m[p]=="\t":
                                continue
                            print(m[p])

                        print("len(m)=",len(m))

                        #print(type(m[1]))
                        #print("m[2]=",m[2])
                        #print(type(m[2]))
                        '''flags=0
                        if d[0]=='"':
                            j=1
                            flags=1
                            while d[j]!=
                            count+=1
                            j+=1
                        if flags==1:
                            for i in range( j+1,len(d)):
                                if d[j]==',':
                                    count+=1
                            c=count
                        else
                            m=d
                            m.split(",")
                            c=len(m)'''

                    #for k in range((",i+1),len(w)):

                        #d=len(w[k].split(","))
                        #c+=d
                    size=c
                    print("dbs=",size)
                elif w[i]=="dw":
                    c=len(w)-1-i
                    c=c*2
                    size=c
                    print("dws= ",size)
                print(w[i],end=" ")
        print()
        line = f.readline()
        line.rstrip()
f.close()




list = SLinkedList()
list.headval = Node(1,2,3,4,5,6,7)
e2 = Node(8,2,3,4,5,6,7)
e3 = Node(10,2,3,4,5,6,7)

list.headval.nextval = e2
e2.nextval = e3

list.AtEnd(9,11,2,3,4,5,6)

list.listprint()
