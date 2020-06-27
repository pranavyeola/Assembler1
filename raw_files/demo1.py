
reg32=["eax","ecx","edx","ebx","esp","ebp","esi","edi"]
reg16=["ax","cx","dx","bx","sp","bp","si","di"]
reg8=["al","cl","dl","bl","ah","ch","dh","bh"]
reg=["eax","ecx","edx","ebx","esp","ebp","esi","edi","ax","cx","dx","bx","sp","bp","si","di","al","cl","dl","bl","ah","ch","dh","bh"]
ins2=["mov","add","adc","sub","sbb","xor","cmp"]
ins1=["push","inc","dec","pop","jmp"]


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
            print("%s\t%s\t%s\t%s\t%s\t%s\t%s"%(printval.name,printval.address,printval.section,printval.type,printval.size,printval.Defined,printval.value))
            #print()
            printval = printval.nextval
#search
    def search(self,symbol):
        temp = self.headval
        while temp is not None:
            if temp.name==symbol:
                return True
            temp = temp.nextval
        return False



def txt(f):
    print("hi")
    adcount=0
    padcount=0
    #f.seek(-1,2)     # go to the file end.
    ##eof = f.tell()   # get the end of file location
    #f.seek(0,0)



     # save current position
    #cur=f.tell()
    #f.seek(0, os.SEEK_END)
    pos= f.tell()    # find the size of file
    #f.seek(cur, os.SEEK_SET)

    line=f.readline()
    line=line.strip()

    #print(line)
    while(True):
         #li = f.readline()
        newpos = f.tell()
        if newpos == pos:  # stream position hasn't changed -> EOF
            break
        else:
            pos = newpos
        flag=0
        if not line:
            line=f.readline()
            line=line.strip()
            continue
        print(line)
        if "global main" in line:
            line=f.readline()
            line=line.strip()
            continue

        pos=line.find(';')
        if pos==-1:
            pos=len(line)
        i=0
        size=0
        while(i<pos):
            size=0
            w=""
            while i<pos and (line[i]!=" "):
                w+=line[i]
                i+=1
            if ":" in line and flag==0:
                symbi=w
                w=""
                flag=1
                i+=1
                continue
            if w in ins2:
                w=""
                count=i
                print(line[count:pos])
                line=line[count:pos]
                line=line.split(",")
                if line[0].strip() in reg32 and line[1].strip() in reg32:
                    size=2
                elif line[0].strip() in reg16 and line[1].strip() in reg16:
                    size=3
                elif (line[0].strip() in reg32 or line[0].strip() in reg8) and line[1].strip().isdecimal():
                    if line[0].strip()=="al":
                        print("al found!!")
                        size=2
                    else:
                        size=3
                elif line[0].strip() in reg16 and line[1].strip().isdecimal():
                    size=4
                elif line[0].strip() in reg and list.search(line[1].strip()):
                    print("hiiii")
                    if line[0].strip() in reg32:
                        if line[0].strip()=="eax":
                            size=5
                        else:
                            size=6

                    elif line[0].strip() in reg16:
                        size=5
                    elif line[0].strip()=="al":
                        print("al found in search")
                        size=2
                    elif line[0].strip() in reg8:
                        size=3
                elif line[0].strip() in reg32 and "dword" in line[1].strip() and "+" in line[1].strip() and "*" in line[1].strip()\
                or "dword" in line[0].strip() and "+" in line[0].strip()and "*" in line[0].strip() and line[1].strip() in reg32:
                    print("OKKK")
                    if "dword" in line[1].strip():
                        l=line[1].split("[")
                    elif "dword" in line[0].strip():
                        l=line[0].split("[")
                    print("l=",l)
                    l[0]=l[0].strip()
                    print(l[0])
                    if l[0]=="dword":
                        l=l[1].strip()[:-1]
                        l=l.split("+")
                        esp=l[0]
                        if l[0] in reg32:
                            print("GOOOD")
                            l=l[1].split("*")
                            if l[0] in reg32 and l[0]!="esp" and (l[1]=="1" or l[1]=="2" or l[1]=="4" or l[1]=="8"):
                                size=3
                            elif l[0]=="esp" and l[1]=="1":
                                size=3

                            elif list.search(l[0]) and l[1]=="1":
                                if esp=="esp":
                                    size=7
                                else:
                                    size=6
                        elif list.search(l[0]):
                            l=l[1].split("*")
                            if l[0] in reg32 and (l[1]=="1" or l[1]=="2" or l[1]=="4" or l[1]=="8"):
                                size=7

                elif ("dword" in line[0].strip() and not "+" in line[0].strip() and not "*" in line[0].strip()and line[1].strip() in reg32)\
                or("dword" in line[1].strip() and  not "+" in line[1].strip()and not "*" in line[1].strip() and line[0].strip() in reg32):
                    if "dword" in line[0].strip():
                        l=line[0].split("[")
                    elif "dword" in line[1].strip():
                        l=line[1].split("[")
                    l[0]=l[0].strip()
                    if l[0]=="dword":
                        l[1]=l[1].strip()[:-1]
                        print("l[1]= ",l[1])
                        if l[1] in reg32:
                            if l[1]=="esp" or l[1]=="ebp":
                                size=3
                            else:
                                size=2
                elif ("dword" in line[0].strip() and "+" in line[0].strip() and line[1].strip() in reg32)\
                or ("dword" in line[1].strip() and "+" in line[1].strip() and line[0].strip() in reg32):
                    print("THATS>>>")
                    if "dword" in line[0].strip():
                        l=line[0].split("[")
                    elif "dword" in line[1].strip():
                        l=line[1].split("[")
                    l[0]=l[0].strip()
                    if l[0]=="dword":
                        l[1]=l[1].strip()[:-1]
                        l=l[1].split("+")
                        if l[0].strip() in reg32 and l[1].strip().isdecimal():
                            if int(l[1].strip())>127:
                                size=6
                            elif int(l[1].strip())<128 and int(l[1].strip())>0:
                                size=3
                elif ("dword" in line[0].strip() and "*" in line[0].strip() and line[1].strip() in reg32)\
                or ("dword" in line[1].strip() and "*" in line[1].strip() and line[0].strip() in reg32):
                    if "dword" in line[0].strip():
                        l=line[0].split("[")
                    elif "dword" in line[1].strip():
                        l=line[1].split("[")
                    l[0]=l[0].strip()
                    if l[0]=="dword":
                        l[1]=l[1].strip()[:-1]
                        l=l[1].split("*")
                        if l[0].strip() in reg32 and l[1].strip().isdecimal():
                            print("*******")
                            if int(l[1].strip())==1:
                                print("(l[1].strip()) =",int(l[1].strip()))
                                size=2
                            elif int(l[1].strip())==2:
                                print("(l[1].strip()) =",int(l[1].strip()))
                                size=3
                            elif int(l[1].strip())==4 or int(l[1].strip())==8:
                                size=7
                elif ("[" in line[0].strip() and line[1].strip() in reg )or ("[" in line[1].strip() and\
                line[0].strip() in reg):
                    print("HUUUUU")
                    if "[" in line[0].strip():
                        l=line[0].split("[")
                        l[1]=l[1].strip()[:-1]
                        print("l[1]= ",l[1])
                        if list.search(l[1]):
                            print("in REG")
                            if line[1].strip() in reg16:
                                print("IN REG16")
                                size=7
                            elif line[1].strip() in reg32 or line[1].strip() in reg8:
                                if line[1].strip()=="al":
                                    size=5
                                else:
                                    size=6
                    elif "[" in line[1].strip():
                        l=line[1].split("[")
                        l[1]=l[1].strip()[:-1]
                        print("l[1]= ",l[1])
                        if list.search(l[1]):
                            print("In RED")
                            if line[0].strip() in reg16:
                                print("In REG16")
                                size=7
                            elif line[0].strip() in reg32 or line[0].strip() in reg8:
                                if line[0].strip()=="al":
                                    size=5
                                else:
                                    size=6

                        else:
                            i+=1
                break
        padcount+=size
        if flag==1:

            addr=hex(adcount)[2:].upper()

            addr="0"*(8-len(addr))+addr
            list.AtEnd(symbi,addr,"Text","Label","NULL","0","1")
        adcount=padcount
        line=f.readline()
        line=line.strip()
              # go back to file beginning








