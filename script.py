#
# """for i in range(1,n+1):
#     print(" "*(n-i),end=' ')
#     print('* '*i)"""
#
# """for i in range(n,0,-1):
#     print(' *' * i)
#     print(" "*(n-i),end=' ')
# """
#
# # a,b,c=[int(x) for x in (input('Enter any two numbers :')).split(",")]
# # print('Product :',a*b*c)
#
# # a,b,c=[eval(x) for x in input('Enter any three Numbers :').split(",")]
# # for i in (a,b,c):
# #         if i.islist():
# #             print('list object')
# #
# # print(f'sum of {a},{b},{c} :',a+b+c )
#
# # n1=int(input('enter nuber 1'))
# # n2=int(input('enter second number'))
# # if n1>n2:
# #     print("number {b} is greater than {a}".format(n1,n2))
# # else :
# #     print('{a} is greater then {b}'.format(n2,n1))
#
# #
# n=98
# if n==1:
#     print('One')
# elif n==2:
#     print('two')
# elif n==3:
#     print('three')
# elif n==4:
#     print('four')
# elif n==5:
#     print('five')
# elif n==6:
#     print('six')
# elif n==7:
#     print('seven')
# elif n==8:
#     print('eight')
# elif n==9:
#     print('nine')
# else:
#     print('Enter single digit value')

#
# s='sunny bai'
# n=0
# for i in s:
#     print(f'{i} is present at positive index {n} and negative index {n-len(s)}')
#     n+=1

# n=int(input('enter a number'))
# sum=0
# i=0
# while i<=n:
#     sum=sum+i
#     i=i+1
#
# print(sum)

# while True:
#     n = input("enter name ")
#     if n=='Durga':
#         print('you are right i am durga')
#         break;

# n=5
# for i in range(1,n):
#     print(' '*(n-i),end='')
#     print('*'*i)

# n=10
# for i in range(1,n+1):
#     print('*',end='')

# n=10
# for i in range(1,n+1):
#     print(' * '*n)

# n=5
# for i in range(1,n+1):
#     print(str( i )*n)


print(ord('A'))

# n=5
# for i in range(1,n+1):
#     print(chr(64+i)*n)

n=5
# for i in range(n+1):
#     print('* '*i)
#
# for i in range(n,0,-1):
#     print('* '*i)

# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     print('*'*i)
#
# for i in range(1,n+1):
#     print(' '*(n-i),end=' ')
#     print(' *'*i)
# n=5
# for i in range(n,0,-1):
#     print(' *'*i)
#     print(' '*(n-i),end='')
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end=' ')
#     print('* '*i)
#
# for i in range(n,0,-1):
#     print(' *' * i)
#     print(" "*(n-i),end=' ')

# s='vikas jamdade'
# i=0
# while i<len(s):
#     if s[i]==' ':
#         i = i + 1
#         continue
#     else:
#          print(s[i],end='","')
#     i=i+1
s='vikas jamdade'
# i=-1
# while i>(-(len(s)+1)):
#     print(s[i],end=' ')
#
#     i=i-1

# try:
#   d=s.index('vt')
# except ValueError:
#     print('Not found given value error')
# else:
#     print('found',d)

# s='vikas jamdade'
# indx=0
# for sub in s:
#     if sub=='d':
#         print(f'index of {sub} is {indx}')
#     indx=indx+1

# s='jamdade'
# rev=''
# for i in s:
#     rev=i+rev
# print(rev)

# s='jamdade'
# i=len(s)-1
# while i >=0:
#     print(s[i],end='')
#     i=i-1
#
# s='vikasjamdade'
# print(s[::-1])

# s='vikas dattu jamdade baramati pune'
# s2=s.split()
# rev=[]
# print(rev)
# for i in s2:
#     rev.append(i)
# print(' '.join(rev))

