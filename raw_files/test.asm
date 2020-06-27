section .data
	a dd 10
	b dd 10,20
section .text
	global main
main:	mov eax,ebx
	mov ecx,edx
	mov ax,cx
	add eax,20
	add ebx,20
	sub ebx,10
	mov ecx,dword[a]
	mov edx,dword[a]
	add ecx,dword[ebx+ecx*4]
	add ecx,dword[ebx*4]
	add ecx,dword[ecx*8]
	add ecx,dword[edx+200]
	add ebx,dword[edx+200]
	add ebx,dword[edx+128]
	add ebx,dword[edx+126]
	add ebx,dword[edx+127]
	add ebx,dword[edx+64]
	add ebx,dword[ebx+64]
	add ebx,dword[ebx+256]
	add ebx,dword[ebx+500]
	add ebx,dword[ebx+257]
	add ebx,dword[ebx+512]
	add eax,dword[eax+512]
        add ebx,dword[ebx+1000]
        add ebx,dword[ebx+511]
	add ebx,dword[ebx+1024]
        add ebx,dword[ebx+1023]
        add ebx,dword[ebx+2334344]
	add ebx,dword[a+200]
;	add ebx,dword[ebx+a*8]