def countb(j,line,word,count):
    countp=count
    count=1
    address=00000000
    w=""
    while(j<len(line)):
        while(line[j]==" "):
            j+=1
        while j<len(line) and line[j].isdecimal():
            w+=line[j]
            j+=1
        count=int(w)
        print("count in bss=",count)
        break
    if word=="resd":
        count*=4
        print("count in resd=",count)
    elif word=="resw":
        count*=2
        print("count in resw=",count)

    print("count=",count)
    return count
def bss(f):
    i=0
    line = f.readline()
    line.rstrip()
    count=0
    countp=0
    address="00000000"
    while(line):
        if "section .data" in line:
            bss(f)
            break
        elif "section .text" in line:
            txt(f)
            break
        i=0
        while(line[i]==" "or line[i]=="\t"):
            i+=1
        print(line)
        #for j in range(i,len(line)):
        #    print("line[%d]=%s "%(j,line[j]))
        section="bss"
        word=""
        for j in range(i,len(line)):
            if line[j]!=" ":
                word+=line[j]
            else:
                symbi=word
                print("symbi=",symbi)
                word=""
                break
        while(j<len(line) and line[j]==" "):
            j+=1
        while(j<len(line) and line[j]!=" "):
            word+=line[j]
            j+=1
            if word=="resd" or word =="resb" or word=="resw":
                address="0"*(8-len(address))+address
                addr=address
                print("address=",address)
                if word=="resd":
                    type="Double"
                elif word=="resw":
                    type="Word"
                else:
                    word="Byte"
                value=line[j:len(line)]
                countp=count
                count=countb(j,line,word,count)
                count=countp+count
                address=hex(count)[2:].upper()
                size=countp

                #print(address)
            else:
                continue
        list.AtEnd(symbi,addr,section,type,value,size,"1")
        line = f.readline()
        line.rstrip()