# s='vikas dattu jamdade baramati pune'
# s2=s.split()
# i=len(s2)-1
# rev=[]
# while i>-1:
#     if i%2==0:
#         rev.append(s2[i][::-1])
#
#     else:
#         rev.append(s2[i])
#     i=i-1
#
# print(' '.join(rev))

# s='vikasjamdade'
# ind=0
# i=0
# while i<len(s):
#     print(f'char {s[i]} is present at +index {ind} and -Index -{len(s)-i}')
#     ind=ind+1
#     i=i+1

s1='ravi'
s2='teja'
s3=''

# i=0
# j=0
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         s3=s3+s1[i]
#     if j<len(s2):
#         s3=s3+s2[j]
#     i,j=i+1,j+1
# print(s3)

# s='A36BR51F'
# al=[]
# num=[]
# for i in s:
#     if i.isalpha():
#         al.append(i)
#     if i.isnumeric():
#         num.append(i)
# final_num=''.join((sorted(al))+(sorted(num)))
# print(final_num)

# s='a4b5c6'
# for i in s:
#     if i.isalpha():
#         x=i
#     else:
#         print(x*int(i),end='')

# s='a4k3b2'
# s1=''
# #aeknbd'
# for i in s:
#     if i.isalpha():
#         s1=s1+i
#         x=ord(i)
#
#     else:
#         s1=s1+chr(int(x)+int(i))
# print(s1)

# s='aasssdfdgggfddllleemm'
# uniq=[]
# for i in s:
#     if i not in uniq:
#         uniq.append(i)
# print(uniq)
# print('set')
# print(set(s))

# s='aabbbccddmnopps'
# d=[]
# for i in s:
#     if i not in d:
#         d.append(i)
#         d.append(str(s.count(i)))


# s='vikasjamdade'
# i=len(s)-1
# rev=''
# while i>=0:
#     rev=rev+s[i]
#     i=i-1
# print(rev)
#
# s='vikasjadmasa'
# even=[]
# odd=[]
# for i in range(len(s)):
#     if i%2==0:
#         even.append(s[i])
#     else:
#         odd.append(s[i])
#
#
# print('chars presnt at even index :',even)
# print('chars presnt at odd index :',odd)




# s1='ravi'
# s2='tejs'
# i,j=0,0
# s3=''
# while i<len(s1) or j<len(s2):
#     if i < len(s1):
#         s3=s3+s1[i]
#     if j <len(s2) :
#         s3=s3+s2[j]
#     i=i+1
#     j=j+1
# print(s3)

# s='aaabbbcccd'
# d=''
# for i in s:
#     if i.isalpha() and i not in d:
#         d = d + str(s.count(i))
#         d=d+i
#
# print(d)

# s='a6b4k4'
# s2=''
# for i in s:
#     if i.isalpha():
#         s2=s2+i
#         x=ord(i)
#     else:
#          s2=s2+(chr(x+int(i)))
# print(s2)

# s='sjksdvdnjsdjjreeddf'
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1
# print(d)

# s={12,32,34,5}
# s.update(range(2,5))
# print(s)
#
# n=eval(input('Enter number of students :'))
#
#
# students={}
# i=0
# while i<=n:
#    name= input('Enter the name of student :')
#    percentage=input('Enter the percentage of student :')
#    students[name]=percentage
#    i=i+1
# for x, y in students.items():
#     print(f'the {x} has {y} % Marks')

# n=5
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(' '*(n-i),end=' ')
#         print('* '*j)

# s='vikas dattu jamdade'
# ind=0
# for i in s:
#     print(f'index of {i} are {ind} and -ve is {ind - len(s)}')
#     ind+=1
#
# s='vikas'
# print(s[::-1])
# rev=''
# for i in s:
#     rev=i+rev
# print(rev)

#sum of first n numbers

# n=100
# i=1
# sum=0
# while i<n:
#     sum=sum+i
#     i=i+1
# print(sum)

