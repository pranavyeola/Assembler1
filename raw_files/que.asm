section .bss
a resd 1
b1 resb 1
section .text
global main
main:
xor edx,edx
mov ebx,35
mov dword[a],ebx
add edx,dword[ebx+ecx*2]
mov edi,edx
b: inc dword [edx]
dec dword [ebx]
jmp c
inc edx
inc edi
jmp b
c:
xor dword[a],10
add dword[a],10
or ecx,[ecx]
or ecx,ecx
or [ecx],ecx
sub dword[a],10
cmp dword[a],10
xor eax,15