def countd(j,line,word,count):

    #countp=count
    count=0
    address=00000000
    while(j<len(line)):
        while(line[j]==" "):
            j+=1
        #value=line[j:len(line)]
        while j<len(line) and  line[j].isdecimal():
            j+=1
            if j==len(line)-1:
                count+=1

        if j<len(line)and line[j]=='"':
            j+=1
            while(j<len(line) and line[j]!='"'):
                count+=1
                j+=1
            if j<len(line)and line[j]=='"':
                j+=1

        elif j<len(line)and line[j]=="," and  line[j+1].isdecimal():
            j+=1
            while j<len(line) and line[j].isdecimal():
                j+=1
            count+=1
        else:
            j+=1
    if word=="dd":
        count*=4
    elif word=="dw":
        count*=2
    #count=countp+count
    #countp=count
    print("count=",count)
    return count
#    "sdfrdgf",10,0
#"sdfrdgf","qwewqe",10,0
def data(f):
    i=0
    line = f.readline()
    line.rstrip()
    count=0
    countp=0
    address="00000000"
    while(line):
        if "section .bss" in line:
            bss(f)
            break
        elif "section .txt" in line:
            txt(f)
            break
        section="data"
        i=0
        while(line[i]==" "or line[i]=="\t"):
            i+=1
        print(line)
        #for j in range(i,len(line)):
        #    print("line[%d]=%s "%(j,line[j]))
        word=""
        for j in range(i,len(line)):
            if line[j]!=" ":
                word+=line[j]
            else:
                symbi=word
                print("symbi=",symbi)
                word=""
                break
        while(j<len(line) and line[j]==" "):
            j+=1
        while(j<len(line) and line[j]!=" "):
            word+=line[j]
            j+=1
            if word=="db" or word =="dd" or word=="dw":
                address="0"*(8-len(address))+address
                addr=address
                print("address=",address)
                if word=="db":
                    type="Byte"
                elif word=="dd":
                    type="Double"
                else:
                    type="Word"
                value=line[j:len(line)]
                countp=count
                count=countd(j,line,word,count)
                size=count
                count=countp+count
                print("countp=",countp)
                address=hex(count)[2:].upper()

                #print(address)
        list.AtEnd(symbi,addr,section,type,value,size,"1")
        line = f.readline()
        line.rstrip()




Filenm=input("Enter  Assembly file name :")
f = open(Filenm,"r")
while True:
    line = f.readline()
    line.rstrip()
    if "section .data" in line or "section .bss" in line:
        break

print(line)
line.rstrip()
i=0

list = SLinkedList()
if "section .data" in line:
    count=data(f)
elif "section .bss" in line:
    count=bss(f)


#list.headval = Node(1,2,3,4,5,6,7)
#e2 = Node(8,2,3,4,5,6,7)
#e3 = Node(10,2,3,4,5,6,7)

#list.headval.nextval = e2
#e2.nextval = e3

#list.AtEnd(9,11,2,3,4,5,6)

#list.AtEnd(1,11,2,3,4,5,6)
list.listprint()
