'''f1=open("cat.jpeg",'rb+')
f2=open("dog.jpg",'rb+')
f3=open("hybrid.jpeg",'ab+')

f3.write(f1.read())
f3.write(f2.read())
'''
f1=open('aha.txt','r')
word=f1.readline()
for i in word:
    print(i)
def check(word):
    o_num=0
    x_num=0
    for i in word:
        if i.lower()=='o':
            o_num+=1
        if i.lower()=='x':
            x_num+=1
    if x_num==o_num:
        return True
    else:
        return False

print(check("oxoxoxoxoXox"))