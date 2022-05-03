reg32={"eax":"000","ecx":"001","edx":"010","ebx":"011","esp":"100","ebp":"101","esi":"110","edi":"111"}
reg16={"ax":"000","cx":"001","dx":"010","bx":"011","sp":"100","bp":"101","si":"110","di":"111"}
reg8={"al":"000","cl":"001","dl":"010","bl":"011","ah":"100","ch":"101","dh":"110","bh":"111"}
reg={"eax":"000","ecx":"001","edx":"010","ebx":"011","esp":"100","ebp":"101","esi":"110","edi":"111","ax":"000","cx":"001","dx":"010","bx":"011","sp":"100","bp":"101","si":"110","di":"111","al":"000","cl":"001","dl":"010","bl":"011","ah":"100","ch":"101","dh":"110","bh":"111"}
op={"add":"000","or":"001","adc":"010","sbb":"011","and":"100","sub":"101","xor":"110","cmp":"111"}
fp1=open("test3.txt","w")
def bintohex(a):
    sum=0
    for i in range(0,len(a),4):
        if (i)%4==0:
            sum=0
        else:
            pass
        for j in range(3,-1,-1):
            sum += int(a[i])*(2**j)
            i=i+1
        if sum == 10:
            fp1.write("A")
        elif sum==11:
            fp1.write("B")
        elif sum==12:
            fp1.write("C")

        elif sum==13:
            fp1.write("D")

        elif sum==14:
            fp1.write("E")

        elif sum==15:
            fp1.write("F")

        else:
            fp1.write(str(sum))

def sib(reg1,base,index,scale):
    if scale=="0":
        t="00"+reg[reg1]+"100"+"00"+reg[index]+reg[base]
    elif scale=="2":
        t="00"+reg[reg1]+"100"+"01"+reg[index]+reg[base]
    elif scale=="4":
        t="00"+reg[reg1]+"100"+"10"+reg[index]+reg[base]
    elif scale=="8":
        t="00"+reg[reg1]+"100"+"11"+reg[index]+reg[base]
    print(t)
    bintohex(t)
    fp1.write("\n")
    return "sib"

def si(reg1,index,scale):
    if scale=="0":
        t="00"+reg[reg1]+"100"+"00"+reg[index]+"101"

    elif scale=="2":
        t="00"+reg[reg1]+"100"+"01"+reg[index]+"101"
    elif scale=="4":
        t="00"+reg[reg1]+"100"+"10"+reg[index]+"101"
    elif scale=="8":
        t="00"+reg[reg1]+"100"+"11"+reg[index]+"101"
    print(t)
    t+=32*"0"
    bintohex(t)
    fp1.write("\n")
    return "si"

def sb(reg1,base,offset):
    if offset>127:
        t="10"+reg[reg1]+reg[base]
        bintohex(t)
        s=hex(offset)
        s=s[2:]+((8-len(s[2:]))*"0")
        fp1.write(s)
    else:
        t="01"+reg[reg1]+reg[base]
        bintohex(t)
        s=hex(offset)
        s=s[2:]
        fp1.write(s)

    fp1.write("\n")
    return "sb"





def check_dword(reg1,w):

    if '[' in w:
        w=w[:-1]
        dw=w.split('[')
        if dw[0]=="dword" and (dw[1] in reg):
            return dw[1]
        elif dw[0]=="dword" and ("+" in dw[1] and "*" in dw[1]):
            base=dw[1].split("+")
            if(base[0])in reg32:
                index=base[1].split("*")
                if index[0] in reg32 and index[1] in ['0','2','4','8']:
                    checksib=sib(reg1,base[0],index[0],index[1])
                    return checksib
        elif dw[0]=="dword" and "*" in dw[1]:
            index=dw[1].split("*")
            if index[0] in reg32 and index[1] in ['0','2','4','8']:
                checksi=si(reg1,index[0],index[1])
                return checksi
        elif dw[0]=="dword" and "+" in dw[1]:
            base=dw[1].split("+")
            if base[0] in reg32 and int(base[1])>=0:
                checksb=sb(reg1,base[0],int(base[1]))
                return checksb


        elif dw[0]=="dword" and (dw[1] not in reg):
            return "mem"



    else:
        return "no"




def regreg(reg1,reg2,regsize):
    t="11"+(regsize[reg1])+(regsize[reg2])
    bintohex(t)
    fp1.write("\n")

def regimm(reg1,opc):
    t="11"+op[opc]+reg[reg1]
    bintohex(t)
    fp1.write("\n")

def regdw_mem(reg1):
    t="00"+reg[reg1]+"101"
    #print(t)
    bintohex(t)
    fp1.write("\n")

def regdw_reg(reg1,dword):
    t="00"+reg[reg1]+reg[dword]
    #print(t)
    bintohex(t)
    fp1.write("\n")



Filenm=input("Enter  Assembly file name :")
flag=0
with open(Filenm, "r") as file:
    data = file.readlines()
    for line in data:
        fp1.write(line)
        fp1.write("\t")
        word = line.split()
        if word[0]=="main:" :
            flag=1
            ww=word[2].split(",")
            if ww[0] in reg:
                f=check_dword(ww[0],ww[1])
                if f=="sib":
                    continue
                if f=="si":
                    continue
                if f=="sb":
                    continue
                if f in reg:
                    regdw_reg(ww[0],f)
                elif f=="mem":
                    regdw_mem(ww[0])

            if f=="no" and (ww[0] in reg32) and (ww[1] in reg32):
                regreg(ww[1],ww[0],reg32)
            elif (ww[0] in reg16) and (ww[1] in reg16):
                regreg(ww[1],ww[0],reg16)
            elif (ww[0] in reg8) and (ww[1] in reg8):
                regreg(ww[1],ww[0],reg8)
            elif (ww[0] in reg) and (ww[1] not in reg) and (ww[1] not in op) and word[1] in op:
                print("up")
                regimm(ww[0],word[1])
            else:
                None
        if flag==1:
            ww=word[1].split(",")
            if ww[0] in reg:
                f=check_dword(ww[0],ww[1])
                if f=="sib":
                    continue
                if f=="si":
                    continue
                if f=="sb":
                    continue
                if f in reg:
                    regdw_reg(ww[0],f)
                elif f=="mem":
                    regdw_mem(ww[0])
            if f=='no' and (ww[0] in reg32) and (ww[1] in reg32):
                regreg(ww[1],ww[0],reg32)
            elif (ww[0] in reg16) and (ww[1] in reg16):
                regreg(ww[1],ww[0],reg16)
            elif (ww[0] in reg8) and (ww[1] in reg8):
                regreg(ww[1],ww[0],reg8)
            elif (ww[0] in reg) and (ww[1] not in reg) and (ww[1] not in op) and (word[0] in op):
                print("down")
                regimm(ww[0],word[0])

            else:
                None
        else:
            continue
print("Mod R/M byte written successfully in test3.txt .Please open it to see the result!!");
