pyton=  ['requests','get','test','post']
java=['httpclient','testng','get','post']
p=set(pyton)
j=set(java)

print(p,j)
交集=p.intersection( j)
print(交集)
print('他们的交集是:',p&j)

print(p.union(j ))
print('他们的并集是:', p|j)


print('他们的差集是:',p.difference(j))
print('他们的差集是:',p-j)


s1={1,2}
s3={1,2,3}
print(s1.issubset(s3))#子集
print(s3.issuperset(s1))#父集
print(s3.update(s1))