# lst=[12,34,45,760,3,8]
# for i in lst:
#     if i>=100:
#         print('Dont process the order ')
#         print(i)
#         break
#     print(i)
# else:
#     print('all items processed ')

# n=8
# for i in range(n):
#     print('*',end=' ')

# n=5
# for i in range(5):
# #     print('*'*n)
# n=int(input('enter the number of rows'))
# for i in range(n):
#     print(int(n)*str(i+1))


# s='learning is my fasion'
#
# print(s[12:14])
# print(s[-10:-7:-1])
#
# s='vikas jamdade'
# print(s[::-1])
# st=s.split()
# i=-1
# n=len(st)-1
# l=[]
# while n>i:
#     l.append(st[n])
#     n=n-1
# print(l)

# s='viaks dattu jamdade baramati pune dorlewadi'
# st=s.split()
# l=[]
# i=0
# while i<len(st):
#     if i%2==0:
#        l.append(st[i][::-1])
#     else:
#         l.append(st[i])
#     i=i+1
# print(l)

# s='viaks dattu jamdade'
# for i in range(len(s)):
#     if i%2==0:
#         print(f'{s[i]} is present at even position : {i}')
#     else :
#         print(f'{s[i]} is present at odd position : {i}')

# s1='ravi'
# s2='tejam'
# i=0
# j=0
# s3=[]
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#        s3.append(s1[i])
#     if j<len(s2):
#         s3.append(s2[j])
#     i=i+1
#     j=j+1
# print(s3)

# s='sdANc2334sdjKc'
# srt=''
# for i in sorted(s):
#     if i.isdigit():
#         srt=srt+i
#     else:
#         srt=srt+i
# print(srt)
# s='a4b5'
# for i in s:
#     if i.isalpha():
#         x=i
#     else:
#         print(x*int(i),end='')
# s='aaabbddbddeet'
# ct=0
# l=''
# for i in s:
#     ct=s.count(i)
#     if i not in l:
#        l=l+i+str(ct)
# print(l)

# s='bsbsdAABBBBt'
# st=''
# for i in s:
#     if s.count(i)>1 and i not in st:
#         st=st+i+' '+'dublicate ocurances are : '+str(s.count(i)) +' '+'\n'
# print(st,'\n')

# s='sdvfvbdsvwcsvssdcsvs'
# st=''
# for i in s:
#     st=st+i+' '+str(s.count(i))+' '+'\n'
# print(st)
#
# s1='were'
# s2='herew'
# if sorted(s1)==sorted(s2):
# #     print(f'string is alagram :', s1,' ',s2 )
# s=[]
# s1='abcdefg'
# s2='xyz'
# s3='12345'
# i,j,k=0,0,0
# while i<len(s1) or j<len(s2) or  k<len(s3):
#     s4=[]
#     if i<len(s1):
#        s4.append(s1[i])
#     if j<len(s2):
#        s4.append(s2[j])
#     if k<len(s3):
#        s4.append(s3[k])
#     i=i+1
#     j=j+1
#     k=k+1
#     s.append(s4)
# print(''.join(str(s)))
# ============================
# l=[121,32,4,56,76]
# max=l[0]
# for i in range(len(l)):
#     if l[i]>max:
#         max=l[i]
# print(max)
# # ===========================
# min=l[0]
# for i in range(len(l)):
#     if l[i]<min:
#         min=l[i]
# print(min)
# # ====================
# def max(l):
#     max=l[0]
#     for i in range(len(l)):
#         if l[i]>max:
#             max=l[i]
#     return max
# ms=max([12,3,4,54,65432,2,34456,744321,2])
# print(ms)
# # ===================
# s=[21,34,54,6712,254,32]
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i]>s[j]:
#             s[i],s[j]=s[j],s[i]
# print(s)
# s=[21,34,54,6712,254,32]
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i]<s[j]:
#             s[i],s[j]=s[j],s[i]
# print(s)



