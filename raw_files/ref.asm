section .data
  Array db "101","sff",10
  four dd 4
  msg db "ABCDEFGHIJKLMNOPQRSTUVWXYZ",10,0
  a dw 1
section .bss
    sum resd 2
    d resb 1
    b resw 2
    c resd 3
section .text
  global main
  main: xor ecx,ecx ;inxd
 zz: xor ebx,ebx;sum
 ;xor eax,ebx
 ;xor sp,55
 xor ax,55
 xor cx,55
 xor al,55
 xor ah,55
 xor ch,4


 xor cl,55
 xor eax,4
 xor esp,a
 xor ebp,a
 xor ecx,a
 xor eax,a
 xor bx,a
 xor bx,b
 xor sp,a
 xor bp,a
 xor cl,a
 xor al,a
 xor al,four
 xor bl,four
 xor ah,four
 xor ch,55
 add ebx , dword[eax+ecx*4]
 mov dword[eax+ecx*4],ebx
 add ebx , dword[eax+ecx*1]
 add ebx , dword[esp+ecx*1]
 add ebx , dword[esp+ecx*4]
 add ebx , dword[eax+ebp*4]
 add ebx , dword[eax+esp*1]
 add dword[eax+a*1],ebx
 add ebx , dword[eax+a*1]
 add ebx , dword[ecx+a*1]
 add eax , dword[esp+a*1]
 add eax,dword[ebp+a*1]
 add ebx , dword[a+ecx*4]
 add dword[a+ecx*4],ebx
 add ebx , dword[a+edi*4]
 add ebx,dword[a+ebp*4]
 mov dword[ecx],eax
 mov dword[eax],ecx
 mov dword[esp],ebp
 mov dword[ebp],esp
 mov dword[ebp],ecx
 mov ecx,dword[ecx]
 mov esp,dword[esp]
 mov ecx,dword[esp]
 mov ecx,dword[ebp]
lp: mov ecx, dword[eax+255]
ab: mov dword[eax+255],ecx
 mov ebp,dword[eax+256]
 pp: mov esp,dword[eax+127]
 mov eax,dword[eax+128]
  mov eax,dword[eax*4]
 mov dword[eax*4],eax
 mov esp,dword[eax*1]
 mov esp,dword[eax]
 mov esp,dword[eax*2]
 mov ebp,dword[ebp*4]
cd: mov ecx,dword[ecx*8]
gh: mov ebp,dword[ebp]
 ;jmp kl
 mov ecx,[a]
 mov [a],ecx
 mov cx,[a]
 mov al,[a]
 mov esp,[a]
 mov sp,[a]
 kl: mov ah,[a]
add ebx,dword[eax+ecx*1]
add ebx,dword[eax+ecx*4]
mn: cmp ecx,4
push dword[ecx]
push cd
push dd
push dword[ecx*8]
push dword[ecx+127]
push dword[ecx+128]
pq: push dword[ecx+ebx*4]
push dword[a+ecx*4]
push dword[a+esp*1]
push dword[a+ebp*4]
push dword[a+ecx*4]
bb: push dword[a+ecx*2]
push dword[a+ebp*8]
push dword[a+ecx*1]
oh: push sp
push ecx
push esp
push ebp
push gm
dd: push a

op: push cx

pop dword[ecx]
pop dword[ecx*8]
x: pop dword[ecx+ebx*4]
pop sp
f: inc dword[ecx]
t: inc dword[ecx*8]
y: jmp [op]
k: jmp lp
ww: jmp a
jmp sp
jmp eax
jmp [ecx+ebx*4]
jmp [ecx]
jmp [ecx*4]
jmp [esp]
jmp [a]
jmp dword[a]
jmp dword[ecx+ebx*4]
jmp dword[ecx]
kk: jmp dword[ecx*4]
jmp dword[esp]




jj: inc dword[ecx+ebx*4]
inc sp

vv: dec dword[ecx]
dec dword[ecx*8]
dec dword[ecx+ebx*4]
rr: dec sp




;  jmp lp
;  mov dword[sum],ebx
 push dword[sum]
 push msg
 push a
 push dword[a]
 push eax
 push esp
 add esp,8
  add esp,ebp
st: add ebp,8
;  add eax,8
  mov eax,ebx
  mov eax,dword[Array+ecx*8]
  mov esp,dword[Array+ecx*8]
  mov esp,dword[four+ecx*8]
ag: mov esp,dword[msg+ecx*8]
  mov esp,dword[a+ecx*8]
  mov esp,dword[sum+ecx*8]
u: mov eax,dword[Array+ecx*1]
v: mov esp,dword[Array+ecx*2]
pr: mov esp,dword[four+ecx*1]
mk: mov esp,dword[msg+ecx*1]
  rt: mov esp,dword[a+ecx*2]
  mov esp,dword[sum+ecx*2]

  add dword[a],ebx
  cc: mov dword[a],ebx
  push 3
  push 128
  push 127
  jmp 3
  jmp 25
  jmp 128
  jmp 127
