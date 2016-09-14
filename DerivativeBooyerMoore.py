f=open('C:/Users/user/Desktop/DNA Search/pattern.txt','r+')
#print(f.readline())
a=[];
b=[];
a=f.readline().upper();
#print(a)
#compressing pattern
for i in range(len(a)):
    if a[i]=='A':
        b.append('00');
        #b.append('0');
    elif a[i]=='C':
        b.append('01')
    elif a[i]=='T':
        b.append('10')
    else:
        b.append('11')
print(b)
#for j in range(len(b)):
#    print(b[j])
m=len(a)
#print(m)
import math
num_of_cells=m % 4;
#print(num_of_cells);
#adding dont care cells for pattern
if(num_of_cells!=0):
    for i in range(4-num_of_cells):
        b.append('xx');

#creating <p,A1,A2>
def shift(b,n):
	n=n%len(b)
	#print(n)
	return b[(len(b)-n):]+b[:(len(b)-n)]

total=4-num_of_cells;
p1=b;
p2=shift(b,total-2);
p3=shift(b,total-1);
p4=shift(b,total);
#pat=[]
#pat[1]=''.join(p1[:2]+p1[2:])

#print(pat[1])

#compressing text
f1=open('C:/Users/user/Desktop/DNA Search/dna.txt','r+')
a1=[];
b1=[];
a1=f1.readline().upper();
#print(a)
txt_len=len(a1);
for i in range(txt_len):
    if a1[i]=='A':
        b1.append('00');
    elif a1[i]=='C':
        b1.append('01')
    elif a1[i]=='T':
        b1.append('10')
    else:
        b1.append('11')
print(b1)
#for j in range(len(b1)):
#    print(b1[j])

#adding dont care cells to txt
if((len(b1)%4)!=0):
    r=len(b1)%4
    for i in range(4-r):
        b1.append('xx');

tbx_count=0
t=b1
tf=''.join(t[:len(t)-4])
tb=''.join(t[len(t)-4:])
for i in range(len(tb)):
    if(tb[i]=='x'):
        tbx_count=tbx_count+1;

#assigning pf,pm,pb and searching for pattern in txt
for i in range(1,4):
    pfx_count=0;
    pbx_count=0;
    if(i==1):
        pf=''.join(p1[:4])
        pm=''.join(p1[4:len(p1)-4])
        pb=''.join(p1[(len(p1)-4):])
        for k in range(len(pf)):
            if(pf[k]=='x'):
                pfx_count=pfx_count+1;
        for k in range(len(pb)):
            if(pb[k]=='x'):
                pbx_count=pbx_count+1;
        print(pf,pm,pb);
    elif(i==2):
        pf=''.join(p2[:4])
        pm=''.join(p2[4:len(p2)-4])
        pb=''.join(p2[(len(p2)-4):])
        for k in range(len(pf)):
            if(pf[k]=='x'):
                pfx_count=pfx_count+1;
        for k in range(len(pb)):
            if(pb[k]=='x'):
                pbx_count=pbx_count+1;
    elif(i==3):
        pf=''.join(p3[:4])
        pm=''.join(p3[4:len(p3)-4])
        pb=''.join(p3[(len(p3)-4):])
        for k in range(len(pf)):
            if(pf[k]=='x'):
                pfx_count=pfx_count+1;
        for k in range(len(pb)):
            if(pb[k]=='x'):
                pbx_count=pbx_count+1;
    else:
        pf=''.join(p4[:4])
        pm=''.join(p4[4:len(p4)-4])
        pb=''.join(p4[(len(p4)-4):])
        for k in range(len(pf)):
            if(pf[k]=='x'):
                pfx_count=pfx_count+1;
        for k in range(len(pb)):
            if(pb[k]=='x'):
                pbx_count=pbx_count+1;
    
    j=0
    found=0;
    temp=0;
    while(j<=len(tf)): #searching fr pattern in tf by mving 1 byte
        #print('j',j)
        index=j+len(pm)
        #print(index);
        if(index<=len(tf)):
            if(int(pm,2) ^ int(tf[j:index],2)==0):#if pm is in tf
                if(int(pf[(4-2)*2:],2)^int(tf[8-pfx_count:8],2)==0):#searching for pf in tf
                    if(int(pb[:len(pb)-2]) ^ int(tf[len(tf)-8:len(tf)-pbx_count])==0):#searching fr pb in tf
                        print('pattern found');
                        found=1;
                        break;
                
        j=j+8
if(found!=1):
    print('pattern not found');
  
		
        
        
            

               









